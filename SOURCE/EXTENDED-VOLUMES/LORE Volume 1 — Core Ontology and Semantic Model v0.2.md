# LORE Volume 1 — Core Ontology and Semantic Model

## Version 0.2 Draft

---

# 1. Purpose

The LORE ontology defines the core semantic objects and relationships required for systems to reason about identity, trust, authority, evidence, context, and lifecycle.

The purpose of the ontology is not to model every domain.

The purpose is to provide stable primitives that allow domains to describe themselves without collapsing important distinctions.

---

# 2. Core Ontological Principle

LORE separates concepts that are frequently combined incorrectly.

The following distinctions are fundamental:

```
Identifier ≠ Object

Object ≠ Representation

Assertion ≠ Evidence

Evidence ≠ Truth

Identity ≠ Authority

Authority ≠ Capability

Capability ≠ Action

Relationship ≠ Permission

Connectivity ≠ Trust
```

The purpose of these separations is to prevent historical patterns where systems accidentally infer more than the available information supports.

---

# 3. Core Object Families

LORE core objects are organized into several semantic families.

## Identity Objects

Represent things that can be referred to.

Examples:

- persons,
- organizations,
- devices,
- applications,
- services,
- agents,
- resources.

Identity answers:

> "Which thing?"

It does not answer:

> "What may this thing do?"

---

## Assertion Objects

Represent claims made by an issuer.

Examples:

- ownership claims,
- compliance claims,
- relationship claims,
- status claims.

An assertion contains:

- issuer,
- subject,
- claim,
- context,
- lifecycle.

An assertion answers:

> "What is being claimed?"

---

## Evidence Objects

Represent support for assertions.

Examples:

- documents,
- measurements,
- attestations,
- signatures,
- observations,
- records.

Evidence answers:

> "Why should this assertion be considered?"

---

## Authority Objects

Represent the ability to delegate or establish permissions.

Authority is not inherent in identity.

Authority must have:

- issuer,
- scope,
- lifecycle,
- constraints.

---

## Capability Objects

Represent permitted actions.

Capabilities should be:

- scoped,
- explicit,
- time bounded,
- revocable.

Possession of a capability is not the same as identity.

---

## Context Objects

Represent conditions affecting interpretation.

Examples:

- time,
- location,
- network,
- environment,
- purpose,
- operational state.

Context answers:

> "Under what conditions does this apply?"

---

## Relationship Objects

Represent connections among entities.

Relationships are first-class objects.

They may represent:

- ownership,
- membership,
- delegation,
- dependency,
- preference,
- association.

Relationships:

- have lifecycle,
- may have evidence,
- may be directional or bidirectional depending on semantics.

---

# 4. LORE Universe

A LORE Universe defines an identity namespace and authority boundary.

A universe provides:

- root identity,
- namespace ownership,
- identity issuance,
- federation relationships.

A universe is not:

- a global authority,
- universal truth,
- automatic trust.

---

# 5. Identity and UID Model

## UID Principle

A LORE UID identifies an object.

It does not imply:

- authority,
- capability,
- ownership,
- trust,
- correctness.

---

## Namespace-Aware UID

A UID must contain sufficient information to identify its issuing universe.

Conceptually:

```
LORE:<ROOT_UID>/<OBJECT_UID>
```

The root component allows:

- authority discovery,
- resolution routing,
- federation traversal.

The root component does not grant trust.

---

## UID Generation

The current candidate:

```
HASH(
    ROOT_UID
    +
    GENERATION_SECRET
    +
    TIMESTAMP
    +
    MONOTONIC_COUNTER
)
```

**[<-- This is crufty - SPG]**

Reviewer target:

The requirement is global uniqueness.

The construction is an implementation choice.

Questions:

- Should timestamps influence canonical identifiers?
- Should ordering be separated from identity?
- Should existing identifier standards be used?

---

# 6. Signed Identity Objects

Identity objects may be signed by their issuing authority.

A signature demonstrates:

> "This authority issued this object."

A signature does not demonstrate:

- trustworthiness,
- authorization,
- ownership,
- capability.

Those require additional semantic objects.

---

# 7. Resolution and Retrieval

LORE clients should not require global knowledge.

The client interacts primarily with a trusted resolution layer.

Example:

```
LORE Client

    |

Home Resolver

    |

LORE Federation
```

The resolver may provide:

- identifier resolution,
- object retrieval,
- assertion retrieval,
- evidence verification,
- relationship traversal,
- query forwarding.

---

# 8. Layered Resolution

Resolvers may exist at multiple layers.

Examples:

- local resolver,
- cache resolver,
- enterprise resolver,
- delegated resolver,
- foreign universe resolver.

The resolver does not become authoritative merely because it answers.

Authority must be delegated.

---

# 9. Delegation Model

Delegation is a first-class relationship.

A delegation defines:

- delegating authority,
- recipient,
- permitted operations,
- constraints,
- expiration,
- revocation.

Example:

```
Root Universe

delegates

Office Resolver

permission:

resolve device assertions

restriction:

cannot issue identities
```

---

# 10. Relationship Semantics

Relationships are intentionally general.

The core model provides relationship families.

Domains should reuse existing families whenever possible.

Examples:

## Ownership

```
Organization
    owns
Device
```

## Membership

```
Person
    member_of
Organization
```

## Delegation

```
Authority
    delegates
Capability
```

## Preference

```
Person
    prefers
Object
```

Domains may extend relationships when existing families are insufficient.

---

# 11. Temporal Model

Time is a core primitive.

LORE recommends:

- UTC/Zulu internal representation,
- explicit timezone handling at boundaries,
- lifecycle-aware timestamps.

Temporal information affects:

- validity,
- expiration,
- applicability,
- ordering,
- historical interpretation.

---

# 12. Location and Network Model

Location and network are separate concepts.

Location may represent:

- physical location,
- logical location,
- organizational location.

Network represents:

- connectivity,
- reachability,
- communication relationships.

Network context may include:

- IPv4,
- IPv6,
- telecommunications,
- dynamic addressing.

Network attachment is not identity.

---

# 13. Non-Human Actors and Conditions

LORE may model:

- people,
- software agents,
- organizations,
- devices,
- environmental conditions.

Non-human events and conditions may participate in relationships.

Examples:

- hurricane,
- earthquake,
- heat wave,
- infrastructure failure.

LORE remains agnostic regarding interpretation.

A condition may be modeled without requiring human-like agency.

---

# 14. Governance Objects

Governance is considered a domain ontology built on the core model.

Examples:

- review notes,
- risks,
- exceptions,
- decisions,
- approvals.

A review note may:

- remain a review artifact,
- become incorporated into a risk record,
- be referenced by an exception record.

This provides a practical test case for indirection semantics.

---

# 15. Core Ontology Boundary

The core ontology should remain intentionally small.

The question for every proposed object:

> Is this universally required for semantic trust relationships?

If not:

It likely belongs in a domain ontology.

---

LORE Volume 1 — Core Ontology and Semantic Model v0.2.md
