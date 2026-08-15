# LORE v0.5.0 Foundational Decision Notes

This document collects the unique foundational decision notes extracted during the audit of v0.2.0 governance and model files (`Draft 2/`), capturing key design choices and trade-offs preserved in the LORE corpus.

---

## 1. Canonical UID Design & Temporal Decoupling ("Crufty Hash Note")

- **Source**: `Draft 2/LORE Open Questions and Decision Log v0.2.md` and `Draft 2/LORE v0.2 Change Log.md`
- **Context**: The proposed construction `HASH(ROOT_UID + GENERATION_SECRET + TIMESTAMP + MONOTONIC_COUNTER)` was annotated with `[<-- This is crufty - SPG]`.
- **Decision**: 
  - Canonical UID semantics require global uniqueness across namespaces, but temporal coupling (timestamp and monotonic counters) introduces unnecessary complexity and state dependencies into identity generation.
  - Identity uniqueness must be decoupled from temporal validity. UIDs remain identifiers only, distinct from assertions of time, capability, or trust.

---

## 2. LORE Universe Concept

- **Source**: `Draft 2/LORE Volume 7 — Identifier, Namespace, and Federation Model v0.2.md` & `LORE v0.2 Change Log.md`
- **Context**: Autonomous systems and diverse domain boundaries require namespace ownership without assuming global centralized consensus.
- **Decision**: 
  - A LORE Universe is a bounded identity namespace and root authority boundary.
  - Universes issue identities and define federation rules, but do not imply universal truth or automatic global trust.

---

## 3. Explicit Indirection & Alias Semantics

- **Source**: `Draft 2/LORE Volume 104`, `Volume 105`, and `Volume 115`
- **Context**: Aliases and pointers introduce security risks when systems implicitly resolve or flatten references into raw objects.
- **Decision**: 
  - Indirection MUST remain explicit across all serialization and runtime interfaces.
  - `ALIAS` is strictly separated from `IDENTITY`, and `OBJECT_REF` from `OBJECT`. A reference cannot be implicitly transformed into an object without preserving the reference wrapper.

---

## 4. Break-Glass Authority & Emergency Recovery

- **Source**: `Draft 2/LORE Volume 84`, `Volume 100`, and `LORE v0.2 Change Log.md`
- **Context**: Recovery mechanisms during human or system unavailability risk becoming permanent backdoors if privileges persist.
- **Decision**: 
  - Pre-issued emergency capabilities must be narrowly-scoped, time-bounded, and auditable.
  - Emergency access must have explicit expiration, review, and revocation workflows. Temporary recovery privileges MUST NOT convert into permanent authority.

---

## 5. Human Transport Layer & Mutation Awareness

- **Source**: `Draft 2/LORE Volume 91`, `Volume 92`, and `Volume 115` extended sidebars
- **Context**: Analysis of human-in-the-loop terminal editing workflows ("Steve as data pipe") revealed that manual copy/paste and session formatting act as a stateful, mutating transport layer.
- **Decision**: 
  - Transport layers mutate context and formatting.
  - Destructive cleanup of intermediate session artifacts destroys evidence of process intent.
  - Systems must preserve evidence trails rather than silently sanitizing operational context.
