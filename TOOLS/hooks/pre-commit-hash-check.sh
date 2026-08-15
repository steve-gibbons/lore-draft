#!/usr/bin/env bash
set -e

echo "=== Running LORE Workbench Pre-Commit Hook ==="

# INTAKE/raw integrity is enforced by lore_validate.py Check 6 via a git-preservable
# SHA-256 manifest (INTAKE/RAW-MANIFEST.sha256) — not filesystem permissions, which git
# does not preserve. Regenerate the manifest with TOOLS/lore_freeze_raw.py after any
# intake. The validator run below performs the check.

# Run lore_validate.py
if [ -f "TOOLS/lore_validate.py" ]; then
    echo "Running standalone validator..."
    python3 TOOLS/lore_validate.py
    if [ $? -ne 0 ]; then
        echo "ERROR: LORE Corpus Workbench validation failed. Commit aborted."
        exit 1
    fi
else
    echo "WARNING: TOOLS/lore_validate.py not found."
fi

echo "=== LORE Pre-Commit Check Passed ==="
exit 0
