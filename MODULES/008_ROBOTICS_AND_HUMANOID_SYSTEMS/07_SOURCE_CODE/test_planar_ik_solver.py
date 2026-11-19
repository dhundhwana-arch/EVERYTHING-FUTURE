import math
import unittest
from planar_ik_solver import forward_kinematics, inverse_kinematics


class TestPlanarIK(unittest.TestCase):
    def test_roundtrip_ik_fk(self):
        t1, t2 = inverse_kinematics(1.2, 0.8, 1.1, 0.9)
        x, y = forward_kinematics(1.2, 0.8, t1, t2)
        self.assertAlmostEqual(x, 1.1, places=6)
        self.assertAlmostEqual(y, 0.9, places=6)

    def test_out_of_workspace(self):
        with self.assertRaises(ValueError):
            inverse_kinematics(1.0, 1.0, 2.5, 0.0)


if __name__ == "__main__":
    unittest.main()
