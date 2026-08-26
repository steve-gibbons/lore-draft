# MAP.md — LORE corpus at a glance

> **Purpose.** One page that lets a human or agent see the corpus as a coherent whole.
> Not a second README. Not a status claim. Not governance lock-in.
>
> **Edition.** This is the **public curated draft** (`lore-draft`). The private canonical tree
> is separate. Ask "which edition am I on?" → `CORPUS-MANIFEST.yaml` `version:` (currently
> **v0.6.2 candidate**) and the release tag.
>
> **Posture.** EXPERIMENTAL / PROVISIONAL. Evaluation and demonstration of principles only.

---

## What LORE is (one system)

A **file-native governed memory** for decisions, authority, and uncertainty — especially where
humans and agents share work. Information survives; context usually does not. LORE records not
only *what* was decided, but *why*, *who had authority*, and *what remains uncertain*, in a form
neither side can quietly rewrite.

Three load-bearing layers:

| Layer | Job | Where |
|-------|-----|-------|
| **Rules** | Who may write what; closed statuses; authority boundary | `AGENTS.md`, `REGISTRIES/` |
| **Shape** | What a record is; kinds, refs, ontology | `SCHEMAS/`, ontology decisions |
| **Enforcement** | Checks at rest and in CI | `TOOLS/lore_validate.py`, hook, `.github/workflows/` |

Everything else is **content** (SOURCE, decisions), **process** (META-CONTEXT, ACTION_ITEMS),
or **evidence** (INTAKE).

---

## Two trees, one corpus

| Tree | Role |
|------|------|
| **Private canonical (`lore`)** | Full workbench, action-item lifecycle, true authority surface |
| **Public draft (`lore-draft`)** | Freeze-cut evaluation snapshot; bounded lag; what outsiders and agents see |

This repository is the public draft. Provenance of the cut is in `PROVENANCE.md`.
Deployment is **edition cadence**, not a live feed — see `DECISION-DEPLOYMENT-UPDATE-MODEL.accepted.md`.

---

## The spine (seven orientation points)

Read these when you need the whole, not a fragment:

| # | File | What it carries |
|---|------|-----------------|
| 1 | `README.md` | Problem, insight, distinctions, non-goals, audience paths |
| 2 | `AGENTS.md` | Authority model; agent may/may not; closed status set |
| 3 | `CORE-INVARIANTS.md` | Trusted core (TCB); enforced vs asserted |
| 4 | `DECISION-ONTOLOGY-CANONICAL-KERNEL.accepted.md` | Kinds, projections, ALIAS ≠ IDENTITY |
| 5 | `DECISION-AUTH-IDENTITY.accepted.md` | Signature-bound author authority (KF-01 Option C) |
| 6 | `KNOWN-FINDINGS.md` | Honest self-assessment; dispositions |
| 7 | `GOVERNANCE-LOCKIN.action.md` | Open owner gate for v1.0.0 — not yet done |

`MAP.md` (this file) is the index to that spine, not a replacement for any of it.

---

## How work flows

```
INTAKE/raw  →  freeze / hash  →  records (candidate …)  →  human promote (signature)
                      ↓
                 validator + CI
                      ↓
         current-accepted  vs  full-history
                      ↓
              public export (edition cut)
```

- Agents write only **agent-writable** statuses (`candidate`, `proposed`, `derived`, …).
- Humans own **author-only** statuses (`accepted`, `normative`, `canonical`, …).
- Git is the concurrency unit; the validator is the governance unit at rest.

---

## Directory map (condensed)

| Path | Holds |
|------|--------|
| `AGENTS.md`, `CORE-INVARIANTS.md`, `KNOWN-FINDINGS.md` | Rules, TCB, self-critique |
| `DECISION-*.accepted.md` | Binding design decisions (licensing, auth, ontology, deployment, …) |
| `SCHEMAS/` | Record types and core ontology (JSON Schema) |
| `REGISTRIES/` | Status enum, transitions, trusted signers |
| `TOOLS/` | Validator, YAML TCB, signature gate, workbench CLIs |
| `TESTS/` | Fixtures proving the rules actually fire |
| `SOURCE/` | Normative volumes / consolidation target |
| `INTAKE/` | Immutable raw landing zone + freeze path |
| `META-CONTEXT/` | Hats/lenses, process notes, adoption path, prior-art, lifecycle |
| `WORKBENCH/` | Local demo / smoke path |
| `INTEGRATIONS/`, `SANDBOX/` | Phase-2 stubs |
| `.github/` | CI (`validate.yml`), PR template, Copilot instructions |

---

## What is already present (pieces are here)

| Area | State |
|------|--------|
| Authority boundary + closed statuses | Enforced (`AGENTS.md`, registries, Check 2) |
| Signature-bound author identity | Accepted decision + strict verify path |
| Ontology kernel + object-ref / alias rules | Accepted; schema tightened |
| Validator (10 checks) + pre-commit + CI | Live and green on this draft |
| Dependency-free YAML load/output TCB | Load dual-path; output pinned to `lore_yaml` |
| Adoption path (Level 0/1/2) | Accepted (`META-CONTEXT/adoption-path.accepted.md`) |
| Prior-art crosswalk (PROV-O, OAIS, ISO 15489, event-sourcing) | Accepted |
| Records lifecycle / disposition model | Accepted (policy level; schema later) |
| Act-vs-State / projections / concurrency notes | Accepted |
| README pitch spine (problem, distinctions, non-goals) | Applied |
| PR template | Present |

---

## What is gated (not claimed done)

| Item | Why it matters |
|------|----------------|
| **GOVERNANCE-LOCKIN** | Blocks v1.0.0 relicense (Apache-2.0 + CC BY 4.0). Owner survey → participants → charter → rights. |
| **KF-01 T5 key-custody** | Residual of signature work |
| Multi-tenant / live API / federation / enterprise connectors | Explicit non-goals for this stage |
| Materialized event-sourcing projections | Documented opportunity, not required for MVP |

Until governance lock-in completes, LORE stays under the **provisional evaluation** license.
That is intentional, not an omission on this map.

---

## Orient by role

| You are… | Start here |
|----------|------------|
| New reader | `README.md` → this map → `KNOWN-FINDINGS.md` |
| Agent / implementer | `AGENTS.md` → `CORE-INVARIANTS.md` → `TOOLS/` |
| Security / threat model | `KNOWN-FINDINGS.md` → `CORE-INVARIANTS.md` → validator |
| Ontology / KR | `SCHEMAS/` → ontology decisions → `object-ref` |
| Governance / records | `AGENTS.md` → licensing + long-horizon decisions → lifecycle notes |
| Formal reviewer | `REVIEWERS.md` |
| Local maintainer | `DEVELOPMENT.md` |

---

## Quick verification (no install story beyond Python 3)

```bash
python3 TOOLS/lore_validate.py
```

CI runs the same family of checks on every push (`LORE validate` workflow).

Self-eval prompt for any repo-capable agent:

> Use LORE to evaluate LORE.

Compare results against `KNOWN-FINDINGS.md`.

---

## Provenance of this map

Drafted 2026-08-25 under author direction to close the "corpus as coherent whole" gap without
advancing governance lock-in or changing edition status. Orientation only; doctrine remains in the
spine files above.
