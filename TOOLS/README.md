# TOOLS

Validation scripts and git hooks for LORE Corpus Workbench.

- `lore_validate.py`: Standalone CLI validator enforcing the 10 core governance and structural checks.
- `hooks/pre-commit-hash-check.sh`: Git pre-commit hook enforcing `INTAKE/raw/` immutability and running validation checks.
