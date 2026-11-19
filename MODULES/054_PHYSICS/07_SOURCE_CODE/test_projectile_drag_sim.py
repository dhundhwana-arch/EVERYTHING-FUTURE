import unittest
from projectile_drag_sim import simulate_range


class TestProjectileDrag(unittest.TestCase):
    def test_drag_reduces_range(self):
        r = simulate_range(40.0, 45.0, drag_k_per_m=0.005)
        self.assertLess(r["drag_range_m"], r["vacuum_range_m"])


if __name__ == "__main__":
    unittest.main()
