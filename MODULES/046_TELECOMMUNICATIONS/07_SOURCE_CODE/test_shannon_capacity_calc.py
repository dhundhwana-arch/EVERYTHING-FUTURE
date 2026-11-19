import unittest
from shannon_capacity_calc import shannon_capacity


class TestShannonCapacity(unittest.TestCase):
    def test_0db_snr_is_1_bps_hz(self):
        r = shannon_capacity(20.0, 0.0)
        self.assertAlmostEqual(r["spectral_efficiency_bps_hz"], 1.0, places=4)
        self.assertAlmostEqual(r["capacity_mbps"], 20.0, places=2)


if __name__ == "__main__":
    unittest.main()
