# LORE Volume 25 — Prior Art Survey and Historical Design Influences

## Version 0.2 Draft

---

# 1. Purpose

This volume documents prior art, historical systems, and design influences relevant to LORE.

The purpose is not to claim novelty where none exists.

The purpose is to identify:

- concepts that already exist,
- lessons from successful systems,
- lessons from failed systems,
- ideas worth adapting,
- and mistakes worth avoiding.

---

# 2. Core Principle

The governing principle:

> Good designs rarely appear from nowhere. They emerge by understanding what worked, what failed, and why.

---

# 3. Prior Art Position

LORE should not be evaluated as a replacement for existing technologies.

Many existing systems already solve portions of the problem.

The question is:

> Are there missing abstractions between these systems that become increasingly important as software becomes more autonomous?

---

# 4. Trusted Computing Base and Security Models

## 4.1 Trusted Computing Base (TCB)

The Trusted Computing Base concept established a foundational principle:

> Security depends on clearly identifying what must be trusted.

Important lessons:

- trust boundaries must be explicit,
- trusted components should be minimized,
- security assumptions should be documented.

LORE application:

A semantic trust system must identify:

- what is authoritative,
- why it is authoritative,
- what happens when it fails.

---

## 4.2 The Rainbow Series

The Trusted Computer System Evaluation Criteria and related Rainbow Series documents introduced important security concepts:

- reference monitors,
- security kernels,
- mandatory access control,
- trusted paths,
- assurance levels.

Lessons:

Security is not only about mechanisms.

It is also about:

- architecture,
- assurance,
- verification,
- explicit trust assumptions.

---

# 5. OpenVMS Privilege Model

OpenVMS provides an important example of granular authority.

The model separated:

- identity,
- privileges,
- rights,
- access decisions.

Lessons:

Privilege should not be binary.

A principal may require:

- specific capabilities,
- limited scope,
- explicit authority.

LORE relevance:

Authority and identity should remain separate.

---

# 6. Unix Philosophy

Unix introduced powerful concepts:

- small composable tools,
- clear abstractions,
- text interfaces,
- simple primitives.

Lessons:

Simple primitives often outlive complex systems.

LORE relevance:

The core model should remain small.

Complexity should emerge through composition.

---

# 7. POSIX

POSIX demonstrates the value of shared interfaces.

Lessons:

Interoperability requires:

- common semantics,
- predictable behavior,
- clear boundaries.

LORE relevance:

The goal should be shared meaning, not implementation uniformity.

---

# 8. PGP and GnuPG

PGP explored decentralized trust.

Important concepts:

- cryptographic identity,
- signatures,
- key ownership,
- trust relationships.

Lessons:

Cryptography can establish origin.

It does not automatically establish truth.

---

# 9. SSL to TLS Evolution

The evolution from SSL to TLS demonstrates:

- security protocols require iteration,
- early assumptions may fail,
- compatibility creates challenges.

Lessons:

Security architectures must support:

- migration,
- deprecation,
- evolution.

LORE relevance:

Lifecycle is not optional.

---

# 10. DNS

DNS demonstrates both successful abstraction and historical limitations.

Successful concepts:

- distributed naming,
- delegation,
- hierarchical authority.

Challenges:

- namespace conflicts,
- trust assumptions,
- cache behavior.

LORE relevance:

Names and identities are not the same thing.

Resolution and authority must remain distinct.

---

# 11. IAM, RBAC, and ABAC

## Identity and Access Management

IAM systems provide:

- authentication,
- identity lifecycle,
- access relationships.

---

## Role-Based Access Control

RBAC provides:

- abstraction over individual permissions,
- manageable authorization structures.

---

## Attribute-Based Access Control

ABAC adds:

- context,
- attributes,
- policy evaluation.

---

Lessons:

Authorization requires abstraction.

However:

Identity, authority, context, and evidence often remain distributed across multiple systems.

---

# 12. PAM

Privileged Access Management addresses:

- elevated access,
- credential protection,
- temporary privilege.

Lessons:

Standing authority is dangerous.

Temporary, scoped access is preferable.

---

# 13. Zero Trust

Zero Trust established a major principle:

> Never assume trust based solely on location or network position.

Lessons:

Trust should be continuously evaluated.

LORE relevance:

Context matters.

---

# 14. Verifiable Credentials and Decentralized Identity

These systems explore:

- portable identity,
- cryptographic claims,
- issuer relationships.

Lessons:

Assertions need:

- issuers,
- verification,
- provenance.

---

# 15. Supply Chain Security

Modern software supply chain models emphasize:

- provenance,
- artifact identity,
- dependency relationships.

Examples:

- software bills of materials,
- signed artifacts,
- build attestations.

Lessons:

Objects have histories.

Those histories affect trust.

---

# 16. Operational Technology Security

OT and ICS security provide critical lessons:

- availability matters,
- safety matters,
- context matters,
- physical consequences exist.

LORE relevance:

A technically valid authorization may still be operationally unsafe.

---

# 17. Graph Technologies

Graph databases and semantic systems demonstrate:

- relationships are valuable data,
- traversal enables discovery,
- connected information provides context.

Lessons:

Relationships should not be treated as secondary metadata.

---

# 18. Compiler and Intermediate Representation Influence

Compiler architecture provides a useful pattern:

```text id="m8q3vx"
Source Language

|

Intermediate Representation

|

Target Output
```

LORE relevance:

A semantic intermediate representation may avoid premature storage and protocol lock-in.

---

# 19. Lessons From Prior Art

Common successful patterns:

- explicit boundaries,
- small primitives,
- delegation,
- lifecycle,
- composability,
- separation of concerns.

Common failures:

- hidden assumptions,
- excessive trust,
- weak lifecycle,
- overloaded concepts,
- unclear authority.

---

# 20. Open Questions

Reviewers should challenge:

1. Is LORE combining existing concepts in a useful way?
2. What prior art already solves the problem?
3. What missing abstraction remains?
4. Which historical lessons are most applicable?
5. Which historical mistakes are most likely to repeat?

---

# 21. Prior Art Principle

The governing principle:

> Innovation is not ignoring history. It is understanding which lessons remain unresolved.

---

LORE Volume 25 — Prior Art Survey and Historical Design Influences v0.2.md
