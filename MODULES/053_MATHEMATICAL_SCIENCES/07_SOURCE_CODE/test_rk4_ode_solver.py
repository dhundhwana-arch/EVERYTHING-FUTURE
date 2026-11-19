import math
import unittest
from rk4_ode_solver import rk4_integrate


class TestRK4Solver(unittest.TestCase):
    def test_exponential_decay_accuracy(self):
        traj = rk4_integrate(lambda t, y: -y, 0.0, 1.0, 1.0, 50)
        self.assertAlmostEqual(traj[-1][1], math.exp(-1.0), places=7)


if __name__ == "__main__":
    unittest.main()
