#!/usr/bin/env python3
"""
LORE - freeze INTAKE/raw evidence into a git-preservable SHA-256 manifest.

Closes KF-06 / the "Check 6 can't pass in CI" gap: git does not preserve `chmod a-w`,
so filesystem immutability cannot survive a fresh checkout. This records the SHA-256 of
every raw evidence file into `INTAKE/RAW-MANIFEST.sha256`, which the validator (Check 6)
verifies. Mutation, unrecorded arrivals, and deleted evidence become detectable - and any
manifest change is a visible git commit (tamper-*evident*, not merely advisory).

Also applies `chmod a-w` locally as belt-and-suspenders (advisory only; not relied upon).

Regenerating the manifest is an intake/acceptance act: review the diff before committing.
Dependency-free (stdlib only). NOTE: full forensic integrity (signing / external witness)
remains a deeper fast-follower; this is the minimal git-preservable form.
"""
import hashlib
import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RAW = os.path.join(REPO, 'INTAKE', 'raw')
MANIFEST = os.path.join(REPO, 'INTAKE', 'RAW-MANIFEST.sha256')
SKIP = {'README.md', '.DS_Store'}


def main():
    if not os.path.isdir(RAW):
        sys.exit("No INTAKE/raw directory.")
    entries = []
    for root, _dirs, files in os.walk(RAW):
        for f in files:
            if f in SKIP:
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, RAW)
            with open(full, 'rb') as fh:
                sha = hashlib.sha256(fh.read()).hexdigest()
            entries.append((rel, sha, full))
    entries.sort()

    with open(MANIFEST, 'w', encoding='utf-8') as mh:
        mh.write("# LORE INTAKE/raw evidence manifest - SHA-256 of each raw file.\n")
        mh.write("# Verified by TOOLS/lore_validate.py Check 6 (git-preservable immutability).\n")
        mh.write("# Regenerate with TOOLS/lore_freeze_raw.py; review the diff before committing.\n")
        for rel, sha, _ in entries:
            mh.write("%s  %s\n" % (sha, rel))

    # advisory local freeze (git does not preserve this)
    frozen = 0
    for _rel, _sha, full in entries:
        try:
            mode = os.stat(full).st_mode
            os.chmod(full, mode & ~0o222)
            frozen += 1
        except OSError:
            pass

    print("Wrote %s" % MANIFEST)
    print("  %d evidence file(s) recorded; %d frozen locally (advisory)." % (len(entries), frozen))


if __name__ == '__main__':
    main()
