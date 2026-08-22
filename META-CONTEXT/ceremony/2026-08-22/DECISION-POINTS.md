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
| 2026-08-22T18:52Z | Gate D nits | *(this commit)* | `bd787d0` | — | private KEYS alias, README, MMETA typo, runbook executed banner |

## Next line (template)

```
| YYYY-MM-DDTHH:MMZ | <point> | <private SHA> | <public SHA or —> | 69FADB14 or — | <one line> |
```
