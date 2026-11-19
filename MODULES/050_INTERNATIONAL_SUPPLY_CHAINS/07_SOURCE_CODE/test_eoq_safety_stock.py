import unittest
from eoq_safety_stock import inventory_policy


class TestEOQSafetyStock(unittest.TestCase):
    def test_exact_eoq(self):
        r = inventory_policy(10000.0, 200.0, 4.0, 0.0, 10.0)
        self.assertAlmostEqual(r["eoq_units"], 1000.0, places=1)
        self.assertEqual(r["safety_stock_units"], 0.0)


if __name__ == "__main__":
    unittest.main()
