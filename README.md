# Sieve access benchmarks

Access Success Rate for **Sieve CDP** and **Sieve Agent**, with per-target data and attributed public provider snapshots.

## Access Success Rate

| Benchmark | Sieve CDP | Sieve Agent |
|---|---:|---:|
| Stealth V2 · 100 targets | **86.0% · 86/100** | **99.0% · 99/100** |
| Web Data Frontier · 82 targets | **86.6% · 71/82** | **93.9% · 77/82** |

Sieve keeps confirmed access from completed observations; later failed observations do not erase an earlier success. Stealth CDP is a first-pass timed probe, while Agent results and the String figures combine retained access evidence. These measurement types are identified in the data rather than presented as one uniform-protocol vendor run.

## Results

The retired MarketWatch PSKY URL is excluded from the current Web Data Frontier cohort. Its original observations remain in `excludedResults`; other target outcomes and upstream snapshots are unchanged.

| Dataset | JSON | CSV |
|---|---|---|
| Sieve · Stealth V2 | [Download](results/2026-10-23/sieve-stealth-v2.json) | [View table](results/2026-10-23/sieve-stealth-v2.csv) |
| Sieve · Web Data Frontier | [Download](results/2026-10-23/sieve-string-frontier.json) | [View table](results/2026-10-23/sieve-string-frontier.csv) |

- [Measurement details and scoring](results/2026-10-23/README.md)
- [Other providers' published data and source manifests](results/upstream/README.md)
- [Sieve file hashes](results/2026-10-23/manifest.json)

The JSON includes each target URL, access outcome, original classifications or strict flags, and known attempt timings/errors. Available HTML byte counts and SHA-256 hashes are retained as evidence references. No prompts, credentials, private session links, raw tool logs, internal addresses or third-party page HTML/screenshots are published.

## Upstream benchmarks

- [String Web Data Frontier](https://github.com/usestring/web-data-frontier-benchmark), pinned at `15875fca8f4b3dfeacc7cecff9b260bb42382bfb`: all three official provider-result runs.
- [Browser Use Stealth Bench V2](https://github.com/browser-use/benchmark/tree/codex/stealth-bench-v2), pinned at `74b427184d84b0df391a9c337def5aadf115a893`: fourteen result/audit JSON and JSONL files, including the confirmation snapshot.

Other providers were not rerun. Their published attempt scores remain unchanged. Source URLs, Git blob hashes and SHA-256 hashes are recorded in the manifests. String's MIT license is retained; Stealth's unspecified upstream license status is documented without claiming a license for its code or task packages.

## Verify the files

```sh
python3 validate.py
```

Published October 23, 2026. This repository contains benchmark data and documentation, not Sieve application code.
