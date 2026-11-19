import unittest
from cmos_power_delay import cmos_metrics


class TestCMOSMetrics(unittest.TestCase):
    def test_voltage_quadratic_scaling(self):
        m1 = cmos_metrics(0.5, 1000.0, 1.0, 1.0, leakage_current_ma=0.0)
        m2 = cmos_metrics(0.5, 1000.0, 0.5, 1.0, leakage_current_ma=0.0)
        self.assertAlmostEqual(m1["dynamic_power_w"], 4.0 * m2["dynamic_power_w"], places=6)

    def test_rc_delay(self):
        m = cmos_metrics(0.1, 2.0, 0.8, 2.0, wire_resistance_ohm=50.0)
        self.assertAlmostEqual(m["rc_delay_ps"], 100.0, places=4)


if __name__ == "__main__":
    unittest.main()
