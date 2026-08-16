# LORE Volume 7 - Identifier, Namespace, and Federation Model

## Version 0.2 Draft

---

# 1. Purpose

This volume defines the concepts surrounding:

- identifiers,
- namespace authority,
- LORE universes,
- federation,
- resolution,
- and cross-boundary relationships.

The purpose is to establish a foundation for distributed operation without confusing:

- identity,
- authority,
- ownership,
- trust,
- and capability.

---

# 2. Core Principle

The foundational principle:

> Identifiers identify. They do not authorize.

A UID does not imply:

- ownership,
- permission,
- capability,
- trust,
- correctness.

An identifier answers:

> "Which object or identity is being referenced?"

It does not answer:

> "What may this object do?"

---

# 3. LORE Universe Model

A LORE universe is a locally governed semantic space.

A universe contains:

- a local root,
- locally authoritative objects,
- relationships,
- assertions,
- evidence,
- lifecycle information.

Conceptually:

```text id="g5w9lm"
LORE Universe

    |

Local Root

    |

Objects + Relationships + Assertions
```

---

# 4. Local Root

The root establishes local namespace authority.

Potential responsibilities:

- generating identifiers,
- maintaining namespace authority,
- managing trust relationships,
- establishing federation,
- managing recovery processes.

---

# 5. Root Is Not Universal Authority

A root has authority only within its defined scope.

Example:

```text id="m8c4pv"
Universe A Root

has authority over

Universe A Objects
```

It does not automatically have authority over:

- foreign universes,
- foreign objects,
- external assertions.

---

# 6. Universe Federation

Independent universes may establish relationships.

Federation is explicit.

Example:

```text id="s7n2kx"
Universe A

trust relationship

Universe B
```

Federation does not mean:

```text id="p9j5rw"
Universe A trusts everything from Universe B
```

Instead:

Federation defines:

- what is shared,
- what is trusted,
- what authority exists,
- what validation is required.

---

# 7. Identifier Design Goals

A LORE identifier system should provide:

## Global Uniqueness

The generated identifier component should minimize collision risk.

---

## Namespace Discovery

The identifier should provide enough information to identify the appropriate namespace authority.

---

## Non-Authority Semantics

The identifier must not imply:

- privilege,
- ownership,
- validity.

---

# 8. Candidate UID Model

A conceptual model:

```text id="7v2h8n"
LORE UID

=

Root UID

+

Generated Unique Component
```

The root component allows foreign systems to determine:

> Which universe should be consulted?

The generated component provides uniqueness.

---

# 9. Generated Component

Possible inputs:

```text id="q8x4mz"
HASH(
    Root Identifier
    +
    Generation Secret
    +
    Time
    +
    Monotonic Increment
)
```

The requirement:

- globally unique by design,
- resistant to guessing,
- resistant to collision.

---

## Design Note

Timestamp inclusion is intentionally flagged for review.

Potential concern:

- information leakage,
- predictable structure,
- unnecessary coupling.

**[<-- This is crufty - SPG]**

The requirement is uniqueness.

The implementation remains open.

---

# 10. Signed Identity Objects

A possible mitigation:

Represent identity information as signed objects.

Example:

```text id="j6w8ps"
Identity Object

+

UID

+

Namespace Authority

+

Signature

+

Lifecycle
```

---

Benefits:

- integrity,
- provenance,
- validation.

---

Open questions:

- Are signatures required everywhere?
- Which objects require signatures?
- How are keys rotated?

---

# 11. Namespace Collisions

Collision is a known challenge.

Examples:

- localhost,
- 127.0.0.1,
- private network ranges,
- common names,
- John Smith,
- Main Street.

---

# 12. Collision Handling Principle

LORE should avoid assuming names are globally meaningful.

Resolution should consider:

- namespace,
- authority,
- context.

Example:

```text id="z5n7mq"
Main Street

+

Location Context

+

Namespace Authority
```

provides more meaning than:

```text id="c3v8kw"
"Main Street"
```

---

# 13. Resolution Model

Clients should not require knowledge of every universe.

Preferred pattern:

```text id="k8r2qd"
Client

 |

Home Resolver

 |

Federated Resolver Network

 |

Foreign Universe
```

---

# 14. Resolver Responsibilities

Resolvers may provide:

- object lookup,
- assertion retrieval,
- evidence retrieval,
- relationship traversal,
- verification assistance.

Resolvers do not become authoritative merely because they answer.

---

# 15. Resolver Delegation

A resolver requires delegated authority or capability.

Questions:

- What may it resolve?
- For whom?
- Under what conditions?
- For how long?

---

# 16. Caching

Distributed systems require caching.

LORE should support caching while preserving:

- provenance,
- expiration,
- authority boundaries,
- freshness.

A cached object is not a new authority source.

---

# 17. Foreign Object Retrieval

Cross-universe retrieval may involve:

- locating foreign objects,
- retrieving assertions,
- validating evidence,
- checking lifecycle,
- evaluating trust relationships.

---

# 18. Federation Failure Modes

Potential failures:

## Foreign Universe Unavailable

Question:

Can stale information be safely used?

---

## Conflicting Assertions

Question:

How are disagreements represented?

---

## Revoked Trust

Question:

How quickly do federation changes propagate?

---

# 19. Break-Glass Recovery

Root lifecycle requires recovery capability.

Potential mechanisms:

- pre-issued emergency capabilities,
- offline recovery material,
- controlled root replacement.

---

# 20. Open Questions

Reviewers should challenge:

1. Should LORE define its own UID format?
2. Should root information appear in identifiers?
3. How much information should identifiers reveal?
4. Are signed identity objects required?
5. How should federation relationships be represented?
6. How should compromised roots recover?
7. What resolver capabilities are safe?

---

# 21. Namespace Principle

The governing principle:

> A namespace provides a place to ask questions. It does not provide the answers by itself.

---

LORE Volume 7 - Identifier, Namespace, and Federation Model v0.2.md
