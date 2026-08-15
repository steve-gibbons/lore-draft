# LORE — Reviewer Start Here

> **EXPERIMENTAL / PROVISIONAL.** This repository and its review apparatus are for
> **evaluation of LORE itself and demonstration of principles only** — not production-ready,
> not for any other use. Your findings are welcome *input*; they are not corpus truth until
> the author accepts them.

Thank you for reviewing LORE. This page is your entry point. ~10 minutes to first finding.

This repository is a **curated public draft** of the LORE governance scaffold — the governance
model and the reviewer apparatus. It is the review target in full; there is no hidden content
to wade through.

## 1. What you are evaluating
The **v0.5 governance scaffold**:
- `AGENTS.md` — the authority & operating model (the heart of the review)
- `SCHEMAS/`, `REGISTRIES/artifact-statuses.yaml` — the object & status model
- `TOOLS/lore_validate.py` — the 10 governance checks (the enforcement TCB)
- `CORPUS-MANIFEST.yaml` and the directory scaffold (`INTAKE/`, `SOURCE/`, etc.)

> **Can't your agent reach GitHub?** Some fetchers can't read GitHub's JS UI. Use raw URLs like
> `https://raw.githubusercontent.com/steve-gibbons/lore-draft/main/AGENTS.md` — the README's
> "Agents that can't browse GitHub" section lists them.

## 2. Bootstrap (read-only)
```
git clone <this repo URL>
cd <repo>
python3 TOOLS/lore_validate.py        # expect: 12 passed, 0 failed
```
Then read `AGENTS.md`. You never need write access.

## 3. Put on your domain lens ("hat")
LORE ships governed reviewer personas. Two ways to adopt one:
- **Conversational (Copilot web / Claude / any chat with repo access):** type `hat P1`.
  The agent reads `META-CONTEXT/reviewer-panel/profiles/evaluator.txt` + the matching lens in
  `META-CONTEXT/reviewer-panel/lenses.md`, composes them, and operates as that lens.
- **Terminal:** `python3 TOOLS/lore_prompt.py P1-SEC-THREATMODEL` and adopt the printed prompt.

Wave-1 lenses (see `META-CONTEXT/reviewer-panel/reviewer-panel-roster.candidate.yaml`):

| ID | Lens |
|---|---|
| `P1-SEC-THREATMODEL` | Security · threat modeling |
| `P2-SEC-SYSTEMIC` | Security · systemic & minimalist |
| `P3-SEC-SPAFFORD` | Security · rigor / forensics / ethics |
| `P4-AI-AGENT` | AI / agent systems |
| `P5-ONTOLOGY-KR` | Knowledge representation / ontology |
| `P6-LONGHORIZON` | Long-horizon / civilizational scale |

**Named-lens rule:** a named lens is *"grounded in the public work of"* that person — never
their opinion or endorsement. Bring your own lens instead if you prefer; the profile still applies.

## 4. Evaluate — the ground rules
- **Read-only.** Make no changes to the corpus (no commits, no pushes).
- Evaluate through your lens: coherence, gaps, contradictions, unstated assumptions, fitness
  against your field's standards.
- **Cite every claim by artifact path + SHA-256.**
- Preserve uncertainty — surface it, don't resolve it. Assign no LORE status.

## 5. Hand your findings back
Produce **one self-contained, evidence-only evaluation report**: your lens, what you read
(paths + hashes), findings ranked by severity, explicit open questions, and your confidence.
**Send it to the author** — they place it into `INTAKE/` under governance. Do not edit the
corpus to "apply" findings; hand them back.

Questions or access issues → contact the author. Thank you.
