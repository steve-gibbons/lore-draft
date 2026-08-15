# LORE Volume 6 — Domain Ontologies and Extension Model

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how domain-specific knowledge extends LORE without expanding or destabilizing the core ontology.

The central principle:

> The core ontology provides universal semantic primitives. Domains provide specialized meaning.

LORE should support many domains without becoming a universal encyclopedia.

---

# 2. Core vs Domain Separation

LORE has two conceptual layers.

## Core Ontology

The core contains concepts required across domains.

Examples:

- Identity
- Object
- Relationship
- Assertion
- Evidence
- Authority
- Capability
- Context
- Lifecycle

---

## Domain Ontology

Domains provide specialized concepts.

Examples:

- cybersecurity,
- governance,
- healthcare,
- home automation,
- entertainment,
- sports,
- operational technology.

---

# 3. Domain Extension Principles

A domain extension should:

## Reuse Before Creating

Before introducing a new object:

Ask:

> Can an existing LORE concept represent this?

---

## Preserve Existing Semantics

A domain should not redefine:

- identity,
- authority,
- evidence,
- lifecycle.

---

## Keep Domain Concepts Local

A domain object should remain domain-specific unless broad adoption demonstrates it belongs in the core.

---

# 4. Domain Object Pattern

A domain object typically includes:

```text id="h3s2qv"
Domain Object

+

Identity

+

Relationships

+

Assertions

+

Evidence

+

Context

+

Lifecycle
```

---

# 5. Cybersecurity Domain Example

Cybersecurity is an initial motivating domain.

Potential objects:

## Asset

Relationship:

```text id="m8r9pu"
Organization

owns

Asset
```

---

## Vulnerability

Potential representation:

```text id="w7kq8a"
Assertion

+

Evidence

+

Impact Context
```

---

## Control

Potential representation:

```text id="x5n4qm"
Capability

+

Relationship

+

Evidence
```

---

## Exception

Potential representation:

```text id="j9c4tv"
Governance Object

+

Lifecycle

+

Decision Relationship
```

---

# 6. Governance Domain Example

Governance demonstrates:

- decision history,
- evidence,
- ownership,
- approval,
- lifecycle.

Potential objects:

- review note,
- risk,
- exception,
- decision,
- approval,
- control assessment.

---

# 7. Home Automation Domain Example

Home environments provide a useful non-enterprise validation domain.

Potential objects:

- device,
- room,
- household member,
- automation,
- preference,
- capability.

Example:

```text id="3v6w1a"
Person

prefers

Temperature Range
```

---

Potential security relationship:

```text id="k2m7zq"
Home Assistant Agent

has capability

Adjust Thermostat

under condition:

Home Occupied
```

---

# 8. Personal Context Domain Example

Personal context is important for agent usefulness.

Potential objects:

- preference,
- interest,
- relationship,
- routine,
- communication preference.

Example:

```text id="g6p3rf"
Person

prefers

Actor
```

---

Additional context:

```text id="u4k9cd"
Sports Outcome

influences

Interaction Context
```

---

# 9. Entertainment Domain Example

Entertainment provides a useful test because it requires semantic understanding rather than security-only reasoning.

Potential objects:

- movie,
- actor,
- franchise,
- character,
- preference.

Example:

```text id="e7s8hm"
Person

favorite_actor

Patrick Stewart
```

The relationship may include:

- source,
- confidence,
- date,
- context.

---

# 10. Sports Domain Example

Sports provides temporal and emotional context.

Potential objects:

- team,
- player,
- league,
- season,
- event.

Example:

```text id="q5v2bn"
Person

supports

Team
```

Additional context:

```text id="r8m3kx"
Team Loss

changes

Interaction Context
```

---

# 11. Operational Technology Domain Example

OT demonstrates:

- safety implications,
- long lifecycles,
- physical consequences.

Potential objects:

- controller,
- process,
- sensor,
- operator,
- maintenance relationship.

Important distinctions:

```text id="a9n6pl"
Network Location

≠

Operational Authority

≠

Safety State
```

---

# 12. Agent Domain Example

Agents are a primary motivating domain.

Potential objects:

- agent identity,
- purpose,
- capability,
- delegated authority,
- context.

Example:

```text id="b6h4yx"
Human

delegates

Capability

to

Agent

for

Purpose

under

Constraints
```

---

# 13. Domain Governance Rules

A domain extension should document:

## Purpose

Why does this domain exist?

---

## Objects

What new concepts are introduced?

---

## Relationships

How do objects connect?

---

## Lifecycle

How do objects change?

---

## Evidence

How are claims supported?

---

## Boundaries

What does the domain intentionally not model?

---

# 14. Domain Review Questions

Reviewers should ask:

1. Does this domain reuse core concepts?
2. Is a new object truly necessary?
3. Does the domain create duplicate semantics?
4. Are relationships explicit?
5. Is lifecycle represented?
6. Is evidence represented?
7. Does this belong in the core instead?

---

# 15. Avoiding the Ontology Trap

A common failure mode:

> A useful model grows until nobody can understand it.

LORE should resist:

- modeling everything,
- creating universal taxonomies,
- forcing every concept into one graph.

The goal is interoperability.

Not completeness.

---

# 16. Domain Principle

The governing principle:

> A domain should add meaning without redefining trust.

---

LORE Volume 6 — Domain Ontologies and Extension Model v0.2.md
