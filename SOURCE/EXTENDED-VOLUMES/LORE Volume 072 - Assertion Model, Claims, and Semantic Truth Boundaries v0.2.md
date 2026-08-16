# LORE Volume 72 - Assertion Model, Claims, and Semantic Truth Boundaries

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents assertions and claims.

The purpose is to establish a clear distinction between:

- what exists,
- what is claimed,
- who makes the claim,
- what supports the claim,
- and whether the claim should influence decisions.

---

# 2. Core Principle

The governing principle:

> An assertion is not truth. An assertion is a statement with an origin, authority, context, and evidence.

---

# 3. Assertion Philosophy

Modern systems frequently treat information as if it were automatically authoritative.

Examples:

- database records,
- API responses,
- certificates,
- user-provided information,
- AI-generated output.

LORE treats these as assertions requiring interpretation.

---

# 4. Assertion Definition

An assertion is a statement about an object, relationship, capability, or condition.

Examples:

```text id="m7q4vx"
"Application X is owned by Team Y"

"Agent Z may access Resource A"

"Device B is located in Facility C"
```

---

# 5. Assertion Components

An assertion may include:

- subject,
- predicate,
- object,
- issuer,
- timestamp,
- context,
- evidence,
- confidence,
- lifecycle.

---

# 6. Assertion Structure

Example:

```yaml id="q8n5mp"
ASSERTION:

  subject:
    Application_X

  predicate:
    owned_by

  object:
    Team_Y

  issued_by:
    AssetManagementSystem

  evidence:
    OwnershipRecord

  valid_until:
    2027-01-01
```

---

# 7. Assertion vs Fact

Critical distinction:

```text id="x6m3qw"
Assertion

=

Someone claims this is true
```

```text id="p9v5kr"
Fact

=

Reality itself
```

---

LORE generally models assertions.

It does not claim direct access to reality.

---

# 8. Assertion Issuers

An issuer may be:

- person,
- organization,
- service,
- device,
- automated system,
- external authority.

---

# 9. Issuer Authority

An issuer should have authority appropriate to the assertion.

Example:

A device inventory system may assert:

```text id="r7n4kp"
Device serial number
```

but may not be authoritative for:

```text id="v8m3qx"
Legal ownership
```

---

# 10. Assertion Scope

Assertions should define:

- what they apply to,
- where they apply,
- when they apply.

---

# 11. Assertion Context

An assertion without context may be misleading.

Example:

```text id="k4p8mw"
"User may access database"

```

Missing:

- which database,
- under what purpose,
- for how long,
- under what conditions.

---

# 12. Assertion Confidence

LORE may represent confidence.

However:

```text id="wye826"
High Confidence

≠

Guaranteed Truth
```

---

# 13. Conflicting Assertions

Multiple assertions may disagree.

Example:

```text id="fzbvqj"
System A:

Application owned by Team A


System B:

Application owned by Team B
```

---

# 14. Conflict Handling

LORE should preserve:

- conflicting claims,
- sources,
- evidence,
- resolution process.

---

# 15. Assertion Validation

Validation may consider:

- issuer authority,
- evidence quality,
- freshness,
- context applicability,
- relationship consistency.

---

# 16. Assertion Lifecycle

Assertions may:

- be created,
- verified,
- updated,
- superseded,
- expired,
- revoked.

---

# 17. Assertion Revocation

Important assertions should support:

- invalidation,
- replacement,
- historical preservation.

---

# 18. Assertion Transformation

Assertions may be:

- copied,
- translated,
- aggregated,
- summarized.

Transformations should preserve lineage.

---

# 19. AI-Generated Assertions

AI systems create special challenges.

An AI-generated statement may be:

- useful information,
- a hypothesis,
- a recommendation.

It should not automatically become:

- authority,
- evidence,
- truth.

---

# 20. Assertion Chains

Assertions may depend on other assertions.

Example:

```text id="u4n8kc"
Application exists

↓

Application owned by Team

↓

Team approved deployment

↓

Agent may deploy
```

---

# 21. Assertion Security

Assertions require protection against:

- forgery,
- unauthorized modification,
- replay,
- context removal.

---

# 22. Assertion Failure Modes

Potential failures:

## Unsupported Assertion

A claim lacks evidence.

---

## Misattributed Assertion

The wrong issuer is associated.

---

## Stale Assertion

A previous state is treated as current.

---

## Context-Free Assertion

A statement is used outside its intended scope.

---

# 23. Assertion Invariants

Candidate requirements:

## Invariant 1

Assertions SHOULD identify their issuer.

---

## Invariant 2

Assertions SHOULD identify supporting evidence where appropriate.

---

## Invariant 3

Assertions SHOULD have lifecycle information.

---

## Invariant 4

Assertions SHOULD preserve context.

---

## Invariant 5

Assertions SHOULD remain distinguishable from facts.

---

# 24. Review Questions

Reviewers should challenge:

1. What qualifies as an assertion?
2. How is issuer authority determined?
3. How are conflicts represented?
4. How are AI-generated claims handled?
5. How are assertions retired?

---

# 25. Closing Principle

The governing principle:

> Reliable systems do not eliminate uncertainty by pretending every claim is true. They manage uncertainty by making claims, evidence, and authority visible.

---

LORE Volume 72 - Assertion Model, Claims, and Semantic Truth Boundaries v0.2.md
