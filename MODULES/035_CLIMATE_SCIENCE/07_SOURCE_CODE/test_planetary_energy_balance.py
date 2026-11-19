import unittest
from planetary_energy_balance import equilibrium_temperature


class TestPlanetaryBalance(unittest.TestCase):
    def test_earth_baseline(self):
        r = equilibrium_temperature(1361.0, 0.30, 0.612)
        self.assertAlmostEqual(r["t_effective_k"], 254.6, places=0)
        self.assertAlmostEqual(r["t_surface_c"], 15.0, delta=1.5)


if __name__ == "__main__":
    unittest.main()
