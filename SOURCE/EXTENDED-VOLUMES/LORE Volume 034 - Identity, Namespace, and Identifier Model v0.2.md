# LORE Volume 34 - Identity, Namespace, and Identifier Model

## Version 0.2 Draft

---

# 1. Purpose

This volume defines the concepts surrounding:

- identity,
- identifiers,
- namespaces,
- roots,
- universes,
- and federation boundaries.

The purpose is to establish a clear separation between:

- naming,
- identification,
- authority,
- ownership,
- capability,
- and trust.

---

# 2. Core Principle

The governing principle:

> An identifier identifies something. It does not define what that thing may do.

---

# 3. Identifier Fundamentals

A LORE identifier exists to answer:

> Which object is this?

It does not answer:

- Is this object trusted?
- Is this object authorized?
- Is this object safe?
- Does this object have authority?

---

# 4. Identifier Separation

Important distinction:

```text id="m7q4vx"
Identifier

≠

Assertion

≠

Capability

≠

Authority
```

---

# 5. Namespace Model

A namespace establishes:

- uniqueness boundaries,
- authority boundaries,
- resolution paths.

A namespace answers:

> Who is responsible for interpreting this identifier?

---

# 6. LORE Universe Model

A LORE universe is defined by:

- a local root,
- objects under that root,
- relationships established within that universe,
- federation relationships to other universes.

Conceptually:

```text id="q8n5mp"
LORE Universe

=

Local Root

+

Local Objects

+

Local Relationships

+

Federated Connections
```

---

# 7. Root Identity

The root is the primary namespace authority.

Responsibilities may include:

- namespace ownership,
- identifier generation,
- federation establishment,
- recovery mechanisms.

---

# 8. Root Authority Boundary

The root should not automatically represent:

- every object,
- every assertion,
- every capability.

The root establishes identity space.

It does not become universal authority.

---

# 9. Identifier Structure

A possible identifier model:

```text id="x6m3qw"
Root Namespace Identifier

+

Generated Unique Component
```

---

# 10. Namespace Discovery

Foreign systems may encounter identifiers without prior knowledge of the originating universe.

Therefore:

The identifier should provide enough information to determine:

- which root created it,
- where resolution should begin,
- which authority should be consulted.

---

# 11. Root Identifier Visibility

A potential design principle:

> Namespace authority information should be discoverable without making identifiers themselves overloaded.

---

# 12. Generated Identifier Component

The generated component should provide global uniqueness.

Potential inputs:

- root identity,
- generator secret,
- randomness,
- time,
- monotonic sequence.

Example conceptual model:

```text id="p9v5kr"
UID

=

Root Identifier

+

Generated Unique Component
```

---

# 13. Timestamp Consideration

A possible UID generation input:

```text id="h5m8qx"
Root Salt

+

Generator Secret

+

Root UUID

+

Time

+

Monotonic Increment
```

Review note:

[<-- This is crufty - SPG]

The timestamp component should be challenged.

Questions:

- Does it provide meaningful value?
- Does it create unnecessary leakage?
- Does it introduce predictable patterns?
- Are simpler uniqueness mechanisms sufficient?

---

# 14. UID Uniqueness vs Namespace Authority

These are separate requirements.

A UID requires:

- uniqueness.

A namespace requires:

- authority identification.

A system should not confuse them.

---

# 15. Non-Root Identifier Model

A possible model:

```text id="r7n4kp"
Non-root UID

=

Root UID

+

Generated Component
```

---

# 16. Namespace Collisions

Known examples of collision-prone names:

- localhost,
- 127.0.0.1,
- 10.x.x.x,
- John Smith,
- Main Street.

Lessons:

Human-readable names frequently lack sufficient uniqueness.

---

# 17. Human Names vs Machine Identity

Humans need:

- memorable names,
- aliases,
- descriptions.

Machines need:

- stable identifiers,
- uniqueness,
- resolution.

These should remain separate.

---

# 18. ASN Analogy

The namespace model has similarities to autonomous system numbers.

Important distinction:

The authority identifier and the generated identifier serve different purposes.

Example:

```text id="v8m3qx"
ASN

identifies authority

while

routing information

defines relationships
```

---

# 19. Signed Identifier Objects

A potential mitigation:

Identifiers may be represented as signed objects.

A signed UID may prove:

- who created it,
- which namespace issued it,
- integrity of identifier metadata.

It does not prove:

- correctness of associated assertions,
- authorization,
- trustworthiness.

---

# 20. Identifier Lifecycle

Identifiers may require lifecycle support:

- creation,
- activation,
- aliasing,
- retirement,
- historical preservation.

---

# 21. Identifier Immutability

Potential principle:

An identifier should remain stable.

Changes should occur through:

- relationships,
- assertions,
- lifecycle events.

---

# 22. Federation Implications

Foreign islands may not know each other's objects.

Therefore:

Federation requires:

- namespace discovery,
- root verification,
- resolver capability,
- trust relationships.

---

# 23. Root Recovery

Because roots are critical:

Recovery may require:

- offline recovery material,
- pre-issued emergency capability tickets,
- multi-party authorization.

---

# 24. Identifier Failure Modes

Potential failures:

## Collision

Two objects receive the same identifier.

---

## Confusion

Different namespaces interpret the same identifier differently.

---

## Leakage

Identifier reveals sensitive information.

---

## Overloading

Identifier becomes a hidden authority mechanism.

---

# 25. Review Questions

Reviewers should challenge:

1. How much namespace information belongs in identifiers?
2. Should roots be visible?
3. Is the generated UID design unnecessarily complex?
4. Should timestamps be removed?
5. Should identifiers be signed?
6. How should namespace transfer work?
7. How should federation discover foreign roots?

---

# 26. Identity Principle

The governing principle:

> A strong identifier tells you what something is and where to begin understanding it. It does not tell you what you may do with it.

---

LORE Volume 34 - Identity, Namespace, and Identifier Model v0.2.md
