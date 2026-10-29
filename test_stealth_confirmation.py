import json
from pathlib import Path
import unittest
from validate import main

ROOT=Path(__file__).parent
class IndependentRepeat(unittest.TestCase):
    def test_metrics_and_protocol(self):
        d=json.loads((ROOT/'results/2026-10-29/sieve-stealth-v2-cdp.json').read_text());p=d['providers'][0]
        self.assertEqual((p['successfulAttempts'],p['successfulTargetsBothRuns']),(175,84))
        self.assertEqual((p['loginInclusiveSuccessfulAttempts'],p['loginInclusiveTargetsBothRuns']),(177,85))
        self.assertEqual(d['measurement']['clientConcurrency']['initial'],10)
        self.assertEqual(d['audit']['finalScreenshotAttempts'],197)
        self.assertEqual(d['audit']['finalCaptureFailures'],1)
        self.assertTrue(d['audit']['dynamoDbLeaseReleaseReadBack'])
    def test_previous_run_not_rewritten(self):
        p=json.loads((ROOT/'results/2026-10-28/sieve-stealth-v2-cdp.json').read_text())['providers'][0]
        self.assertEqual((p['successfulAttempts'],p['successfulTargetsBothRuns']),(170,81))
    def test_no_private_payload(self):
        text=(ROOT/'results/2026-10-29/sieve-stealth-v2-cdp.json').read_text()
        for key in ['/Users/','/jobs/','Bearer ','session_id','172.31.','wss://','"url"','"instruction"','"prompt"']:self.assertNotIn(key,text)
    def test_all_manifests(self):main()
if __name__=='__main__':unittest.main()
