---
id: DECISION-ONTOLOGY-ENFORCEABILITY-001
type: decision-record
status: accepted
title: "The LORE ontology is enforceable, and extended only within a domain contract"
decision_maker: "Author (Steve Gibbons), sole authority - ratified in-session 2026-08-16"
decided_at: "2026-08-16"
rationale: >
  The P1-P6 evaluation panel's headline finding (P5-1) was that LORE's ontology (the trust
  primitives in Vol 1) is largely NOT represented in the enforced schema layer - the validator
  checks document governance, not the trust ontology. Asked whether the ontology is meant to be
  descriptive or enforceable, the author decided: it IS intended to be enforced, and extended by
  domains within the confines of a governed domain contract (governance-team-owned; sketched in
  SANDBOX/domain-contract-*). This locks the direction that closes P5-1 at the doctrine level.
provenance:
  created_by: agent
  under_author_direction: true
  author_preseeded: true
  signature_pending: "Detached signature per DECISION-AUTH-IDENTITY to be attached by the author in their environment; recorded here as in-session author ratification, not a cryptographic signature the agent can produce."
  inputs:
    - path: INTAKE/eval-P1-P6-full-panel.evidence-only.md
    - path: SANDBOX/domain-contract-model.candidate.md
    - path: "LORE-v0.5-package/SOURCE-VOLUMES/LORE Volume 1 - Core Ontology and Semantic Model.md"
---

> **ACCEPTED (author-ratified in-session 2026-08-16).** Recorded by the agent under author
> direction; the cryptographic signature per `DECISION-AUTH-IDENTITY.accepted.md` remains the
> author's step (see `provenance.signature_pending`). Addresses finding **P5-1**.

# 1. Decision

1. The LORE **ontology is enforceable** - the trust primitives (OBJECT, OBJECT_REF, ASSERTION,
   EVIDENCE, AUTHORITY, CAPABILITY, EVENT, CONTEXT, RELATIONSHIP, ALIAS; Vol 1 §3, §20) are to be
   **represented in `SCHEMAS/` and checked by the validator**, not left prose-only.
2. Domains **extend** the ontology **only within a governed domain contract** (the model sketched
   in `SANDBOX/domain-contract-model.candidate.md`): additive, namespaced, versioned, signed;
   extensions may add constraints, never remove core ones; core stays the minimal TCB.

# 2. CORE-INVARIANT 12 - RATIFIED 2026-08-16 into CORE-INVARIANTS.md

> **Invariant 12 - Ontology is represented and enforced.** Every core trust primitive has a schema
> in `SCHEMAS/` and a validator check (Check 4); the ontology may be extended only by a registered
> **domain contract** whose extensions are additive, namespaced, and versioned, and which cannot
> relax any core check. *Grounded in CORE-INVARIANT 10 (represent, then enforce); closes P5-1.*

**RATIFIED** by the author in-session 2026-08-16 (on stated authority) and added to the normative
`CORE-INVARIANTS.md` as invariant 12; detached signature per `DECISION-AUTH-IDENTITY` remains the
author's environment step.

# 3. Build path (sequenced; author adopted this order 2026-08-16)

1. ✅ **DONE - `assertion` + `evidence`.** Schemas authored (`SCHEMAS/assertion.schema.json`,
   `SCHEMAS/evidence.schema.json`) and **enforced** in `lore_validate.py` Check 4:
   ASSERTION != TRUTH (a claim may hold only an agent-writable status; Vol 1 §9) and
   EVIDENCE != AUTHORITY + must be contextual (source/method/collected; Vol 1 §11-12). Proven by
   fixtures `pos_07`/`pos_08` (accepted) and `neg_07`/`neg_08` (rejected). Validator 18/0.
   P5-1 moves from "named" to "represented AND enforced" for these two primitives.
2. ✅ **DONE - `relationship` + `capability` + `event`.** Schemas authored and enforced in
   Check 4: RELATIONSHIP must be explicit and typed (subject/predicate/object; Vol 1 §19 -
   closes the typed-relationship gap all three external reviews flagged); CAPABILITY must have
   explicit scope (issuer/holder/action/scope required, expiration recommended-with-warning;
   Vol 2 §28 Inv 1); EVENT must preserve causality/accountability (event_type/timestamp/actor/
   subject; Vol 1 §15). Proven by `pos_09..11` (accepted) and `neg_09..11` (rejected). Validator 24/0.
3. ✅ **DONE - `object` + `authority` + `context` + `alias`.** Schemas authored and enforced in
   Check 4: OBJECT is typed existence (object_class required; existence != authority; Vol 1 §4/§23);
   AUTHORITY must have lineage (issuer/subject/scope/derives_from required; possession without
   lineage is not authority - invariant 11 / Vol 1 §13); CONTEXT carries a trust_level and a
   CONTEXT_HINT may not be authoritative (the reduced-trust handoff; Vol 1 §17-18); ALIAS != IDENTITY
   (alias/alias_type/resolves_to/owner/resolution_history required; Vol 2 §19). Proven by
   `pos_12..15` (accepted) and `neg_12..15` (rejected). Validator 32/0.
   **Full Vol 1 §3 ontology is now represented AND enforced** - P5-1 is closed at the primitive level.
4. ⏸ Graduate the domain-contract schema (decision **T3.4**, on hold pending author).
5. ✅ Manifest generated (decision **T3.5**): new schemas are indexed automatically - authoring all
   nine primitives needed no manifest hand-edit (the generator picked them up: 18 schemas).

## Coverage (Vol 1 §3 primitives)
Enforced: `object`, `object-ref`, `assertion`, `evidence`, `authority`, `capability`, `event`,
`context` (incl. `context_hint`/`trusted_context` via trust_level), `relationship`, `alias`.
This makes candidate **CORE-INVARIANT 12** (ontology represented + enforced) fully backed by
implementation - ready for author signature into `CORE-INVARIANTS.md`.

# 4. Provenance & scope
Derived from finding P5-1 (`INTAKE/eval-P1-P6-full-panel.evidence-only.md`) and the author's
stated intent. Tracked by `DECISION-PROSE-RECONCILIATION-001` (Tier 3.1). The author is sole
authority; the candidate invariant and the schema build remain to be scheduled/ratified.
