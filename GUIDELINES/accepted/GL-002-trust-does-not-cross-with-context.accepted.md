# GL-002 - Trust does not cross a boundary just because context does

- **id:** GL-002
- **type:** guideline (strong) - the **handoff application** of the `CONTEXT_HINT ≠ TRUSTED_CONTEXT` invariant
- **status:** accepted  (author accepted 2026-08-15, with proviso)
- **date:** 2026-08-15

> A scoped specialization, **not** a new principle: it operationalizes `CONTEXT_HINT ≠ TRUSTED_CONTEXT`
> for boundary crossings (agent→agent, env A→B, export, serialization, API). EXPERIMENTAL / provisional.

## Truism
> **Context can be copied across a boundary. Trust does not travel with the copy.**

What must be re-established at the crossing is the *relationship* - evidence, authority, scope,
time - not the bytes.

## "What survived the crossing?" - the checkpoint
At every handoff, ask of the crossed context: **provenance? authority? evidence? scope? freshness?
lifecycle? uncertainty?** Anything that did not survive must be re-established, not assumed.

## Design principle (author proviso - the load-bearing part)
Handoffs are excellent opportunities to run all sorts of checks - **but the check burden must not
fall on the human.**

1. **Automate the checks.** The system/agent runs the "what survived?" checks at the crossing; the
   human is not the checker.
2. **Make the reasonable decision the easy path.** The safe/default choice is the path of least
   resistance (cf. the engineering discipline *"make the secure path easy and the insecure path difficult"*).
3. **Unreasonable decisions are allowed - but must be *supported*.** Overriding the easy/reasonable
   path requires, and is backed by, explicit **authority + evidence + rationale**, and is recorded.
   (Break-glass style: friction + justification, never silent prohibition.)

> The human decides; the system does the work and makes the right thing easy.

## Heed it internally
LORE's own crossings - agent-to-agent handoffs (Grok / Gemini / Perplexity), exports, and the
**assisted-evaluation procedure itself** - should auto-run the crossing checks and present the easy,
reasonable default, reserving `authority + evidence + rationale` for overrides.

## Relations
- **Parent invariant:** `CONTEXT_HINT ≠ TRUSTED_CONTEXT` (this guideline applies it to handoffs).
- **Kin:** GL-001 (the metric is not the thing); LL-002 (operator context-confusion); the
  `break-glass-record` type; the discipline "make the secure path easy."
- **Note:** the proviso (easy reasonable default + justified override) is a *reusable* pattern beyond
  handoffs; it may warrant its own guideline later.

## Status
Strong guideline (advisory-strong; not validator-enforced). Lifecycle: candidate → author ratifies →
accepted. Author-only promotion.

## Disposition record (this file doubles as the record)
- **Evaluated:** C26, via the assisted-evaluation procedure.
- **Author disposition (2026-08-15):** *accepted; promote as a scoped handoff guideline, with the
  proviso that "handoffs are excellent opportunities to perform all sorts of checks, but that
  activity burden should not fall on the humans - help the human make a reasonable decision (the easy
  path) and support unreasonable decisions with authority + evidence + rationale."*
- **inputs:** C26 candidate (body SHA `67bca448…`); canonical conversation JSON (`36b5673e…`).
- **transformation:** chat-harvested handoff packaging → governed strong guideline (scoped application).
