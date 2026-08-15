Understood. Adjustment recorded:

- Progress summaries: every ~5 volumes only.
- End of each non-summary volume: a one-liner joke/aside instead.
- Keep the actual volume output uninterrupted.

Proceeding. (And thank you for the clarification — that was a better UX requirement than what I inferred.)

---

# LORE Volume 89 — Assertion Model, Claims, and Semantic Statements

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents assertions.

The purpose is to establish a clear distinction between:

- statements,
- evidence,
- authority,
- and truth.

---

# 2. Core Principle

The governing principle:

> An assertion is a claim about reality. It is not reality itself.

---

# 3. Assertion Philosophy

Systems constantly exchange statements:

Examples:

- "This user is an administrator."
- "This system owns this resource."
- "This certificate is valid."
- "This component is approved."

The existence of the statement does not guarantee correctness.

---

# 4. Assertion Definition

An assertion is a statement made by a principal about an object, relationship, state, or condition.

---

# 5. Assertion Structure

An assertion may include:

```text id="m7q4vx"
Subject

+

Predicate

+

Object

+

Context

+

Source

+

Evidence
```

---

# 6. Assertion Example

```yaml id="q8n5mp"
ASSERTION:

  subject:
    Application_A

  predicate:
    owned_by

  object:
    Team_B

  source:
    Asset_System

  context:
    Production
```

---

# 7. Assertion vs Evidence

Important distinction:

```text id="x6m3qw"
Assertion:

"Application A is owned by Team B"
```

---

```text id="p9v5kr"
Evidence:

Inventory record

+

Approval history

+

Repository metadata
```

---

# 8. Assertion vs Truth

LORE does not store:

> Absolute truth.

LORE stores:

> Claims, their sources, and the evidence supporting them.

---

# 9. Assertion Sources

Assertions may originate from:

- humans,
- systems,
- sensors,
- applications,
- external authorities.

---

# 10. Assertion Authority

Not all assertion sources are equivalent.

A source may have:

- authority,
- reputation,
- reliability,
- scope limitations.

---

# 11. Assertion Context

An assertion without context may be misleading.

Example:

```text id="r7n4kp"
"User may deploy software"
```

requires:

- which software,
- which environment,
- when,
- under what conditions.

---

# 12. Assertion Lifecycle

Assertions may:

- originate,
- become accepted,
- change,
- expire,
- become invalid.

---

# 13. Assertion Conflict

Multiple assertions may disagree.

Example:

```text id="v8m3qx"
System A:

Resource owned by Team X


System B:

Resource owned by Team Y
```

---

# 14. Conflict Preservation

LORE should preserve:

- conflicting claims,
- sources,
- evidence,
- resolution history.

---

# 15. Assertion Confidence

Assertions may include:

- confidence,
- evidence quality,
- freshness.

However:

```text id="k4p8mw"
Confidence

≠

Truth
```

---

# 16. Assertion Delegation

A principal may make assertions based on delegated authority.

Example:

```text id="wye826"
Organization

delegates

Inventory Authority

to

System
```

---

# 17. Assertion Security Risks

Potential attacks:

## Assertion Forgery

Creating false claims.

---

## Assertion Amplification

A weak claim becomes treated as fact.

---

## Assertion Replay

Using an old claim after conditions changed.

---

## Assertion Laundering

Hiding the original source.

---

# 18. Assertion Failure Modes

Potential failures:

## Unsupported Assertion

No evidence exists.

---

## Stale Assertion

The claim is outdated.

---

## Misapplied Assertion

A valid claim is used incorrectly.

---

## Ambiguous Assertion

Meaning is unclear.

---

# 19. Assertion Invariants

Candidate requirements:

## Invariant 1

Assertions SHOULD identify their source.

---

## Invariant 2

Assertions SHOULD preserve context.

---

## Invariant 3

Assertions SHOULD remain distinguishable from evidence.

---

## Invariant 4

Assertions SHOULD have lifecycle information.

---

## Invariant 5

Assertions influencing decisions SHOULD be explainable.

---

# 20. Review Questions

Reviewers should challenge:

1. What qualifies as an assertion?
2. How are assertions trusted?
3. How are conflicting assertions handled?
4. How are stale assertions identified?
5. How are assertions prevented from becoming accidental truth?

---

# 21. Closing Principle

> A mature system does not ask only "what does this claim say?" It asks "who said it, why should we consider it, and does it still apply?"

---

LORE Volume 89 — Assertion Model, Claims, and Semantic Statements v0.2.md

One-liner: **An assertion without provenance is like a D&D spell scroll with no author — it might be powerful, but nobody knows who to blame when the dragon appears.**
