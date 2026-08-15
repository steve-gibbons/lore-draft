# LORE Volume 2 — Trust, Security, and Authorization

## Version 0.2 Draft

---

# 1. Purpose

This volume defines the LORE approach to trust, security boundaries, authorization relationships, and delegated authority.

The primary design goal:

> Prevent systems from accidentally treating identity, possession, assertion, or connectivity as sufficient justification for action.

LORE does not replace existing security controls.

LORE provides semantic context to improve security decisions.

---

# 2. Security Philosophy

## Trust Is Not a Property of a Thing

A common security failure is treating trust as an inherent property:

```
"This object is trusted."
```

LORE instead models trust as a relationship:

```
Subject
    |
    | under conditions
    |
Authority evaluates
    |
    v
Trust decision
```

Trust depends on:

- who is making the decision,
- what is being evaluated,
- what evidence exists,
- what context applies,
- what lifecycle state exists.

---

# 3. Identity, Authentication, and Authorization

LORE intentionally separates:

## Identity

Answers:

> "What is this?"

Examples:

- person,
- service,
- device,
- agent,
- organization.

---

## Authentication

Answers:

> "Can this identity claim be verified?"

Examples:

- cryptographic proof,
- credential verification,
- attestation.

---

## Authorization

Answers:

> "Should this action be allowed?"

Authorization requires:

- identity,
- authority,
- capability,
- context,
- policy,
- evidence.

---

# 4. Authority Model

Authority is not inherited automatically.

Authority must be:

- explicitly represented,
- scoped,
- delegated,
- lifecycle managed.

Example:

Incorrect:

```
Employee
 |
has account
 |
can access everything
```

Preferred:

```
Principal

has

Capability

for

Action

on

Object

under

Context
```

---

# 5. Capability Model

Capabilities represent permitted actions.

A capability should define:

- issuer,
- holder,
- action,
- target,
- constraints,
- expiration,
- revocation.

Example:

``` id="7f6b3q"
Capability:

Issuer:
    Operations Authority

Holder:
    Maintenance Agent

Action:
    Restart Service

Target:
    Production System A

Validity:
    30 minutes
```

---

# 6. Least Authority

LORE applies the principle:

> The minimum authority necessary for the intended purpose should be granted for the minimum necessary duration.

This includes:

- human users,
- software agents,
- services,
- automation,
- delegated resolvers.

---

# 7. Agent Security Envelope

The motivating use case for LORE is increasingly capable software agents.

Current common pattern:

```
Agent

+

Permanent Credential

+

Broad Permission

+

External Systems
```

This creates a mismatch between:

- capability,
- authority,
- purpose,
- context,
- containment.

LORE proposes a semantic envelope:

```
Agent Identity

+

Approved Purpose

+

Scoped Authority

+

Supporting Evidence

+

Time Bound

+

Containment Boundary

+

Lifecycle
```

---

# 8. Blast Radius and Containment

Containment is a first-class security property.

A security decision should consider:

> What is the maximum consequence if this object, credential, assertion, or actor behaves incorrectly?

Containment dimensions include:

- scope,
- authority,
- dependency,
- time,
- geography,
- population,
- recovery capability.

---

# 9. Time-Bounded Authority

Permanent authority creates accumulated risk.

LORE emphasizes:

- expiration,
- renewal,
- review,
- revocation.

A temporary exception that never expires becomes permanent privilege.

---

# 10. Trust Anchors

Trust anchors are explicit objects.

Examples:

- root identities,
- certificate authorities,
- organizational authorities,
- federation roots.

Trust anchors require lifecycle management:

- creation,
- activation,
- rotation,
- replacement,
- revocation,
- recovery.

A trust anchor is not permanent simply because it was trusted previously.

---

# 11. Root Lifecycle

A LORE root requires:

## Normal Lifecycle

- creation,
- publication,
- operation,
- renewal.

## Change Lifecycle

- rotation,
- migration,
- replacement.

## Failure Lifecycle

- compromise response,
- revocation,
- recovery,
- emergency transition.

---

# 12. Break-Glass Capabilities

Emergency access is necessary.

Emergency access is dangerous.

LORE treats break-glass authority as:

- pre-designed,
- constrained,
- auditable,
- time limited.

A recovery mechanism must not become an unrestricted permanent authority path.

---

# 13. Delegation Security

Delegation is a security boundary.

A delegated authority must specify:

- issuer,
- recipient,
- purpose,
- scope,
- constraints,
- duration.

Example:

```
Enterprise Root

delegates

Regional Resolver

ability:

resolve approved object classes

restriction:

cannot issue identities
```

---

# 14. Resolver Security

Resolvers are trusted services but are not automatically authorities.

Potential threats:

## Resolver Compromise

A compromised resolver may:

- return false objects,
- hide valid information,
- provide stale information.

Mitigations:

- signed responses,
- provenance preservation,
- independent verification.

---

## Cache Poisoning

Cached information requires:

- source attribution,
- retrieval timestamp,
- expiration,
- validation state.

A cache is not a new authority.

---

## Split Resolution

Different resolvers may return different information.

LORE preserves:

- competing assertions,
- source identity,
- evidence,
- trust context.

The system does not simply select an answer without context.

---

# 15. Federation Security

Federation establishes relationships between independent LORE universes.

Federation requires:

- explicit trust relationship,
- scope,
- purpose,
- lifecycle.

Example:

```
Universe A

trust relationship

Universe B

for:

device ownership assertions
```

Not:

```
Universe A trusts everything from Universe B
```

---

# 16. Evidence and Provenance

Security decisions should preserve:

- who asserted information,
- when it was asserted,
- what evidence supported it,
- what authority issued it,
- whether it remains valid.

Provenance is not optional metadata.

It is part of the security model.

---

# 17. Security Boundaries

LORE should make boundaries visible:

- identity boundary,
- authority boundary,
- delegation boundary,
- organizational boundary,
- lifecycle boundary,
- trust boundary.

A hidden boundary is a future failure point.

---

# 18. Security Review Questions

Reviewers should challenge:

1. Does LORE accidentally recreate existing authorization systems?
2. Are identity and authority sufficiently separated?
3. Can authority be laundered through delegation?
4. Can provenance itself become an attack target?
5. Can assertions be poisoned?
6. Can stale information remain trusted too long?
7. Can emergency mechanisms become permanent privilege?
8. Does the model sufficiently constrain autonomous agents?
9. Does LORE create new confused-deputy opportunities?

---

# 19. Core Security Principle

The central security principle:

> Possession is not permission. Identity is not authority. Assertion is not evidence. Evidence is not truth.

Security decisions require context, lifecycle, and explicit relationships.

---

LORE Volume 2 — Trust, Security, and Authorization v0.2.md
