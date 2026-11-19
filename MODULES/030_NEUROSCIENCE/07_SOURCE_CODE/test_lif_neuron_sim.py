import unittest
from lif_neuron_sim import simulate_lif


class TestLIFNeuron(unittest.TestCase):
    def test_subthreshold_zero_spikes(self):
        r = simulate_lif(0.5, 100.0)
        self.assertEqual(r["spikes"], 0.0)

    def test_suprathreshold_fires(self):
        r = simulate_lif(2.5, 100.0)
        self.assertGreater(r["spikes"], 0.0)


if __name__ == "__main__":
    unittest.main()
