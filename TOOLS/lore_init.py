#!/usr/bin/env python3
"""lore init — create local workbench tree and optional transport token."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# allow running as script
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lore_common import (
    ALL_KINDS, append_event, config_path, die, dump_yaml, env_flag,
    lore_dir, now_iso, objects_dir, redact, secrets_dir, verbose, workbench_id,
)
from lore_auth import create_verifier_record, generate_token, store_verifier


DEFAULT_CONFIG = """\
format_version: 1

workbench:
  id: "{wb_id}"
  created_at: "{created}"

storage:
  objects_dir: ".lore/objects"
  events_file: ".lore/events/events.ndjson"

defaults:
  format: yaml
  object_namespace: "local"
  author_id: "author:local"
  agent_id: "agent:local"

transport:
  enabled: false
  listen: "127.0.0.1:22469"
  require_bearer_token: true

auth:
  token_record: ".lore/secrets/token.json"
  algorithm: "argon2id"
"""


def main() -> int:
    ap = argparse.ArgumentParser(prog="lore init")
    ap.add_argument("--generate-token", action="store_true",
                    help="Create transport bearer token (printed once)")
    ap.add_argument("--force", action="store_true", help="Overwrite config if present")
    args = ap.parse_args()

    root = Path(os.environ.get("LORE_REPO", os.getcwd())).resolve()
    ld = lore_dir(root)
    dry = env_flag("LORE_DRY_RUN") or env_flag("LORE_CHECK")

    if ld.exists() and not args.force:
        # Additive init: ensure subdirs exist but do not overwrite an existing config.
        # Print an explicit message at normal (non-verbose) level so the caller knows
        # the workbench was found and nothing was overwritten.
        print(f"Workbench already initialized at {ld} (use --force to overwrite config)")
        if dry:
            print(f"[dry-run] would verify subdirs under {ld}")
            return 0
        # Still create any missing subdirs (idempotent).
        for kind in ALL_KINDS:
            (objects_dir(root) / kind).mkdir(parents=True, exist_ok=True)
        (ld / "events").mkdir(parents=True, exist_ok=True)
        (ld / "cache").mkdir(parents=True, exist_ok=True)
        secrets_dir(root).mkdir(parents=True, exist_ok=True)
        append_event("init", actor="author:local", success=True,
                     detail={"generate_token": False, "already_present": True}, root=root)
        return 0

    if dry:
        print(f"[dry-run] would create {ld}")
        if args.generate_token:
            print("[dry-run] would generate and print a lore_… token once")
        return 0

    # directories
    for kind in ALL_KINDS:
        (objects_dir(root) / kind).mkdir(parents=True, exist_ok=True)
    (ld / "events").mkdir(parents=True, exist_ok=True)
    (ld / "cache").mkdir(parents=True, exist_ok=True)
    secrets_dir(root).mkdir(parents=True, exist_ok=True)

    cfg = config_path(root)
    if not cfg.exists() or args.force:
        wb = workbench_id()
        text = DEFAULT_CONFIG.format(wb_id=wb, created=now_iso())
        cfg.write_text(text, encoding="utf-8")
        verbose(f"wrote {cfg}")

    # NOTE: init deliberately does NOT write the repo .gitignore. Runtime state lives
    # in ~/.lore (or $LORE_HOME), outside any repo, so there is nothing repo-local to
    # ignore. The old block appended `*.asc` to the repo .gitignore, which silently hid
    # detached signatures (KEYS/*.asc, RAW-MANIFEST.sha256.asc, author-only artifact
    # sigs) - the KF-01 signing workflow. Removed 2026-08-16.

    token_printed = None
    if args.generate_token:
        tok = generate_token()
        rec = create_verifier_record(tok)
        store_verifier(rec, root)
        token_printed = tok
        print("Transport token (shown once — store it securely):")
        print(tok)
        print("(Verifier stored under .lore/secrets/token.json; raw token is not saved.)")

    append_event("init", actor="author:local", success=True,
                 detail={"generate_token": bool(args.generate_token)}, root=root)
    print(f"Initialized workbench at {ld}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
