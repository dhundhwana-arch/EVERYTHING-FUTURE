import unittest
from ev_range_energy import estimate_ev_range


class TestEVRange(unittest.TestCase):
    def test_higher_speed_reduces_range(self):
        slow = estimate_ev_range(60.0, 1800.0, 70.0)
        fast = estimate_ev_range(60.0, 1800.0, 120.0)
        self.assertGreater(slow["estimated_range_km"], fast["estimated_range_km"])


if __name__ == "__main__":
    unittest.main()
