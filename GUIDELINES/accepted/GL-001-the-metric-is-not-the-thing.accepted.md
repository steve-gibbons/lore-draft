# GL-001 - The metric is not the thing

- **id:** GL-001
- **type:** guideline (strong)  - advisory-strong, **not** a hard invariant (cf. `CORE-INVARIANTS.md`)
- **status:** accepted  (author accepted as a candidate for a strong guideline, 2026-08-15)
- **date:** 2026-08-15

> A strong guideline LORE heeds **internally**. The caution is borrowed from a neighboring domain
> (systems science / economics) - attributed, not claimed as novel LORE doctrine. EXPERIMENTAL / provisional.

## Truism
> **The metric is not the thing.**

A metric is an *assertion-generating process*, not evidence of the thing it measures. And
measurement is an **intervention**: what you measure becomes what you manage, becomes an incentive,
becomes changed behavior - even when no one is trying to "game" anything.

## Known failure patterns
1. **Goodhart** - when a metric becomes a target, it ceases to be a good metric.
2. **Proxy damage** - optimizing a proxy can damage the thing the proxy represents.
3. **Reflexivity** - measuring changes the system measured; observation is not passive.
4. **Proxy-confidence detachment** - a score detaches from context, authority, and evidence,
   reintroducing the very failure LORE exists to attack.

## Attribution (neighboring domain)
This is **Goodhart's law** and its relatives (Campbell's law, the cobra effect) from systems science,
economics, and management cybernetics. LORE **adopts and attributes** it - it is not novel to LORE
(prior-art honesty; cf. KF-09).

## Heed it internally (self-application)
Every LORE-produced number - trust score, confidence, coverage, completeness, validation pass-rate -
is an **assertion**, not evidence of the underlying object, and MUST carry the same lifecycle /
provenance / scope discipline as any governed object. LORE must not let its own scores become
proxy-confidence.

> **Live example (this corpus):** during the KF-06 hardening, `python3 TOOLS/lore_validate.py`
> reported **`12 passed, 0 failed`** *against a corrupted evidence file* - the manifest had been
> regenerated over the mutation (see LL-001). The metric said "healthy"; the thing was not.
> `12/12` is a metric, not the integrity it stands for.

## Status of this guideline
- **Strong guideline** = strongly recommended; shapes design and review, but is not validator-enforced.
  If it later warrants enforcement, it graduates to `CORE-INVARIANTS.md`.
- Lifecycle: **candidate** → author ratifies → **accepted** (strong guideline). Author-only promotion.

## Disposition record (this file doubles as the record)
- **Evaluated:** C16 (metric-as-intervention / Goodhart), via the assisted-evaluation procedure.
- **Author disposition (2026-08-15):** *accept as a candidate for a strong guideline; the caution
  comes from a neighboring domain and we heed it internally; pass "The metric is not the thing" as a
  truism with known failure patterns.*
- **inputs:** C16 candidate `INTAKE/raw/lore-recovery/04_candidates/C16_metrics_measurement_intervention.candidate.md`
  (body SHA `1bd38b95…`); canonical conversation JSON (`36b5673e…`).
- **transformation:** promotion of a chat-harvested concept into a governed strong guideline.
