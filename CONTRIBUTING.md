# Contributing to the LORE Corpus Workbench

This document codifies the standard workflow for anyone working with the LORE corpus
and workbench harness — human authors, agents, or reviewers. Read it before making
any changes to governed artifacts.

---

## Mental model in one paragraph

LORE objects pass through a lifecycle: created by an agent in a writable status
(`candidate`, `proposed`, etc.), validated by the governance checks, and promoted by
the **author** to an author-only status (`accepted`, `verified`, etc.) once the artifact
meets the governance bar. Transport lands objects in quarantine — receipt is not trust.
Every status transition is recorded in the event log. Cryptographic signing by the author
makes promotion non-repudiable and is required at v1.0.0.

---

## Quickstart

```sh
# 1. Initialise a local workbench (one-time per machine)
lore init [--generate-token]

# 2. Create an object
lore create assertion --file draft.yaml   # writes to ~/.lore/objects/assertion/

# 3. Validate before committing
lore check draft.yaml                     # single artifact
lore validate                             # full corpus + fixtures

# 4. Author promotes when ready
lore promote assertion:local:<id> accepted --reason "reviewed"

# 5. (Author) Sign the promoted artifact
gpg --armor --detach-sign -u '<root-fpr>!' path/to/artifact.yaml

# 6. Re-run full validation
lore validate
```

---

## Workflow step by step

### Step 1 — Initialise the workbench

```sh
lore init
```

Creates `~/.lore/` (or `$LORE_HOME/`) with the object store, event log, config, and
secrets directories. Use `--generate-token` if you plan to run `lore serve` and need
transport authentication. Use `--force` to reinitialise over an existing config.

The workbench lives at `~/.lore` by default, decoupled from any repo checkout, so
`lore` commands work from any directory. Override with `$LORE_HOME`.

---

### Step 2 — Create objects

```sh
lore create <kind> [--subkind <subkind>] [--file FILE] [--status STATUS]
```

**Kinds:** `principal` · `policy` · `object-ref` · `relationship` · `act` · `assertion` ·
`authority` · `capability` · `handoff`

**Subkinds:** `object-ref/alias` · `act/event` · `assertion/evidence` ·
`assertion/evaluation` · `assertion/context-hint`

New objects start in `candidate` status by default. The harness only allows
**agent-writable** statuses at creation time. The printed id (e.g.
`assertion:local:3f8a2b1c`) is the stable reference to use in other objects.

Content may be supplied via `--file draft.yaml`, `--stdin`, or added to the content
block after creation.

---

### Step 3 — Validate

```sh
lore check draft.yaml          # fast single-artifact check (exits 0/1)
lore validate                  # full 10-check corpus + test fixtures
lore validate --file FILE      # validate one file as part of the full harness
```

`lore check` is designed for editor save-hooks and pre-commit workflows. It validates
the schema, status enum, transition legality, and kind-specific required fields —
all in one pass with structured JSON output if needed (`--format json`).

`lore validate` is the CI gate. It runs all 10 governance checks, verifies INTAKE/raw
manifest integrity, and exercises all test fixtures. **This must pass before any
commit.**

The pre-commit hook at `TOOLS/hooks/pre-commit-hash-check.sh` runs `lore validate`
automatically. Install it:

```sh
cp TOOLS/hooks/pre-commit-hash-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---

### Step 4 — Handoffs (agent coordination)

```sh
lore handoff create --from agent:a --to agent:b --objective-ref OBJ-001
lore handoff inbox          # pending handoffs + gate status
lore handoff show <id>      # full record
```

Handoffs are coordination records, not kernel objects. They carry epistemic separation
(`observations` vs. `inferences` vs. `recommendations`), a `human_gate` field, and an
`effect_class` (`none` · `destructive` · `external`). A gate of `approve-promote`,
`approve-destructive`, or `approve-external` requires an author decision before the
referenced action proceeds.

---

### Step 5 — Author promotion

Promotion is an **author act**. The harness enforces:
- Target status must be in the `author_only` enum (`accepted`, `normative`, `canonical`,
  `verified`, `released`, `superseded`, `deleted`).
- The transition from the current status must appear in `REGISTRIES/artifact-statuses.yaml`.

```sh
lore promote <ref> <new-status> [--reason "text"]
```

`<ref>` may be a full id (`assertion:local:abc12345`), a kind:ns:id, or a file path.

After promoting, **sign the artifact** (required at v1.0.0, see
`DECISION-AUTH-IDENTITY.accepted.md`):

```sh
gpg --armor --detach-sign -u '<root-fpr>!' path/to/artifact.yaml
# Then add to the artifact:
#   provenance:
#     signature: path/to/artifact.yaml.asc
#     signer_fpr: "<40-hex fingerprint>"
```

---

### Step 6 — Export

```sh
lore export --format summary                   # overview table
lore export --min-status --format jsonl        # accepted+ objects as JSON stream
lore export --kind assertion --out ./review/   # all assertions → directory
```

`lore export` de-envelopes the stored objects and writes the clean content payload.
It does not modify the workbench; it is safe to run at any time.

---

### Step 7 — Transport (serve / pull / push)

```sh
lore serve [--listen HOST:PORT]   # default 127.0.0.1:22469
lore pull http://host:port/v1/objects/<id>
lore push http://host:port <object-ref>...
```

**Receipt is not trust.** Pulled/pushed objects land in `quarantined` status
regardless of what the payload claims. Promote manually after review.

The transport token (generated at `lore init --generate-token`) authenticates
network access to the workbench. It authorises **quarantine import only** — never
promotion or destructive clearance.

---

## Governance checks (what CI enforces)

| Check | What it verifies |
|-------|-----------------|
| 1 | Status is in the closed enum |
| 2 | Author-only status is backed by a signature or preseed flag (KF-01) |
| 3 | Status transition is allowed by the transition matrix |
| 4 | Kind-specific required fields are present |
| 5 | SHA-256 hash matches referenced file (when declared) |
| 6 | INTAKE/raw evidence matches the RAW-MANIFEST.sha256 |
| 7 | object-ref has a valid target_id |
| 8 | derived/generated objects name their inputs |
| 9 | Unverified proposals retain an uncertainty status |
| 10 | CORPUS-MANIFEST.yaml is present and consistent |

Run `lore validate` locally before pushing. CI (`validate.yml`) runs the same checks
on every push and pull request and will block merge on failure.

---

## Adding a new fixture

Place positive cases in `TESTS/fixtures/positive/pos_NN_<description>.yaml` and negative
cases in `TESTS/fixtures/negative/neg_NN_<description>.yaml`. The validator picks them
up automatically. Name them so the filename describes the invariant being tested.
Verify with `lore validate` or `python3 TESTS/test_validator.py`.

---

## File layout reference

```
TOOLS/               Python tools (lore_*.py) — one concern per file
TESTS/fixtures/      Positive and negative validator fixtures
REGISTRIES/          Closed enums and transition rules (source of truth)
SCHEMAS/             JSON Schema per kind + object-envelope.schema.{json,yaml}
INTAKE/raw/          Raw evidence files (immutable after lore freeze)
DECISIONS/           Accepted governance decisions
GUIDELINES/          Accepted guidelines
LESSONS_LEARNED/     Accepted lessons
META-CONTEXT/        Reviewer panel, lenses, context records
~/.lore/             Runtime workbench state (outside the repo)
```

---

## Key invariants to keep in mind

- **OBJECT_REF ≠ OBJECT** — store references, not embedded envelopes.
- **ASSERTION ≠ TRUTH** — assertions must hold agent-writable status only.
- **ALIAS ≠ IDENTITY** — aliases require type, resolution, ownership, and history.
- **Authority has lineage** — possession without lineage is not authority (Inv 11).
- **A thing cannot be accountable** — destructive/external acts must name a human
  principal in the `accountable` field (Inv 13).
- **Receipt is not trust** — quarantine first, promote after review.
- **Represent, then enforce** — model the constraint first, then add the gate (Inv 10).
