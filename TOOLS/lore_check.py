#!/usr/bin/env python3
"""lore check — fast pre-write artifact validator.

Validates a single LORE artifact envelope (file or stdin) against the schema/governance
rules BEFORE it is committed to disk. Useful in editor save-hooks, pre-commit pipelines,
or as a manual sanity step.

This is a thin wrapper around LoreValidator.validate_file(). Unlike lore_validate.py
(which runs the full corpus + fixture suite), lore_check focuses on ONE artifact and
exits immediately with a structured result.

Exit codes:
    0  — artifact is valid (warnings may have been printed)
    1  — artifact has errors
    2  — usage / environment error

Usage:
    lore check <file>                  Validate a file
    lore check --stdin                 Read from stdin (YAML or JSON)
    lore check <file> --format json    Machine-readable output
    lore check <file> --quiet          Suppress output; use exit code only
    cat draft.yaml | lore check --stdin --format json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lore_common import die
from lore_validate import LoreValidator


def _repo_root() -> str:
    return os.path.abspath(
        os.environ.get("LORE_REPO", os.path.join(os.path.dirname(__file__), ".."))
    )


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="lore check",
        description="Validate a single LORE artifact before writing it to disk.",
        epilog=(
            "Examples:\n"
            "  lore check draft.yaml\n"
            "  cat draft.yaml | lore check --stdin\n"
            "  lore check draft.yaml --format json"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    ap.add_argument("file", nargs="?", help="Artifact file to check (.yaml or .json)")
    ap.add_argument("--stdin", action="store_true", help="Read artifact from stdin")
    ap.add_argument(
        "--format", choices=["text", "json"], default="text",
        help="Output format (default: text)",
    )
    ap.add_argument("--quiet", "-q", action="store_true",
                    help="Suppress output; rely on exit code only")
    args = ap.parse_args()

    if not args.file and not args.stdin:
        ap.print_help()
        return 2

    tmp_path = None
    if args.stdin:
        content = sys.stdin.read()
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml",
                                         delete=False, encoding="utf-8") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        filepath = tmp_path
        label = "<stdin>"
    else:
        filepath = os.path.abspath(args.file)
        label = args.file
        if not os.path.isfile(filepath):
            if not args.quiet:
                print(f"lore check: file not found: {filepath}", file=sys.stderr)
            return 2

    validator = LoreValidator(_repo_root())

    try:
        ok, errors, warnings = validator.validate_file(filepath)
    finally:
        if tmp_path:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass

    if args.format == "json":
        result = {
            "file": label,
            "valid": ok,
            "errors": errors,
            "warnings": warnings,
        }
        if not args.quiet:
            print(json.dumps(result, indent=2))
    else:
        if not args.quiet:
            tag = "PASS" if ok else "FAIL"
            print(f"[{tag}] {label}")
            for w in warnings:
                print(f"  ~ {w}")
            for e in errors:
                print(f"  - {e}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
