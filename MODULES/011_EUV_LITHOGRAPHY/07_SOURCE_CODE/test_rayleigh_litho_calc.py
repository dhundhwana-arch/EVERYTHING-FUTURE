import unittest
from rayleigh_litho_calc import rayleigh_lithography


class TestRayleighLitho(unittest.TestCase):
    def test_high_na_improves_resolution_reduces_dof(self):
        euv = rayleigh_lithography(13.5, 0.33)
        high_na = rayleigh_lithography(13.5, 0.55)
        self.assertLess(high_na["cd_nm"], euv["cd_nm"])
        self.assertLess(high_na["dof_nm"], euv["dof_nm"])

    def test_k1_limit(self):
        with self.assertRaises(ValueError):
            rayleigh_lithography(13.5, 0.33, k1=0.20)


if __name__ == "__main__":
    unittest.main()
