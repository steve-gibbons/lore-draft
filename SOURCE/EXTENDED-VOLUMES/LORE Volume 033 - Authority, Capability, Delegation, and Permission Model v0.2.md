# LORE Volume 33 - Authority, Capability, Delegation, and Permission Model

## Version 0.2 Draft

---

# 1. Purpose

This volume defines the distinctions among:

- authority,
- capability,
- delegation,
- permission,
- and enforcement.

The purpose is to prevent a recurring security failure:

> Treating the ability to perform an action as proof that the action is appropriate.

---

# 2. Core Principle

The governing principle:

> Identity establishes who something is. Authority establishes what it may represent. Capability establishes what it may attempt. Context determines whether action is appropriate.

---

# 3. Identity Is Not Authority

A foundational distinction:

```text id="m7q4vx"
Identity

≠

Authority
```

An object may have a valid identity while possessing:

- no authority,
- limited authority,
- expired authority,
- delegated authority.

---

# 4. Authority Model

Authority represents the recognized ability to make statements or grant permissions within a defined scope.

Authority may include:

- issuer,
- scope,
- conditions,
- lifecycle,
- delegation rules.

---

# 5. Capability Model

Capability represents an actionable ability.

Example:

```text id="q8n5mp"
Principal

has capability

Perform Action

on Object
```

A capability should include:

- action scope,
- target scope,
- expiration,
- constraints.

---

# 6. Capability Is Not Permission

Important distinction:

```text id="x6m3qw"
Capability

≠

Permission
```

A capability may allow an attempt.

A permission decision determines whether the attempt should succeed.

---

# 7. Authorization Model

Authorization remains the responsibility of enforcement systems.

LORE provides context:

- identity,
- relationships,
- evidence,
- authority,
- capability,
- lifecycle.

Existing systems determine:

- allow,
- deny,
- require approval,
- require additional evidence.

---

# 8. Delegation Model

Authority frequently moves between principals.

Example:

```text id="p9v5kr"
Human

delegates

Capability

to

Agent
```

---

# 9. Delegation Requirements

Delegation should define:

- delegator,
- delegate,
- scope,
- purpose,
- constraints,
- expiration,
- revocation.

---

# 10. Delegation Chains

Authority may flow through multiple parties.

Example:

```text id="h5m8qx"
Organization

|

Administrator

|

Service

|

Agent
```

---

# 11. Delegation Risk

Delegation introduces risks:

- unintended expansion,
- unclear ownership,
- privilege inheritance,
- hidden dependencies.

---

# 12. Authority Laundering

A critical threat:

A sequence of individually valid delegations may create an outcome that no participant intended.

Example:

```text id="r7n4kp"
Authority A

delegates limited capability

|

Authority B

delegates modified capability

|

Unexpected authority
```

---

# 13. Capability Scope

Capabilities should be constrained by:

- object,
- action,
- time,
- purpose,
- environment.

---

Example:

Broad:

```text id="v8m3qx"
Access Database
```

Better:

```text id="k4p8mw"
Read Customer Records

for

Support Ticket Resolution

until

17:00 UTC
```

---

# 14. Time-Bounded Authority

Time is a containment mechanism.

Examples:

- emergency access,
- maintenance access,
- temporary delegation.

---

# 15. Break-Glass Capability

Emergency authority should be:

- prepared in advance,
- narrowly scoped,
- auditable,
- time-limited.

---

Example:

```text id="n6q3xp"
Emergency Repair Capability

+

Predefined Recovery Process

+

Post-Use Review
```

---

# 16. Purpose Binding

A capability may be associated with purpose.

Example:

```text id="w5m9qx"
Agent Capability

purpose:

Schedule Meetings

not:

Modify All User Data
```

---

# 17. Contextual Authority

Authority may depend on:

- time,
- location,
- relationship,
- operational state,
- risk conditions.

---

# 18. Capability Revocation

Revocation must consider:

- active sessions,
- cached capabilities,
- delegated authority,
- dependent systems.

---

# 19. Capability Discovery

Questions:

- What capabilities exist?
- Who issued them?
- Who currently holds them?
- What constraints apply?

---

# 20. Agent Authority Model

Agents require special attention.

An agent should not receive:

```text id="z7p4mx"
Permanent Broad Authority
```

Prefer:

```text id="c5m8vx"
Scoped Capability

+

Purpose

+

Evidence

+

Expiration

+

Containment
```

---

# 21. Relationship to Existing Security Models

LORE does not replace:

- IAM,
- RBAC,
- ABAC,
- PAM,
- policy engines.

Instead:

```text id="m8q3vx"
LORE

provides

semantic context

to

authorization systems
```

---

# 22. Authority Failure Modes

Potential failures:

## Identity Confusion

Identity mistaken for authority.

---

## Capability Expansion

Limited access becomes excessive.

---

## Delegation Abuse

Authority transferred improperly.

---

## Expiration Failure

Temporary authority becomes permanent.

---

# 23. Review Questions

Reviewers should challenge:

1. Are authority and capability sufficiently separated?
2. Is delegation modeled correctly?
3. How should capability scope be represented?
4. How are delegation chains evaluated?
5. Can authority laundering occur?
6. What belongs in LORE versus enforcement systems?

---

# 24. Authority Principle

The governing principle:

> The safest authority is explicit, scoped, time-bounded, explainable, and easy to revoke.

---

LORE Volume 33 - Authority, Capability, Delegation, and Permission Model v0.2.md
