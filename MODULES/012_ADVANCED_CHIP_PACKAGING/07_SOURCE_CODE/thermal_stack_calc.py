#!/usr/bin/env python3
"""
1D IC Package Junction-to-Ambient Thermal Resistance Calculator (Pure Python)
Module: 012_ADVANCED_CHIP_PACKAGING | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict


def junction_temperature(
    power_w: float,
    ambient_c: float,
    r_jc_c_per_w: float,
    r_tim_c_per_w: float,
    r_hs_c_per_w: float,
    max_tj_c: float = 105.0,
) -> Dict[str, float]:
    """Compute junction temperature Tj and thermal margin for a 1D resistance stack."""
    if power_w < 0:
        raise ValueError("Power must be non-negative.")
    r_total = r_jc_c_per_w + r_tim_c_per_w + r_hs_c_per_w
    tj = ambient_c + power_w * r_total
    return {
        "r_total_c_per_w": round(r_total, 4),
        "junction_temp_c": round(tj, 2),
        "thermal_margin_c": round(max_tj_c - tj, 2),
        "within_spec": 1.0 if tj <= max_tj_c else 0.0,
    }


if __name__ == "__main__":
    print("300W AI Accelerator Package:", junction_temperature(300.0, 35.0, 0.05, 0.04, 0.12))
