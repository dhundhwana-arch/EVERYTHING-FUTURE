import unittest
from qubit_bell_sim import bell_state_probabilities


class TestQubitBellSim(unittest.TestCase):
    def test_bell_state_entanglement(self):
        probs = bell_state_probabilities()
        self.assertAlmostEqual(probs["00"], 0.5, places=5)
        self.assertAlmostEqual(probs["11"], 0.5, places=5)
        self.assertAlmostEqual(probs["01"], 0.0, places=5)
        self.assertAlmostEqual(probs["10"], 0.0, places=5)
        self.assertAlmostEqual(sum(probs.values()), 1.0, places=5)


if __name__ == "__main__":
    unittest.main()
