import unittest
from diagnostic_bayes_calc import diagnostic_predictive_values


class TestDiagnosticBayes(unittest.TestCase):
    def test_base_rate_fallacy_check(self):
        r = diagnostic_predictive_values(0.95, 0.95, 0.01)
        self.assertAlmostEqual(r["ppv_pct"], 16.1, places=1)
        self.assertGreater(r["npv_pct"], 99.0)


if __name__ == "__main__":
    unittest.main()
