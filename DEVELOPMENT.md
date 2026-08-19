# LORE Corpus Workbench - Local Development Guide

Welcome to the **LORE Corpus Workbench** repository scaffold.

> This is the local **developer / maintainer** guide. For orientation and the project overview,
> start at [`README.md`](README.md); reviewers, see [`REVIEWERS.md`](REVIEWERS.md).

## 0. Becoming LORE-aware (clone → reference the local TLD)

The fastest way to make an AI agent LORE-aware is to give it the corpus locally and let it
read itself:

```bash
git clone https://github.com/your-org/lore-draft
```

Then point the agent at the **now-local top-level directory** - e.g. *"start reading at
`./lore` and adopt the LORE process"*. From the TLD an agent can discover its own governance:
[`AGENTS.md`](AGENTS.md) (authority model + hard constraints), [`CORE-INVARIANTS.md`](CORE-INVARIANTS.md),
the [`REGISTRIES/`](REGISTRIES/) status enums, and the [`TOOLS/`](TOOLS/) validators. Adopt an
operating hat with `python3 TOOLS/lore_prompt.py --list`.

Reference the local path, not a URL: a checkout gives the agent the whole traceable structure
(schemas, registries, validators, raw manifest) to reason over, rather than a single rendered
page. Embedded agents (e.g. Docker's Gordon) have used exactly this pattern to produce
governed, LORE-conforming evaluations - see `INTAKE/raw/examples/docker/`.

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
