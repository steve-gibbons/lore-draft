# LORE Prior-Art Crosswalk (candidate)

> **Status: candidate**  
> **Addresses:** KF-09 (Unmapped overlap with prior art)  
> **Authority:** Agent-drafted under author direction. Not yet accepted.  
> **Date:** 2026-08-24

## Purpose
Make the relationship between LORE and established standards explicit so reviewers and adopters can see what is reused, what is specialized, and what is intentionally different. This is a mapping, not a claim of conformance.

## 1. W3C PROV-O / PROV-DM

**Core PROV concepts**
- Entity - a thing with fixed aspects
- Activity - something that occurs over time and acts on entities
- Agent - something that bears some form of responsibility for an activity

**Key relationships**
- wasGeneratedBy, used, wasDerivedFrom, wasAttributedTo, wasAssociatedWith, actedOnBehalfOf

**LORE mapping**
| PROV concept | LORE counterpart | Notes |
|--------------|------------------|-------|
| Entity | object (abstract) / concrete kinds (principal, assertion, evidence, ...) | LORE makes kinds first-class via `type` + `subkind` |
| Activity | act (subkind event when triggered) | LORE distinguishes act from the resulting state |
| Agent | principal (principal_kind = human / thing / organization / service) | Accountability is restricted to human principals (inv 13) |
| wasDerivedFrom | transformation-record + inputs list | Explicit, hash-bound |
| wasGeneratedBy | transformation or act that produced the artifact |
| wasAttributedTo / wasAssociatedWith | authority + capability + accountable field | LORE requires lineage on authority |
| Provenance of the provenance | CORPUS-MANIFEST + RAW-MANIFEST + signatures | LORE treats the corpus itself as governed |

**Deliberate differences**
- LORE adds a closed status enum and authority boundary that PROV does not prescribe.
- LORE separates ALIAS from IDENTITY and ASSERTION from TRUTH as enforceable invariants.
- LORE keeps the validator dependency-free and the corpus file-native for the MVP.

## 2. OAIS / ISO 14721 (Open Archival Information System)

**Relevant OAIS packages**
- SIP (Submission Information Package)
- AIP (Archival Information Package)
- DIP (Dissemination Information Package)

**LORE mapping**
- INTAKE/raw + freeze manifest ≈ SIP landing + integrity check
- Governed corpus (accepted / normative records + schemas + registries) ≈ AIP
- Public draft export / handoff packages ≈ DIP (point-in-time, reduced-trust by design)

**Preservation actions**
- Supersede-not-delete aligns with OAIS preservation of provenance.
- LORE does not yet model full retention schedules or media migration (see KF-12).

## 3. ISO 15489 (Records Management)

**Key ideas**
- Authenticity, reliability, integrity, usability
- Capture, classification, access, retention, disposition

**LORE mapping**
- Authenticity / integrity: signature binding (KF-01 Option C) + raw-manifest hashes
- Reliability: explicit rationale and uncertainty preservation
- Capture: INTAKE pipeline
- Classification: closed status enum + ontology kinds
- Access / disposition: still thin (KF-12 remains open)

LORE is intentionally stronger on authority lineage and agent-vs-author separation than a classic records system, and weaker on formal retention schedules.

## 4. Event-sourcing / CQRS style systems

**Typical pattern**
- Append-only event log is the source of truth
- Current state is a projection
- Commands produce events; queries read projections

**LORE current posture**
- Primary store is still file-state + git history, not a pure event log.
- transformation-record and act/event records provide an explicit change history.
- Status transitions are constrained, but concurrency / merge semantics are not yet governance-aware (see KF-15).

**Future alignment opportunity**
- Treat accepted status changes and authority grants as the event types.
- Maintain a "current-accepted" projection separate from full history.
- Keep the file representation as one possible projection rather than the sole store.

## 5. Summary table

| Standard | Reused ideas | LORE specialization | Gap still open |
|----------|--------------|---------------------|----------------|
| PROV-O | Entity / Activity / Agent, derivation | Closed status, authority lineage, ALIAS != IDENTITY | Formal OWL export |
| OAIS | SIP / AIP / DIP packaging, integrity | Point-in-time public draft, signature gates | Full media / migration model |
| ISO 15489 | Authenticity, capture, classification | Agent authority boundary, uncertainty preservation | Retention / legal-hold |
| Event-sourcing | Explicit change history | File + git as current store | Act-vs-State projections, merge rules |

## Provenance
Drafted 2026-08-24 as the second fast-follower item for KF-09. Agent-generated under author direction. Status remains `candidate` until author acceptance.
