import unittest
from breguet_range_calc import breguet_jet_range_km


class TestBreguetRange(unittest.TestCase):
    def test_higher_ld_increases_range(self):
        r1 = breguet_jet_range_km(250.0, 1.6e-5, 15.0, 200000.0, 140000.0)
        r2 = breguet_jet_range_km(250.0, 1.6e-5, 20.0, 200000.0, 140000.0)
        self.assertGreater(r2["range_km"], r1["range_km"])


if __name__ == "__main__":
    unittest.main()
