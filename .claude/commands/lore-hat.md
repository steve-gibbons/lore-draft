---
description: Adopt a LORE evaluator/maintainer hat (EXPERIMENTAL, provisional)
argument-hint: <lens-id> [--profile evaluator|maintainer]
allowed-tools: Bash(python3 TOOLS/lore_prompt.py:*)
---

EXPERIMENTAL / provisional — for evaluation of the LORE corpus itself and demonstration
of principles only. Not production-ready.

Assemble the requested LORE hat, then adopt the printed prompt as your operating
instructions for the rest of this session, and state clearly which hat is now active
(profile + lens). Honor the named-lens rule: a named lens is "grounded in the public work
of" that person — never their actual opinion or endorsement.

If no lens id is provided in the arguments below, instead run
`python3 TOOLS/lore_prompt.py --list` and show the available profiles and lenses.

Arguments: $ARGUMENTS

Assembled hat:

!`python3 TOOLS/lore_prompt.py $ARGUMENTS`
