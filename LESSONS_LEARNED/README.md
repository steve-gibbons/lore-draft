# LESSONS_LEARNED

Scar tissue for the LORE workbench - lessons distilled from what actually happened while building
and operating LORE, recorded so the *why* survives (Vol 91 Evidence Preservation; the "learn
lessons, not mechanisms" principle).

## Convention
- `candidates/` - **proposed** lessons (agent- or human-drafted). Status `proposed` / `candidate`;
  **not normative** until the author accepts (promotion out of `candidates/` is author-only).
- Each lesson records, in LORE terms:
  - **Problem** - what failed / nearly failed.
  - **Circumstance filters** - the applicability conditions (when the lesson applies; Vol 68 Context /
    Vol 120 Validity). A lesson without its filters is a superstition.
  - **Recipe** - the remedy/procedure *under those circumstances*.
  - **Evidence** - observed facts (assertion ≠ evidence), with hashes / commit refs.
  - **Provenance** - inputs + transformation (incident → generalized lesson).
- Structured to conform to the LORE `anti-pattern` schema (`problem` + `remedy`) where applicable.

## Lifecycle
1. **candidate** - drafted (agent or human) in `candidates/`; status `proposed` / `candidate`.
2. **accepted** - the author ratifies; the lesson moves out of `candidates/` (e.g. to `accepted/`)
   and its status becomes author-set (`accepted` / `normative`).

Promotion is **author-only**. A lesson never self-promotes; each records its own lifecycle state.
