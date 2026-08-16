# Decision Record - LORE Authenticated Author Identity (DECIDED)

> **Status: accepted** (author-ratified 2026-08-15; agent-drafted under author direction). Owner:
> **Author (Steve Gibbons)**, sole authority. EXPERIMENTAL / provisional.
> **Decision (2026-08-15):** adopt **Option C (layered)** - content signatures as the source of
> truth for author-only status, signed commits as CI defense-in-depth, and an agent-signing subkey
> for delegation. Build sequence and remaining implementation choices below.
>
> **Addresses:** KF-01 (declarative, not authenticated) - the highest-conviction finding, root of
> KF-02/KF-06 and part of KF-07/KF-14.  **Relates to:** CORE-INVARIANTS 10 ("represent, then
> enforce") & 11 ("authority has lineage"); KF-06 (shares the signing substrate); KF-02 (CI as an
> enforcement point); the agent-signing-subkey plan in `KEYS/README.md`.

## The gap (stated plainly)
"Author-only" status is gated by **a field the writer sets themselves**: `TOOLS/lore_validate.py`
Check 2 admits an author-only status iff `provenance.author_preseeded == true`. Author identity is
otherwise just an unauthenticated git `user.email`. So the root of authority is *self-asserted*:
any writer - or adversarial INTAKE that carries `author_preseeded: true` - can mint author
authority. LORE records authority claims without binding them to anything unforgeable.

This is exactly what CORE-INVARIANT 10 forbids: a *named* distinction (author-only) that is
asserted, not represented-then-enforced. Authenticating this core is LORE's primary hardening path.

## Threat model (what the fix must defend against)
- **T1 Authority forgery** *(primary)* - a non-author writer emits an author-only status by writing
  `author_preseeded: true`.
- **T2 Identity spoofing** - git `user.email` set to the author's address.
- **T3 Adversarial INTAKE** - untrusted intake content carrying the preseed flag is promoted.
- **T4 Post-approval tampering** - content changed after the author blessed it *(overlaps KF-06;
  largely handled by the signed manifest)*.
- **T5 Key custody / binding** - proving the trusted key is actually held by the legitimate human.
  **Out of scope here** (the "deeper KF-01 track" per `KEYS/README.md`); this decision authenticates
  *signatures to a root*, not the root's custody. Tracked to hardware-token/HSM, rotation,
  revocation, multi-party custody.
- **T6 Agent over-reach** - an agent wielding the author root instead of a delegated lower-trust key.

## Existing substrate (what we already have)
- **Published author key** - `KEYS/steve-gibbons-D9B04B5C.asc` (ed25519, fp `…D9B04B5C`).
- **Content-signature verifier** - `lore_verify_manifest_sig.py`, but **private-repo only**; not yet
  in the public `TOOLS/` and not wired into the author-only gate.
- **Referenced-but-missing root list** - `KEYS/README.md` and CORE-INVARIANT 11 both cite
  `REGISTRIES/trusted-signers.txt` as the author-authority root, **but that file does not exist**.
  Creating it is step 1 - "represent" the root before enforcing against it.
- **Planned delegation** - an agent-signing subkey certified by the primary (KEYS/README), so agents
  sign lower-trust artifacts under a key whose *lineage* traces to the author (invariant 11).

## Options considered
| Option | How authority is bound | Verifiable at rest? | Survives outside git? | New machinery | Fit |
|---|---|---|---|---|---|
| **A - Signed commits** | author-only writes must arrive in a git commit signed by a trusted-signer fingerprint; CI verifies | No (needs git history) | No | Low (reuse git + CI) | Cheapest bridge; but authority lives in the transport, and the working-tree validator can't check it |
| **B - Content signatures** | each author-only artifact carries a detached `.asc` over its canonical bytes; Check 2 verifies signature vs trusted-signers instead of reading a boolean | Yes | Yes | Medium (canonicalization + signing workflow) | Transport-independent; reuses the private verifier; aligns with the KF-06 manifest |
| **C - Layered (B + A + delegation)** ✅ | content signature is the source of truth; signed commits add transport defense-in-depth; agent-signing subkey for lower-trust artifacts | Yes | Yes | Highest | Matches invariants 10 & 11 end-to-end; each layer independently useful |

## Decided direction (author-ratified 2026-08-15) - Option C, layered
Content signatures (B) are the load-bearing fix for T1-T3; signed commits and delegation are
hardening layers that ship after. Each layer is independently useful, so the build is sequenced,
not all-or-nothing.

## Build tasks (on ratification)
1. **Represent the root.** Create `REGISTRIES/trusted-signers.txt` (the file `KEYS/README.md` and
   invariant 11 already cite): trusted fingerprint(s) + policy. *Resolves the dangling reference.*
2. **Enforce at rest.** Promote `lore_verify_manifest_sig.py` into public `TOOLS/`; change Check 2
   so an author-only status requires a valid detached signature over the artifact's canonical bytes
   from a trusted-signers fingerprint - not a boolean. *(Closes T1-T3.)*
3. **Defense-in-depth in transit.** Verify signed commits in CI (folds into KF-02's CI enablement).
   *(Hardens T2.)*
4. **Delegation / lineage.** Add the agent-signing subkey certified by the primary, so agents never
   wield the author root; record its policy in `REGISTRIES/trusted-signers.txt`. *(Closes T6;
   invariant 11.)*

## Resolved implementation choices
1. **Mechanism: ratified - Option C (layered).**
2. **Migration of existing author-only artifacts** *(recommended default; confirm at build):* require
   signatures for **new** author-only emissions immediately; **batch re-sign** the existing
   author-only artifacts as a bounded follow-up before v1.0.0, rather than blocking step 2 on a full
   re-sign.
3. **`author_preseeded` field** *(recommended default; confirm at build):* **retain it as a claim
   that a signature must corroborate** during migration (belt-and-suspenders), then **remove** it
   once all author-only artifacts are signature-gated.

## Provenance
Derived from KF-01 (`KNOWN-FINDINGS.md`), CORE-INVARIANTS 10 & 11, the TCB section naming the
author's identity as the root of authority, and the existing key/verifier/delegation substrate
(`KEYS/`, private `lore_verify_manifest_sig.py`). Mechanism ratified by the author (Option C,
2026-08-15); migration and field-handling carry recommended defaults to confirm at build. The
author is the sole authority.
