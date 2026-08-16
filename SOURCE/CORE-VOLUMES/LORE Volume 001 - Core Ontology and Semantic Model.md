<!-- lore_anchor_id: 8f3m1p -->
# LORE Volume 1 - Core Ontology and Semantic Model

**Filename:** `LORE-Volume-1-Core-Ontology-and-Semantics.md`  
**Status:** Draft  
**Version:** 0.1  

---

# 1. Purpose

This volume defines the fundamental concepts represented by LORE.

It answers:

> What things exist in the LORE universe, and what do they mean?

LORE begins with semantics.

Implementation, storage, transport, and integration mechanisms must preserve these meanings.

A system that stores information without preserving meaning has preserved data, not context.

---

# 2. Ontology as the Foundation

An ontology defines:

- what entities exist,
- what properties they possess,
- how entities relate,
- what distinctions matter.

LORE uses ontology because trust depends on distinctions.

Examples:

These are not equivalent:

```
OBJECT
OBJECT_REF

ASSERTION
EVIDENCE

AUTHORITY
CAPABILITY

CONTEXT_HINT
TRUSTED_CONTEXT
```

A trustworthy system must preserve these differences.

---

# 3. Semantic Model Overview

The primary LORE concepts are:

```text
OBJECT
    |
    +-- OBJECT_REF
    |
    +-- ASSERTION
            |
            +-- EVIDENCE

AUTHORITY
    |
    +-- CAPABILITY

EVENT

CONTEXT

RELATIONSHIP
```

These concepts combine to represent trustworthy human and machine context.

---

# 4. OBJECT

An OBJECT represents a thing that exists within a LORE context.

Examples:

- person,
- system,
- document,
- service,
- device,
- organization,
- process,
- artifact.

An OBJECT may have:

- identity,
- attributes,
- relationships,
- lifecycle.

An OBJECT is not automatically trusted.

Existence does not imply authority.

---

# 5. OBJECT_REF

An OBJECT_REF represents a reference to an object.

A reference is not the object itself.

This distinction is fundamental.

Example:

```yaml
OBJECT_REF:
  target:
    customer_database
```

The reference requires resolution.

Questions include:

- Is resolution permitted?
- Is the target available?
- Is the target current?
- Is the relationship still valid?

---

# 6. Indirection

Indirection is a powerful tool.

It enables:

- reuse,
- abstraction,
- delegation,
- distributed systems,
- integration.

However, indirection introduces risk.

A reference can hide:

- changed meaning,
- changed ownership,
- changed authority,
- changed destination.

Therefore:

> Indirection MUST remain visible.

A system should never silently transform:

```
REFERENCE
```

into:

```
OBJECT
```

without preserving the relationship.

---

# 7. OBJECT_ALIAS

An alias provides a human-friendly name for an object.

Examples:

```
production
admin
primary_database
```

Aliases are useful.

Aliases are dangerous.

An alias may change meaning over time.

Therefore aliases MUST preserve:

- alias type,
- resolution history,
- ownership,
- lifecycle.

An alias is not an identity.

---

# 8. ASSERTION

An ASSERTION represents a claim.

Examples:

- "This service is healthy."
- "This person is authorized."
- "This event occurred."
- "This configuration is approved."

An assertion answers:

> Someone claims this is true.

It does not answer:

> Is this true?

---

# 9. ASSERTION Versus Fact

LORE intentionally avoids treating assertions as facts.

A claim may be:

- accurate,
- incomplete,
- outdated,
- incorrect,
- malicious.

Therefore:

```
ASSERTION != TRUTH
```

The system must preserve the reasoning path from claim to confidence.

---

# 10. EVIDENCE

EVIDENCE supports an assertion.

Examples:

Technical evidence:

- cryptographic signatures,
- measurements,
- logs,
- test results.

Human evidence:

- approvals,
- attestations,
- reviews.

External evidence:

- certificates,
- authoritative records.

---

# 11. Evidence Is Contextual

Evidence without context is incomplete.

Example:

Insufficient:

```yaml
EVIDENCE:
  status:
    healthy
```

Better:

```yaml
EVIDENCE:
  source:
    monitoring_system

  collected:
    timestamp

  method:
    automated_check

  scope:
    production_api
```

The question remains:

> Why should this evidence be trusted?

---

# 12. Evidence Is Not Authority

A recurring security failure:

```
Evidence exists
      |
      v
System assumes permission
```

LORE rejects this.

Evidence answers:

> What happened?

Authority answers:

> Who is allowed to decide or act?

These are separate concepts.

---

# 13. AUTHORITY

AUTHORITY represents the ability to make valid decisions, assertions, or grants.

Authority includes:

- issuer,
- subject,
- scope,
- constraints,
- lifecycle.

Example:

```yaml
AUTHORITY:
  issuer:
    SECURITY_TEAM

  subject:
    ADMINISTRATOR

  scope:
    ACCESS_MANAGEMENT
```

Authority must have provenance.

---

# 14. CAPABILITY

A CAPABILITY represents bounded operational permission.

A capability answers:

> What may this subject do?

A capability is not:

- ownership,
- identity,
- trustworthiness,
- unlimited access.

Capabilities should be:

- narrow,
- explicit,
- reviewable,
- revocable.

---

# 15. EVENT

An EVENT represents a meaningful transition.

Examples:

- creation,
- delegation,
- approval,
- revocation,
- recovery,
- lifecycle change.

Events preserve history.

Without events, systems lose:

- causality,
- accountability,
- explanation.

---

# 16. CONTEXT

CONTEXT represents information required to interpret objects, assertions, and actions.

Context includes:

- assumptions,
- relationships,
- constraints,
- history,
- purpose.

Context is often the missing element in modern systems.

---

# 17. CONTEXT_HINT

A CONTEXT_HINT represents potentially useful but untrusted information.

Example:

An AI agent passes prior conversation context to another agent.

The receiving system may use the information.

However:

```
CONTEXT_HINT
```

does not equal:

```
ASSERTION
```

or:

```
TRUSTED_CONTEXT
```

---

# 18. Context Promotion

Context may move through lifecycle states.

Example:

```text
CONTEXT_HINT

      |
      | validation

      v

CONTEXT_ASSERTION

      |
      | evidence and authority

      v

TRUSTED_CONTEXT
```

Promotion requires explicit justification.

---

# 19. RELATIONSHIP

Relationships connect objects and provide meaning.

Examples:

```
USER
    owns
DEVICE

ADMIN
    manages
SERVICE

CERTIFICATE
    supports
ASSERTION
```

Relationships are first-class concepts.

They should not be hidden in undocumented conventions.

---

# 20. Semantic Separation Rules

The following distinctions are fundamental:

| Concept A | Concept B | Difference |
|---|---|---|
| OBJECT | OBJECT_REF | Thing vs reference |
| ASSERTION | EVIDENCE | Claim vs support |
| EVIDENCE | AUTHORITY | Proof vs permission |
| AUTHORITY | CAPABILITY | Ability to grant vs ability to act |
| CONTEXT_HINT | TRUSTED_CONTEXT | Possible context vs verified context |
| ALIAS | IDENTITY | Name vs entity |

---

# 21. Serialization Requirements

The semantic model must survive representation.

Whether stored as:

- YAML,
- JSON,
- database records,
- messages,
- documents,

the distinctions must remain visible.

A parser should not be required to understand a hidden convention.

---

# 22. Design Questions

Open questions:

1. Which concepts are mandatory in the core?
2. Which concepts are extensions?
3. How should relationships be represented?
4. How should semantic versioning apply?
5. How should conflicting ontologies interact?
6. How should external schemas map into LORE?

---

# 23. Summary

LORE begins by making distinctions explicit.

A trustworthy system must know the difference between:

- a thing,
- a reference to a thing,
- a claim about a thing,
- evidence supporting that claim,
- authority affecting that thing,
- capability acting upon that thing,
- context explaining that thing.

The foundation of trust is not knowing more.

The foundation of trust is knowing what kind of thing you know.

---

**End of LORE Volume 1 - Core Ontology and Semantic Model**
```

Volume 2 follows.
