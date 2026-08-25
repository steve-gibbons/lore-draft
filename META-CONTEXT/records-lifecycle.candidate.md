# Minimal Records Lifecycle & Disposition Model for LORE

> **Status: candidate**  
> **Addresses:** KF-12  
> **Date:** 2026-08-24

## Problem restated
LORE preserves everything by design (supersede-not-delete). That satisfies provenance and audit goals but leaves no explicit retention schedule, disposition authority, or legal-hold concept. ISO 15489 and records-management practice expect these.

## Minimal model (phase-1)

### 1. Retention classes (proposed closed set)
- `retain-indefinite` - default for accepted / normative / canonical design records and all raw evidence under INTAKE/raw.
- `retain-while-relevant` - working candidates, proposals, and intermediate evaluations that may be pruned after supersession once a human has confirmed no residual value.
- `retain-legal-hold` - explicit override that freezes disposition regardless of other class.

### 2. Disposition actions
- `supersede` - already implemented; the prior record remains in the corpus with status `superseded`.
- `archive` - move to a designated long-term storage projection (future; not required for MVP).
- `expunge` - hard removal. **Forbidden** for any record that has ever held an author-only status or that appears in a RAW-MANIFEST, unless a break-glass record + dual human authorization is present.

### 3. Authority
- Only a human principal with author-level authority may assign or change a retention class or issue a legal-hold.
- Agents may propose a retention class on new candidate records; they may never clear a legal-hold or authorize expunge.

### 4. Legal-hold
- A legal-hold is itself a LORE record (proposed type: assertion/subkind or a dedicated policy record) that references the held objects by id.
- While a hold is active, disposition actions other than supersede are blocked by policy (enforcement can begin as validator warnings and graduate to hard checks).

### 5. Default for the current corpus
- All existing accepted / normative material and all INTAKE/raw content are treated as `retain-indefinite`.
- No expunge path is opened by this candidate.

## Implementation notes (non-blocking for acceptance of the model)
- Schema addition for an optional `retention_class` field on artifact records can follow later.
- Validator Check for legal-hold can be added once the record type is accepted.
- Until then, the model is asserted policy that humans and agents are expected to follow.

## Relationship to other findings
- Complements the OAIS / ISO 15489 mapping in the prior-art crosswalk (KF-09).
- Does not relax the supersede-not-delete invariant for authoritative records.
- Keeps the core/deployment boundary intact (CORE-INVARIANT 14).

## Provenance
Drafted 2026-08-24 as the sixth and final fast-follower item in this pass. Agent-generated under author direction.
