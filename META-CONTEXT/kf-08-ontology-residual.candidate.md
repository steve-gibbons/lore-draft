# KF-08 Residual Notes - Ontology Thinness / Conflation

> **Status: candidate**  
> **Addresses residual of:** KF-08  
> **Date:** 2026-08-24

## What has already advanced
- Canonical kernel (CORE-INVARIANT 12) established the three-layer ontology and made the key distinctions enforceable via Check 4 (kind + subkind).
- ASSERTION != TRUTH, EVIDENCE != AUTHORITY, ALIAS != IDENTITY, CONTEXT_HINT != TRUSTED_CONTEXT are now represented and checked.
- object-ref schema tightened (this commit) so that alias subkind carries the fields needed to preserve type, resolution, ownership and history.

## Residual gaps (still fast-follower / monitor)
1. **Remote / cross-corpus resolution** of `target_id` remains out of scope for the MVP validator. Check 7 only does advisory local resolution when a workbench objects directory is present. Unresolved references stay non-blocking with an explicit [advisory] warning.
2. **Single `status` field** still carries lifecycle + authority + epistemic load. Splitting into orthogonal dimensions is possible later but is not required for correctness of the current closed enum + transition matrix.
3. **Formal term definitions** beyond the schema descriptions and CORE-INVARIANTS remain thin; a glossary volume can absorb them when the prior-art crosswalk is accepted.

## Disposition proposal
- Treat the residual as monitored accepted risk for phase-1.
- Re-open only if a concrete exploit or interoperability failure appears that the current representation cannot express.

## Provenance
Drafted together with the object-ref schema update as the third fast-follower item. Agent-generated under author direction.
