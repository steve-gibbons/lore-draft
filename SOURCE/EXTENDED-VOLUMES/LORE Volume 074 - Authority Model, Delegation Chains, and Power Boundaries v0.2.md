# LORE Volume 74 - Authority Model, Delegation Chains, and Power Boundaries

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents authority.

The purpose is to separate:

- who exists,
- who may act,
- why they may act,
- how authority was granted,
- and how authority can be constrained.

---

# 2. Core Principle

The governing principle:

> Authority is not an attribute of identity. Authority is a relationship granted, bounded, and maintained through explicit mechanisms.

---

# 3. Authority Philosophy

Many security failures result from collapsing:

- identity,
- access,
- privilege,
- capability,
- and responsibility.

LORE treats these as separate concepts.

---

# 4. Authority Definition

Authority represents the ability of a principal to perform an action under defined conditions.

Authority includes:

- holder,
- issuer,
- scope,
- purpose,
- constraints,
- evidence,
- lifecycle.

---

# 5. Identity Does Not Create Authority

Important distinction:

```text id="m7q4vx"
Principal Exists

≠

Principal Has Authority
```

---

# 6. Authority Sources

Authority may originate from:

- ownership,
- delegation,
- organizational role,
- explicit approval,
- automated policy,
- external trust relationship.

---

# 7. Authority Relationship

Authority is modeled as:

```text id="q8n5mp"
Authority Grantor

|

grants authority

|

Principal

|

for action

|

against resource
```

---

# 8. Authority Example

```yaml id="x6m3qw"
AUTHORITY:

  issuer:
    Operations_Manager

  holder:
    Deployment_Agent

  action:
    deploy

  target:
    Application_X

  constraints:

    environment:
      staging

    expiration:
      24_hours
```

---

# 9. Authority Scope

Authority may be constrained by:

- action,
- resource,
- environment,
- time,
- location,
- purpose,
- quantity,
- frequency.

---

# 10. Least Authority

LORE follows:

> Grant the minimum authority required to accomplish the intended objective.

---

# 11. Authority Expansion

Authority can expand unintentionally.

Example:

```text id="p9v5kr"
Read Access

|

becomes

|

Write Access

|

becomes

|

Administrative Access
```

---

# 12. Authority Attenuation

Authority should be reducible.

Example:

```text id="r7n4kp"
Administrator

may:

manage all applications


Agent receives:

restart one service
```

---

# 13. Delegation Model

Delegation transfers authority from one principal to another.

A delegation should preserve:

- original source,
- chain of custody,
- limitations,
- expiration.

---

# 14. Delegation Chain

Example:

```text id="v8m3qx"
Organization

|

Administrator

|

Automation Service

|

AI Agent

|

Temporary Capability
```

---

# 15. Delegation Invariants

A delegation:

- cannot create authority from nothing,
- cannot exceed the grantor's authority,
- should preserve lineage,
- should remain inspectable.

---

# 16. Authority Lineage

A decision should be able to answer:

> How did this principal obtain this authority?

Example:

```text id="k4p8mw"
Corporate Policy

↓

Team Role

↓

Manager Approval

↓

Agent Capability

↓

Requested Action
```

---

# 17. Standing Authority vs Temporary Authority

Important distinction:

```text id="wye826"
Standing Authority

exists continuously
```

```text id="fzbvqj"
Temporary Authority

exists for a purpose and duration
```

---

# 18. Temporary Authority Principle

Temporary authority should have:

- explicit purpose,
- expiration,
- review requirements.

---

# 19. Authority Revocation

Authority should support:

- immediate revocation,
- scheduled expiration,
- replacement,
- historical preservation.

---

# 20. Emergency Authority

Emergency authority may be necessary.

However:

Emergency access should include:

- narrow scope,
- justification,
- logging,
- retrospective review.

---

# 21. Authority and Agents

Agents require special attention.

An agent should not receive:

- broad standing privilege,
- inherited human authority,
- unclear delegation.

---

# 22. Authority Decision Process

A decision may evaluate:

```text id="u4n8kc"
Request

+

Principal

+

Authority

+

Context

+

Evidence

=

Decision
```

---

# 23. Authority Conflicts

Conflicts may occur:

Example:

```text id="9ax18t"
Policy allows action

but

Emergency restriction denies action
```

---

LORE should preserve:

- conflicting authorities,
- precedence rules,
- resolution process.

---

# 24. Authority Security Risks

Potential attacks:

## Privilege Escalation

Obtaining excessive authority.

---

## Delegation Laundering

Making authority origin unclear.

---

## Authority Persistence

Temporary access becomes permanent.

---

## Scope Confusion

Authority applies beyond intended limits.

---

# 25. Authority Failure Modes

Potential failures:

## Unknown Authority

A principal acts without clear justification.

---

## Excessive Authority

The granted capability exceeds need.

---

## Orphaned Authority

Authority remains after ownership changes.

---

## Invisible Delegation

Authority exists but cannot be traced.

---

# 26. Authority Invariants

Candidate requirements:

## Invariant 1

Authority SHOULD have an identifiable issuer.

---

## Invariant 2

Authority SHOULD have explicit scope.

---

## Invariant 3

Authority SHOULD have lifecycle controls.

---

## Invariant 4

Delegation SHOULD preserve lineage.

---

## Invariant 5

Authority decisions SHOULD be explainable.

---

# 27. Review Questions

Reviewers should challenge:

1. How is authority created?
2. How is authority constrained?
3. How is delegation represented?
4. How is excessive privilege detected?
5. How is authority recovered after compromise?

---

# 28. Closing Principle

The governing principle:

> The most dangerous authority is authority that exists without a clear origin, purpose, boundary, or expiration.

---

LORE Volume 74 - Authority Model, Delegation Chains, and Power Boundaries v0.2.md
