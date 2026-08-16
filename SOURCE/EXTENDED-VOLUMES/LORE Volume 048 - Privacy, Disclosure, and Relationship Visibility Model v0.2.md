# LORE Volume 48 - Privacy, Disclosure, and Relationship Visibility Model

## Version 0.2 Draft

---

# 1. Purpose

This volume explores privacy considerations within LORE.

The purpose is to address an important tension:

> A system cannot make informed trust decisions without information, but unnecessary disclosure creates additional risk.

LORE must represent relationships without requiring unrestricted visibility of all relationships.

---

# 2. Core Principle

The governing principle:

> Trust requires information. Security requires controlling who receives that information.

---

# 3. Privacy Is Not Absence of Information

A common misconception:

```text id="m7q4vx"
Privacy

=

No Information Exists
```

A more useful model:

```text id="q8n5mp"
Privacy

=

Appropriate Information Access
```

---

# 4. Relationship Visibility

LORE relationships may contain sensitive information.

Examples:

- ownership,
- employment,
- organizational relationships,
- device relationships,
- operational dependencies.

---

# 5. Relationship Visibility Model

A relationship may have:

- existence,
- participants,
- attributes,
- evidence,
- visibility rules.

---

# 6. Discovery vs Disclosure

Important distinction:

```text id="x6m3qw"
Knowing Something Exists

≠

Knowing Everything About It
```

---

Example:

A system may know:

```text id="p9v5kr"
Object X exists
```

without receiving:

- ownership details,
- operational history,
- internal metadata.

---

# 7. Minimum Necessary Disclosure

A useful principle:

> Provide sufficient information for the decision being made, and no more.

---

# 8. Query-Specific Disclosure

Different questions require different information.

Example:

Question:

"Can I contact this service?"

May require:

- service identity,
- availability,
- contact authority.

May not require:

- internal architecture,
- employee ownership,
- unrelated relationships.

---

# 9. Relationship Confidentiality

Relationships themselves may require protection.

Examples:

```text id="h5m8qx"
Company A

depends-on

Vendor B
```

may reveal:

- business strategy,
- operational dependencies,
- security posture.

---

# 10. Privacy and Federation

Cross-universe queries require careful disclosure.

A foreign resolver should not automatically receive all local information.

---

# 11. Resolver Disclosure Model

A resolver may provide:

- direct answer,
- limited answer,
- proof of authority,
- proof of relationship,
- refusal.

---

# 12. Privacy-Preserving Verification

A useful capability:

> Prove enough to satisfy a decision without revealing unnecessary information.

---

Examples:

Instead of:

```text id="r7n4kp"
Full Identity Record
```

Provide:

```text id="v8m3qx"
Verified Member Of Authorized Group
```

---

# 13. Evidence Disclosure

Evidence may contain sensitive information.

Important distinction:

```text id="k4p8mw"
Evidence Exists

≠

Evidence Must Be Fully Shared
```

---

# 14. Evidence Minimization

Potential approaches:

- summaries,
- proofs,
- attestations,
- scoped disclosures.

---

# 15. Privacy and Agents

Agents create additional privacy considerations.

Questions:

- What information may an agent access?
- What information may an agent retain?
- What information may an agent disclose?

---

# 16. Agent Memory

Persistent agents may accumulate:

- conversations,
- decisions,
- relationships,
- credentials.

Lifecycle management becomes essential.

---

# 17. Privacy and AI Context

AI systems may infer information beyond explicit data.

Potential concerns:

- inference,
- correlation,
- unintended disclosure.

---

# 18. Metadata Privacy

Metadata may reveal:

- relationships,
- behavior patterns,
- operational structure.

Examples:

- timestamps,
- access patterns,
- dependency graphs.

---

# 19. Privacy Threats

Potential attacks:

## Relationship Enumeration

Discovering hidden relationships.

---

## Metadata Analysis

Inferring sensitive information.

---

## Correlation Attacks

Combining separate disclosures.

---

## Resolver Abuse

Using legitimate queries for unintended discovery.

---

# 20. Privacy Controls

Potential controls:

- access policies,
- disclosure scopes,
- query auditing,
- relationship visibility rules,
- federation boundaries.

---

# 21. Privacy and Transparency Balance

A difficult design problem:

More transparency:

- improves accountability,
- improves explainability.

Less transparency:

- reduces exposure.

---

# 22. Auditability

Privacy controls themselves require accountability.

Questions:

- Who requested information?
- Why?
- What was disclosed?
- Under what authority?

---

# 23. Relationship to Existing Privacy Systems

LORE does not replace:

- privacy management platforms,
- data protection programs,
- consent systems,
- regulatory frameworks.

LORE provides semantic relationship context.

---

# 24. Regulatory Considerations

Different domains may impose requirements involving:

- disclosure,
- retention,
- consent,
- access rights.

LORE should represent relevant relationships without embedding every regulatory model.

---

# 25. Privacy Failure Modes

Potential failures:

## Excessive Disclosure

Too much information exposed.

---

## Insufficient Disclosure

Decision makers lack needed context.

---

## Hidden Relationships

Important dependencies remain unknown.

---

## Privacy Theater

Controls exist without reducing exposure.

---

# 26. Review Questions

Reviewers should challenge:

1. What information should be globally discoverable?
2. What information should remain local?
3. How should proofs differ from disclosures?
4. How should relationship privacy work?
5. How should agents handle sensitive context?
6. How should privacy and explainability be balanced?

---

# 27. Privacy Principle

The governing principle:

> A trustworthy system should reveal enough context to justify decisions while preserving boundaries around information that does not need to be shared.

---

LORE Volume 48 - Privacy, Disclosure, and Relationship Visibility Model v0.2.md
