# Sieve access benchmarks

Access Success Rate for **Sieve CDP** and **Sieve Agent**, with per-target data and attributed public provider snapshots.

## Access Success Rate

| Benchmark | Sieve CDP | Sieve Agent |
|---|---:|---:|
| Stealth V2 · 100 targets | **87.5% · 175/200 observations** | **99.0% · 99/100 targets** |
| Web Data Frontier · 82 targets | **86.6% · 71/82** | **97.6% · 80/82** |

Stealth CDP now reports the independent October29 two-round Production repeat using the original strict judge:175 accessible observations out of200. Its binary matrix requires both runs to pass (84/100). The login-inclusive alternative is88.5% (177/200), or85/100 targets passing both runs. October28's85% result remains preserved. Agent results and Web Data Frontier retain their existing measurements and are not relabeled as fresh timed two-run results. Production used automatic default/residential exit selection, not forced Decodo for every navigation or a controlled IPRoyal comparison.

## Results

The retired MarketWatch PSKY URL is excluded from the current Web Data Frontier cohort. Its original observations remain in `excludedResults`; other target outcomes and upstream snapshots are unchanged.

| Dataset | JSON | CSV |
|---|---|---|
| Sieve CDP · Stealth V2 · October29 independent repeat | [Download](results/2026-10-29/sieve-stealth-v2-cdp.json) | [View attempts](results/2026-10-29/sieve-stealth-v2-cdp.csv) |
| Sieve CDP · Stealth V2 · October28 complete run | [Download](results/2026-10-28/sieve-stealth-v2-cdp.json) | [View attempts](results/2026-10-28/sieve-stealth-v2-cdp.csv) |
| Sieve · Stealth V2 · previous snapshot / Agent | [Download](results/2026-10-23/sieve-stealth-v2.json) | [View table](results/2026-10-23/sieve-stealth-v2.csv) |
| Sieve · Web Data Frontier | [Download](results/2026-10-23/sieve-string-frontier.json) | [View table](results/2026-10-23/sieve-string-frontier.csv) |

- [Latest two-round CDP measurement and scoring](results/2026-10-29/README.md)
- [Previous snapshot and Agent/Frontier measurement details](results/2026-10-23/README.md)
- [Other providers' published data and source manifests](results/upstream/README.md)
- [Sieve file hashes](results/2026-10-23/manifest.json)
- [Reviewed production Agent follow-ups](results/2026-10-23/prod-agent-followups.json)

The files include per-target outcomes, original classifications or strict flags, and known timings/errors. Historical snapshots include target URLs; the new CDP export uses frozen task IDs only. Available byte counts and SHA-256 hashes are retained as evidence references. No prompts, credentials, private session links, raw tool logs, internal addresses or third-party page HTML/screenshots are published.

## Upstream benchmarks

- [String Web Data Frontier](https://github.com/usestring/web-data-frontier-benchmark), pinned at `15875fca8f4b3dfeacc7cecff9b260bb42382bfb`: all three official provider-result runs.
- [Browser Use Stealth Bench V2](https://github.com/browser-use/benchmark/tree/codex/stealth-bench-v2), pinned at `74b427184d84b0df391a9c337def5aadf115a893`: fourteen result/audit JSON and JSONL files, including the confirmation snapshot.

Other providers were not rerun. Their published attempt scores remain unchanged. The new CDP run uses the same frozen dataset,60-second observation and original judge with complete two-repeat coverage; provider dates, egress, browser versions and solver configurations still differ. Source URLs, Git blob hashes and SHA-256 hashes are recorded in the manifests. String's MIT license is retained; Stealth's unspecified upstream license status is documented without claiming a license for its code or task packages.

## Verify the files

```sh
python3 validate.py
```

Originally published October 23, 2026; complete CDP rerun published October 29, 2026. This repository contains benchmark data and documentation, not Sieve application code.
