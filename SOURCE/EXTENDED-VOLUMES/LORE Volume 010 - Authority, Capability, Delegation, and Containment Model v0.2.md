# LORE Volume 10 - Authority, Capability, Delegation, and Containment Model

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents:

- authority,
- capability,
- delegation,
- constraints,
- and containment.

The purpose is to address a recurring security failure pattern:

> Systems possess more capability than they require, with insufficient understanding of why they are allowed to act.

---

# 2. Core Principle

LORE separates:

```text id="a7m4qp"
Identity

≠

Authority

≠

Capability

≠

Action
```

Knowing who something is does not determine what it may do.

Having a capability does not necessarily determine why it should be used.

---

# 3. Authority Model

## Definition

Authority is the legitimate ability to influence or authorize actions within a defined scope.

Authority may derive from:

- ownership,
- delegation,
- organizational role,
- policy,
- external trust relationship.

---

# 4. Authority Is Contextual

Authority is not universal.

Example:

```text id="h5k8mw"
Administrator Authority

may apply to:

Development Environment

but not:

Production Environment
```

---

# 5. Capability Model

## Definition

A capability is a bounded ability to perform an action.

Examples:

- read a resource,
- modify a configuration,
- execute an operation,
- request a service.

---

# 6. Capability Properties

A useful capability should be:

## Scoped

The capability applies only to defined objects or actions.

---

## Time-Bounded

The capability has a lifecycle.

Example:

```text id="r9n4vx"
Vendor Access

valid:

Maintenance Window

expires:

End of Contract
```

---

## Reviewable

The capability can be understood by humans and systems.

---

## Revocable

The capability can be withdrawn.

---

# 7. Delegation Model

## Definition

Delegation transfers authority or capability from one principal to another.

Example:

```text id="p7m3qs"
Human

delegates

Capability

to

Agent
```

---

# 8. Delegation Does Not Create Authority

A delegate cannot provide more authority than the delegator possesses.

Conceptually:

```text id="w8c5lz"
Delegated Authority

<=

Original Authority
```

---

# 9. Delegation Chains

Delegation may occur across multiple parties.

Example:

```text id="k6v2xn"
Organization

|

Administrator

|

Automation Service

|

Agent
```

---

# 10. Delegation Chain Risks

Potential risks:

- privilege expansion,
- unclear ownership,
- hidden dependencies,
- authority laundering.

---

# 11. Authority Laundering

A potential attack:

An actor receives limited authority.

That actor delegates or transforms it.

The resulting capability appears broader than the original.

---

# 12. Delegation Validation

A delegation should preserve:

- original authority,
- scope,
- constraints,
- expiration,
- provenance.

---

# 13. Capability Tickets

A potential implementation mechanism.

A capability ticket may contain:

```text id="m4q8yr"
Capability

+

Issuer

+

Subject

+

Scope

+

Constraints

+

Expiration

+

Signature
```

---

# 14. Capability Tickets Are Not Identity

A ticket proves:

> This capability was issued.

It does not prove:

- the holder is trustworthy,
- the intended purpose remains valid,
- the action should occur.

---

# 15. Break-Glass Capabilities

Emergency access requires special handling.

Potential characteristics:

- pre-issued,
- tightly controlled,
- auditable,
- time-limited,
- revocable.

---

# 16. Break-Glass Lifecycle

Example:

```text id="x3m7qv"
Prepared

    |

Activated

    |

Used

    |

Reviewed

    |

Retired
```

---

# 17. Containment Model

## Definition

Containment limits the consequence of failure.

Containment is a first-class security property.

---

# 18. Containment Dimensions

Potential containment boundaries:

## Scope

What can be affected?

---

## Time

How long can it operate?

---

## Dependency

What systems can it influence?

---

## Population

Who or what can be affected?

---

## Geography

Where can it operate?

---

## Recovery

How easily can consequences be reversed?

---

# 19. Blast Radius

The key question:

> What is the maximum consequence if this authority is misused?

---

# 20. Agent Security Envelope

The original motivating use case.

Current pattern:

```text id="z6p4km"
Agent

|

Permanent Credential

|

Broad Authority

|

External Systems
```

---

Desired pattern:

```text id="b9w5cx"
Agent Identity

+

Purpose

+

Scoped Capability

+

Evidence

+

Context

+

Expiration

+

Containment
```

---

# 21. Human Authorization Relationship

LORE should preserve the relationship between:

- human intent,
- delegated authority,
- automated action.

Example:

```text id="q5m8vn"
Human

approves purpose

|

Agent

uses capability

|

Action

```

---

# 22. Autonomous Systems

A capable system should be able to determine:

- what it may do,
- why it may do it,
- whether conditions remain valid,
- what consequences exist.

---

# 23. Authority and Context

Authority without context is dangerous.

Example:

```text id="c7x2mq"
Can Modify Database

```

is incomplete.

Better:

```text id="n4p8zw"
Can Modify Database

for:

Approved Migration

during:

Maintenance Window

with:

Rollback Capability
```

---

# 24. Review Questions

Reviewers should challenge:

1. Is authority modeled correctly?
2. Is capability separate enough from identity?
3. Can delegation chains be safely bounded?
4. Can authority laundering occur?
5. Are capability tickets sufficient?
6. How should break-glass access work?
7. Is containment represented adequately?
8. Are agents sufficiently different from existing principals?

---

# 25. Authority Principle

The governing principle:

> Possessing the ability to act does not mean having sufficient justification to act.

---

LORE Volume 10 - Authority, Capability, Delegation, and Containment Model v0.2.md
