# LORE Volume 102 — Relationship Model, Connections, and Semantic Dependency

## Version 0.2 Draft

---

# 1. Purpose

This volume defines how LORE represents relationships.

The purpose is to address a fundamental challenge:

> Systems often understand individual objects but fail to understand the relationships that give those objects meaning.

---

# 2. Core Principle

The governing principle:

> Meaning does not exist only within objects. Meaning also exists in the relationships among objects.

---

# 3. Relationship Philosophy

Modern systems contain enormous numbers of relationships:

- ownership,
- dependency,
- trust,
- authority,
- delegation,
- evidence,
- communication,
- containment.

These relationships frequently determine risk more than the objects themselves.

---

# 4. Relationship Definition

A relationship represents a meaningful association between entities.

A relationship may connect:

- principals,
- objects,
- assertions,
- evidence,
- policies,
- capabilities.

---

# 5. Relationship Structure

A relationship may include:

```text id="m7q4vx"
Source Entity

+

Relationship Type

+

Target Entity

+

Authority

+

Context

+

Lifecycle
```

---

# 6. Relationship Example

A simple statement:

```text id="q8n5mp"
Application A

uses

Database B
```

is incomplete.

LORE may also need:

```text id="x6m3qw"
Purpose:

transaction processing


Authority:

read/write


Context:

production environment


Lifecycle:

active
```

---

# 7. Relationship vs Association

Important distinction:

```text id="p9v5kr"
Association

=

Something is connected
```

```text id="r7n4kp"
Relationship

=

The meaning of the connection is understood
```

---

# 8. Relationship Types

Potential relationship categories:

## Ownership

Who is responsible?

---

## Dependency

What relies on what?

---

## Trust

What confidence exists?

---

## Authority

Who may act?

---

## Evidence

What supports a claim?

---

## Delegation

Who received transferred authority?

---

# 9. Relationship Context

Relationships require context.

Example:

```text id="v8m3qx"
Vendor

provides

Service
```

Questions:

- Which service?
- For whom?
- Under what agreement?
- For what purpose?
- Until when?

---

# 10. Relationship Lifecycle

Relationships change.

Examples:

- created,
- modified,
- suspended,
- transferred,
- terminated.

---

# 11. Relationship Graph

LORE naturally represents relationships as a graph.

Example:

```text id="k4p8mw"
Principal

↓

owns

↓

Application

↓

depends on

↓

Database

↓

protected by

↓

Policy
```

---

# 12. Relationship Traversal

Understanding impact requires traversal.

Questions:

- What depends on this object?
- What trusts this principal?
- What authority flows from this relationship?
- What evidence supports it?

---

# 13. Relationship and Blast Radius

Relationships determine impact.

Example:

```text id="wye826"
Compromised Credential

+

Many Relationships

=

Large Potential Impact
```

---

# 14. Relationship and Change

Changes often affect relationships.

Example:

A system migration may alter:

- ownership,
- dependencies,
- authority paths,
- trust relationships.

---

# 15. Relationship and Agents

Agents introduce dynamic relationships.

Examples:

- agent uses tool,
- agent receives capability,
- agent trusts evidence source,
- agent delegates task.

These relationships require visibility.

---

# 16. Relationship Security Risks

Potential attacks:

## Relationship Spoofing

Creating false connections.

---

## Relationship Hiding

Removing visibility of important dependencies.

---

## Relationship Confusion

Interpreting one relationship as another.

---

## Relationship Explosion

Creating excessive complexity.

---

# 17. Relationship Failure Modes

Potential failures:

## Unknown Dependency

A relationship exists but is undocumented.

---

## Broken Relationship

A dependency no longer functions.

---

## Stale Relationship

The relationship no longer reflects reality.

---

## Ambiguous Relationship

Meaning is unclear.

---

# 18. Relationship Invariants

Candidate requirements:

## Invariant 1

Important relationships SHOULD be explicit.

---

## Invariant 2

Relationships SHOULD have defined meaning.

---

## Invariant 3

Relationships SHOULD preserve context.

---

## Invariant 4

Relationships SHOULD have lifecycle awareness.

---

## Invariant 5

High-impact relationships SHOULD be discoverable.

---

# 19. Review Questions

Reviewers should challenge:

1. Which relationships matter?
2. Which relationships must be explicit?
3. How are relationship changes tracked?
4. How are relationship graphs analyzed?
5. How does LORE avoid unmanageable complexity?

---

# 20. Closing Principle

> Objects tell us what exists. Relationships tell us what matters.

---

LORE Volume 102 — Relationship Model, Connections, and Semantic Dependency v0.2.md

One-liner: **The architect said, "The system is simple." The dependency graph quietly unfolded from a small box into a very judgmental spider.**
