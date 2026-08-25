#!/usr/bin/env python3
"""Shared helpers for LORE workbench harness (v0.1). Stdlib only."""

from __future__ import annotations

import hashlib
import json
import os
import re
import secrets
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Canonical ontology (DECISION-ONTOLOGY-CANONICAL-KERNEL-001): `object` is the ABSTRACT base
# (never stored). KERNEL_KINDS are the concrete stored flavors; SUBKINDS refine them via
# kind+subkind. `thing` and `state` are DERIVED PROJECTIONS, not stored kinds.
KERNEL_KINDS = ("principal", "policy", "object-ref", "relationship", "act", "assertion", "authority", "capability")
SUBKINDS = {
    "object-ref": ("alias",),
    "act": ("event",),
    "assertion": ("evidence", "evaluation", "context-hint"),
}
PROJECTIONS = ("thing", "state")
ADMIN_KINDS = ("handoff",)
ALL_KINDS = KERNEL_KINDS + ADMIN_KINDS

AGENT_WRITABLE = {
    "candidate", "proposed", "derived", "generated",
    "evidence-only", "quarantined", "unknown", "unresolved",
}

# Author-only / preseeded statuses (per AGENTS.md). Agents and foreign sources
# may never introduce these; only a human author (root path) may assign them.
AUTHOR_ONLY = {
    "accepted", "normative", "canonical", "verified",
    "released", "superseded", "deleted",
}

HANDOFF_STATUSES = set(AGENT_WRITABLE)
GATE_VALUES = {"none", "review", "approve-promote", "approve-destructive", "approve-external"}
EFFECT_CLASSES = {"none", "destructive", "external"}

# Credential-shaped patterns, shared by ingest-redaction and egress-scanning.
# Each captures a leading `key=` group (group 1) where applicable so redaction can
# keep the key and drop only the value.
CREDENTIAL_PATTERNS = [
    ("aws-access-key-id", r"(A(?:KIA|SIA)[0-9A-Z]{16})"),
    ("aws-signature-qs", r"((?:X-Amz-)?Signature=)[^&\s\"']+"),
    ("aws-credential-qs", r"(X-Amz-Credential=)[^&\s\"']+"),
    ("aws-security-token-qs", r"([Xx]-[Aa]mz-[Ss]ecurity-[Tt]oken=|[Xx]-amz-security-token=)[^&\s\"']+"),
    ("aws-access-key-qs", r"(AWSAccessKeyId=)[^&\s\"']+"),
    ("bearer-token", r"(Bearer\s+)[A-Za-z0-9._\-]{12,}"),
    ("lore-token", r"(lore_)[A-Za-z0-9_\-]{12,}"),
]

# Egress policy defaults. These are *preferences* (author-tunable), distinct from
# the trust-driven ingress rules: egress is about disclosure and safety, not trust.
DEFAULT_EGRESS_PREFS = {
    "block_on_secrets": True,        # refuse to export credential-bearing content
    "block_ungated_effects": True,   # refuse to export destructive/external effects w/o a cleared gate
    "block_on_hash_mismatch": True,  # refuse to export a record whose content integrity fails
}


def env_flag(name: str) -> bool:
    return os.environ.get(name, "0") in ("1", "true", "True", "yes")


def repo_root() -> Path:
    return Path(os.environ.get("LORE_REPO", os.getcwd())).resolve()


def lore_home() -> Path:
    """Workbench runtime-state root. Defaults to ~/.lore (per author direction,
    2026-08-16), overridable with $LORE_HOME. Decoupled from CWD/repo so `lore`
    uses one stable workbench no matter where it is invoked."""
    env = os.environ.get("LORE_HOME")
    return (Path(env).expanduser() if env else Path.home() / ".lore").resolve()


def lore_dir(root: Optional[Path] = None) -> Path:
    # Runtime state lives in ~/.lore (or $LORE_HOME), NOT the CWD/repo. `root` is
    # retained for call-signature compatibility but no longer selects the state
    # location; set $LORE_HOME to relocate (e.g. for tests).
    return lore_home()


def objects_dir(root: Optional[Path] = None) -> Path:
    return lore_dir(root) / "objects"


def events_path(root: Optional[Path] = None) -> Path:
    return lore_dir(root) / "events" / "events.ndjson"


def config_path(root: Optional[Path] = None) -> Path:
    return lore_dir(root) / "config.yaml"


def secrets_dir(root: Optional[Path] = None) -> Path:
    return lore_dir(root) / "secrets"


def token_record_path(root: Optional[Path] = None) -> Path:
    return secrets_dir(root) / "token.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def workbench_id() -> str:
    return f"workbench:local:{secrets.token_hex(4)}"


def new_object_id(kind: str, namespace: str = "local") -> str:
    # compact unique-ish id
    return f"{kind}:{namespace}:{secrets.token_hex(8)}"


def content_sha256(content: Any) -> str:
    """Stable-ish hash of content mapping."""
    raw = json.dumps(content, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def append_event(action: str, *, actor: str = "local", object_refs: Optional[List[str]] = None,
                 success: bool = True, detail: Optional[Dict] = None, root: Optional[Path] = None) -> None:
    path = events_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        "ts": now_iso(),
        "actor": actor,
        "action": action,
        "object_refs": object_refs or [],
        "success": success,
        "detail": detail or {},
    }
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, separators=(",", ":")) + "\n")


class YamlSupportError(RuntimeError):
    """A document used a construct the dependency-free parser does not implement.

    Raised rather than guessed at. The original fallback parsed only flat `key: value`
    lines; handed a nested document it returned a mapping of empty strings, and the
    caller died later somewhere unrelated (`'str' object has no attribute 'get'`) with
    nothing naming the real cause. TOOLS/lore_yaml now covers the subset this corpus
    actually uses, so this fires only for genuinely unsupported constructs — anchors,
    aliases, merge keys, tags, multi-document streams.

    Degrading silently to a wrong answer is worse than stopping: *executed is not
    success* (CORE-INVARIANT 9), and the corpus cannot enforce what its own tools
    cannot reliably read (CORE-INVARIANT 10). Installing PyYAML is deliberately not
    the remedy — the zero-dependency posture of the TCB is an author imperative.
    See ACTION_ITEMS/open/AI-003.
    """


def load_simple_yaml(text: str, *, source: str = "<text>") -> Dict[str, Any]:
    """Load a YAML document. PyYAML when present, TOOLS/lore_yaml otherwise.

    lore_yaml implements the subset this corpus uses and is verified against PyYAML
    over every YAML file in the repository (TESTS/test_yaml_parser.py), so a document
    means the same thing whether or not PyYAML happens to be installed. That equality
    is the property worth having here; it is what three separate defects came from
    lacking.
    """
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text) or {}
    except ImportError:
        pass
    stripped = text.strip()
    if stripped.startswith("{"):
        return json.loads(stripped)
    from lore_yaml import YamlParseError, parse as _parse
    try:
        return _parse(text) or {}
    except YamlParseError as exc:
        raise YamlSupportError(
            "cannot parse %s without PyYAML: %s\n"
            "  TOOLS/lore_yaml covers the subset this corpus uses; this document is\n"
            "  outside it. Failing closed rather than guessing.\n"
            "  See ACTION_ITEMS/open/AI-003." % (source, exc)) from exc


def dump_yaml(data: Any) -> str:
    """Emit YAML via the dependency-free serializer only (AI-003 Option B).

    Always uses TOOLS/lore_yaml.dump so output shape is identical regardless of
    whether PyYAML is installed. PyYAML remains preferred on the *load* path
    (see load_simple_yaml); it is deliberately not used for output so that
    representation never depends on ambient packages.

    Callers that want JSON already branch on LORE_FORMAT before calling this.
    """
    from lore_yaml import dump as _dump
    return _dump(data)


def read_object_file(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return json.loads(text)
    return load_simple_yaml(text)


def write_object_file(path: Path, data: Dict[str, Any], fmt: str = "yaml") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "json" or path.suffix == ".json":
        path.write_text(json.dumps(data, indent=2, default=str) + "\n", encoding="utf-8")
    else:
        path.write_text(dump_yaml(data), encoding="utf-8")


def enforce_incoming(record: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    """Governance checkpoint for a record CROSSING A TRUST BOUNDARY into this
    workbench - exchange pull, vendor ingest, or a watcher polling the bus.

    This is the live-bus analogue of the CI validator's enforcement-at-rest: a
    foreign record is *data, not an instruction*, so a status it claims for
    itself is never honored. Any author-only status (claimed directly or via the
    exchange origin_status) is BLOCKED and recorded as a governance flag; the
    record is forced to `quarantined` regardless. Never raises - it returns the
    sanitized record plus a list of human-readable flags (empty when clean).
    """
    flags: List[str] = []
    lore = record.setdefault("lore", {})
    claimed = lore.get("status")
    origin_status = ((record.get("provenance", {}) or {}).get("exchange", {}) or {}).get("origin_status")
    for where, st in (("claimed status", claimed), ("exchange origin_status", origin_status)):
        if st in AUTHOR_ONLY:
            flags.append(
                f"BLOCKED: author-only status '{st}' arrived via {where}; a foreign "
                f"source cannot introduce author-only statuses. Forced to quarantined."
            )
    # Trust boundary: receipt != trust. Force quarantine no matter what arrived.
    lore["status"] = "quarantined"
    if flags:
        prov = record.setdefault("provenance", {})
        gf = prov.setdefault("governance_flags", [])
        for f in flags:
            if f not in gf:
                gf.append(f)
    return record, flags


def scan_secrets(text: str) -> List[Tuple[str, int]]:
    """Return [(label, count)] for each credential class found in text. Empty = clean."""
    out: List[Tuple[str, int]] = []
    for label, pat in CREDENTIAL_PATTERNS:
        n = len(re.findall(pat, text))
        if n:
            out.append((label, n))
    return out


def redact_secrets(text: str) -> Tuple[str, List[Dict[str, Any]]]:
    """Redact credential *values*, keeping any leading `key=`. Returns (text, notes)."""
    notes: List[Dict[str, Any]] = []
    for label, pat in CREDENTIAL_PATTERNS:
        rx = re.compile(pat)

        def _sub(m: "re.Match") -> str:
            return (m.group(1) + "[REDACTED]") if m.lastindex and m.group(1).endswith("=") \
                else "[REDACTED]"

        text, n = rx.subn(_sub, text)
        if n:
            notes.append({"kind": label, "count": n})
    return text, notes


def enforce_outgoing(record: Dict[str, Any],
                     prefs: Optional[Dict[str, bool]] = None) -> Tuple[List[str], List[str]]:
    """Governance checkpoint for a record LEAVING this workbench - exchange push,
    transport push, or a watcher exporting to a shared bus.

    Egress is the mirror of `enforce_incoming`, but the concern is different:
    ingress is about *trust* (foreign data cannot claim authority), egress is
    about *disclosure and safety* (do not leak secrets, do not propagate ungated
    effects or corrupted records outward). It does not mutate the record - it
    reports (blocks, warnings). `blocks` are hard stops the caller should refuse
    (unless the author overrides); `warnings` are advisory. Policies are
    preferences, author-tunable via `prefs` (see DEFAULT_EGRESS_PREFS).
    """
    p = dict(DEFAULT_EGRESS_PREFS)
    if prefs:
        p.update({k: bool(v) for k, v in prefs.items() if k in p})
    blocks: List[str] = []
    warnings: List[str] = []
    content = record.get("content") or {}

    # a. Secret exfiltration: never push credential-bearing content into a shared area.
    found = scan_secrets(json.dumps(content, sort_keys=True, default=str))
    if found:
        msg = "SECRET: credential-shaped material in content (" + \
              ", ".join(f"{l}x{n}" for l, n in found) + ")"
        (blocks if p["block_on_secrets"] else warnings).append(msg)

    # b. Ungated effects: a destructive/external handoff must have a cleared human gate.
    ec = content.get("effect_class")
    gate = content.get("human_gate") or {}
    if ec in ("destructive", "external") and not gate.get("decision_ref"):
        (blocks if p["block_ungated_effects"] else warnings).append(
            f"EFFECT: effect_class '{ec}' has no cleared human_gate.decision_ref")

    # c. Integrity: do not propagate a record whose stored content hash is wrong.
    stored = (record.get("provenance") or {}).get("content_sha256")
    if stored is not None and stored != content_sha256(content):
        (blocks if p["block_on_hash_mismatch"] else warnings).append(
            "INTEGRITY: content_sha256 does not match content")

    return blocks, warnings


def redact(s: str) -> str:
    """Never leak bearer tokens in output."""
    return re.sub(r"lore_[A-Za-z0-9_\-]{8,}", "lore_<redacted>", s)


def die(msg: str, code: int = 2) -> None:
    print(redact(msg), file=sys.stderr)
    sys.exit(code)


def verbose(msg: str) -> None:
    if env_flag("LORE_VERBOSE") or env_flag("LORE_DEBUG"):
        print(redact(msg), file=sys.stderr)


def debug(msg: str) -> None:
    if env_flag("LORE_DEBUG"):
        print(redact(msg), file=sys.stderr)
