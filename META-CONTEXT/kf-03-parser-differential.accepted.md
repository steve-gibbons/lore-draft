# KF-03 Residual - Parser Differential / Single-Point Enforcement

> **Status: accepted**  
> **Addresses:** KF-03  
> **Authority:** Accepted by author 2026-08-25.  
> **Date:** 2026-08-24 (drafted) / 2026-08-25 (accepted)

## Current posture (already implemented)
- `TOOLS/lore_common.load_simple_yaml` is the single source of truth for YAML loading across the validator and related tools.
- Prefer PyYAML (`yaml.safe_load`) when the package is present.
- Fall back to `TOOLS/lore_yaml` for the exact subset the corpus uses.
- Fail closed (`YamlSupportError`) on constructs outside that subset (anchors, aliases, merge keys, tags, multi-document streams). No silent degradation to wrong data.
- **Output path (`dump_yaml`) is pinned to `lore_yaml.dump` only** (AI-003 Option B, applied 2026-08-25). Output shape no longer depends on whether PyYAML is installed.
- Equality between PyYAML and lore_yaml over the repository YAML set is the property under test (`TESTS/test_yaml_parser.py` referenced in lore_common).

This already removes the original "hand-rolled parser returns empty strings and the caller dies elsewhere" failure mode, and the ambient-dependent output shape defect.

## Residual risk
1. When PyYAML is absent, the load TCB is still a single implementation (lore_yaml). A differential relative to a full YAML 1.2 processor remains possible for documents that stay inside the supported subset but are interpreted differently by a later consumer that uses a different parser.
2. The validator itself is still the sole enforcement point at rest (plus the pre-commit hook and CI gate when present).

## Recommended operator practice (defense-in-depth without changing the zero-dependency imperative)
- Prefer running the validator (and CI) in an environment that has PyYAML installed. The dual-path *load* design makes this a pure strengthening, not a requirement.
- Treat any document that triggers `YamlSupportError` as out-of-corpus until rewritten into the supported subset or accepted with an explicit author decision.
- Keep the fixture suite and the PyYAML equality tests green as the regression gate for parser behaviour.

## Disposition
- Residual treated as accepted risk for phase-1, monitored by the equality tests.
- Do not add a mandatory external dependency to the core validator; the author imperative of a dependency-free TCB stands.
- Revisit only if a concrete differential exploit is demonstrated against the supported subset.

## Provenance
Drafted 2026-08-24 as the fourth fast-follower item. Agent-generated under author direction. Accepted by author 2026-08-25. Output-path note updated the same day after AI-003 Option B landed.
