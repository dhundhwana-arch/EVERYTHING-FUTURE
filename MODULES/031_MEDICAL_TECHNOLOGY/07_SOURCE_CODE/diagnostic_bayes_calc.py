#!/usr/bin/env python3
"""
Clinical Diagnostic Bayes Post-Test Probability (PPV / NPV) Calculator
Module: 031_MEDICAL_TECHNOLOGY | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict


def diagnostic_predictive_values(sensitivity: float, specificity: float, prevalence: float) -> Dict[str, float]:
    """Compute Positive Predictive Value (PPV) and Negative Predictive Value (NPV)."""
    for val in (sensitivity, specificity, prevalence):
        if not (0.0 <= val <= 1.0):
            raise ValueError("Probabilities must be in [0, 1].")
    tp = sensitivity * prevalence
    fp = (1.0 - specificity) * (1.0 - prevalence)
    tn = specificity * (1.0 - prevalence)
    fn = (1.0 - sensitivity) * prevalence
    ppv = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    npv = tn / (tn + fn) if (tn + fn) > 0 else 0.0
    return {"ppv_pct": round(100.0 * ppv, 2), "npv_pct": round(100.0 * npv, 2)}


if __name__ == "__main__":
    print("95% Sens / 95% Spec at 1% Prevalence:", diagnostic_predictive_values(0.95, 0.95, 0.01))
