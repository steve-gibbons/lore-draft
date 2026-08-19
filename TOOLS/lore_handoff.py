#!/usr/bin/env python3
"""Handoff administrivia records — create / inbox / show."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lore_common import (
    AGENT_WRITABLE, EFFECT_CLASSES, GATE_VALUES, HANDOFF_STATUSES,
    append_event, content_sha256, die, env_flag, load_simple_yaml,
    lore_dir, new_object_id, now_iso, objects_dir, read_object_file,
    verbose, write_object_file,
)


def _root() -> Path:
    return Path(os.environ.get("LORE_REPO", os.getcwd())).resolve()


def empty_handoff_content() -> Dict[str, Any]:
    return {
        "from": "",
        "to": "",
        "objective_ref": "",
        "scope_constraints": [],
        "handoff_status": "candidate",
        "actions_performed": [],
        "observations": [],
        "inferences": [],
        "recommendations": [],
        "evidence_refs": [],
        "limitations": [],
        "derivation": {
            "prior_handoff_refs": [],
            "transformations": [],
        },
        "attestation": {
            "executed": False,
            "environment": "",
            "execution_type": "",
            "actor_or_agent_id": "",
            "timestamp": None,
        },
        "human_gate": {
            "required": "none",
            "reason": None,
            "requested_by": None,
            "decision_ref": None,
        },
        "effect_class": "none",
        "notes": None,
    }


def validate_handoff_content(c: Dict[str, Any]) -> None:
    """Light sanity checks — harness, not a full schema engine."""
    hs = c.get("handoff_status", "candidate")
    if hs not in HANDOFF_STATUSES:
        die(f"handoff_status must be agent-writable workflow label, got: {hs}", 2)
    gate = (c.get("human_gate") or {}).get("required", "none")
    if gate not in GATE_VALUES:
        die(f"human_gate.required invalid: {gate}", 2)
    if gate in ("approve-promote", "approve-destructive", "approve-external"):
        # decision_ref required only *after* human disposition; creation may leave null
        pass
    ec = c.get("effect_class", "none")
    if ec not in EFFECT_CLASSES:
        die(f"effect_class invalid: {ec}", 2)
    # keep epistemic buckets as lists
    for key in ("observations", "inferences", "recommendations", "limitations",
                "actions_performed", "evidence_refs", "scope_constraints"):
        if key in c and not isinstance(c[key], list):
            die(f"{key} must be a list", 2)


def cmd_create(args: argparse.Namespace) -> int:
    root = _root()
    if not lore_dir(root).is_dir():
        die("no workbench; run lore init", 2)

    content = empty_handoff_content()
    if args.file:
        raw = load_simple_yaml(Path(args.file).read_text(encoding="utf-8"))
        if isinstance(raw, dict) and "content" in raw:
            content.update(raw["content"])
        elif isinstance(raw, dict):
            content.update(raw)
    if args.from_id:
        content["from"] = args.from_id
    if args.to_id:
        content["to"] = args.to_id
    if args.objective_ref:
        content["objective_ref"] = args.objective_ref

    validate_handoff_content(content)

    oid = new_object_id("handoff")
    env = {
        "lore": {
            "format_version": 1,
            "kind": "handoff",
            "id": oid,
            "status": "candidate",
            "created_at": now_iso(),
            "created_by": args.created_by or "agent:local",
        },
        "content": content,
        "provenance": {
            "source_refs": [],
            "derived_from": list(content.get("derivation", {}).get("prior_handoff_refs") or []),
            "content_sha256": content_sha256(content),
        },
    }

    if env_flag("LORE_CHECK") or env_flag("LORE_DRY_RUN"):
        print(f"[dry-run/check] would create {oid}")
        if os.environ.get("LORE_FORMAT") == "json":
            print(json.dumps(env, indent=2, default=str))
        return 0

    path = objects_dir(root) / "handoff" / f"{oid.split(':')[-1]}.yaml"
    write_object_file(path, env)
    append_event("handoff_create", actor=env["lore"]["created_by"],
                 object_refs=[oid], root=root)
    print(oid)
    verbose(f"wrote {path}")
    return 0


def cmd_inbox(_args: argparse.Namespace) -> int:
    root = _root()
    d = objects_dir(root) / "handoff"
    if not d.is_dir():
        return 0
    for f in sorted(d.glob("*.yaml")):
        try:
            data = read_object_file(f)
            c = data.get("content", {})
            gate = (c.get("human_gate") or {}).get("required", "none")
            print(f"{data.get('lore', {}).get('id')}\tgate={gate}\t"
                  f"from={c.get('from')}\tto={c.get('to')}")
        except Exception as e:
            verbose(str(e))
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    root = _root()
    d = objects_dir(root) / "handoff"
    target = args.id
    for f in d.glob("*.yaml"):
        data = read_object_file(f)
        if data.get("lore", {}).get("id") == target or f.stem in target:
            from lore_common import dump_yaml
            if os.environ.get("LORE_FORMAT") == "json":
                print(json.dumps(data, indent=2, default=str))
            else:
                print(dump_yaml(data))
            return 0
    die(f"handoff not found: {target}", 2)
    return 2


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="lore handoff",
        description=(
            "Create and inspect handoff administrivia records.\n"
            "Handoffs coordinate agent-to-agent context transfer; they carry "
            "observations, inferences, recommendations, and a human_gate field.\n"
            "They are NOT a LORE kernel class — they live outside the ontology."
        ),
        epilog=(
            "Examples:\n"
            "  lore handoff create --from agent:a --to agent:b --objective-ref OBJ-001\n"
            "  lore handoff inbox\n"
            "  lore handoff show handoff:local:abc12345"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("create", help="Create a new handoff record")
    c.add_argument("--from", dest="from_id", metavar="ACTOR",
                   help="Sending agent/author id")
    c.add_argument("--to", dest="to_id", metavar="ACTOR",
                   help="Receiving agent/author id")
    c.add_argument("--objective-ref", metavar="OBJ_ID",
                   help="Reference to the objective this handoff serves")
    c.add_argument("--file", metavar="FILE",
                   help="Load handoff content from a YAML file")
    c.add_argument("--created-by", default="agent:local",
                   dest="created_by", help="Actor id (default: agent:local)")

    sub.add_parser("inbox", help="List all handoff records with their human_gate status")
    s = sub.add_parser("show", help="Print a single handoff record by id")
    s.add_argument("id", help="Handoff id or id suffix")

    args = ap.parse_args()
    if args.cmd == "create":
        return cmd_create(args)
    if args.cmd == "inbox":
        return cmd_inbox(args)
    if args.cmd == "show":
        return cmd_show(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
