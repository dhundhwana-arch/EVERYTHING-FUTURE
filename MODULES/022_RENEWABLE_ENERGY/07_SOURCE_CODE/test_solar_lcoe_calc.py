import unittest
from solar_lcoe_calc import calculate_solar_lcoe


class TestSolarLCOE(unittest.TestCase):
    def test_higher_cf_lowers_lcoe(self):
        low_cf = calculate_solar_lcoe(800.0, 12.0, 0.15)
        high_cf = calculate_solar_lcoe(800.0, 12.0, 0.25)
        self.assertLess(high_cf["lcoe_usd_per_kwh"], low_cf["lcoe_usd_per_kwh"])


if __name__ == "__main__":
    unittest.main()
