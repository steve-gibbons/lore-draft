# OBS / Accepted — Public-export TCB closure (lore_yaml)

**Status:** accepted  
**Date:** 2026-08-22  
**OBS ID:** OBS-EXPORT-TCB-CLOSURE-001  
**Authority:** agent-drafted; author gate required for any promotion or public commit

## Summary

If a public-exported tool imports another module as its no-PyYAML fallback, that
module is part of the published TCB and must be on the export whitelist. Shipping
`TOOLS/lore_common.py` without `TOOLS/lore_yaml.py` recreates AI-003 at the
private-to-public boundary: the author's machine (PyYAML installed) is green;
CI on a bare runner is red.

Do not install PyYAML in CI. That would hide the defect again.

Do not publish `TESTS/test_yaml_parser.py` on the public tree. Its oracle *is*
PyYAML; that test belongs on the private side.

## Evidence (this instance)

| What | Value |
|------|-------|
| Public SHA | `e381186` (lore-draft) |
| Private SHA at QA | `54896f4` |
| CI | [run 32596478452](https://github.com/steve-gibbons/lore-draft/actions/runs/32596478452) |
| Failure | `ModuleNotFoundError: No module named 'lore_yaml'` in `lore_build_manifest.py --check` |
| Local | `python3 TOOLS/lore_build_manifest.py --check` EXIT 0 on `~/Developer/lore-public` because PyYAML is installed |
| Author-sig | PASS (always()); does not prove the parser TCB |

Same class as OBS-EXPORT-PLACEHOLDERS-AND-LEAKSCAN-SELFREF: the tree you tested
is not the tree you published.

## Normative implication (on acceptance)

- `TOOLS/lore_yaml.py` is on POLICY-EXPORT-WHITELIST-001 (landed with this candidate).
- Public CI must stay PyYAML-free.
- AI-003 stays **open** until lore-draft CI is green on a bare runner after this file ships.
- Closing AI-003 is a later author act, not this OBS.

## Suggested next author actions

1. Review this note. Edit if desired.
2. Land the whitelist amend on private main (this branch).
3. `lore publish` live; overlay lore-draft; push.
4. Confirm CI green on the new public SHA without PyYAML.
5. Then, and only then, promote this OBS and consider closing AI-003.

## Provenance

- Parent: ACTION_ITEMS/open/AI-003-tools-silently-require-pyyaml.md
- QA: 2026-08-22 author spot-check of lore-draft @ e381186
- Agent: draft only; no status promotion, no push to lore-draft, no claim of canonicity.

## Close evidence (author, 2026-08-22)

Date accepted: 2026-08-22
Public SHA: 6584959
CI: https://github.com/steve-gibbons/lore-draft/actions/runs/32603261039 SUCCESS
Private at publish: 4960a21
Pin: cccae6a
TR-005: ae1d547 (receipt; not re-exported)

AI-003 close-condition is met. Closing AI-003 remains a later author act.
