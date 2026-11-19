import unittest
from standards_traceability import evaluate_compliance


class TestStandardsTraceability(unittest.TestCase):
    def test_compliance_summary(self):
        reqs = [
            {"req_id": "R1", "standard_ref": "ISO 9001", "status": "COMPLIANT"},
            {"req_id": "R2", "standard_ref": "", "status": "PENDING"},
        ]
        res = evaluate_compliance(reqs)
        self.assertEqual(res["compliance_pct"], 50.0)
        self.assertEqual(res["missing_standard_refs"], ["R2"])


if __name__ == "__main__":
    unittest.main()
