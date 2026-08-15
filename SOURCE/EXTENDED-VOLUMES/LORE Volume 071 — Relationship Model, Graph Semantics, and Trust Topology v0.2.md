# LORE Volume 71 — Relationship Model, Graph Semantics, and Trust Topology

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents relationships between objects.

The purpose is to treat relationships as first-class security and semantic concepts.

The central idea:

> Objects rarely create meaning by themselves. Meaning emerges from relationships.

---

# 2. Core Principle

The governing principle:

> A system that understands objects but not relationships understands inventory, not reality.

---

# 3. Relationship Philosophy

Traditional systems often represent:

- users,
- resources,
- permissions,
- attributes.

However, many important decisions depend on relationships:

- ownership,
- dependency,
- delegation,
- creation,
- trust,
- containment.

---

# 4. Relationship Definition

A relationship represents a semantic connection between two or more objects.

Example:

```text id="m7q4vx"
Principal A

owns

Resource B
```

---

# 5. Relationship Properties

A relationship may include:

- source object,
- target object,
- relationship type,
- creator,
- authority,
- evidence,
- context,
- lifecycle.

---

# 6. Relationship as an Object

A critical design concept:

```text id="q8n5mp"
Relationship

is itself

a managed entity
```

---

The relationship may have:

- identity,
- ownership,
- provenance,
- expiration.

---

# 7. Relationship Examples

Examples include:

## Ownership

```text
Organization

owns

Application
```

---

## Dependency

```text
Service A

depends on

Service B
```

---

## Delegation

```text
Administrator

delegates authority to

Agent
```

---

## Creation

```text
Developer

created

Software Component
```

---

# 8. Relationship Direction

Relationships may be directional.

Example:

```text id="x6m3qw"
Agent

uses

Capability
```

does not imply:

```text
Capability

uses

Agent
```

---

# 9. Relationship Symmetry

Some relationships may be symmetric.

Example:

```text id="p9v5kr"
System A

connected to

System B
```

However, symmetry should not be assumed.

---

# 10. Relationship Semantics

A relationship type should define:

- meaning,
- allowed participants,
- lifecycle,
- security implications.

---

# 11. Relationship Strength

Not all relationships have equal significance.

Examples:

- informational,
- operational,
- authoritative,
- security-critical.

---

# 12. Trust Topology

LORE relationships create a trust topology.

Example:

```text id="r7n4kp"
Human

|

delegates

|

Agent

|

accesses

|

Service

|

depends on

|

Database
```

---

# 13. Trust Path Analysis

A decision may require understanding paths.

Question:

> How did this principal obtain this authority?

---

Example:

```text
User

↓

Organization Membership

↓

Role Assignment

↓

Capability

↓

Action
```

---

# 14. Relationship Traversal

Potential queries:

- What owns this object?
- What depends on this service?
- Who can affect this resource?
- What authority paths exist?

---

# 15. Graph Model

LORE naturally resembles a graph:

```text id="v8m3qx"
Objects

(nodes)

+

Relationships

(edges)
```

---

# 16. Graph Security Value

Graph relationships enable:

- blast-radius analysis,
- dependency discovery,
- authority tracing,
- impact assessment.

---

# 17. Graph Risks

Graph representations introduce risks:

## Complexity

Large graphs may become difficult to understand.

---

## Sensitive Relationship Exposure

Relationships may reveal confidential information.

---

## Incorrect Inference

A relationship may be interpreted incorrectly.

---

# 18. Explicit vs Derived Relationships

Important distinction:

```text id="k4p8mw"
Recorded Relationship

≠

Inferred Relationship
```

---

# 19. Relationship Inference

Inference may be useful.

Example:

```text
Application

runs on

Server

therefore:

Application

depends on

Server
```

---

However:

Inferred relationships require:

- explanation,
- confidence,
- source information.

---

# 20. Relationship Provenance

Every important relationship should answer:

- Who created it?
- Why does it exist?
- What supports it?
- When was it verified?

---

# 21. Relationship Lifecycle

Relationships may:

- be created,
- change,
- expire,
- become invalid,
- be revoked.

---

# 22. Relationship Conflicts

Systems may encounter:

```text
Team A owns Application X

Team B owns Application X
```

LORE should preserve:

- conflict,
- sources,
- resolution process.

---

# 23. Relationship Security

Important relationships should be protected from:

- unauthorized modification,
- deletion,
- forgery.

---

# 24. Relationship Failure Modes

Potential failures:

## Hidden Relationship

Important dependency is unknown.

---

## Incorrect Relationship

Decision relies on false information.

---

## Stale Relationship

Past information remains active.

---

## Excessive Relationship

Trust expands unintentionally.

---

# 25. Relationship Invariants

Candidate requirements:

## Invariant 1

Important relationships SHOULD have identifiable owners.

---

## Invariant 2

Security-relevant relationships SHOULD have provenance.

---

## Invariant 3

Relationship changes SHOULD be recorded.

---

## Invariant 4

Inferences SHOULD be distinguishable from facts.

---

# 26. Review Questions

Reviewers should challenge:

1. Which relationships matter?
2. Which relationships require protection?
3. How are relationships validated?
4. How are conflicts resolved?
5. How does graph complexity remain manageable?

---

# 27. Closing Principle

The governing principle:

> Trust is not a property stored inside objects. Trust emerges from the network of relationships between them.

---

LORE Volume 71 — Relationship Model, Graph Semantics, and Trust Topology v0.2.md
