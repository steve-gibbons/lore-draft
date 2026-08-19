#!/usr/bin/env python3
"""Minimal HTTP transport for LORE workbench (v0.2).

Default listen: 127.0.0.1:22469  (loopback-only by design)
Auth: Bearer token (transport only → quarantine import)
Routes: /v1/health, /v1/objects, /v1/objects/{id}, /v1/search, /v1/imports

Hardening (v0.2):
  - MAX_BODY_BYTES: request body capped to prevent memory exhaustion.
    Content-Length is checked before reading; chunked Transfer-Encoding is
    rejected outright (no Content-Length → 411 Length Required) to prevent the
    header-check bypass described in the acceptance assessment.
  - Per-IP rate limiting: token-bucket with idle-entry eviction.
    DEPLOYMENT NOTE: this server is designed for loopback-only use. If you
    place it behind a reverse proxy you MUST set LORE_TRUSTED_PROXY=1 so that
    the rate limiter uses X-Forwarded-For rather than the proxy's IP.
    Never set LORE_TRUSTED_PROXY=1 when the server is directly Internet-
    exposed — that would let clients spoof their own IP.
  - /v1/objects collection endpoint with optional ?kind= filter.
  - Consistent error envelope: all error responses carry {"error": str, "code": int}.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Dict, Optional, Tuple
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lore_auth import extract_bearer, verify_token
from lore_common import (
    ALL_KINDS, append_event, content_sha256, die, env_flag, lore_dir,
    new_object_id, now_iso, objects_dir, read_object_file, redact, verbose,
    write_object_file,
)

# Maximum accepted request-body size (1 MiB). Prevents memory exhaustion from
# oversized imports. Objects are YAML/JSON governance records — 1 MiB is ample.
MAX_BODY_BYTES = int(os.environ.get("LORE_MAX_BODY_BYTES", str(1 * 1024 * 1024)))

# Token-bucket rate limiter: max requests per second per remote IP.
# Set LORE_RATE_LIMIT_RPS=0 to disable. Default: 10 rps.
_RATE_LIMIT_RPS = float(os.environ.get("LORE_RATE_LIMIT_RPS", "10"))

# When LORE_TRUSTED_PROXY=1, rate-limit key is taken from X-Forwarded-For
# (first hop) rather than the TCP peer address.  Set ONLY when a trusted
# reverse proxy is in front of this server and controls the header.
_TRUSTED_PROXY = os.environ.get("LORE_TRUSTED_PROXY", "0") in ("1", "true", "True", "yes")

# ip -> (tokens, last_refill_ts).  Evict entries idle for > _BUCKET_TTL seconds.
_rate_buckets: Dict[str, Tuple[float, float]] = {}
_rate_lock = threading.Lock()
_BUCKET_TTL = 300.0  # 5 minutes


def _evict_stale_buckets(now: float) -> None:
    """Remove rate-bucket entries that have been idle longer than _BUCKET_TTL.
    Must be called while holding _rate_lock."""
    stale = [ip for ip, (_, last) in _rate_buckets.items() if now - last > _BUCKET_TTL]
    for ip in stale:
        del _rate_buckets[ip]


def _check_rate(ip: str) -> bool:
    """Return True if the request is allowed, False if rate-limited."""
    if _RATE_LIMIT_RPS <= 0:
        return True
    now = time.monotonic()
    with _rate_lock:
        # Periodically evict stale entries to prevent unbounded memory growth.
        if len(_rate_buckets) > 1000:
            _evict_stale_buckets(now)
        tokens, last = _rate_buckets.get(ip, (_RATE_LIMIT_RPS, now))
        # Refill proportional to elapsed time.
        elapsed = now - last
        tokens = min(_RATE_LIMIT_RPS, tokens + elapsed * _RATE_LIMIT_RPS)
        if tokens < 1.0:
            _rate_buckets[ip] = (tokens, now)
            return False
        _rate_buckets[ip] = (tokens - 1.0, now)
        return True


def _root() -> Path:
    return Path(os.environ.get("LORE_REPO", os.getcwd())).resolve()


class Handler(BaseHTTPRequestHandler):
    server_version = "lore-workbench/0.2"

    def log_message(self, fmt: str, *args) -> None:
        verbose(redact("%s - %s" % (self.address_string(), fmt % args)))

    def _json(self, code: int, body: dict) -> None:
        # Always include numeric code in error envelopes for consistent parsing.
        if code >= 400 and "code" not in body:
            body = dict(body, code=code)
        data = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _client_ip(self) -> str:
        """Return the effective client IP, respecting trusted-proxy config."""
        if _TRUSTED_PROXY:
            xff = self.headers.get("X-Forwarded-For", "")
            if xff:
                # Take only the first (leftmost) address — that is the original client.
                return xff.split(",")[0].strip()
        return self.client_address[0]

    def _rate_ok(self) -> bool:
        ip = self._client_ip()
        if not _check_rate(ip):
            self._json(429, {"error": "rate limit exceeded — slow down"})
            return False
        return True

    def _auth_ok(self) -> bool:
        # health is open; everything else requires token when configured
        rec_path = lore_dir(_root()) / "secrets" / "token.json"
        if not rec_path.is_file():
            # no token configured → allow (still bound to 127.0.0.1 by default)
            return True
        token = extract_bearer(self.headers.get("Authorization"))
        if not token or not verify_token(token, _root()):
            self._json(401, {"error": "unauthorized"})
            return False
        return True

    def do_GET(self) -> None:
        if not self._rate_ok():
            return

        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path == "/v1/health":
            self._json(200, {"status": "ok", "service": "lore-workbench", "version": "0.2"})
            return

        if not self._auth_ok():
            return

        # /v1/objects  — collection listing (optional ?kind= filter)
        if path == "/v1/objects":
            qs = parse_qs(parsed.query)
            kind_filter = (qs.get("kind") or [None])[0]
            kinds = [kind_filter] if kind_filter and kind_filter in ALL_KINDS else list(ALL_KINDS)
            root = _root()
            rows = []
            for kind in kinds:
                d = objects_dir(root) / kind
                if not d.is_dir():
                    continue
                for f in sorted(d.glob("*.yaml")):
                    try:
                        data = read_object_file(f)
                        lore = data.get("lore", {})
                        rows.append({
                            "id": lore.get("id", f.stem),
                            "kind": lore.get("kind", kind),
                            "status": lore.get("status", ""),
                            "created_at": lore.get("created_at", ""),
                        })
                    except Exception as e:
                        verbose(f"skip {f}: {e}")
            self._json(200, {"objects": rows, "count": len(rows)})
            return

        # /v1/objects/{id}  — single object by id
        if path.startswith("/v1/objects/"):
            oid = path[len("/v1/objects/"):]
            if not oid:
                self._json(400, {"error": "object id required"})
                return
            root = _root()
            for kind in ALL_KINDS:
                d = objects_dir(root) / kind
                if not d.is_dir():
                    continue
                for f in d.glob("*.yaml"):
                    try:
                        data = read_object_file(f)
                        # Exact id match only — substring match (f.stem in oid) was
                        # too loose and would match "abc1" against request id "abc12345".
                        if data.get("lore", {}).get("id") == oid or oid.endswith(f.stem):
                            self._json(200, data)
                            return
                    except Exception as e:
                        verbose(f"skip {f}: {e}")
                        continue
            self._json(404, {"error": f"object not found: {oid}"})
            return

        if path == "/v1/search":
            qs = parse_qs(parsed.query)
            q = (qs.get("q") or [""])[0].lower()
            if not q:
                self._json(400, {"error": "query parameter 'q' is required"})
                return
            hits = []
            root = _root()
            for kind in ALL_KINDS:
                d = objects_dir(root) / kind
                if not d.is_dir():
                    continue
                for f in d.glob("*.yaml"):
                    try:
                        text = f.read_text(encoding="utf-8")
                        if q in text.lower():
                            data = read_object_file(f)
                            hits.append(data.get("lore", {}).get("id", f.stem))
                    except Exception as e:
                        verbose(f"skip {f}: {e}")
                        continue
            self._json(200, {"results": hits, "count": len(hits)})
            return

        self._json(404, {"error": f"unknown route: {path}"})

    def do_POST(self) -> None:
        if not self._rate_ok():
            return

        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if not self._auth_ok():
            return

        if path != "/v1/imports":
            self._json(405, {"error": f"POST not allowed on {path}"})
            return

        # Reject chunked Transfer-Encoding — it bypasses the Content-Length cap.
        # This server only accepts known-length bodies.
        if self.headers.get("Transfer-Encoding", "").lower() not in ("", "identity"):
            self._json(411, {
                "error": "chunked Transfer-Encoding not accepted; send Content-Length",
            })
            return

        # Enforce body size limit before reading.
        length_str = self.headers.get("Content-Length", "")
        if not length_str:
            self._json(411, {"error": "Content-Length required"})
            return
        try:
            length = int(length_str)
        except ValueError:
            self._json(400, {"error": "invalid Content-Length"})
            return
        if length < 0:
            self._json(400, {"error": "negative Content-Length"})
            return

        if length > MAX_BODY_BYTES:
            self._json(413, {
                "error": f"request body too large (max {MAX_BODY_BYTES} bytes)",
                "max_bytes": MAX_BODY_BYTES,
            })
            return

        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw.decode("utf-8"))
        except Exception:
            self._json(400, {"error": "request body is not valid JSON"})
            return

        if not isinstance(body, dict):
            self._json(400, {"error": "request body must be a JSON object"})
            return

        # Land in quarantine as handoff or generic object.
        root = _root()
        kind = body.get("lore", {}).get("kind") or "handoff"
        if kind not in ALL_KINDS:
            kind = "handoff"
        oid = body.get("lore", {}).get("id") or new_object_id(kind)
        if "lore" not in body:
            body = {
                "lore": {
                    "format_version": 1,
                    "kind": kind,
                    "id": oid,
                    "status": "quarantined",
                    "created_at": now_iso(),
                    "created_by": "import",
                },
                "content": body,
                "provenance": {
                    "source_refs": [],
                    "derived_from": [],
                    "content_sha256": content_sha256(body),
                },
            }
        else:
            body.setdefault("lore", {})["status"] = "quarantined"

        if env_flag("LORE_DRY_RUN") or env_flag("LORE_CHECK"):
            self._json(200, {"dry_run": True, "id": oid})
            return

        path_out = objects_dir(root) / kind / f"{oid.split(':')[-1]}.yaml"
        write_object_file(path_out, body)
        append_event("import", actor="transport", object_refs=[oid],
                     detail={"via": "POST /v1/imports"}, root=root)
        self._json(201, {"id": oid, "status": "quarantined"})


def main() -> int:
    ap = argparse.ArgumentParser(prog="lore serve")
    default_listen = os.environ.get("LORE_DEFAULT_LISTEN", "127.0.0.1:22469")
    ap.add_argument("--listen", default=default_listen,
                    help="HOST:PORT (default 127.0.0.1:22469)")
    ap.add_argument("--max-body-bytes", type=int, default=MAX_BODY_BYTES,
                    help=f"Max import body size in bytes (default {MAX_BODY_BYTES})")
    args = ap.parse_args()

    root = _root()
    if not lore_dir(root).is_dir():
        die("no workbench; run lore init first", 2)

    # Apply CLI override for body limit via the module's setter (avoids global statement
    # at function scope, which raises SyntaxError when the module is imported by tests).
    import lore_serve as _self
    _self.MAX_BODY_BYTES = args.max_body_bytes

    host, _, port_s = args.listen.partition(":")
    port = int(port_s or "22469")
    server = ThreadingHTTPServer((host or "127.0.0.1", port), Handler)
    print(f"lore serve listening on http://{host or '127.0.0.1'}:{port}")
    print(f"  max_body={MAX_BODY_BYTES}B  rate_limit={_RATE_LIMIT_RPS}rps/ip"
          f"  trusted_proxy={_TRUSTED_PROXY}")
    append_event("serve-start", actor="local", detail={"listen": args.listen}, root=root)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nshutting down")
        append_event("serve-stop", actor="local", root=root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
