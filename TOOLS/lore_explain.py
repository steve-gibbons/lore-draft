#!/usr/bin/env python3
"""--explain TOPIC for the workbench harness."""

from __future__ import annotations

import sys

TOPICS = {
    "init": "Create .lore/ tree, config, and optional transport token.",
    "create": "Write a typed object: kind[+subkind]. Kinds: principal|policy|object-ref|relationship|act|assertion|authority|capability|handoff. Subkinds: object-ref/alias, act/event, assertion/{evidence,evaluation,context-hint}.",
    "handoff": "Administrivia coordination record. Not a LORE kernel class. Separates observations/inferences/recommendations and carries human_gate.",
    "human_gate": "none|review|approve-promote|approve-destructive|approve-external. Only the author may clear promote/destructive/external.",
    "token": "Bearer token authenticates transport possession only. Never grants promotion or destructive authority.",
    "serve": "Minimal HTTP listener (default 127.0.0.1:22469). Import lands in quarantine.",
    "pull": "Fetch remote object into local quarantine. Receipt is not trust or acceptance.",
    "object": "The ABSTRACT base: all objects share the lore/content/provenance envelope and are never stored bare. OBJECT_REF stays a reference (OBJECT_REF != OBJECT).",
    "status": "Agent-writable statuses only from the harness unless author context is explicit.",
    "kernel": "Canonical ontology (DECISION-ONTOLOGY-CANONICAL-KERNEL-001): abstract 'object' base; concrete kinds principal, policy, object-ref(+alias), relationship, act(+event), assertion(+evidence/evaluation/context-hint), authority, capability; 'thing' and 'state' are derived projections, not stored.",
}


def main() -> int:
    topic = (sys.argv[1] if len(sys.argv) > 1 else "").lower().strip()
    if not topic or topic in ("help", "list"):
        print("Topics:", ", ".join(sorted(TOPICS)))
        return 0
    # fuzzy
    for k, v in TOPICS.items():
        if topic in k or k in topic:
            print(f"{k}: {v}")
            return 0
    print(f"No explanation for '{topic}'. Try: lore --explain list")
    return 0


if __name__ == "__main__":
    sys.exit(main())
