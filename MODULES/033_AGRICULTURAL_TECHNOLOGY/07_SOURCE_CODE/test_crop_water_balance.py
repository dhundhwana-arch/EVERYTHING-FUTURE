import unittest
from crop_water_balance import simulate_irrigation


class TestCropWaterBalance(unittest.TestCase):
    def test_triggers_irrigation_in_dry_period(self):
        res = simulate_irrigation([6.0] * 14, [0.0] * 14, kc=1.0, taw_mm=80.0, raw_fraction=0.5)
        self.assertGreaterEqual(res["irrigation_events"], 2.0)

    def test_no_irrigation_when_rain_sufficient(self):
        res = simulate_irrigation([4.0] * 7, [10.0] * 7, kc=1.0, taw_mm=100.0)
        self.assertEqual(res["irrigation_events"], 0.0)


if __name__ == "__main__":
    unittest.main()
