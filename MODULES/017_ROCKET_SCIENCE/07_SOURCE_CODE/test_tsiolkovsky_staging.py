import unittest
from tsiolkovsky_staging import stage_delta_v, two_stage_vehicle


class TestTsiolkovsky(unittest.TestCase):
    def test_stage_delta_v(self):
        dv = stage_delta_v(300.0, 1000.0, 100.0)
        self.assertAlmostEqual(dv, 300.0 * 9.80665 * 2.302585, places=1)

    def test_two_stage_reaches_leo_dv(self):
        res = two_stage_vehicle(15000, 390000, 26000, 311, 105000, 4500, 348)
        self.assertGreater(res["total_dv_m_s"], 9000.0)


if __name__ == "__main__":
    unittest.main()
