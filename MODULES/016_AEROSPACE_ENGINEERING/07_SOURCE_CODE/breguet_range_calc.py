#!/usr/bin/env python3
"""
Jet Aircraft Breguet Range Equation Calculator (Pure Python)
Module: 016_AEROSPACE_ENGINEERING | EVERYTHING FUTURE (v2.0.0)
"""

import math
from typing import Dict

G0 = 9.80665


def breguet_jet_range_km(
    cruise_speed_m_s: float,
    tsfc_kg_per_n_s: float,
    lift_to_drag: float,
    w_initial_kg: float,
    w_final_kg: float,
) -> Dict[str, float]:
    """Compute theoretical cruise range in km via the Breguet jet range equation."""
    if cruise_speed_m_s <= 0 or tsfc_kg_per_n_s <= 0 or lift_to_drag <= 0 or w_initial_kg <= w_final_kg:
        raise ValueError("Invalid aircraft performance parameters.")
    range_m = (cruise_speed_m_s / (G0 * tsfc_kg_per_n_s)) * lift_to_drag * math.log(w_initial_kg / w_final_kg)
    return {"range_km": round(range_m / 1000.0, 2), "fuel_fraction_pct": round(100.0 * (1.0 - w_final_kg / w_initial_kg), 2)}


if __name__ == "__main__":
    print("Long-Range Jet Estimate:", breguet_jet_range_km(250.0, 1.6e-5, 18.0, 200000.0, 130000.0))
