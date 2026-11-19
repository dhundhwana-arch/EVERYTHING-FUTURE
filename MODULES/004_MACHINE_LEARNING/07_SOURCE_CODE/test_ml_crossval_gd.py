import unittest
from ml_crossval_gd import fit_linear_gd, k_fold_cv


class TestMLCrossVal(unittest.TestCase):
    def test_exact_linear_fit(self):
        xs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        ys = [3.0 * x + 2.0 for x in xs]
        w, b = fit_linear_gd(xs, ys, lr=0.01, epochs=4000)
        self.assertAlmostEqual(w, 3.0, places=2)
        self.assertAlmostEqual(b, 2.0, places=2)

    def test_kfold_cv(self):
        xs = [float(i) for i in range(1, 9)]
        ys = [2.0 * x + 1.0 for x in xs]
        res = k_fold_cv(xs, ys, k=4, lr=0.01, epochs=3000)
        self.assertLess(res["mean_rmse"], 0.05)


if __name__ == "__main__":
    unittest.main()
