import unittest
from ore_recovery_calc import metallurgical_recovery


class TestOreRecovery(unittest.TestCase):
    def test_two_product_balance(self):
        r = metallurgical_recovery(1.0, 25.0, 0.1)
        self.assertGreater(r["metal_recovery_pct"], 85.0)
        self.assertLess(r["mass_pull_pct"], 10.0)


if __name__ == "__main__":
    unittest.main()
