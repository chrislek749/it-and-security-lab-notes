import unittest
from analyse import parse, detect, ROOT

class DetectionTests(unittest.TestCase):
    def test_supplied_dataset(self):
        events=parse((ROOT/'synthetic_authentication.log').read_text())
        self.assertEqual(len(events),24)
        self.assertEqual(sum(e['result']=='FAILURE' for e in events),17)
        self.assertEqual([(a['rule'],a['trigger']) for a in detect(events)],[
            ('MULTI_ACCOUNT_FAILURES','E009'),('REPEATED_ACCOUNT_FAILURES','E015'),('SUCCESS_AFTER_FAILURES','E017')])

    def test_typo_then_success_is_not_alert(self):
        events=parse('E1 | 2026-09-01T09:00:00Z | a | 192.0.2.1 | FAILURE | NOT_REACHED\nE2 | 2026-09-01T09:00:10Z | a | 192.0.2.1 | SUCCESS | PASSED')
        self.assertEqual(detect(events),[])

    def test_failures_outside_window_do_not_accumulate(self):
        text='\n'.join(f'E{i} | 2026-09-01T09:{i*6:02}:00Z | a | 192.0.2.1 | FAILURE | NOT_REACHED' for i in range(5))
        self.assertEqual(detect(parse(text)),[])

    def test_other_account_success_is_not_correlated(self):
        text='\n'.join(f'E{i} | 2026-09-01T09:00:0{i}Z | a | 192.0.2.1 | FAILURE | NOT_REACHED' for i in range(5))
        text+='\nE5 | 2026-09-01T09:00:10Z | b | 192.0.2.1 | SUCCESS | PASSED'
        self.assertNotIn('SUCCESS_AFTER_FAILURES',[a['rule'] for a in detect(parse(text))])

if __name__=='__main__': unittest.main()
