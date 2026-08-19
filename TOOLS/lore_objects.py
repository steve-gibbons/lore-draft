#!/usr/bin/env python3
"""create / get / list / search / check for LORE workbench objects."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lore_common import (
    AGENT_WRITABLE, ALL_KINDS, KERNEL_KINDS, PROJECTIONS, SUBKINDS, append_event, content_sha256,
    die, env_flag, load_simple_yaml, lore_dir, new_object_id, now_iso,
    objects_dir, read_object_file, redact, verbose, write_object_file,
)


def _root() -> Path:
    return Path(os.environ.get("LORE_REPO", os.getcwd())).resolve()


def ensure_workbench(root: Path) -> None:
    if not lore_dir(root).is_dir():
        die("no workbench found; run: lore init", 2)


def build_envelope(kind: str, content: Dict[str, Any], *,
                   subkind: Optional[str] = None,
                   status: str = "candidate",
                   obj_id: Optional[str] = None,
                   created_by: str = "agent:local") -> Dict[str, Any]:
    if kind == "object":
        die("'object' is the abstract base and cannot be stored; use a concrete kind", 2)
    if kind in PROJECTIONS:
        die(f"'{kind}' is a derived projection, not a stored kind", 2)
    if kind not in ALL_KINDS:
        die(f"unknown kind: {kind}", 2)
    if subkind is not None and subkind not in SUBKINDS.get(kind, ()):
        allowed = ", ".join(SUBKINDS.get(kind, ())) or "none"
        die(f"unknown subkind '{subkind}' for kind '{kind}' (allowed: {allowed})", 2)
    if status not in AGENT_WRITABLE:
        # harness is agent-context by default; author can override later
        die(f"status '{status}' is not agent-writable in this harness", 2)
    oid = obj_id or new_object_id(kind)
    lore = {
        "format_version": 1,
        "kind": kind,
        "id": oid,
        "status": status,
        "created_at": now_iso(),
        "created_by": created_by,
    }
    if subkind is not None:
        lore["subkind"] = subkind
    return {
        "lore": lore,
        "content": content or {},
        "provenance": {
            "source_refs": [],
            "derived_from": [],
            "content_sha256": content_sha256(content or {}),
        },
    }


def object_path(root: Path, kind: str, oid: str) -> Path:
    # filename from the id tail
    tail = oid.split(":")[-1] if ":" in oid else oid
    return objects_dir(root) / kind / f"{tail}.yaml"


def cmd_create(args: argparse.Namespace) -> int:
    root = _root()
    ensure_workbench(root)
    kind = args.kind
    if kind not in ALL_KINDS:
        die(f"kind must be one of: {', '.join(ALL_KINDS)}", 2)

    content: Dict[str, Any] = {}
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
        raw = load_simple_yaml(text) if not args.file.endswith(".json") else json.loads(text)
        # allow either full envelope or bare content
        if isinstance(raw, dict) and "lore" in raw and "content" in raw:
            content = raw.get("content") or {}
            # respect supplied id/status lightly
            if "lore" in raw and raw["lore"].get("id"):
                args.id = raw["lore"]["id"]
            if "lore" in raw and raw["lore"].get("status"):
                args.status = raw["lore"]["status"]
        else:
            content = raw if isinstance(raw, dict) else {"value": raw}
    elif args.stdin:
        text = sys.stdin.read()
        raw = load_simple_yaml(text)
        content = raw if isinstance(raw, dict) else {"value": raw}

    # light sanity: refuse obvious embedded objects under source_refs if present
    for ref in (content.get("source_refs") or content.get("evidence_refs") or []):
        if isinstance(ref, dict) and "content" in ref and "lore" in ref:
            die("refusing to silently embed a full object where an OBJECT_REF is expected", 2)

    env = build_envelope(kind, content, subkind=getattr(args, "subkind", None),
                         status=args.status or "candidate",
                         obj_id=args.id, created_by=args.created_by or "agent:local")

    if env_flag("LORE_CHECK") or env_flag("LORE_DRY_RUN"):
        print(json.dumps(env, indent=2, default=str) if os.environ.get("LORE_FORMAT") == "json"
              else f"[dry-run/check] would write {env['lore']['id']}")
        return 0

    path = object_path(root, kind, env["lore"]["id"])
    write_object_file(path, env)
    append_event("create", actor=env["lore"]["created_by"],
                 object_refs=[env["lore"]["id"]], root=root)
    print(env["lore"]["id"])
    verbose(f"wrote {path}")
    return 0


def resolve_ref(root: Path, ref: str) -> Path:
    # accept kind:ns:id or path
    if "/" in ref or ref.endswith(".yaml") or ref.endswith(".json"):
        p = Path(ref)
        if not p.is_absolute():
            p = root / p
        return p
    parts = ref.split(":")
    if len(parts) >= 3:
        kind = parts[0]
        return object_path(root, kind, ref)
    # search
    for kind in ALL_KINDS:
        p = object_path(root, kind, ref)
        if p.is_file():
            return p
    die(f"object not found: {ref}", 2)
    return Path()  # unreachable


def cmd_get(args: argparse.Namespace) -> int:
    root = _root()
    ensure_workbench(root)
    path = resolve_ref(root, args.ref)
    data = read_object_file(path)
    fmt = os.environ.get("LORE_FORMAT", "text")
    if fmt == "json":
        print(json.dumps(data, indent=2, default=str))
    else:
        from lore_common import dump_yaml
        print(dump_yaml(data))
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    root = _root()
    ensure_workbench(root)
    kinds = [args.kind] if args.kind else list(ALL_KINDS)
    rows = []
    for kind in kinds:
        d = objects_dir(root) / kind
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.yaml")) + sorted(d.glob("*.json")):
            try:
                data = read_object_file(f)
                lore = data.get("lore", {})
                if args.status and lore.get("status") != args.status:
                    continue
                rows.append((lore.get("id", f.stem), lore.get("kind", kind),
                             lore.get("status", ""), lore.get("created_at", "")))
            except Exception as e:
                verbose(f"skip {f}: {e}")
    fmt = os.environ.get("LORE_FORMAT", "text")
    if fmt == "json":
        print(json.dumps([{"id": r[0], "kind": r[1], "status": r[2], "created_at": r[3]} for r in rows], indent=2))
    else:
        for r in rows:
            print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    root = _root()
    ensure_workbench(root)
    q = args.query.lower()
    kinds = [args.kind] if args.kind else list(ALL_KINDS)
    hits = []
    for kind in kinds:
        d = objects_dir(root) / kind
        if not d.is_dir():
            continue
        for f in list(d.glob("*.yaml")) + list(d.glob("*.json")):
            try:
                text = f.read_text(encoding="utf-8")
                if q in text.lower() or q in f.name.lower():
                    data = read_object_file(f)
                    lore = data.get("lore", {})
                    if args.status and lore.get("status") != args.status:
                        continue
                    hits.append(lore.get("id", f.stem))
            except Exception as e:
                verbose(f"skip {f}: {e}")
                continue
    for h in hits:
        print(h)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="lore objects",
        description="Create, retrieve, list, and search LORE kernel objects.",
        epilog=(
            "Kinds: principal | policy | object-ref | relationship | act | "
            "assertion | authority | capability | handoff\n"
            "Subkinds: object-ref/alias  act/event  "
            "assertion/{evidence,evaluation,context-hint}\n\n"
            "Examples:\n"
            "  lore create assertion --file draft.yaml\n"
            "  lore get assertion:local:abc12345\n"
            "  lore list capability --status proposed\n"
            "  lore search 'payments' --kind capability"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("create", help="Create a new typed object and write it to the workbench")
    c.add_argument("kind", help=f"Object kind: {', '.join(ALL_KINDS)}")
    c.add_argument("--subkind", help="Optional kind refinement (e.g. alias, event, evidence)")
    c.add_argument("--file", metavar="FILE", help="Load content from a YAML/JSON file")
    c.add_argument("--stdin", action="store_true", help="Read content from stdin")
    c.add_argument("--status", default="candidate",
                   help="Initial status (must be agent-writable, default: candidate)")
    c.add_argument("--id", metavar="ID", help="Override generated object id")
    c.add_argument("--created-by", default="agent:local",
                   dest="created_by", help="Actor id (default: agent:local)")

    g = sub.add_parser("get", help="Retrieve and print an object by ref or id")
    g.add_argument("ref", help="Object id, kind:ns:id, or file path")

    lp = sub.add_parser("list", help="List objects, optionally filtered by kind and status")
    lp.add_argument("kind", nargs="?", help="Restrict to this kind")
    lp.add_argument("--status", help="Restrict to this status")

    s = sub.add_parser("search", help="Full-text search across objects")
    s.add_argument("query", help="Search string (case-insensitive substring match)")
    s.add_argument("--kind", help="Restrict to this kind")
    s.add_argument("--status", help="Restrict to this status")

    args = ap.parse_args()
    if args.cmd == "create":
        return cmd_create(args)
    if args.cmd == "get":
        return cmd_get(args)
    if args.cmd == "list":
        return cmd_list(args)
    if args.cmd == "search":
        return cmd_search(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
