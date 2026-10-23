"""Append reviewed observations, preserving every original judgment."""
import csv
from copy import deepcopy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT/'results/2026-10-23'

def project(original, followups):
    data = deepcopy(original)
    agent = next(p for p in data['providers'] if p['provider'] == 'sieve-agent')
    for case in followups['cases']:
        if case['testName'] == 'Air Busan':
            continue
        row = next(r for r in agent['results'] if r['testName'] == case['testName'])
        assert row['url'] == case['url']
        source = followups['sourceId'] + '/' + case['testName']
        if any(o['sourceId'] == source for o in row['observations']):
            continue
        observation = dict(case, sourceId=source, strictUpstreamSuccess=None,
            promptAdjusted=True, precededByHomepage=False, observedOn=followups['observedOn'],
            applicationBuild=followups['applicationBuild'], protocol=followups['protocol'])
        row['observations'].append(observation)
        row['observationCount'] = len(row['observations'])
        row['success'] = any(o['success'] for o in row['observations'])
        if case['success']:
            row['htmlBytes'], row['htmlSha256'] = case['htmlBytes'], case['htmlSha256']
    agent['successfulTargets'] = sum(r['success'] for r in agent['results'])
    agent['overallSuccessRate'] = agent['successfulTargets']/agent['totalTargets']
    data['measurement']['reviewedProdFollowups'] = 'prod-agent-followups.json'
    return data

def main():
    followups = json.loads((RESULTS/'prod-agent-followups.json').read_text())
    path = RESULTS/'sieve-string-frontier.json'
    data = project(json.loads(path.read_text()), followups)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
    with path.with_suffix('.csv').open(newline='') as f:
        reader = csv.DictReader(f)
        fields, rows = reader.fieldnames, list(reader)
    agent = next(p for p in data['providers'] if p['provider'] == 'sieve-agent')
    lookup = {r['testName']: r for r in agent['results']}
    for row in rows:
        if row['provider'] != 'sieve-agent':
            continue
        value = lookup[row['test']]
        row.update(success=str(value['success']), htmlBytes=value.get('htmlBytes') or '',
                   htmlSha256=value.get('htmlSha256') or '')
    with path.with_suffix('.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    path = RESULTS/'manifest.json'
    manifest = json.loads(path.read_text())
    if not any(x['path']=='prod-agent-followups.json' for x in manifest['sieveFiles']):
        manifest['sieveFiles'].append({'path':'prod-agent-followups.json'})
    for item in manifest['sieveFiles']:
        body = (RESULTS/item['path']).read_bytes()
        item.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    path.write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'agent':agent['successfulTargets'], 'total':agent['totalTargets']}))

if __name__ == '__main__':
    main()
