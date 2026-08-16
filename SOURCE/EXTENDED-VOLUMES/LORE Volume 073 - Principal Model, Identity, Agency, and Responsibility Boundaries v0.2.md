# LORE Volume 73 - Principal Model, Identity, Agency, and Responsibility Boundaries

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents principals.

The purpose is to establish clear boundaries between:

- identity,
- entities capable of action,
- delegated authority,
- responsibility,
- and accountability.

---

# 2. Core Principle

The governing principle:

> A principal is not merely an identity. A principal is an entity that may be held responsible for actions performed within an authority context.

---

# 3. Principal Philosophy

Modern systems frequently collapse multiple concepts:

- account,
- user,
- identity,
- credential,
- actor,
- owner,
- authority.

This creates ambiguity.

LORE separates these concepts.

---

# 4. Principal Definition

A principal is an entity that can participate in actions, relationships, or authority decisions.

Examples:

- human,
- organization,
- service,
- device,
- autonomous agent.

---

# 5. Identity vs Principal

Important distinction:

```text id="m7q4vx"
Identity

describes recognition

```

```text id="q8n5mp"
Principal

is the entity participating in trust relationships
```

---

# 6. Human Principals

A human principal may represent:

- employee,
- customer,
- administrator,
- operator,
- owner.

---

# 7. Human Identity Relationships

A human may have:

- multiple identities,
- multiple accounts,
- multiple roles.

Example:

```text id="x6m3qw"
Person

|

Identity Provider Account

|

Application Account
```

---

# 8. Organization Principals

Organizations may act as principals.

Examples:

- companies,
- departments,
- teams,
- legal entities.

---

# 9. Service Principals

Services often require independent identity.

Examples:

- APIs,
- applications,
- automation systems.

A service should not automatically inherit human authority.

---

# 10. Device Principals

Devices may participate in trust relationships.

Examples:

- laptops,
- servers,
- sensors,
- embedded systems.

---

# 11. Agent Principals

Autonomous agents require explicit modeling.

An agent principal should include:

- creator,
- owner,
- purpose,
- authority,
- lifecycle,
- operating constraints.

---

# 12. Agent Identity Boundary

Critical distinction:

```text id="p9v5kr"
Human Identity

≠

Agent Identity
```

---

A human may authorize an agent without becoming the direct actor.

---

# 13. Acting Principal vs Responsible Principal

A useful distinction:

```text id="r7n4kp"
Actor

performed action
```

```text id="v8m3qx"
Responsible Principal

held accountability
```

---

# 14. Delegated Agency

Delegation creates relationships:

```text id="k4p8mw"
Principal A

delegates authority to

Principal B
```

---

The delegation should preserve:

- origin,
- limits,
- purpose,
- expiration.

---

# 15. Principal Attributes

Potential attributes:

- identity references,
- ownership,
- organizational membership,
- capabilities,
- lifecycle state.

---

# 16. Principal Lifecycle

Principals may:

- be created,
- activated,
- modified,
- suspended,
- retired.

---

# 17. Principal Relationships

Examples:

## Ownership

```text id="wye826"
Organization

owns

Service Principal
```

---

## Management

```text id="fzbvqj"
Administrator

manages

Device Principal
```

---

## Delegation

```text id="u4n8kc"
Human

authorizes

Agent
```

---

# 18. Principal Discovery

Principals may be discovered through:

- registration,
- identity providers,
- federation,
- observation.

---

# 19. Principal Resolution

A system may ask:

- What is this principal?
- Who controls it?
- What authority does it have?
- Who is accountable?

---

# 20. Principal Security

Principal information requires protection.

Potential risks:

- impersonation,
- identity confusion,
- unauthorized modification,
- ownership ambiguity.

---

# 21. Principal Failure Modes

Potential failures:

## Identity Collapse

Multiple entities appear to be one.

---

## Authority Confusion

Identity is mistaken for permission.

---

## Ownership Ambiguity

No responsible party exists.

---

## Orphaned Principal

A principal remains active without ownership.

---

# 22. Principal Invariants

Candidate requirements:

## Invariant 1

Principals SHOULD have stable identity.

---

## Invariant 2

Principals SHOULD have accountable ownership.

---

## Invariant 3

Authority SHOULD be separate from identity.

---

## Invariant 4

Delegation SHOULD preserve lineage.

---

## Invariant 5

Agents SHOULD not inherit human identity implicitly.

---

# 23. Review Questions

Reviewers should challenge:

1. What qualifies as a principal?
2. How are principals distinguished from identities?
3. How are agents represented?
4. Who is accountable for delegated actions?
5. How are orphaned principals handled?

---

# 24. Closing Principle

The governing principle:

> Trustworthy systems require knowing not only who acted, but what entity acted, under whose authority, and who remains responsible.

---

LORE Volume 73 - Principal Model, Identity, Agency, and Responsibility Boundaries v0.2.md
