import unittest
from sat_link_budget import compute_link_budget


class TestSatLinkBudget(unittest.TestCase):
    def test_doubling_distance_adds_6db_loss(self):
        l1 = compute_link_budget(10.0, 20.0, 20.0, 500.0, 12.0)
        l2 = compute_link_budget(10.0, 20.0, 20.0, 1000.0, 12.0)
        self.assertAlmostEqual(l2["fspl_db"] - l1["fspl_db"], 6.02, places=1)


if __name__ == "__main__":
    unittest.main()
