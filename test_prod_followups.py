import json
import unittest
from copy import deepcopy
from apply_prod_followups import RESULTS, project

class FollowupTests(unittest.TestCase):
    def test_idempotence_and_original_observations(self):
        data=json.loads((RESULTS/'sieve-string-frontier.json').read_text())
        followups=json.loads((RESULTS/'prod-agent-followups.json').read_text())
        self.assertEqual(project(data,followups),data)
        baseline=deepcopy(data)
        agent=baseline['providers'][1]
        self.assertEqual(agent['provider'],'sieve-agent')
        for r in agent['results']:
            r['observations']=[o for o in r['observations'] if not o['sourceId'].startswith(followups['sourceId']+'/')]
            r['success']=any(o['success'] for o in r['observations'])
        after=project(baseline,followups)
        self.assertEqual(after['providers'][0],baseline['providers'][0])
        for before,row in zip(agent['results'],after['providers'][1]['results']):
            self.assertEqual(before['strictEverPassed'],row['strictEverPassed'])
            self.assertEqual(row['observations'][:len(before['observations'])],before['observations'])
        self.assertEqual(after['providers'][1]['successfulTargets'],80)
        self.assertEqual(after['providers'][1]['totalTargets'],82)

    def test_no_private_evidence_published(self):
        text=(RESULTS/'prod-agent-followups.json').read_text()
        for forbidden in ('/jobs/','session_id','Bearer ','10.40.','/Users/'):
            self.assertNotIn(forbidden,text)
        cases=json.loads(text)['cases']
        best=next(c for c in cases if c['testName']=='Best Buy')
        self.assertFalse(best['exactFrozenSkuVerified'])
        self.assertEqual(sum(c['success'] for c in cases),3)

if __name__=='__main__': unittest.main()
