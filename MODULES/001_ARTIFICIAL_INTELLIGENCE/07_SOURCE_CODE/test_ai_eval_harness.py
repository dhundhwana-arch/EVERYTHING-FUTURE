import unittest
from ai_eval_harness import compute_metrics


class TestAIEvalHarness(unittest.TestCase):
    def test_perfect_predictions(self):
        m = compute_metrics([1, 0, 1, 0], [1, 0, 1, 0], [1.0, 0.0, 1.0, 0.0])
        self.assertEqual(m["accuracy"], 1.0)
        self.assertEqual(m["f1"], 1.0)
        self.assertEqual(m["ece"], 0.0)

    def test_mixed_predictions(self):
        m = compute_metrics([1, 1, 0, 0], [1, 0, 0, 1], [0.9, 0.4, 0.1, 0.6])
        self.assertEqual(m["accuracy"], 0.5)
        self.assertEqual(m["precision"], 0.5)
        self.assertEqual(m["recall"], 0.5)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            compute_metrics([], [], [])


if __name__ == "__main__":
    unittest.main()
