# Independent Production CDP repeat — October29

This is a new independent run, not a rewrite of [October28's complete200-attempt result](../2026-10-28/README.md). Production remained `1.13.0 / f003a5d` with its existing Decodo configuration. The supplier/runtime fingerprint was checked before admission and during execution; no change was observed. Native auto-egress tries the default desktop exit first and selects residential exits when needed: this is a whole-service result, not a forced-proxy comparison with IPRoyal.

| Metric | October29 result |
|---|---:|
| Original-judge accessible observations | **175/200 · 87.5%** |
| Round1 / Round2 | 87/100 / 88/100 |
| Targets accessible in both rounds | **84/100** |
| Alternative: include login walls | 177/200 · 88.5% |
| Alternative: both rounds, including login walls | 85/100 |

The chart uses strict accessible observations. The matrix passes a website only when both original judgments are accessible. The login-inclusive alternative is separate and makes no authenticated-content claim. The separate Agent99/100 cumulative result remains unchanged; it is not this timed CDP run.

## Files

- [Per-target JSON with both original outcomes](sieve-stealth-v2-cdp.json)
- [All200 attempts as CSV](sieve-stealth-v2-cdp.csv)
- [Publication hashes](manifest.json)
- [Previous complete run](../2026-10-28/README.md)
- [Earlier Agent and Frontier snapshot](../2026-10-23/README.md)
- [Attributed upstream snapshots](../upstream/README.md)

Classifications are175 accessible,20 bot blocks,two login walls and three unresolved acquisition/capture measurements. Congress.gov returned4505 in both scheduled rounds, consistent with the subsequently diagnosed provider restricted-target policy; no policy-evasion retries were performed. One final body-read timeout prevented a judgment. Two additional early-capture timeouts recovered by the final capture. Every scheduled attempt remains in the denominator.

## Protocol and verification

The fixed100-site dataset,1365×900 viewport,20-second navigation timeout,60-second observation,20/60-second captures and original access-v3 Luna judge are unchanged from [upstream commit74b4271](https://github.com/browser-use/benchmark/tree/74b427184d84b0df391a9c337def5aadf115a893/stealth_bench). The dataset SHA-256 is `6dee4f2eb9954c96445222b0fb8b7228689300f84001de4ba4ee9a952b0f3228`. Sieve acquisition/bearer authentication and target preflight occur outside observation; provisioning has a360-second bound. Native solving was not requested.

Ten client jobs ran concurrently from the start; observed established CDP peak was ten. Rounds did not overlap and no task was retried. All200 original result/judgment pairs and dataset/source hashes were reconciled. There were198 acquisitions,197 complete final screenshots and one incomplete final capture retained as unresolved. All198 observed browser sessions were gone after the run, and DynamoDB showed zero live desktop claims at the read-only end check. Physical-host occupancy peak was not instrumented.

A fixed five-target sample was visually checked in both rounds, with incomplete-capture/native-error cases and extra warning cases examined separately. The existing age-confirmation rubric boundary remains flagged without changing original judgments. Not every attempt is manually certified. Other providers were not rerun; dates, egress, browser versions and solver settings still differ. Agent workflows are a different protocol. This cohort does not establish representative web-wide or long-term reliability.

Only safe task-ID-level results and evidence hashes are public. No decrypted task package/URLs, prompts, private sessions, internal addresses, credentials, raw logs, screenshots or HTML are exported. Historical results and upstream files remain unchanged.
