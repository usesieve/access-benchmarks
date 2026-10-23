"""Exclude one retired fixture from the current cohort; preserve every result."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / 'results/2026-10-23'
NAME = 'marketwatch'
URL = 'https://www.marketwatch.com/investing/stock/psky'
REASON = 'Retired PSKY quote URL redirects to search rather than the frozen stock page.'
SOURCE = 'https://www.sec.gov/Archives/edgar/data/2041610/000110465926113913/tm2626659d7_8k.htm'


def project(data):
    # This edits only cohort membership, never success or strict classifications.
    import copy
    data = copy.deepcopy(data)
    for provider in data['providers']:
        removed = [r for r in provider['results'] if r['testName'] == NAME]
        if any(r['url'] != URL for r in removed):
            raise ValueError('Only the exact retired PSKY fixture is excluded')
        archive = provider.setdefault('excludedResults', [])
        if removed:
            archive.extend(r for r in removed if r not in archive)
        elif not any(r['testName'] == NAME and r['url'] == URL for r in archive):
            raise ValueError('Missing original fixture and exclusion evidence')
        provider['results'] = [r for r in provider['results'] if r['testName'] != NAME]
        provider['totalTargets'] = len(provider['results'])
        provider['successfulTargets'] = sum(r['success'] for r in provider['results'])
        provider['overallSuccessRate'] = provider['successfulTargets'] / provider['totalTargets']
    measurement = data['measurement']
    measurement.setdefault('originalScoredTargets', 83)
    measurement['scoredTargets'] = 82
    measurement['excludedTargets'] = 18
    measurement['cohortExclusions'] = [{'testName': NAME, 'url': URL, 'reason': REASON, 'source': SOURCE}]
    measurement['promptAdjustedFollowupsIncluded'] = [
        name for name in measurement['promptAdjustedFollowupsIncluded'] if name != NAME]
    assert all(p['totalTargets'] == 82 for p in data['providers'])
    return data


def main():
    target = RESULTS / 'sieve-string-frontier.json'
    data = project(json.loads(target.read_text()))
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    csv_path = target.with_suffix('.csv')
    with csv_path.open(newline='') as stream:
        reader = csv.DictReader(stream)
        fields, rows = reader.fieldnames, list(reader)
    assert all(row['url'] == URL for row in rows if row['test'] == NAME)
    rows = [row for row in rows if row['test'] != NAME]
    assert len(rows) == sum(p['totalTargets'] for p in data['providers'])
    with csv_path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    manifest_path = RESULTS / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    for item in manifest['sieveFiles']:
        body = (RESULTS / item['path']).read_bytes()
        item.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({p['provider']: {'success': p['successfulTargets'], 'total': p['totalTargets']}
                      for p in data['providers']}))


if __name__ == '__main__':
    main()
