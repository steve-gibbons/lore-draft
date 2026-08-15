# LORE — a governed-memory experiment

> **EXPERIMENTAL / PROVISIONAL public draft.** For evaluation and demonstration of principles
> only — not production-ready. Licensing is a decision-in-progress ([`DECISION-LICENSING.needs-decision.md`](DECISION-LICENSING.needs-decision.md)).

**What is this, in one breath?** LORE is a small, self-contained framework for recording not
just *what* a project decided, but **why**, **who had the authority to decide it**, and **what's
still uncertain** — in a form that both people and AI agents can read, and that neither can quietly
rewrite. Think "version control for reasoning and authority," aimed especially at AI-agent
workflows. This repo is a curated public draft of the governance scaffold.

No prior exposure needed. Start below.

## Find your part (pick the one that sounds like you)
| You are… | Open these, in order |
|---|---|
| **Just curious / no background** | this page → [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md) (we list our own weaknesses) → [`AGENTS.md`](AGENTS.md) |
| **Building AI agents** | [`AGENTS.md`](AGENTS.md) (the rules agents follow) → [`META-CONTEXT/reviewer-panel/`](META-CONTEXT/reviewer-panel/) (the "hat/lens" system) → [`.github/copilot-instructions.md`](.github/copilot-instructions.md) |
| **Security / threat-modeling** | [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md) (KF-01…) → [`CORE-INVARIANTS.md`](CORE-INVARIANTS.md) (the TCB) → [`TOOLS/lore_validate.py`](TOOLS/lore_validate.py) |
| **Ontology / knowledge representation** | [`SCHEMAS/`](SCHEMAS/) → [`REGISTRIES/artifact-statuses.yaml`](REGISTRIES/artifact-statuses.yaml) → `object-ref` (ALIAS ≠ IDENTITY) |
| **Governance / records / legal** | [`AGENTS.md`](AGENTS.md) → [`DECISION-LICENSING.needs-decision.md`](DECISION-LICENSING.needs-decision.md) → [`SOURCE/long-horizon-rationale.proposed.md`](SOURCE/long-horizon-rationale.proposed.md) |
| **A skeptic ("does it even work?")** | run the validator (below), then read [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md) — we pre-published our own flaws |
| **A formal reviewer** | [`REVIEWERS.md`](REVIEWERS.md) — the full review guide |

## Directory map / legend
**Top-level docs**
| Path | What it is |
|---|---|
| `README.md` | You are here — orientation |
| `REVIEWERS.md` | The review guide (bootstrap → hat → evaluate → hand back) |
| `AGENTS.md` | **The heart** — authority model, what agents may/may not do, the closed status set |
| `CORE-INVARIANTS.md` | The minimal "what must be true" (the trusted core / TCB), honestly marking enforced vs. asserted |
| `KNOWN-FINDINGS.md` | Our own pre-review self-assessment — known weaknesses, so reviewers skip the obvious |
| `DECISION-LICENSING.needs-decision.md` | A governed decision-*in-progress* — states the tension and the direction LORE commits to |
| `CORPUS-MANIFEST.yaml` | Machine-readable index of the corpus |
| `PROVENANCE.md` | How this public draft relates to its private origin — verifiable, without exposing it |

**Directories**
| Path | What it holds | Who cares |
|---|---|---|
| `SCHEMAS/` | The record types (JSON Schema): artifact, decision, transformation, object-ref, break-glass… | ontology, KR |
| `REGISTRIES/` | The closed status enum + who may set what (transition rules) | governance, security |
| `TOOLS/` | The validator (10 checks), the hat/prompt assembler, the git hook | everyone |
| `TESTS/` | Positive/negative fixtures proving the validator actually enforces the rules | skeptics |
| `META-CONTEXT/reviewer-panel/` | The reviewer "hats" (lenses), profiles, and the assembler's inputs | reviewers, AI |
| `SOURCE/` | The corpus's own content (currently: LORE's long-horizon rationale) | governance |
| `INTAKE/` | The landing zone for incoming evidence (raw → normalized), with immutability rules | contributors |
| `INTEGRATIONS/`, `SANDBOX/` | Phase-2 stubs | — |
| `.github/`, `.claude/` | Copilot instructions + CI; the `/lore-hat` command | AI-tool users |

## Try this
1. **Watch it check itself** (nothing to install — pure Python 3):
   ```bash
   python3 TOOLS/lore_validate.py
   ```
   Expect `12 passed, 0 failed`. That's the 10 governance rules enforcing on the test fixtures.

2. **Put on a reviewer "hat"** — adopt a domain lens and evaluate LORE. In GitHub Copilot or Claude
   with this repo open, just type:
   ```
   hat P1
   ```
   (or run `python3 TOOLS/lore_prompt.py P1-SEC-THREATMODEL`). Try `hat list` to see all six lenses.

3. **Read the honest self-critique** — [`KNOWN-FINDINGS.md`](KNOWN-FINDINGS.md). A governance system
   that publishes its own weaknesses before you find them is either confident or foolish; you decide.

4. **See the core idea in one file** — [`PROVENANCE.md`](PROVENANCE.md). This public repo proves
   where it came from *without* being able to reconstruct the private source. That's ALIAS ≠ IDENTITY,
   made literal.

5. **See reasoning preserved, not just outcomes** — [`DECISION-LICENSING.needs-decision.md`](DECISION-LICENSING.needs-decision.md)
   records a decision *before it's made*: the tension, the options, and the direction chosen.

## For maintainers
Run the validator as above. To install the pre-commit integrity hook (write-protects `INTAKE/raw/`
and runs the validator before each commit):
```bash
cp TOOLS/hooks/pre-commit-hash-check.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```
CI runs the same validator on every push/PR (`.github/workflows/validate.yml`).

## Governance
[`AGENTS.md`](AGENTS.md) is authoritative — role definitions, authority boundaries, the closed status
set, and transition rules. Everything else is downstream of it.
