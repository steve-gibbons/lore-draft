<!-- lore_anchor_id: 7q9n2k -->
# LORE Volume 2 — Trust, Security, and Authorization

**Filename:** `LORE-Volume-2-Trust-Security-and-Authorization.md`  
**Status:** Draft  
**Version:** 0.1  

---

# 1. Purpose

This volume defines how LORE establishes, evaluates, and limits trust.

It answers:

> Why should information be trusted, and why should an action be permitted?

LORE treats trust and authorization as related but separate concepts.

A trusted statement does not automatically grant authority.

Authority does not automatically imply correctness.

Permission does not automatically imply wisdom.

---

# 2. Trust Philosophy

Trust is not a property attached permanently to an object.

Trust is a relationship between:

- a subject,
- an assertion,
- evidence,
- authority,
- context,
- time.

A statement may be trusted in one context and inappropriate in another.

---

# 3. Trust Is Not Identity

A common design mistake:

```
Identity
    |
    v
Trust
```

LORE rejects this assumption.

Knowing who something is does not automatically answer:

- Is it correct?
- Is it current?
- Is it authorized?
- Is it appropriate?

Identity is one input to trust evaluation.

It is not the conclusion.

---

# 4. Trust Model

A simplified trust relationship:

```
ASSERTION
    |
    v
EVIDENCE
    |
    v
EVALUATION
    |
    v
TRUST DECISION
```

The evaluation considers:

- source,
- evidence quality,
- authority,
- freshness,
- scope,
- intended use.

---

# 5. Evidence-Based Trust

LORE prefers evidence-backed assertions.

A useful model:

```yaml
ASSERTION:
  claim:
    SERVICE_HEALTHY

  evidence:
    - MONITORING_RESULT

  authority:
    - OPERATIONS_TEAM

  context:
    - PRODUCTION_ENVIRONMENT
```

The goal is not absolute certainty.

The goal is explainable confidence.

---

# 6. Evidence Chains

Evidence may itself require context.

Example:

```
ASSERTION
    |
    supported by
    |
EVIDENCE
    |
    supported by
    |
SOURCE
```

LORE preserves these relationships.

A reviewer should be able to ask:

> Why do we believe this?

and receive a meaningful answer.

---

# 7. Trust Promotion

Information may move through trust states.

Example:

```
UNKNOWN

    |
    v

OBSERVED

    |
    v

ASSERTED

    |
    v

EVIDENCE_SUPPORTED

    |
    v

TRUSTED_CONTEXT
```

Promotion requires explicit criteria.

Trust should not increase merely because information has existed for a long time.

---

# 8. Trust Decay

Trust can become invalid.

Reasons include:

- time,
- changed ownership,
- changed environment,
- revoked authority,
- superseding evidence.

Therefore:

LORE SHOULD support:

- expiration,
- revocation,
- replacement,
- historical preservation.

---

# 9. Conflicting Assertions

Real systems contain disagreement.

Examples:

- two systems report different states,
- two authorities disagree,
- old evidence conflicts with new evidence.

LORE should preserve disagreement rather than silently select a winner.

Example:

```
ASSERTION_A
    |
    conflicts with
    |
ASSERTION_B
```

The conflict itself is valuable context.

---

# 10. Security Boundaries

Trust boundaries must be explicit.

Examples:

- human to agent,
- agent to agent,
- client to server,
- plugin to host,
- organization to organization.

A trust boundary exists wherever assumptions change.

---

# 11. Capability-Based Authorization

LORE uses a capability-oriented authorization model.

A capability represents:

> A bounded ability to perform an action on a resource under defined conditions.

A capability includes:

- issuer,
- holder,
- action,
- target,
- constraints,
- expiration,
- delegation rules.

Example:

```yaml
CAPABILITY:

  issuer:
    AUTHORITY_REF

  holder:
    SUBJECT_REF

  action:
    READ

  target:
    RESOURCE_REF

  expiration:
    TIMESTAMP
```

---

# 12. Authority Versus Capability

These concepts must remain separate.

```
AUTHORITY
    |
    grants
    |
CAPABILITY
    |
    permits
    |
ACTION
```

Authority answers:

> Who may grant permission?

Capability answers:

> What may be done?

---

# 13. Least Privilege

Capabilities SHOULD be:

- narrow,
- explicit,
- time-limited,
- reviewable.

The goal is not maximum restriction.

The goal is:

> Maximum useful capability with minimum unnecessary authority.

---

# 14. Capability Scope

Scope is the primary security boundary.

A capability should define:

- domain,
- resource,
- action,
- time,
- conditions.

Example:

```
READ
    /
    production
    /
    api
    /
    users
```

is preferable to:

```
ADMIN EVERYTHING
```

---

# 15. Hierarchical Resource Matching

Many systems contain natural trees:

```
/organization
    /department
        /service
            /resource
```

LORE supports hierarchical capability matching.

The hierarchy should remain visible.

---

# 16. Globbing-Style Capability Matching

LORE favors predictable pattern matching.

Example:

```
/production/api/*
```

means:

All objects beneath this known path.

The purpose is human understanding.

Security administrators should be able to predict the result of a pattern.

---

# 17. Why Not SQL-Like Wildcards?

SQL-style patterns are optimized for querying.

Example:

```sql
LIKE '%admin%'
```

Authorization requires stronger guarantees.

Potential problems:

- hidden matches,
- unclear scope,
- difficult auditing,
- unexpected expansion.

LORE prefers semantics closer to filesystem globbing.

---

# 18. Negative Authorization

Negative rules are intentionally deferred.

Examples:

```
ALLOW everything
DENY one exception
```

or:

```
ALLOW one thing
DENY another
```

These systems become difficult to reason about.

The principle:

> The absence of authority should be easier to understand than the presence of exceptions.

Negative rules may exist in extensions.

They should not complicate the core model unnecessarily.

---

# 19. Aliases

Aliases improve usability.

They also introduce risk.

Example:

```
admin
```

Questions:

- Which administrator?
- Which role?
- Current or historical?
- Organization-specific?

Aliases MUST preserve:

- type,
- resolution,
- history,
- ownership.

An alias is not identity.

---

# 20. Delegation

Delegation allows controlled transfer of authority.

Example:

```
ADMIN

   delegates

AGENT

   accesses

SERVICE
```

Delegation MUST preserve:

- original authority,
- delegation chain,
- reduced scope,
- expiration.

---

# 21. Delegation Constraint

A delegated capability cannot exceed its parent.

Formally:

```
CHILD_CAPABILITY ⊆ PARENT_CAPABILITY
```

A child may have less authority.

Never more.

---

# 22. Capability Tickets

LORE may use ticket-based authorization patterns.

Existing systems provide valuable lessons.

Examples:

- Kerberos tickets,
- signed tokens,
- certificate-based authorization.

LORE extends these concepts by adding:

- evidence,
- lifecycle,
- context,
- provenance.

---

# 23. Server-Side Validation

Clients should not be trusted to enforce authorization.

A client may present:

```
CAPABILITY
```

The server must evaluate:

- signature,
- issuer,
- scope,
- expiration,
- revocation,
- context.

The capability is evidence of permission.

It is not a bypass.

---

# 24. MCP and Agent Authorization

LORE can integrate with agent protocols through adapters.

A minimal architecture:

```
AGENT

    |
    presents capability

    v

LORE ADAPTER

    |
    validates

    v

MCP SERVER
```

The integration layer should remain simple.

Authorization complexity belongs in the trust architecture.

---

# 25. Plugin Security

Plugins are trust boundaries.

Plugins SHOULD NOT receive:

- ambient authority,
- unrestricted filesystem access,
- unrestricted network access,
- host credentials.

Instead:

```
HOST

    grants

CAPABILITY

    to

PLUGIN
```

---

# 26. Process Isolation

High-risk plugins SHOULD prefer process isolation.

Benefits:

- reduced blast radius,
- stronger boundaries,
- easier auditing,
- clearer authority.

Tradeoffs:

- communication overhead,
- operational complexity.

---

# 27. Security Anti-Patterns

## Ambient Authority

A component can do anything because of where it runs.

---

## Capability Creep

Permissions accumulate without review.

---

## Hidden Expansion

A friendly name silently expands authority.

---

## Permanent Emergency Access

Temporary recovery mechanisms become permanent privileges.

---

## Trust by Proximity

Something is trusted because it is nearby.

---

## Identity Equals Authority

Knowing who someone is does not define what they may do.

---

# 28. Security Invariants

Candidate MUST requirements:

## Invariant 1

Capabilities MUST have explicit scope.

---

## Invariant 2

Delegated capabilities MUST NOT exceed parent capabilities.

---

## Invariant 3

Authorization decisions MUST consider lifecycle state.

---

## Invariant 4

References and aliases MUST NOT silently expand authority.

---

## Invariant 5

Trust promotion MUST require explicit justification.

---

# 29. Design Questions

Open questions:

1. Should capability syntax become a formal standard?
2. How should glob patterns be standardized?
3. How should conflicting capabilities resolve?
4. How should revocation propagate?
5. How much authorization logic belongs in LORE versus consuming systems?
6. Should offline capability verification be supported?

---

# 30. Summary

LORE treats security as explainable authority.

A trustworthy authorization decision should answer:

- Who granted this?
- Who holds it?
- What can they do?
- What limits apply?
- What evidence supports it?
- When does it expire?
- What changed?

Security is not only preventing action.

Security is preserving the ability to explain why action was allowed.

---

**End of LORE Volume 2 — Trust, Security, and Authorization**
```

Volume 3 follows.
