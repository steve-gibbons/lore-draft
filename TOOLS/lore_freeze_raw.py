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
SIGNERS = os.path.join(REPO, 'REGISTRIES', 'trusted-signers.txt')
# .gdoc files are live Google Drive sync pointer files (JSON stubs with a doc_id that
# Drive rewrites continuously). They carry no evidence content and must not be hashed
# into the manifest — the hash would race the sync process and fail every check.
SKIP_NAMES = {'README.md', '.DS_Store'}
SKIP_SUFFIXES = {'.gdoc'}


def _root_fingerprints():
    """Return list of fingerprints with role 'root' from trusted-signers.txt."""
    roots = []
    if not os.path.isfile(SIGNERS):
        return roots
    with open(SIGNERS, encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(None, 2)
            if len(parts) >= 2 and parts[1] == 'root':
                roots.append(parts[0].upper().replace(' ', ''))
    return roots


def main():
    if not os.path.isdir(RAW):
        sys.exit("No INTAKE/raw directory.")
    entries = []
    skipped = []
    for root, _dirs, files in os.walk(RAW):
        for f in files:
            if f in SKIP_NAMES:
                continue
            if any(f.endswith(s) for s in SKIP_SUFFIXES):
                rel = os.path.relpath(os.path.join(root, f), RAW)
                skipped.append(rel)
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, RAW)
            with open(full, 'rb') as fh:
                sha = hashlib.sha256(fh.read()).hexdigest()
            entries.append((rel, sha, full))
    entries.sort()

    lines = [
        "# LORE INTAKE/raw evidence manifest - SHA-256 of each raw file.\n",
        "# Verified by TOOLS/lore_validate.py Check 6 (git-preservable immutability).\n",
        "# Regenerate with TOOLS/lore_freeze_raw.py; review the diff before committing.\n",
    ]
    for rel, sha, _ in entries:
        lines.append("%s  %s\n" % (sha, rel))
    new_content = "".join(lines)

    # Read the existing manifest (if any) to detect a no-op run.
    existing = None
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, 'r', encoding='utf-8') as fh:
            existing = fh.read()

    if existing == new_content:
        print("Manifest unchanged (%d evidence file(s)); no write performed." % len(entries))
        sig = MANIFEST + '.asc'
        if os.path.exists(sig):
            print("  Existing signature is still valid (manifest not touched).")
        return

    with open(MANIFEST, 'w', encoding='utf-8') as mh:
        mh.write(new_content)

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
    if skipped:
        print("  WARNING: %d file(s) excluded from manifest (live sync artifacts — not verifiable):" % len(skipped))
        for s in sorted(skipped):
            print("    EXCLUDED (not hashed): %s" % s)
        print("  These files exist in INTAKE/raw but are outside the integrity boundary.")

    # A fresh manifest invalidates any prior detached signature - this is the LL-001
    # control working as intended: re-signing must be a conscious author act, so a
    # laundered regen cannot silently inherit the old signature. (Track F test harness.)
    sig = MANIFEST + '.asc'
    if os.path.exists(sig):
        roots = _root_fingerprints()
        root_hint = (roots[0] + '!') if roots else '<root-key-fpr>!'
        print("  NOTE: %s no longer matches this manifest." % os.path.basename(sig))
        print("        Author, to re-sign (ROOT act - pin the root key with ! so a shared")
        print("        keyring can't default to a delegated subkey):")
        print("          gpg --armor --detach-sign \\")
        print("              -u '%s' \\" % root_hint)
        print("              INTAKE/RAW-MANIFEST.sha256")
        print("        Verify:  python3 TOOLS/lore_verify_manifest_sig.py")


if __name__ == '__main__':
    main()
