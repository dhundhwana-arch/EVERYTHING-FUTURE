import unittest
from factory_oee_littles_law import compute_oee_and_wip


class TestFactoryOEE(unittest.TestCase):
    def test_oee_and_littles_law(self):
        r = compute_oee_and_wip(0.9, 0.9, 0.9, 20.0, 3.0)
        self.assertAlmostEqual(r["oee_pct"], 72.9, places=1)
        self.assertEqual(r["steady_state_wip_units"], 60.0)


if __name__ == "__main__":
    unittest.main()
