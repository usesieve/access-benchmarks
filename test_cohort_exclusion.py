import copy
import json
import unittest
from pathlib import Path

from exclude_retired_marketwatch import project, URL


class CohortExclusionTests(unittest.TestCase):
    def test_original_observations_and_other_target_outcomes_are_preserved(self):
        data = json.loads((Path(__file__).parent / 'results/2026-10-23/sieve-string-frontier.json').read_text())
        before = copy.deepcopy(data)
        result = project(data)
        self.assertEqual(data, before)
        for old, new in zip(data['providers'], result['providers']):
            self.assertEqual(new['totalTargets'], 82)
            self.assertFalse(any(r['testName'] == 'marketwatch' for r in new['results']))
            self.assertEqual(new['results'], [r for r in old['results'] if r['testName'] != 'marketwatch'])
            self.assertTrue(any(r['testName'] == 'marketwatch' and r['url'] == URL
                                for r in new['excludedResults']))
            self.assertEqual(new['successfulTargets'], sum(r['success'] for r in new['results']))
        self.assertEqual(project(result), result)

    def test_exclusion_is_exact_url_not_a_blanket_domain_filter(self):
        data = json.loads((Path(__file__).parent / 'results/2026-10-23/sieve-string-frontier.json').read_text())
        data['providers'][0]['results'].append({'testName': 'marketwatch', 'url': 'https://www.marketwatch.com/investing/stock/skyd'})
        with self.assertRaises(ValueError):
            project(data)


if __name__ == '__main__':
    unittest.main()
