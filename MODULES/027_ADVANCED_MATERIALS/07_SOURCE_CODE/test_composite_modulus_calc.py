import unittest
from composite_modulus_calc import composite_bounds


class TestCompositeModulus(unittest.TestCase):
    def test_voigt_exceeds_reuss(self):
        r = composite_bounds(230.0, 3.5, 0.6)
        self.assertGreater(r["voigt_upper_gpa"], r["reuss_lower_gpa"])


if __name__ == "__main__":
    unittest.main()
