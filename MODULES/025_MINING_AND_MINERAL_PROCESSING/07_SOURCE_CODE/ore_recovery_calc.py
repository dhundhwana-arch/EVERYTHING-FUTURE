#!/usr/bin/env python3
"""
Mineral Processing Two-Product Metallurgical Mass Balance & Recovery Calculator
Module: 025_MINING_AND_MINERAL_PROCESSING | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict


def metallurgical_recovery(feed_grade_pct: float, conc_grade_pct: float, tail_grade_pct: float) -> Dict[str, float]:
    """Compute mass pull (%) and metal recovery (%) using the two-product formula."""
    if not (tail_grade_pct < feed_grade_pct < conc_grade_pct):
        raise ValueError("Require tail_grade < feed_grade < conc_grade.")
    mass_pull = (feed_grade_pct - tail_grade_pct) / (conc_grade_pct - tail_grade_pct)
    recovery = mass_pull * (conc_grade_pct / feed_grade_pct)
    return {
        "mass_pull_pct": round(100.0 * mass_pull, 2),
        "metal_recovery_pct": round(100.0 * recovery, 2),
    }


if __name__ == "__main__":
    print("Copper Flotation Balance:", metallurgical_recovery(0.8, 25.0, 0.1))
