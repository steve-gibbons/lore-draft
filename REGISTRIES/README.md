# REGISTRIES

Contains closed enums and transition rules for governance and artifact lifecycle states.

- `artifact-statuses.yaml`: Definitive status registry detailing `agent_writable` and `author_only` enums, plus allowed transitions.
- `trusted-signers.txt`: The author-authority root list (OpenPGP signing-key fingerprints + role + label) for KF-01 / CORE-INVARIANT 11. Trust binds to the signing-key fingerprint (role), and every accepted signature must chain to a `root` key (lineage). **EXPERIMENTAL test harness** — to be replaced by robust key management (HSM/hardware token, rotation, revocation, multi-party custody).
