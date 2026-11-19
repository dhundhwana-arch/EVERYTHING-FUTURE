import unittest
from thermal_stack_calc import junction_temperature


class TestThermalStack(unittest.TestCase):
    def test_within_thermal_spec(self):
        r = junction_temperature(250.0, 30.0, 0.05, 0.05, 0.10, max_tj_c=100.0)
        self.assertEqual(r["junction_temp_c"], 80.0)
        self.assertEqual(r["within_spec"], 1.0)


if __name__ == "__main__":
    unittest.main()
