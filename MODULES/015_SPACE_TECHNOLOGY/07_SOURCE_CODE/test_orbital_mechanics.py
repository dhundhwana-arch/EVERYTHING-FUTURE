import unittest
from orbital_mechanics import hohmann_transfer


class TestOrbitalMechanics(unittest.TestCase):
    def test_leo_to_geo_hohmann(self):
        res = hohmann_transfer(400.0, 35786.0)
        self.assertAlmostEqual(res["v_circ_1_km_s"], 7.6686, places=2)
        self.assertAlmostEqual(res["total_dv_km_s"], 3.85, places=1)
        self.assertAlmostEqual(res["transfer_time_hr"], 5.28, places=1)


if __name__ == "__main__":
    unittest.main()
