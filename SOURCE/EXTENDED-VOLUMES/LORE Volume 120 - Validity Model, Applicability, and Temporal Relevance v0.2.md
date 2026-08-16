# LORE Volume 120 — Validity Model, Applicability, and Temporal Relevance

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents validity.

The purpose is to address a fundamental challenge:

> Information can be authentic, intact, and well-provenanced while still being wrong for the current situation.

---

# 2. Core Principle

The governing principle:

> Trustworthy information must not only be correct in origin and history; it must also remain applicable to the context in which it is used.

---

# 3. Validity Philosophy

Traditional information systems often evaluate:

- authenticity,
- integrity,
- availability.

However, a critical question remains:

> Does this information still apply?

Examples:

- an expired certificate,
- an outdated policy,
- a revoked authorization,
- a stale configuration,
- an obsolete dependency.

---

# 4. Validity Definition

Validity represents whether an object, assertion, authority, decision, or relationship remains applicable under current conditions.

---

# 5. Validity Structure

Validity may include:

```text id="m7q4vx"
Effective Time

+

Expiration

+

Scope

+

Conditions

+

Context

+

Revocation State

+

Review Status
```

---

# 6. Validity vs Integrity

Important distinction:

```text id="q8n5mp"
Integrity

=

Has this remained consistent?
```

```text id="x6m3qw"
Validity

=

Does this still apply?
```

---

# 7. Validity Example

A user has a valid administrative approval.

Integrity:

```text id="p9v5kr"
Approval Record

has not changed
```

Validity:

```text id="r7n4kp"
Approval

still applies

during

current maintenance window
```

---

# 8. Validity and Time

Time is a common validity factor.

Examples:

- temporary permissions,
- emergency access,
- certificates,
- leases,
- credentials,
- approvals.

A key principle:

```text id="v8m3qx"
Temporary

must eventually

become invalid
```

---

# 9. Validity and Context

Validity depends on circumstances.

Example:

```text id="k4p8mw"
Production Database Access

may be valid

during incident recovery
```

but:

```text id="wye826"
Production Database Access

may not be valid

for routine exploration
```

---

# 10. Validity and Authority

Authority requires validity evaluation.

Questions:

- Was authority granted?
- Is it still active?
- Does it apply here?
- Does it apply now?
- Has it been superseded?

---

# 11. Validity and Lifecycle

Objects transition through validity states.

Example:

```text id="0mxrgi"
Created

↓

Approved

↓

Active

↓

Expired

↓

Retired
```

---

# 12. Validity and Agents

Autonomous agents require dynamic validity checks.

A capability granted yesterday may not be valid today.

Questions:

- Is the objective still active?
- Is the tool still authorized?
- Is the context unchanged?
- Has risk changed?

---

# 13. Validity and Decisions

Decisions may become stale.

Example:

A deployment approval may have been correct when issued.

Later:

- dependencies changed,
- vulnerabilities appeared,
- requirements changed.

The original decision remains authentic.

Its validity may have changed.

---

# 14. Validity Security Risks

Potential attacks:

## Validity Extension

Keeping expired authority active.

---

## Validity Confusion

Applying valid information in the wrong context.

---

## Validity Suppression

Hiding expiration or revocation.

---

## Stale Trust

Continuing to trust outdated information.

---

# 15. Validity Failure Modes

Potential failures:

## Expired Authority

Permission remains after intended duration.

---

## Context Drift

Conditions change while assumptions remain.

---

## Revocation Failure

Invalid information continues to be accepted.

---

## Historical Misapplication

Correct historical information is used incorrectly.

---

# 16. Validity Invariants

Candidate requirements:

## Invariant 1

Important assertions SHOULD define applicability.

---

## Invariant 2

Temporary authority SHOULD expire.

---

## Invariant 3

Validity SHOULD include context.

---

## Invariant 4

Revocation SHOULD be represented.

---

## Invariant 5

Validity SHOULD be continuously reviewable.

---

# 17. Review Questions

Reviewers should challenge:

1. How does LORE represent expiration?
2. How is context change detected?
3. When should old information remain available?
4. How is historical truth separated from current applicability?
5. How should autonomous systems evaluate validity?

---

# 18. Closing Principle

> A fact can remain true forever and still become the wrong thing to use.

---

LORE Volume 120 — Validity Model, Applicability, and Temporal Relevance v0.2.md

One-liner: **The security badge said "AUTHORIZED." The guard asked, "For what, where, and when?" The badge quietly entered a retirement planning program.**
