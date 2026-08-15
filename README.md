# LORE Corpus Workbench — Local Development Guide

Welcome to the **LORE Corpus Workbench** repository scaffold.

> **Reviewers:** start at [`REVIEWERS.md`](REVIEWERS.md), not here. This page is the local
> developer/maintainer guide.

## 1. Initial Git Setup & Branching

If working in a fresh checkout:

```bash
git init
git checkout -b bootstrap/corpus-workbench-scaffold
```

## 2. Pre-Commit Hook Installation

Install the mandatory pre-commit integrity hook:

```bash
cp TOOLS/hooks/pre-commit-hash-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

The pre-commit hook enforces:
- Immudb-style write protection on `INTAKE/raw/` (`chmod a-w`).
- Automatic execution of `TOOLS/lore_validate.py` prior to committing.

## 3. Running the Standalone Validator

Execute all 10 governance and structural validation checks:

```bash
python3 TOOLS/lore_validate.py
```

To validate a specific document or fixture directory:

```bash
python3 TOOLS/lore_validate.py --path TESTS/fixtures/positive/pos_01_valid_candidate_artifact.yaml
```

## 4. Governance Principles & Operating Rules

Refer to [`AGENTS.md`](AGENTS.md) for full role definitions, authority boundaries, closed status enums, and transition matrices.
