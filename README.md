# LORE - a governed-memory experiment

> **EXPERIMENTAL / PROVISIONAL.** For evaluation and demonstration of principles only - not
> production-ready. The licensing direction is recorded in
> [`DECISION-LICENSING.accepted.md`](DECISION-LICENSING.accepted.md) (evaluation-only now →
> Apache-2.0 + CC BY 4.0 at the **v1.0.0** milestone; the draft license text lives in the public
> draft repo).

> **Maintainers / developers:** local setup - clone, hooks, validator - is in
> [`DEVELOPMENT.md`](DEVELOPMENT.md).  **Reviewers:** start at [`REVIEWERS.md`](REVIEWERS.md).

**What is this, in one breath?** LORE is a small, self-contained framework for recording not just
*what* a project decided, but **why**, **who had the authority to decide it**, and **what's still
uncertain** - in a form that both people and AI agents can read, and that neither can quietly
rewrite. Think "version control for reasoning and authority," aimed especially at AI-agent
workflows. This is the **public curated draft** of LORE (not the private canonical tree). It is an
intentional, freeze-cut export for evaluation and demonstration. The private repository
may be ahead; bounded lag is by design. Ask "which edition am I on?" — see the release
tag and `CORPUS-MANIFEST.yaml` `version:` field.

No prior exposure needed. Start below.

## Try it (no install)
Open this repo in any agent that can read a repository - GitHub Copilot Chat, Claude, etc. - and say:

> **Use LORE to evaluate LORE.**

The agent picks up [`AGENTS.md`](AGENTS.md) (and [`.github/copilot-instructions.md`](.github/copilot-instructions.md)),
adopts LORE's own reviewer lenses, and turns them back on LORE itself - a self-referential
evaluation that is also the fastest way to see what the framework *does*. Compare what it finds
against our own [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md). For a local
agent, clone and point it at the top-level directory - see [`DEVELOPMENT.md`](DEVELOPMENT.md).

**Want to read LORE itself?** Normative volumes live under [`SOURCE/`](SOURCE/) (core set: [`SOURCE/CORE-VOLUMES/`](SOURCE/CORE-VOLUMES/), *Origin & Design Intent* → *Implementation*). Extended and historical material is under the other `SOURCE/` trees. Public-draft shape may differ — see PROVENANCE on that edition.

## Find your part (pick the one that sounds like you)
| You are… | Open these, in order |
|---|---|
| **Just curious / no background** | this page → [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md) (we list our own weaknesses) → [`AGENTS.md`](AGENTS.md) |
| **Building AI agents** | [`AGENTS.md`](AGENTS.md) (the rules agents follow) → [`META-CONTEXT/reviewer-panel/`](META-CONTEXT/reviewer-panel/) (the "hat/lens" system) → [`.github/copilot-instructions.md`](.github/copilot-instructions.md) |
| **Security / threat-modeling** | [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md) (KF-01…) → [`CORE-INVARIANTS.md`](CORE-INVARIANTS.md) (the TCB) → [`TOOLS/lore_validate.py`](TOOLS/lore_validate.py) |
| **Ontology / knowledge representation** | [`SCHEMAS/`](SCHEMAS/) → [`REGISTRIES/artifact-statuses.yaml`](REGISTRIES/artifact-statuses.yaml) → `object-ref` (ALIAS ≠ IDENTITY) |
| **Governance / records / legal** | [`AGENTS.md`](AGENTS.md) → [`DECISION-LICENSING.accepted.md`](DECISION-LICENSING.accepted.md) → [`SOURCE/long-horizon-rationale.accepted.md`](SOURCE/long-horizon-rationale.accepted.md) |
| **Setting up locally / maintaining** | [`DEVELOPMENT.md`](DEVELOPMENT.md) - clone, hooks, validator |
| **A formal reviewer** | [`REVIEWERS.md`](REVIEWERS.md) |

## Directory map / legend
**Top-level docs**
| Path | What it is |
|---|---|
| `README.md` | You are here - orientation |
| `DEVELOPMENT.md` | Local developer / maintainer guide (clone, hooks, validator) |
| `REVIEWERS.md` | The review guide |
| `AGENTS.md` | **The heart** - authority model, what agents may/may not do, the closed status set |
| `CORE-INVARIANTS.md` | The minimal "what must be true" (the trusted core / TCB), honestly marking enforced vs. asserted |
| `KNOWN-FINDINGS.md` | Our own pre-review self-assessment - known weaknesses |
| `DECISION-LICENSING.accepted.md` | The licensing decision (eval-only → Apache-2.0 + CC BY 4.0 at v1.0.0) |
| `DECISION-AUTH-IDENTITY.accepted.md` | The KF-01 decision - binding author authority to a signature, not a self-set flag |
| `GOVERNANCE-LOCKIN.action.md` | Open owner action - the governance-formation gate for v1.0.0 |
| `CORPUS-MANIFEST.yaml` | Machine-readable index of the corpus |

**Directories** (the core governance scaffold; the repo also holds working drafts, evidence, and release bundles)
| Path | What it holds | Who cares |
|---|---|---|
| `SCHEMAS/` | The record types (JSON Schema): artifact, decision, transformation, object-ref, break-glass…; plus the enforced core ontology - object, assertion, evidence, authority, capability, event, context, relationship, alias | ontology, KR |
| `REGISTRIES/` | The closed status enum + who may set what (transitions) + trusted signers | governance, security |
| `TOOLS/` | The validator (10 checks), the hat/prompt assembler, the author-signature gate, the git hook | everyone |
| `TESTS/` | Positive/negative fixtures proving the validator actually enforces the rules | skeptics |
| `META-CONTEXT/` | Reviewer "hats" (lenses), the self-assessment, and process records | reviewers, AI |
| `SOURCE/` | Normative sources (corpus consolidation target); working volumes are in the `Draft *` dirs | anyone reading LORE |
| `INTAKE/` | The landing zone for incoming evidence (raw → normalized), with immutability rules | contributors |
| `INTEGRATIONS/`, `SANDBOX/` | Phase-2 stubs | - |
| `.github/`, `.claude/` | Copilot instructions + CI; the `/lore-hat` command | AI-tool users |

## Try this
1. **Watch it check itself** (nothing to install - pure Python 3):
   ```bash
   python3 TOOLS/lore_validate.py
   ```
   The 10 governance rules enforce on the test fixtures (`N passed, 0 failed`).

2. **Put on a reviewer "hat"** - adopt a domain lens and evaluate LORE. In an agent with this repo
   open, type `hat P1` (or run `python3 TOOLS/lore_prompt.py P1-SEC-THREATMODEL`). `hat list` shows
   all six lenses.

3. **Read the honest self-critique** - [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md).
   A governance system that publishes its own weaknesses before you find them is either confident or
   foolish; you decide.

4. **See reasoning preserved, not just outcomes** - [`DECISION-LICENSING.accepted.md`](DECISION-LICENSING.accepted.md)
   records a decision with its tension, options, and the direction chosen.

## Deployment & updates (not realtime)
LORE is consumed as a point-in-time **snapshot** (what you clone is what you run) and updated by
**periodic, rarely-interrupting conversation handoffs** - an *edition* cadence, not a live feed.
Handoffs arrive at reduced trust and are promoted on your schedule. Bounded staleness is normal and
by design; ask "which edition am I on, and when was it cut?" See
[`DECISION-DEPLOYMENT-UPDATE-MODEL.accepted.md`](DECISION-DEPLOYMENT-UPDATE-MODEL.accepted.md).

## Governance
[`AGENTS.md`](AGENTS.md) is authoritative - role definitions, authority boundaries, the closed status
set, and transition rules. Everything else is downstream of it. Local setup and maintenance live in
[`DEVELOPMENT.md`](DEVELOPMENT.md).
