# LORE Volume 26 — Open Questions, Research Areas, and Future Exploration

## Version 0.2 Draft

---

# 1. Purpose

This volume captures unresolved questions and research areas.

The purpose is not to present incomplete concepts as decisions.

The purpose is to preserve important questions so they remain visible during future design work.

---

# 2. Core Principle

The governing principle:

> Unknowns should be represented explicitly rather than hidden behind assumptions.

---

# 3. Foundational Question

The central research question:

> Is there a missing semantic layer between existing security, identity, authorization, and distributed systems technologies?

---

# 4. Identity Research Questions

## 4.1 Identifier Design

Questions:

- What information belongs in an identifier?
- What information should never be encoded into an identifier?
- How should namespace authority be represented?
- How should collisions be prevented?

---

## 4.2 Namespace Authority

Questions:

- Should identifiers contain recognizable root information?
- How should foreign systems discover the correct authority?
- How should namespace ownership transfer occur?

---

## 4.3 Identifier Security

Questions:

- Should identifiers be signed objects?
- Should signatures prove creation authority?
- How should identifier compromise be handled?

---

# 5. Relationship Research Questions

Relationships appear to be a fundamental modeling primitive.

Questions:

- Which relationships belong in the core?
- How should relationship families be defined?
- How should domains introduce new relationship types?
- How should conflicting relationships be represented?

---

# 6. Bidirectional Relationship Research

A key question:

> Should relationships always be represented as traversable in both directions?

Example:

```text id="m7q4vx"
Person

owns

Device
```

should support:

```text id="q8n5mp"
Device

owned-by

Person
```

Questions:

- Is this always true?
- How is inverse meaning defined?
- Can all relationships have inverses?

---

# 7. Time Research Questions

Time appears repeatedly as a missing primitive in existing systems.

Questions:

- Should time be a first-class object?
- How should recurring schedules be modeled?
- How should historical state be reconstructed?
- How should future applicability be represented?

---

# 8. Time Map Research

Potential concept:

A time map represents applicability over time.

Examples:

- operating hours,
- maintenance windows,
- business rules,
- seasonal access,
- temporary authority.

Questions:

- Is this sufficiently general?
- Does it belong in the core?
- How should conflicts resolve?

---

# 9. Location Research Questions

Location is frequently overloaded.

Questions:

- Is location a primitive?
- Is physical location separate from logical location?
- How should uncertainty be represented?

Important distinction:

```text id="x6m3qw"
Location

≠

Network Location

≠

Trust
```

---

# 10. Context Research Questions

Questions:

- Which context dimensions matter?
- How should context confidence be represented?
- How should context be authenticated?
- How should privacy affect availability?

---

# 11. Evidence Research Questions

Questions:

- What qualifies as evidence?
- How is evidence quality represented?
- How are competing evidence sources evaluated?
- How is evidence expiration handled?

---

# 12. Authority Research Questions

Questions:

- What is the smallest useful authority unit?
- How should delegation work?
- How should authority chains be evaluated?
- How should authority conflicts resolve?

---

# 13. Capability Research Questions

Questions:

- Are capabilities objects?
- Are capabilities assertions?
- Are capabilities always scoped?
- How should capability inheritance work?

---

# 14. Agent Research Questions

Agents create additional uncertainty.

Questions:

- Does agent autonomy require new security primitives?
- Can existing IAM models be extended?
- What minimum containment is required?
- How should agent intent be represented?

---

# 15. Resolver Research Questions

Resolvers may become an important architectural component.

Questions:

- What authority does a resolver require?
- How are resolver permissions delegated?
- How should resolver compromise be detected?
- How should caching work?

---

# 16. Federation Research Questions

Questions:

- How do independent universes discover each other?
- How are trust relationships created?
- How are relationships revoked?
- How are conflicting universes handled?

---

# 17. Storage Research Questions

Questions:

- Is graph storage the natural representation?
- Is a relational model sufficient?
- Should multiple storage models coexist?
- What is the canonical intermediate representation?

---

# 18. Compiler Architecture Research

Potential architecture:

```text id="p9v5kr"
Input Formats

|

Parser

|

LORE Intermediate Representation

|

Multiple Outputs
```

Questions:

- Is this abstraction useful?
- What belongs in the intermediate representation?
- How should semantic loss be reported?

---

# 19. Cryptography Research

Questions:

- Which objects require signatures?
- Which relationships require verification?
- How are keys rotated?
- How are compromised authorities recovered?

---

# 20. Privacy Research

Questions:

- Who controls personal context?
- How is consent represented?
- How is sensitive context minimized?
- How are personal relationships protected?

---

# 21. Human Factors Research

Questions:

- Can humans understand LORE decisions?
- Does additional context improve trust?
- Does complexity overwhelm users?
- What explanations are actually useful?

---

# 22. Operational Technology Research

OT environments introduce additional constraints.

Questions:

- How does LORE interact with safety systems?
- How should availability requirements influence trust?
- How should physical consequences affect authorization context?

---

# 23. Research Methodology

Potential approaches:

- prototypes,
- adversarial testing,
- simulations,
- domain experiments,
- external review.

---

# 24. Things Not Yet Decided

LORE intentionally does not yet decide:

- final storage format,
- final protocol,
- final schema,
- final governance structure,
- final implementation language.

---

# 25. Review Questions

Reviewers should identify:

1. Which questions are actually important?
2. Which questions are distractions?
3. Which assumptions should be discarded?
4. Which research should happen first?
5. What experiments would provide the most information?

---

# 26. Research Principle

The governing principle:

> The purpose of research is not to defend the model. It is to discover whether the model deserves to exist.

---

LORE Volume 26 — Open Questions, Research Areas, and Future Exploration v0.2.md
