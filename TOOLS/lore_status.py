#!/usr/bin/env python3
"""Workbench status snippet (objects counts, pending gates, token presence)."""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lore_common import ALL_KINDS, lore_dir, objects_dir, read_object_file, token_record_path


def main() -> int:
    root = Path(os.environ.get("LORE_REPO", os.getcwd())).resolve()
    ld = lore_dir(root)
    if not ld.is_dir():
        print("workbench: (none)")
        return 0
    print(f"workbench: {ld}")
    counts = {}
    pending_gates = 0
    for kind in ALL_KINDS:
        d = objects_dir(root) / kind
        n = len(list(d.glob("*.yaml"))) + len(list(d.glob("*.json"))) if d.is_dir() else 0
        counts[kind] = n
        if kind == "handoff" and d.is_dir():
            for f in d.glob("*.yaml"):
                try:
                    data = read_object_file(f)
                    gate = (data.get("content") or {}).get("human_gate", {}).get("required", "none")
                    if gate and gate != "none":
                        pending_gates += 1
                except Exception as e:
                    print(f"warn: skip {f}: {e}", file=sys.stderr)
    print("objects:", " ".join(f"{k}={v}" for k, v in counts.items() if v))
    print(f"pending_gates: {pending_gates}")
    tok = token_record_path(root)
    print(f"transport_token: {'present' if tok.is_file() else 'absent'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
