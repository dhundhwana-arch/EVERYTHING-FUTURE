#!/usr/bin/env python3
"""
300mm Silicon Wafer Dies-Per-Wafer (DPW) & Poisson/Murphy Yield Calculator
Module: 010_SEMICONDUCTOR_FABRICATION | EVERYTHING FUTURE (v2.0.0)
"""

import math
from typing import Dict


def estimate_wafer_yield(wafer_dia_mm: float, die_area_mm2: float, defect_density_cm2: float) -> Dict[str, float]:
    """Estimate gross dies per wafer, Poisson yield, and Murphy yield."""
    if wafer_dia_mm <= 0 or die_area_mm2 <= 0 or defect_density_cm2 < 0:
        raise ValueError("Invalid wafer or die parameters.")
    r = wafer_dia_mm / 2.0
    dpw = int((math.pi * r * r) / die_area_mm2 - (math.pi * wafer_dia_mm) / math.sqrt(2.0 * die_area_mm2))
    area_cm2 = die_area_mm2 / 100.0
    ad = area_cm2 * defect_density_cm2
    y_poisson = math.exp(-ad)
    y_murphy = ((1.0 - math.exp(-ad)) / ad) ** 2 if ad > 1e-9 else 1.0
    return {
        "gross_dies_per_wafer": float(max(dpw, 0)),
        "poisson_yield_pct": round(100.0 * y_poisson, 2),
        "murphy_yield_pct": round(100.0 * y_murphy, 2),
        "good_dies_murphy": float(int(max(dpw, 0) * y_murphy)),
    }


if __name__ == "__main__":
    print("300mm Wafer (100 mm^2 die, D0=0.2/cm^2):", estimate_wafer_yield(300.0, 100.0, 0.2))
