# Public provider result snapshots

These files preserve publicly published provider results, not new competitor runs. Numeric results are unchanged; manifests make the snapshots verifiable.

| Source | Revision | Included results |
|---|---|---|
| [String Web Data Frontier](https://github.com/usestring/web-data-frontier-benchmark) | `15875fca8f4b3dfeacc7cecff9b260bb42382bfb` | [July, August and September official JSON runs](string/manifest.json), including per-provider, per-target and per-attempt success, latency and error records |
| [Browser Use Stealth V2](https://github.com/browser-use/benchmark/tree/codex/stealth-bench-v2) | `74b427184d84b0df391a9c337def5aadf115a893` | [14 JSON/JSONL files](stealth-v2/manifest.json): effective, original and retry outcomes, summaries, provenance, sensitivity and release-audit data, including the confirmation snapshot |

Useful starting points:

- [String September run](string/benchmark-2026-09-16T01-03-47-074Z.json)
- [Stealth effective attempts](stealth-v2/attempts.jsonl)
- [Stealth summary](stealth-v2/summary.json)
- [Stealth confirmation summary](stealth-v2/confirmation-20260925/summary.json)

String is MIT-licensed; its original [LICENSE](string/LICENSE) is retained. No license file was present in the pinned Browser Use revision; its license status is recorded in the manifest, and no upstream software license is represented. Upstream implementation code, encrypted task packages, screenshot archives, third-party page HTML and README text are not mirrored here. Attribution and the original URLs remain in each manifest.
