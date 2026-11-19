import unittest
from wafer_yield_calc import estimate_wafer_yield


class TestWaferYield(unittest.TestCase):
    def test_zero_defects_full_yield(self):
        r = estimate_wafer_yield(300.0, 100.0, 0.0)
        self.assertEqual(r["poisson_yield_pct"], 100.0)
        self.assertGreater(r["gross_dies_per_wafer"], 600)

    def test_higher_defects_lower_yield(self):
        low = estimate_wafer_yield(300.0, 100.0, 0.1)
        high = estimate_wafer_yield(300.0, 100.0, 0.8)
        self.assertLess(high["murphy_yield_pct"], low["murphy_yield_pct"])


if __name__ == "__main__":
    unittest.main()
