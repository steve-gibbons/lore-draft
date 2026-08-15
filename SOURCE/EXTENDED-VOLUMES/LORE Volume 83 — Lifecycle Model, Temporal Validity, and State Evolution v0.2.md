# LORE Volume 83 — Lifecycle Model, Temporal Validity, and State Evolution

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents lifecycle.

The purpose is to address a fundamental problem:

> Systems frequently make decisions using information that was once valid but is no longer applicable.

---

# 2. Core Principle

The governing principle:

> Trust requires not only knowing what something is, but knowing where it is in its lifecycle.

---

# 3. Lifecycle Philosophy

Everything meaningful changes over time.

Examples:

- identities,
- authorities,
- capabilities,
- relationships,
- evidence,
- assertions,
- contexts.

A static representation is incomplete.

---

# 4. Lifecycle Definition

Lifecycle represents the progression of an object, relationship, assertion, or authority through time.

---

# 5. Lifecycle States

A generic lifecycle may include:

```text id="m7q4vx"
Created

↓

Active

↓

Modified

↓

Suspended

↓

Expired

↓

Retired
```

---

# 6. Creation

Creation establishes:

- existence,
- ownership,
- initial state,
- provenance.

Questions:

- Who created it?
- Why was it created?
- What authority allowed creation?

---

# 7. Activation

An object may exist without being active.

Example:

```text id="q8n5mp"
Capability Created

≠

Capability Available
```

---

# 8. Modification

Changes should preserve:

- previous state,
- change source,
- reason,
- authorization.

---

# 9. Suspension

Suspension temporarily prevents use.

Examples:

- compromised account,
- maintenance state,
- pending review.

---

# 10. Expiration

Expiration represents planned invalidity.

Examples:

- temporary authority,
- credentials,
- approvals,
- exceptions.

---

# 11. Retirement

Retirement indicates the object should no longer participate.

Examples:

- decommissioned systems,
- obsolete capabilities,
- replaced evidence sources.

---

# 12. Temporal Validity

Important distinction:

```text id="x6m3qw"
Exists

≠

Valid Now
```

---

# 13. Validity Model

A validity evaluation may include:

- start time,
- expiration time,
- renewal state,
- revocation state,
- environmental conditions.

---

# 14. Stale Information Problem

A recurring failure pattern:

```text id="p9v5kr"
Previously Correct Information

+

Current Decision

=

Incorrect Result
```

---

# 15. Lifecycle and Security

Security failures frequently involve lifecycle failures:

Examples:

- forgotten accounts,
- unused credentials,
- expired certificates,
- abandoned permissions.

---

# 16. Lifecycle and Authority

Authority should have lifecycle.

Example:

```text id="r7n4kp"
Emergency Access

Created

↓

Used

↓

Expired

↓

Removed
```

---

# 17. Lifecycle and Agents

Agents require explicit lifecycle management.

Questions:

- When was the agent created?
- Who owns it?
- Is it still needed?
- What authority remains?

---

# 18. Lifecycle and Evidence

Evidence requires freshness.

Example:

```text id="v8m3qx"
Inventory Record

created:

January

```

may not represent:

```text id="k4p8mw"
Current Ownership

August
```

---

# 19. Lifecycle Transitions

Transitions should preserve:

- previous state,
- initiating principal,
- justification,
- timestamp.

---

# 20. Lifecycle Events

Important events may include:

- creation,
- approval,
- delegation,
- renewal,
- revocation,
- expiration,
- deletion.

---

# 21. Historical Preservation

Retirement does not necessarily mean deletion.

Historical information may be required for:

- incident response,
- compliance,
- investigation,
- learning.

---

# 22. Lifecycle Security Risks

Potential attacks:

## Resurrection

An expired object becomes active again.

---

## Stale Trust

Old authority remains effective.

---

## Lifecycle Bypass

State transitions occur without authorization.

---

## Hidden Retirement

Objects disappear without accountability.

---

# 23. Lifecycle Failure Modes

Potential failures:

## Missing Lifecycle

Objects exist without state management.

---

## Incorrect State

System believes something is active when it is not.

---

## Orphaned Object

No responsible owner exists.

---

## Infinite Lifetime

Temporary objects become permanent.

---

# 24. Lifecycle Invariants

Candidate requirements:

## Invariant 1

Important objects SHOULD have lifecycle state.

---

## Invariant 2

Lifecycle transitions SHOULD be attributable.

---

## Invariant 3

Expiration SHOULD be explicit where applicable.

---

## Invariant 4

Historical state SHOULD be recoverable where needed.

---

## Invariant 5

Retired authority SHOULD not remain effective.

---

# 25. Review Questions

Reviewers should challenge:

1. Which objects require lifecycle?
2. How are state transitions controlled?
3. How is stale information detected?
4. How are expired authorities removed?
5. What history must be preserved?

---

# 26. Closing Principle

> A system that understands what something is but not how it changes over time cannot reliably determine whether it should still be trusted.

---

LORE Volume 83 — Lifecycle Model, Temporal Validity, and State Evolution v0.2.md
