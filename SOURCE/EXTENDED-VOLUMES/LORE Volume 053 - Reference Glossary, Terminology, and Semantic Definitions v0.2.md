# LORE Volume 53 — Reference Glossary, Terminology, and Semantic Definitions

## Version 0.2 Draft

---

# 1. Purpose

This volume defines terminology used throughout LORE documentation.

The purpose is to reduce ambiguity and prevent familiar words from being interpreted differently across domains.

---

# 2. Core Principle

The governing principle:

> Precise language is a security control.

Ambiguous terminology creates ambiguous decisions.

---

# 3. Object

An object is an identifiable entity represented within a LORE universe.

An object may represent:

- physical entities,
- digital entities,
- services,
- organizations,
- people,
- concepts,
- resources.

---

# 4. Identifier

An identifier is a representation used to refer to an object.

Important distinction:

```text id="m7q4vx"
Identifier

≠

Object
```

An identifier points to something.

It does not define:

- ownership,
- authority,
- trust,
- permissions.

---

# 5. Unique Identifier (UID)

A UID is an identifier intended to uniquely distinguish an object.

A UID provides:

- reference,
- uniqueness,
- correlation.

A UID does not automatically provide:

- authenticity,
- authorization,
- provenance.

---

# 6. Reference

A reference is a relationship between an identifier and an object.

A reference answers:

> What does this identifier point toward?

---

# 7. Principal

A principal is an entity capable of possessing identity and authority.

Examples:

- person,
- organization,
- service,
- device,
- agent.

---

# 8. Identity

Identity represents the characteristics by which an entity is recognized.

Important distinction:

```text id="q8n5mp"
Identity

≠

Authority
```

Knowing who something is does not determine what it may do.

---

# 9. Authority

Authority represents the ability to perform actions or make decisions.

Authority may be:

- granted,
- delegated,
- constrained,
- expired,
- revoked.

---

# 10. Capability

A capability is a bounded representation of authority.

A capability should define:

- permitted action,
- permitted object,
- scope,
- duration,
- constraints.

---

# 11. Action

An action is an operation performed against an object.

Examples:

- read,
- modify,
- execute,
- delegate,
- approve,
- revoke.

---

# 12. Relationship

A relationship represents a connection between objects.

Examples:

```text id="x6m3qw"
Person

owns

Device
```

---

```text id="p9v5kr"
Application

uses

Service
```

---

# 13. Assertion

An assertion is a statement made by a source.

Example:

```text id="h5m8qx"
"Device X belongs to Organization Y"
```

---

# 14. Evidence

Evidence is information supporting or challenging an assertion.

Important distinction:

```text id="r7n4kp"
Assertion

≠

Evidence
```

An assertion is a claim.

Evidence provides support.

---

# 15. Provenance

Provenance describes the origin and history of information.

Questions answered:

- Where did this come from?
- Who created it?
- How was it transformed?
- What happened afterward?

---

# 16. Context

Context describes circumstances affecting interpretation.

Examples:

- time,
- location,
- purpose,
- environment,
- operational state.

---

# 17. Lifecycle

Lifecycle describes how something changes over time.

Possible states:

- created,
- active,
- modified,
- suspended,
- expired,
- retired.

---

# 18. Trust

Trust represents confidence that an object, assertion, or relationship is appropriate for a purpose.

Trust is:

- contextual,
- evidence-based,
- bounded.

---

# 19. Trust Is Not Truth

Important distinction:

```text id="v8m3qx"
Trusted

≠

Absolutely True
```

LORE represents confidence and justification, not universal truth.

---

# 20. Verification

Verification is the process of evaluating whether information satisfies requirements.

Verification may consider:

- signatures,
- authority,
- provenance,
- lifecycle,
- context.

---

# 21. Universe

A universe is a logical trust domain containing:

- objects,
- identifiers,
- relationships,
- authorities,
- policies.

---

# 22. Federation

Federation is a relationship between independent trust domains.

Federation does not imply:

- equality,
- unrestricted trust,
- shared ownership.

---

# 23. Resolver

A resolver is a service that retrieves and interprets LORE information.

A resolver is not automatically authoritative.

---

# 24. Root

A root is a foundational trust anchor.

Roots establish:

- namespace authority,
- trust boundaries,
- initial relationships.

---

# 25. Delegation

Delegation is the transfer of limited authority from one principal to another.

Good delegation includes:

- scope,
- purpose,
- expiration,
- accountability.

---

# 26. Containment

Containment limits the impact of failure or misuse.

Containment dimensions:

- authority,
- time,
- scope,
- dependency,
- recovery.

---

# 27. Blast Radius

Blast radius represents the maximum consequence of failure.

A key design question:

> If this relationship is wrong, what can happen?

---

# 28. Agent

An agent is a software entity capable of interpreting objectives and performing actions.

An agent is not automatically:

- a person,
- an owner,
- an authority.

---

# 29. Delegated Intelligence

Delegated intelligence describes situations where an agent acts on behalf of another principal.

The delegation relationship should remain explicit.

---

# 30. Semantic Model

The semantic model defines:

- concepts,
- relationships,
- meanings,
- constraints.

It should remain independent from implementation details.

---

# 31. Protocol

A protocol defines how systems communicate.

A protocol should not redefine the underlying semantic model.

---

# 32. Implementation

An implementation is a concrete realization of LORE concepts.

Multiple implementations should be possible.

---

# 33. Deployment

A deployment is an operational instance of LORE.

Examples:

- personal,
- enterprise,
- cloud,
- embedded.

---

# 34. Security Boundary

A security boundary separates areas with different trust assumptions.

Examples:

- organizations,
- systems,
- networks,
- universes.

---

# 35. Review Principle

The terminology itself should be reviewed.

A word that causes misunderstanding becomes a security problem.

---

# 36. Glossary Questions

Reviewers should challenge:

1. Are these terms sufficiently precise?
2. Are familiar words creating hidden assumptions?
3. Are any concepts overloaded?
4. Are important concepts missing?
5. Should any terms be renamed?

---

# 37. Terminology Principle

The governing principle:

> Shared understanding is the foundation on which shared trust can be built.

---

LORE Volume 53 — Reference Glossary, Terminology, and Semantic Definitions v0.2.md
