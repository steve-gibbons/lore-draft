#!/usr/bin/env bash
set -e

echo "=== Running LORE Workbench Pre-Commit Hook ==="

# Check write permissions on INTAKE/raw/
if [ -d "INTAKE/raw" ]; then
    WRITABLE_RAW=$(find INTAKE/raw -type f -perm /222 2>/dev/null || true)
    if [ -n "$WRITABLE_RAW" ]; then
        echo "ERROR: Writable files detected under INTAKE/raw/. Raw evidence must be read-only (chmod a-w)."
        echo "Writable files:"
        echo "$WRITABLE_RAW"
        exit 1
    fi
fi

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
