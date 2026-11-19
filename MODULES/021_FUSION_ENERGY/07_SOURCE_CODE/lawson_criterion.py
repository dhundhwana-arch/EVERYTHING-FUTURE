#!/usr/bin/env python3
"""
D-T Fusion Lawson Triple Product & Engineering Q-Factor Calculator (Pure Python)
Module: 021_FUSION_ENERGY | EVERYTHING FUTURE (v1.0.0)
"""

from typing import Dict

# Reference ignition threshold for D-T at ~15 keV: ~3e21 keV * s / m^3
DT_IGNITION_TRIPLE_PRODUCT = 3.0e21


def evaluate_fusion_regime(
    density_m3: float,
    temp_kev: float,
    confinement_s: float,
    q_plasma: float,
    thermal_eff: float = 0.40,
    heating_eff: float = 0.50,
) -> Dict[str, float]:
    """Compute Lawson triple product, ignition fraction, and net engineering gain Q_eng."""
    if density_m3 <= 0 or temp_kev <= 0 or confinement_s <= 0:
        raise ValueError("Plasma parameters must be positive.")
    triple = density_m3 * temp_kev * confinement_s
    # Q_eng = net electrical output / recirculating electrical input = thermal_eff * heating_eff * (Q_plasma + 1) - 1
    q_eng = thermal_eff * heating_eff * (q_plasma + 1.0) - 1.0
    return {
        "triple_product_kev_s_m3": triple,
        "ignition_ratio": round(triple / DT_IGNITION_TRIPLE_PRODUCT, 4),
        "q_engineering": round(q_eng, 4),
        "net_electric": 1.0 if q_eng > 0 else 0.0,
    }


if __name__ == "__main__":
    print("ITER-like Q=10 regime:", evaluate_fusion_regime(1e20, 15.0, 3.0, q_plasma=10.0))
