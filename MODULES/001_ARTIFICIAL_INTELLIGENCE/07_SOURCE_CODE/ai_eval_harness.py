#!/usr/bin/env python3
"""
Standalone AI Classification Evaluation Harness (Zero External Dependencies)
Module: 001_ARTIFICIAL_INTELLIGENCE | EVERYTHING FUTURE (v1.0.0)
Owner: DIVYESH BAMBHANIYA
"""

from typing import List, Dict, Tuple


def compute_metrics(y_true: List[int], y_pred: List[int], y_prob: List[float], n_bins: int = 5) -> Dict[str, float]:
    """Compute binary accuracy, precision, recall, F1, and Expected Calibration Error (ECE)."""
    if not (len(y_true) == len(y_pred) == len(y_prob)) or len(y_true) == 0:
        raise ValueError("Input lists must be non-empty and of equal length.")

    n = len(y_true)
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)

    accuracy = (tp + tn) / n
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    # Expected Calibration Error (ECE)
    ece = 0.0
    for b in range(n_bins):
        low = b / n_bins
        high = (b + 1) / n_bins
        indices = [
            i for i, prob in enumerate(y_prob)
            if (low <= prob < high) or (b == n_bins - 1 and prob == 1.0)
        ]
        if indices:
            avg_conf = sum(y_prob[i] for i in indices) / len(indices)
            avg_acc = sum(1 for i in indices if y_true[i] == 1) / len(indices)
            ece += (len(indices) / n) * abs(avg_acc - avg_conf)

    return {
        "samples": float(n),
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "ece": round(ece, 4),
    }


if __name__ == "__main__":
    y_t = [1, 1, 0, 1, 0, 0, 1, 0]
    y_p = [1, 1, 0, 0, 0, 1, 1, 0]
    probs = [0.92, 0.85, 0.15, 0.45, 0.20, 0.60, 0.88, 0.10]
    print("AI Evaluation Harness Output:", compute_metrics(y_t, y_p, probs))
