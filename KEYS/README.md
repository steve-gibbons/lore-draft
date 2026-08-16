# Author key (OpenPGP)

The LORE author-authority root, published here so reviewers can verify signed artifacts
without trusting a keyserver round-trip. **EXPERIMENTAL / provisional** - part of the
Track F forensic-signing *test harness*, explicitly intended to be replaced by robust key
management (hardware token / HSM, rotation, revocation, multi-party custody).

| | |
|---|---|
| **Key** | `steve-gibbons-D9B04B5C.asc` (in this directory) |
| **Owner** | Steve Gibbons `<steve_gibbons@icloud.com>` |
| **Short id** | `D9B04B5C` |
| **Primary fingerprint** | `7309 F037 A945 7C76 01C7  F3BF 0683 54FB D9B0 4B5C` |
| **Type** | ed25519 |
| **Also on** | MIT keyserver / `hkps://keyserver.ubuntu.com` |

## What this key is (and is not)
A fingerprint listed in `REGISTRIES/trusted-signers.txt` **is** the LORE author-authority
root (finding **KF-01**; **CORE-INVARIANT 11** - *authority has lineage*). Verifying a
signature against this key proves the signed bytes are what the author signed and that the
signer is the trusted root. It does **not** by itself prove the key is held by the
legitimate author - key-custody/binding is the deeper KF-01 track.

## Verify a signature (example)
```bash
gpg --import KEYS/steve-gibbons-D9B04B5C.asc
# then, for any LORE artifact shipped with a detached .asc signature:
gpg --verify <artifact>.asc <artifact>
# confirm the reported primary fingerprint equals the value in the table above.
```
Compare the fingerprint out-of-band; do not trust a fingerprint printed by the same
channel that delivered the key.

## Delegation (planned)
An **agent-signing subkey**, certified by the primary above, is under consideration so an
agent may sign lower-trust artifacts under a delegated key whose authority *lineage* traces
to the author's primary - without ever wielding the author root. When added, it appears in
the same exported key block and its policy is recorded in `REGISTRIES/trusted-signers.txt`.
