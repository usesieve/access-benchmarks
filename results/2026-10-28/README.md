# Stealth V2: complete Production CDP rerun

Measured October 28, 2026; published October 29, 2026. Sieve Production `1.13.0 / f003a5d`, normal authenticated CDP, 100 frozen targets, two fresh non-overlapping rounds. No website retries were used.

| Metric | Result |
|---|---:|
| Original-judge accessible observations | **170/200 · 85%** |
| Round 1 / Round 2 | 84/100 / 86/100 |
| Targets accessible in both rounds | **81/100** |
| Alternative: include login walls | 172/200 · 86% |
| Alternative: both rounds, including login walls | 82/100 |

The chart uses the original strict attempt metric. The binary website matrix passes a target only when **both** repetitions are accessible. Login-inclusive figures are separate and do not claim authenticated content.

## Data

- [Per-target JSON with both original attempt outcomes](sieve-stealth-v2-cdp.json)
- [All 200 attempts as CSV](sieve-stealth-v2-cdp.csv)
- [Publication file hashes](manifest.json)
- [Previous Sieve snapshot, preserved unchanged](../2026-10-23/README.md)
- [Attributed upstream provider snapshots](../upstream/README.md)

Original classifications: 170 accessible, 24 bot blocks, two login walls, two acquisition/judge errors, one uncertain page, and one rendered network-error page. All 200 scheduled observations remain in the denominator. The two acquisition failures returned gateway code4505; that code alone does not establish the exact provider/country root cause. Two first snapshots timed out, but their final captures succeeded and the original judgments are retained.

## Reproduction scope

The frozen dataset SHA-256 is `6dee4f2eb9954c96445222b0fb8b7228689300f84001de4ba4ee9a952b0f3228`, from [Browser Use benchmark commit74b4271](https://github.com/browser-use/benchmark/tree/74b427184d84b0df391a9c337def5aadf115a893/stealth_bench). Dataset membership, viewport1365×900, navigation timeout20seconds, observation60seconds, snapshots20/60seconds and the original access-v3 Luna judge are unchanged. Sieve-specific acquisition and bearer authentication are outside the observation window, with up to360seconds allowed for provisioning/cold start. Native solving was not requested.

Client concurrency changed from five to ten after51 completed observations; existing attempts drained and were not rerun. The observed public CDP session peak was ten. All198 observed established browser sessions were confirmed gone after completion. Physical desktop occupancy and DynamoDB lease release were not independently read back because the existing read-only AWS login had expired.

This CDP run now has the same frozen task set, observation protocol, judge and two-repeat coverage as the attributed provider runs. Providers were **not** rerun: dates, browser versions, egress and native solver settings still differ. It is not a matched-IP experiment or a representative web-wide success estimate. Sieve Agent's separate99/100 cumulative result is unchanged and is not this timed two-run protocol.

## Audit and privacy

Every exported outcome was reconciled with the retained original result and judgment, and all198 acquired attempts had final screenshots. A fixed five-target visual sample covered both rounds; missing-measurement cases and additional warning cases were checked separately. One sampled site's genuine age-confirmation screen is a usable-content rubric boundary; its original accessible judgments remain unchanged. This is not manual certification of every attempt.

The export contains task IDs and safe outcome metadata only—not decrypted task instructions/URLs, credentials, private session links, raw logs, internal addresses, screenshots or third-party HTML. Screenshot SHA-256 references identify private evidence without publishing its contents.
