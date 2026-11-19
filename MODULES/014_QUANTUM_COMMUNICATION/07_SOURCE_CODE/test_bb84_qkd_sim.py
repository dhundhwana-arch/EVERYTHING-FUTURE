import unittest
from bb84_qkd_sim import bb84_sift_and_qber


class TestBB84(unittest.TestCase):
    def test_clean_channel_zero_qber(self):
        r = bb84_sift_and_qber([0, 1, 1, 0], ["+", "x", "+", "x"], ["+", "+", "+", "x"], [0, 0, 1, 0])
        self.assertEqual(r["sifted_len"], 3.0)
        self.assertEqual(r["qber_pct"], 0.0)
        self.assertEqual(r["eavesdropper_alert"], 0.0)

    def test_eavesdropper_detected(self):
        r = bb84_sift_and_qber([0, 1, 1, 0], ["+", "+", "+", "+"], ["+", "+", "+", "+"], [1, 1, 0, 0])
        self.assertEqual(r["qber_pct"], 50.0)
        self.assertEqual(r["eavesdropper_alert"], 1.0)


if __name__ == "__main__":
    unittest.main()
