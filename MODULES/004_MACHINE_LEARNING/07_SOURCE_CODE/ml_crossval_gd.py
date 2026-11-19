#!/usr/bin/env python3
"""
Gradient Descent Linear Regression with K-Fold Cross-Validation (Pure Python)
Module: 004_MACHINE_LEARNING | EVERYTHING FUTURE (v1.0.0)
"""

import math
from typing import List, Tuple, Dict


def fit_linear_gd(x: List[float], y: List[float], lr: float = 0.01, epochs: int = 1000) -> Tuple[float, float]:
    """Fit y = w*x + b via batch gradient descent."""
    n = len(x)
    w, b = 0.0, 0.0
    for _ in range(epochs):
        dw = sum(2.0 * ((w * xi + b) - yi) * xi for xi, yi in zip(x, y)) / n
        db = sum(2.0 * ((w * xi + b) - yi) for xi, yi in zip(x, y)) / n
        w -= lr * dw
        b -= lr * db
    return w, b


def k_fold_cv(x: List[float], y: List[float], k: int = 4, lr: float = 0.01, epochs: int = 1000) -> Dict[str, float]:
    """Evaluate linear regression using k-fold cross-validation."""
    n = len(x)
    if k < 2 or k > n:
        raise ValueError("k must satisfy 2 <= k <= len(x)")
    fold_size = n // k
    rmses = []
    for fold in range(k):
        start = fold * fold_size
        end = start + fold_size if fold < k - 1 else n
        x_val, y_val = x[start:end], y[start:end]
        x_tr = x[:start] + x[end:]
        y_tr = y[:start] + y[end:]
        w, b = fit_linear_gd(x_tr, y_tr, lr=lr, epochs=epochs)
        mse = sum(((w * xi + b) - yi) ** 2 for xi, yi in zip(x_val, y_val)) / len(x_val)
        rmses.append(math.sqrt(mse))
    return {"mean_rmse": round(sum(rmses) / len(rmses), 5), "folds": float(k)}


if __name__ == "__main__":
    xs = [float(i) for i in range(1, 13)]
    ys = [2.5 * xi + 1.0 for xi in xs]
    w, b = fit_linear_gd(xs, ys, lr=0.005, epochs=3000)
    print(f"Fitted: y = {w:.4f}x + {b:.4f} | CV:", k_fold_cv(xs, ys, k=4, lr=0.005, epochs=3000))
