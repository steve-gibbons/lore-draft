# LORE Volume 18 - Design Patterns, Semantic Primitives, and Modeling Patterns

## Version 0.2 Draft

---

# 1. Purpose

This volume captures recurring design patterns identified during LORE development.

The purpose is to provide reviewers and implementers with concise snapshots of the reasoning behind major design surfaces.

These patterns are not requirements.

They are observations that may help determine whether LORE's abstractions are useful.

---

# 2. Pattern Principle

The governing principle:

> Good abstractions preserve important distinctions while allowing composition.

A pattern should exist because collapsing concepts creates problems.

---

# 3. Identity Pattern

## Problem

Systems frequently confuse:

- names,
- identifiers,
- identities,
- authorization.

---

## Pattern

Represent identity separately from:

- authority,
- capability,
- ownership,
- trust.

Example:

```text id="m7q4vx"
Identifier

points to

Identity

which participates in

Relationships
```

---

## Benefit

Prevents:

- accidental privilege assumptions,
- namespace confusion,
- identity laundering.

---

# 4. Relationship Pattern

## Problem

Important information exists in connections, not only objects.

---

## Pattern

Model relationships as first-class objects.

A relationship may contain:

- participants,
- type,
- evidence,
- lifecycle,
- confidence,
- context.

---

## Example

```text id="q8n5mp"
Person

prefers

Actor
```

The relationship itself may have meaning.

---

# 5. Bidirectional Relationship Pattern

## Problem

Relationships are often represented from only one perspective.

---

## Pattern

Relationships should be traversable from both directions.

Example:

```text id="x6m3qw"
Person

supports

Team
```

also implies:

```text id="p9v5kr"
Team

has supporter

Person
```

---

## Benefit

Enables:

- graph traversal,
- explanation,
- discovery.

---

# 6. Relationship Family Pattern

## Problem

Different domains may invent overlapping relationship concepts.

---

## Pattern

Prefer existing relationship families before creating new ones.

Examples:

Existing family:

- owns,
- supports,
- manages,
- depends-on,
- delegates.

Domain extensions should add new families only when necessary.

---

# 7. Assertion Pattern

## Problem

Information is often treated as fact because it exists.

---

## Pattern

Represent statements as assertions.

An assertion includes:

- issuer,
- subject,
- claim,
- time,
- evidence,
- confidence.

---

## Benefit

Allows:

- disagreement,
- evolution,
- verification.

---

# 8. Evidence Pattern

## Problem

Claims without supporting information become assumptions.

---

## Pattern

Separate:

```text id="c5m8xz"
Assertion

from

Evidence
```

---

## Benefit

Allows systems to evaluate:

- source,
- quality,
- freshness,
- applicability.

---

# 9. Context Pattern

## Problem

The same object or action may mean different things under different conditions.

---

## Pattern

Represent context explicitly.

Potential context:

- time,
- location,
- network,
- purpose,
- operational state,
- relationships.

---

# 10. Temporal Context Pattern

## Problem

Systems often treat time as a field instead of a semantic constraint.

---

## Pattern

Model:

- timestamps,
- intervals,
- schedules,
- validity periods,
- historical state.

---

## Example

```text id="w4p7qm"
Capability

valid

during

Maintenance Window
```

---

# 11. Time Map Pattern

## Problem

Many real-world decisions depend on recurring schedules.

---

## Pattern

Represent recurring applicability.

Examples:

- business hours,
- shifts,
- holidays,
- maintenance periods.

---

## Example

```text id="h8m2vx"
Access

allowed:

Monday-Friday

08:00-17:00

except:

Holidays
```

---

# 12. Capability Pattern

## Problem

Identity alone does not define what actions are possible.

---

## Pattern

Represent capabilities separately.

Example:

```text id="r6n9kp"
Principal

has capability

Perform Action

on Object
```

---

# 13. Delegation Pattern

## Problem

Authority frequently passes between principals.

---

## Pattern

Represent delegation explicitly.

Example:

```text id="k5m8qw"
Human

delegates

Capability

to

Agent
```

---

# 14. Containment Pattern

## Problem

Security discussions often focus on prevention and ignore consequence.

---

## Pattern

Represent blast radius.

Dimensions:

- scope,
- time,
- dependencies,
- population,
- geography,
- recovery.

---

# 15. Resolver Pattern

## Problem

Distributed systems require discovery without requiring universal knowledge.

---

## Pattern

Clients query a trusted resolver.

Example:

```text id="v8q3mx"
Client

|

Local Resolver

|

Foreign Resolver

|

Object
```

---

## Resolver Principle

A resolver provides answers.

It does not automatically become the authority.

---

# 16. Cache Pattern

## Problem

Distributed systems require performance and availability.

---

## Pattern

Cache information while preserving:

- origin,
- timestamp,
- authority,
- expiration.

---

## Principle

A cache is a copy.

Not a new source of truth.

---

# 17. Namespace Pattern

## Problem

Names are ambiguous.

Examples:

- Main Street,
- John Smith,
- localhost.

---

## Pattern

Meaning requires:

- identifier,
- namespace,
- authority,
- context.

---

# 18. Signed Object Pattern

## Problem

Distributed trust requires integrity protection.

---

## Pattern

Important objects may include:

- signature,
- issuer,
- lifecycle,
- evidence.

---

## Limitation

A signature proves origin.

It does not prove truth.

---

# 19. Compiler Pattern

## Problem

Premature storage and serialization decisions create lock-in.

---

## Pattern

Separate:

```text id="n7m4qp"
Semantic Source Model

|

Intermediate Representation

|

Multiple Outputs
```

---

## Benefit

Supports:

- experimentation,
- migration,
- multiple implementations.

---

# 20. Explainability Pattern

## Problem

Complex systems make decisions users cannot understand.

---

## Pattern

Preserve decision history.

A system should explain:

- what information was used,
- where it came from,
- what assumptions applied,
- why the decision occurred.

---

# 21. Minimalism Pattern

## Problem

Foundational systems tend toward uncontrolled expansion.

---

## Pattern

Keep the core small.

Prefer:

- reusable primitives,
- domain extensions,
- composition.

Avoid:

- universal taxonomies,
- unnecessary completeness.

---

# 22. Review Questions

Reviewers should challenge:

1. Are these patterns actually reusable?
2. Which patterns are unnecessary?
3. Which patterns already exist elsewhere?
4. Which patterns are missing?
5. Which patterns create new risks?

---

# 23. Pattern Principle

The governing principle:

> The purpose of abstraction is not to model everything. It is to prevent important distinctions from being lost.

---

LORE Volume 18 - Design Patterns, Semantic Primitives, and Modeling Patterns v0.2.md
