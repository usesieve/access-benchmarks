import json
from pathlib import Path
import unittest
from validate import main

ROOT=Path(__file__).parent

class TwoRoundPublication(unittest.TestCase):
    def test_complete_original_metrics(self):
        data=json.loads((ROOT/'results/2026-10-28/sieve-stealth-v2-cdp.json').read_text())
        p=data['providers'][0]
        self.assertEqual((p['totalAttempts'],p['successfulAttempts'],p['successfulTargetsBothRuns']),(200,170,81))
        self.assertEqual((p['loginInclusiveSuccessfulAttempts'],p['loginInclusiveTargetsBothRuns']),(172,82))
        self.assertEqual(p['classifications'],{'accessible':170,'bot_block':24,'login_wall':2,'judge_or_capture_error':2,'uncertain':1,'network_error':1})
        self.assertFalse(data['audit']['allAttemptsHumanCertified'])
        self.assertFalse(data['audit']['rawJudgmentsEdited'])
        self.assertEqual(data['measurement']['clientConcurrency']['changedAfterRecordedAttempts'],51)

    def test_new_export_has_no_task_package_or_private_evidence(self):
        text=(ROOT/'results/2026-10-28/sieve-stealth-v2-cdp.json').read_text()
        for value in ['/Users/','/jobs/','Bearer ','session_id','172.31.','wss://','"url"','"instruction"','"prompt"']:
            self.assertNotIn(value,text)
        self.assertNotIn('OPENAI_API_KEY',text)

    def test_all_publication_hashes_and_outcomes(self):main()

if __name__=='__main__':unittest.main()
