import unittest
from defensive_security_calc import password_entropy_bits


class TestDefensiveSecurity(unittest.TestCase):
    def test_weak_vs_strong(self):
        self.assertEqual(password_entropy_bits("12345")["strength"], "WEAK")
        self.assertEqual(password_entropy_bits("X9!kL2#mP8$vQ4&z")["strength"], "STRONG")


if __name__ == "__main__":
    unittest.main()
