import unittest
from desalination_osmotic import osmotic_min_energy


class TestDesalinationOsmotic(unittest.TestCase):
    def test_standard_seawater(self):
        r = osmotic_min_energy(35.0, 25.0)
        self.assertAlmostEqual(r["osmotic_pressure_bar"], 29.7, delta=1.5)
        self.assertGreater(r["ideal_min_kwh_per_m3"], 0.7)


if __name__ == "__main__":
    unittest.main()
