# LORE Corpus Workbench

The **LORE Corpus Workbench** — a governance and provenance scaffold for a corpus of
governed context. This repository is a curated public draft; see [`PROVENANCE.md`](PROVENANCE.md).

> **Reviewers:** start at [`REVIEWERS.md`](REVIEWERS.md). This page is the maintainer guide.

## Validate the corpus
Run all 10 governance and structural validation checks:

```bash
python3 TOOLS/lore_validate.py
```

Validate a specific document or fixture:

```bash
python3 TOOLS/lore_validate.py --path TESTS/fixtures/positive/pos_01_valid_candidate_artifact.yaml
```

## Pre-commit integrity hook (optional, for maintainers)

```bash
cp TOOLS/hooks/pre-commit-hash-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Enforces write-protection on `INTAKE/raw/` and runs the validator before each commit.

## Governance principles & operating rules
See [`AGENTS.md`](AGENTS.md) for role definitions, authority boundaries, closed status enums,
and transition matrices.
