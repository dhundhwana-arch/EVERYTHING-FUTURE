import unittest
from lawson_criterion import evaluate_fusion_regime


class TestLawsonCriterion(unittest.TestCase):
    def test_iter_like_q10(self):
        res = evaluate_fusion_regime(1e20, 15.0, 3.0, q_plasma=10.0, thermal_eff=0.4, heating_eff=0.5)
        self.assertGreater(res["ignition_ratio"], 1.0)
        self.assertGreater(res["q_engineering"], 0.0)

    def test_low_q_not_net_electric(self):
        res = evaluate_fusion_regime(1e19, 10.0, 0.5, q_plasma=1.5, thermal_eff=0.4, heating_eff=0.5)
        self.assertEqual(res["net_electric"], 0.0)


if __name__ == "__main__":
    unittest.main()
