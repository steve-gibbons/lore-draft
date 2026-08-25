# LORE Data-Architecture Notes (Act-vs-State, Projections, Concurrency)

> **Status: candidate**  
> **Addresses:** KF-15  
> **Date:** 2026-08-24

## 1. Act vs State

LORE distinguishes:

- **Act** (verb) - something that happened or is proposed to happen. Represented by the `act` kind (subkind `event` when it has a trigger). An act has an actor, an action, optional effect class, and (when risky) an accountable human principal.
- **State** - a derived projection of the world at a point in time. State is **not** a stored kernel kind; it is a projection over acts, assertions, and authority records.

This matches the canonical kernel decision: `thing` and `state` are derived projections, never stored bare.

Consequence: the source of truth for "what changed" is the set of acts and transformation-records; the source of truth for "what is currently accepted" is the set of artifacts whose status is in the author-only accepted family, subject to supersession.

## 2. Projections

Two projections are required for correct use even if they are not yet materialized as separate stores:

1. **Current-accepted projection**  
   The set of artifacts that currently hold an accepted / normative / canonical / verified / released status and have not been superseded or deleted. This is what most day-to-day readers and agents should consume.

2. **Full-history projection**  
   Every record, including candidates, proposals, superseded items, and the complete transformation / act chain. This is the audit and recovery surface.

Today both projections are obtained by filtering the same file tree + git history. Future work may materialize them (event log + read models) without changing the core invariants.

## 3. Concurrency and merge semantics

Current model:
- The unit of concurrency control is the git repository.
- Status transitions are validated against the closed matrix, but git merge itself is not governance-aware.
- Two concurrent accepted decisions on the same subject can be merged by git without LORE detecting the conflict.

Phase-1 mitigation (asserted, not yet enforced):
- Treat simultaneous author-only status claims on the same logical subject as a conflict that must be resolved by a human before either is treated as current-accepted.
- Prefer small, frequent commits of decisions so the window for silent divergence is short.
- Use the reviewer hats and the assisted-evaluation procedure to surface contradictions.

Future hardening (out of scope for this candidate):
- Explicit conflict records or a merge-gate that refuses to promote when two accepted lineages exist for the same subject without an explicit reconciliation act.

## 4. Relationship to event-sourcing

LORE is currently file-state + explicit change records, not a pure event-sourced system. The prior-art crosswalk (KF-09) records the alignment opportunity: treat status changes and authority grants as the event types and keep the file tree as one possible projection.

## Disposition
These notes close the "model undefined" gap for KF-15 at the documentation level. Implementation of materialised projections or governance-aware merge remains future work and does not block the current MVP adoption path.

## Provenance
Drafted 2026-08-24 as the fifth fast-follower item. Agent-generated under author direction.
