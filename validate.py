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
    print('All provider totals, CSV row counts and source-file hashes verified.')


if __name__=='__main__':main()
