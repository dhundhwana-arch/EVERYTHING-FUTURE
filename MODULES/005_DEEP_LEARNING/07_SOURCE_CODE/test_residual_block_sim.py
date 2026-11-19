import unittest
from residual_block_sim import compare_gradient_flow


class TestResidualBlock(unittest.TestCase):
    def test_residual_prevents_vanishing(self):
        r = compare_gradient_flow(50, 0.8)
        self.assertEqual(r["vanished_plain"], 1.0)
        self.assertGreater(r["residual_chain_grad"], 1.0)


if __name__ == "__main__":
    unittest.main()
