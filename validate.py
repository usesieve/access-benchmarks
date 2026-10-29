"""Validate published counts and byte-identical result manifests, without network access."""
import csv
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def main():
    for path in ROOT.glob('results/**/manifest.json'):
        manifest=json.loads(path.read_text())
        for item in manifest.get('files',manifest.get('sieveFiles',[])):
            body=(path.parent/item['path']).read_bytes()
            assert len(body)==item['bytes'],item['path']
            assert hashlib.sha256(body).hexdigest()==item['sha256'],item['path']
            if 'gitBlobSha' in item:
                assert hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest()==item['gitBlobSha']
    for path in ROOT.glob('results/2026-10-23/sieve-*.json'):
        data=json.loads(path.read_text())
        for provider in data['providers']:
            rows=provider['results']
            assert len(rows)==provider['totalTargets']
            assert sum(row['success'] for row in rows)==provider['successfulTargets']
            assert abs(provider['overallSuccessRate']-provider['successfulTargets']/len(rows))<1e-10
        with path.with_suffix('.csv').open() as file:
            assert len(list(csv.DictReader(file)))==sum(p['totalTargets'] for p in data['providers'])
    for path in ROOT.glob('results/*/sieve-stealth-v2-cdp.json'):
        data=json.loads(path.read_text())
        assert data['schemaVersion']==2
        for provider in data['providers']:
            targets=provider['results'];attempts=[a for target in targets for a in target['attempts']]
            assert len(targets)==len({r['testId'] for r in targets})==provider['totalTargets']==100
            assert len(attempts)==provider['totalAttempts']==200
            assert sum(a['strictUpstreamSuccess'] for a in attempts)==provider['successfulAttempts']
            assert provider['overallSuccessRate']==provider['successfulAttempts']/200
            assert sum(a['loginInclusiveSuccess'] for a in attempts)==provider['loginInclusiveSuccessfulAttempts']
            assert provider['loginInclusiveSuccessRate']==provider['loginInclusiveSuccessfulAttempts']/200
            for row in targets:
                assert [a['repetition'] for a in row['attempts']]==[1,2]
                assert row['success']==all(a['originalClassification']=='accessible' for a in row['attempts'])
                assert row['loginInclusiveSuccess']==all(a['originalClassification'] in {'accessible','login_wall'} for a in row['attempts'])
                for a in row['attempts']:
                    assert a['strictUpstreamSuccess']==(a['originalClassification']=='accessible')
                    assert a['loginInclusiveSuccess']==(a['originalClassification'] in {'accessible','login_wall'})
            assert sum(r['success'] for r in targets)==provider['successfulTargetsBothRuns']
            assert sum(r['loginInclusiveSuccess'] for r in targets)==provider['loginInclusiveTargetsBothRuns']
            with path.with_suffix('.csv').open() as file:
                flat=list(csv.DictReader(file));assert len(flat)==200
                assert len({(a['testId'],a['repetition']) for a in flat})==200
                original={(r['testId'],str(a['repetition'])):a for r in targets for a in r['attempts']}
                assert all(a['originalClassification']==original[a['testId'],a['repetition']]['originalClassification'] for a in flat)
    print('All provider totals, CSV row counts and source-file hashes verified.')


if __name__=='__main__':main()
