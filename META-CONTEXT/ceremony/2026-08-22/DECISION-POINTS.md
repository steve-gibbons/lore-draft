# Ceremony 2026-08-22 — decision points (key state)

**Status:** evidence / process log (not an accepted record)  
**Rule:** append a row at every branch cut, policy amend, accept/sign, or public SHA pin. Do not rewrite history; add a line.

## Key state (this ceremony)

| Role | Fingerprint | Notes |
|------|-------------|-------|
| Author primary (root lineage) | `7309F037A9457C7601C7F3BF068354FBD9B04B5C` | D9B04B5C; published in `KEYS/` |
| Active signing subkey | `69FADB148F4DCAC85FD59E183E5A2E38850E0C22` | 69FADB14; used for all 2026-08-22 `lore sign` |
| Public checkout | `~/Developer/lore-public` → `steve-gibbons/lore-draft` | |
| Private checkout | `~/Developer/lore` → `steve-gibbons/lore` | |

Unusable / missing-secret subkeys remain listed in `REGISTRIES/trusted-signers.txt`. They are not used here.

## Log

| When (UTC) | Point | Private SHA | Public SHA (`lore-draft`) | Signer | What |
|------------|-------|-------------|---------------------------|--------|------|
| 2026-08-22 | Gate A | (pre-package) | `dffb11c` | — | Author: promote recommended minimum |
| 2026-08-22 | Gate B OBS-001 | `1606891` | `dffb11c` | 69FADB14 | accept + detach-sign |
| 2026-08-22 | Gate B IBMBOB-001 | `f767bf4` | `dffb11c` | 69FADB14 | accept + detach-sign |
| 2026-08-22 | Gate B PROP-001 | `49c0907` | `dffb11c` | 69FADB14 | accept + detach-sign (`lore publish` spec; verb not implemented) |
| 2026-08-22 | Export order | `c722df4` | `dffb11c` | — | PRESERVE before leak-scan; skip-copy PRESERVE paths |
| 2026-08-22T17:31Z | Leak-scan amend | `2d944dc` | `dffb11c` | — | Drop public-identity patterns; keep path/URL/non-public mail |
| 2026-08-22T17:43Z | Whitelist Gate B | `43b7276` | `dffb11c` | — | OBS/IBMBOB/PROP accepted+.asc + DECISION-POINTS.md on whitelist |
| 2026-08-22T17:54Z | Public export | `43b7276` | `f2ab129` | — | lore-draft overlay; leak-scan CLEAN; manifest rebuilt on published tree |
| 2026-08-22T18:16Z | TR-002 accepted | `49082f1` | `f2ab129` | 69FADB14 | signed TR-PUBLIC-EXPORT-002.accepted.yaml |
| 2026-08-22T18:31Z | Whitelist TR-002 | `c5f1279` | `e54e567` | — | accepted TR yaml+.asc on whitelist for public overlay |
| 2026-08-22T18:34Z | Public TR overlay | `c5f1279` | `8467838` | — | TR-002 accepted+.asc + whitelist yaml on lore-draft |
| 2026-08-22T18:45Z | CI always() | `649c266` | `8467838` | — | signature convention + LL-004 no longer muted |
| 2026-08-22T18:46Z | Public gitignore | `649c266` | `cf2869a` | — | Developer path note + extensionless iCloud hole |
| 2026-08-22T18:49Z | Public KEYS | `649c266` | `bd787d0` | — | current bundle + 69FADB14; D9B04B5C.asc alias |
| 2026-08-22T18:52Z | Gate D nits | `9931b91` | `bd787d0` | — | private KEYS alias, README, MMETA typo, runbook executed banner |
| 2026-08-22T19:05Z | lore publish | `f628244` | `8847d5f` | — | compose export+manifest+validate; no commit/push/TR-promote |
| 2026-08-22T19:16Z | Public publish overlay | `f628244` | `23d4d59` | — | lore publish live; leak-scan CLEAN; validate 48/0 |
| 2026-08-22T19:23Z | Tree-local verbs + TR next | `a23bcec` | `23d4d59` | — | dispatcher/CI skip missing tools; next export is TR-003 (002 accepted stays) |
| 2026-08-22T19:39Z | Public overlay | `a23bcec` | `ac9741d` | — | tree-local dispatcher+CI; TR-003.draft; TR-002 still accepted |
| 2026-08-22T20:00Z | TR-003 accepted | `5e835a6` | `ac9741d` | 69FADB14 | signed TR-003 |
| 2026-08-22T20:01Z | TR template verbs | `17be150` | `ac9741d` | -- | generator verbs |
| 2026-08-22T20:04Z | Whitelist TR-003 | `6ecd264` | `ac9741d` | -- | TR-003 yaml+asc |
| 2026-08-22T20:22Z | Public export | `5ac867a` | `e381186` | -- | lore publish; TR-003 on lore-draft |
| 2026-08-22T20:29Z | TR-004 receipt | `54896f4` | `e381186` | 69FADB14 | accept TR-004 private only; no re-export |
| 2026-08-22T21:10Z | QA CI hole | `54896f4` | `e381186` | — | lore_yaml absent on public; local PyYAML hid it |
| 2026-08-22T21:30Z | Whitelist TCB | `4960a21` | `e381186` | — | TOOLS/lore_yaml.py + OBS-EXPORT-TCB-CLOSURE candidate; AI-003 stays open |

| 2026-08-22T22:43Z | Public export | `4960a21` | `6584959` | — | lore_yaml TCB; CI green run 32603261039 |

| 2026-08-22T22:47Z | Pin public SHA | `cccae6a` | `6584959` | — | pin lore_yaml public SHA 6584959 (CI green) |
| 2026-08-22T22:52Z | TR-005 receipt | `ae1d547` | `6584959` | 69FADB14 | accept TR-PUBLIC-EXPORT-005; receipt for 6584959; not re-exported |
| 2026-08-22T22:59Z | OBS TCB accept | `788619b` | `6584959` | 69FADB14 | accept + detach-sign OBS-EXPORT-TCB-CLOSURE-001 (private-only) |
| 2026-08-22T23:02Z | Close AI-003 | `84a2454` | `6584959` | — | close AI-003; lore_yaml on public TCB at 6584959 |
| 2026-08-22T23:05Z | Drop parenthetical | `a164b4f` | `6584959` | — | drop stale AI-003 parenthetical |
| 2026-08-22T23:31Z | Whitelist OBS | `457ef48` | `6584959` | — | OBS-EXPORT-TCB-CLOSURE accepted.md+.asc on whitelist |
| 2026-08-22T23:49Z | Public export | `1b4d5dc` | `26fd6d0` | — | OBS-EXPORT-TCB-CLOSURE accepted+.asc on lore-draft |
| 2026-08-22T23:52Z | Pin public SHA | `1eae0a5` | `26fd6d0` | — | pin 26fd6d0; CI green run 32606248246 |
| 2026-08-23T00:10Z | TR-006 accepted | `b326be6` | `26fd6d0` | 69FADB14 | author Steve Gibbons: sidecar .asc like TR-005; Check 2 pre-sign not blocking if TR-005 matches; git rm tracked draft |
| 2026-08-23T00:30Z | Public export | `93168c7` | `854c734` | — | TR-006 accepted+.asc on lore-draft |
| 2026-08-23T00:33Z | Pin public SHA | `3e4b497` | `854c734` | — | pin 854c734; CI green run 32608028357 |
| 2026-08-23T00:42Z | TR-007 accepted | `05159ae` | `854c734` | 69FADB14 | author Steve Gibbons: private-only receipt for 854c734; not re-exported (TR-005 pattern); skip DP-only overlay |
| 2026-08-23T01:04Z | Freeze v0.6.0 | `011d874` | `854c734` | 69FADB14 | signed tags v0.6.0 both trees; do not publish |
| 2026-08-23T03:21Z | OBS Check 2 sidecar | `309f736` | `854c734` | — | OBS-CHECK2-TR-SIDECAR candidate; TRs lack provenance.signature; out of v0.6.0 |
| 2026-08-23T03:28Z | TR-007 Check 2 | `c83d008` | `854c734` | 69FADB14 | backfill provenance.signature+signer_fpr; re-sign; lore check PASS |
| 2026-08-23T03:39Z | TR-005 Check 2 | `dba9709` | `6584959` | 69FADB14 | backfill provenance.signature+signer_fpr; re-sign; lore check PASS |
| 2026-08-23T03:50Z | OBS Check 2 accept | `130a798` | `854c734` | 69FADB14 | accept+sign OBS-CHECK2-TR-SIDECAR; private-only; no publish |
| 2026-08-23T03:58Z | TR-006 Check 2 | `94e4631` | `854c734` | 69FADB14 | backfill provenance.signature+signer_fpr; re-sign; lore check PASS; overlay next |
## Next line (template)

```
| YYYY-MM-DDTHH:MMZ | <point> | <private SHA> | <public SHA or —> | 69FADB14 or — | <one line> |
```
