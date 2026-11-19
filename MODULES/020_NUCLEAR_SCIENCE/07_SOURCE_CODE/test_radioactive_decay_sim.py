import unittest
from radioactive_decay_sim import decay_remaining


class TestRadioactiveDecay(unittest.TestCase):
    def test_three_half_lives(self):
        r = decay_remaining(800.0, 5.0, 15.0)
        self.assertAlmostEqual(r["remaining_atoms"], 100.0, places=3)


if __name__ == "__main__":
    unittest.main()
