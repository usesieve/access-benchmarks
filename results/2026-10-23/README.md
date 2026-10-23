# Sieve access benchmark results

Published October 23, 2026. Retained successful observations remain successful; subsequent failed observations do not erase them.

## Access Success Rate

| Benchmark | Sieve CDP | Sieve Agent |
|---|---:|---:|
| Stealth V2 · 100 targets | **86.0% · 86/100** | **99.0% · 99/100** |
| Web Data Frontier · 82 targets | **86.6% · 71/82** | **97.6% · 80/82** |

## Download results

| Benchmark | Structured results | Per-target table |
|---|---|---|
| Stealth V2 | [JSON](sieve-stealth-v2.json) | [CSV](sieve-stealth-v2.csv) |
| Web Data Frontier | [JSON](sieve-string-frontier.json) | [CSV](sieve-string-frontier.csv) |

Each provider contains a target URL, success outcome and the retained original classification or observation flags. HTML byte counts and SHA-256 hashes are included when available. Prompts, credentials, raw tool logs, private session links and third-party HTML are not included. Missing timing or status evidence is not invented.

Known String attempt records retain their individual success, elapsed time and sanitized error category. Stealth CDP elapsed times include the observation hold; they are not a page-ready or time-to-first-byte latency comparison.

## Measurement

- **Stealth CDP:** 100 first-pass visits using the pinned upstream 20/60-second probe and judge, with native solver off. The gateway target preflight occurs before the navigation observation window. Original outcomes are **85 accessible, 1 login wall, 9 bot blocks, 4 capture/acquisition errors and 1 uncertain**. Login walls count as access here; strict `accessible` alone is **85/100**. No second pass is claimed.
- **Stealth Agent:** Access Success Rate based on reviewed website-content observations, including login boundaries. Evidence is retained across observations. It is a different measurement from the timed CDP probe and is not presented as a matched two-pass Agent score.
- **Web Data Frontier:** 82 reviewed targets, combining 68 standalone deep pages and the existing String deep-page stage on 14 shared domains. That shared stage followed a homepage visit; it is not a homepage-only result. Eighteen fixtures are excluded, including the retired MarketWatch PSKY URL that redirects to search. Its original observations remain in `excludedResults`, outside the current denominator; all other target outcomes are unchanged.
- **String scoring:** the original status-and-expected-text judgments remain in `strictUpstreamSuccess` / `strictEverPassed`. The access column keeps confirmed target content across runs, rejecting JavaScript shells, application-error pages and wrong-target redirects. Three prompt-adjusted follow-ups are tagged separately. Expected grading text was never sent to the Agent.
- Most new CDP/Agent rechecks served application build `1c7d70b`; the reported figures also include earlier dated observations. The files do not imply that every target was rerun on one build or date.

### Production Agent follow-ups

[Reviewed results](prod-agent-followups.json) on build `1.12.0 / 1e1874d` add confirmed content access for Neiman Marcus, Realtor and Best Buy. Best Buy's site redirected to a genuine AirPods Pro 2 page with a different visible SKU; this is product-family access, not identical frozen-offer verification. Ticketmaster and AXS still failed to deliver target content and also encountered native egress error4505. The separate Air Busan homepage follow-up failed and does not change this deep-page denominator or Stealth's score. Original observations and strict flags remain intact; these follow-ups do not claim the original controlled prompt or timed protocol.

## Other providers

[Public upstream result snapshots](../upstream/README.md) include all published provider outcomes from the pinned source revisions: String's three official JSON runs and Stealth V2's effective/original/retry classifications, summaries and audit data. Competitors were **not rerun**.

Their published per-attempt metrics and Sieve's retained-observation Access Success Rate are distinct. Use the per-target observations and measurement fields rather than treating this table as a fresh, uniform-protocol vendor ranking.

## Verify the publication

```sh
python3 validate.py
```

Run the validator from the repository root. It makes no service calls and does not load API keys. [Manifest](manifest.json) records SHA-256 hashes for the published Sieve files; upstream manifests identify the exact source commit, source URL, Git blob hash and SHA-256 for every mirrored file.
