#!/usr/bin/env bash
set -e

echo "=== Running LORE Workbench Pre-Commit Hook ==="

# INTAKE/raw integrity is enforced by lore_validate.py Check 6 via a git-preservable
# SHA-256 manifest (INTAKE/RAW-MANIFEST.sha256) - not filesystem permissions, which git
# does not preserve. Regenerate the manifest with TOOLS/lore_freeze_raw.py after any
# intake. The validator run below performs the check.

# Run lore_validate.py
if [ -f "TOOLS/lore_validate.py" ]; then
    echo "Running standalone validator..."
    # NB: `cmd; if [ $? -ne 0 ]` is dead under `set -e` (errexit aborts first);
    # test the command directly instead (SIG-SH-003).
    if ! python3 TOOLS/lore_validate.py; then
        echo "ERROR: LORE Corpus Workbench validation failed. Commit aborted."
        exit 1
    fi
else
    echo "WARNING: TOOLS/lore_validate.py not found."
fi

# Guard: a `*.asc`-style rule in .gitignore would silently block NEW detached
# signatures (KEYS/*.asc, RAW-MANIFEST.sha256.asc, author-only artifact sigs)
# from being added - the core of the signing workflow (KF-01). We probe
# hypothetical paths because `git check-ignore` skips already-tracked files.
echo "Checking signatures cannot be gitignored..."
sig_bad=0
for p in KEYS/__sigguard__.asc INTAKE/__sigguard__.asc __sigguard__.asc; do
    if git check-ignore -q "$p" 2>/dev/null; then
        echo "ERROR: .gitignore would ignore '$p' - a '*.asc'-style rule crept in. Remove it."
        sig_bad=1
    fi
done
[ "$sig_bad" -eq 0 ] || { echo "ERROR: signatures would be gitignored. Commit aborted."; exit 1; }

# Guard: shell footgun signatures (SIG-SH-001 pipefail/SIGPIPE, and any later sets).
if [ -f "TOOLS/lore_lint.py" ]; then
    echo "Scanning shell scripts for footgun signatures..."
    python3 TOOLS/lore_lint.py || { echo "ERROR: shell footgun signature matched. Commit aborted."; exit 1; }
fi

echo "=== LORE Pre-Commit Check Passed ==="
exit 0
