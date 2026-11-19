#!/usr/bin/env python3
"""
Tsiolkovsky Rocket Equation & Multi-Stage Delta-V Analyzer (Pure Python)
Module: 017_ROCKET_SCIENCE | EVERYTHING FUTURE (v1.0.0)
"""

import math
from typing import List, Dict

G0 = 9.80665


def stage_delta_v(isp_s: float, m_initial_kg: float, m_final_kg: float) -> float:
    """Compute stage delta-v in m/s using Tsiolkovsky's rocket equation."""
    if isp_s <= 0 or m_final_kg <= 0 or m_initial_kg <= m_final_kg:
        raise ValueError("Require isp_s > 0 and m_initial_kg > m_final_kg > 0.")
    return isp_s * G0 * math.log(m_initial_kg / m_final_kg)


def two_stage_vehicle(
    payload_kg: float,
    s1_prop_kg: float, s1_dry_kg: float, s1_isp_s: float,
    s2_prop_kg: float, s2_dry_kg: float, s2_isp_s: float,
) -> Dict[str, float]:
    """Compute total delta-v and payload mass fraction for a 2-stage launch vehicle."""
    m0_s2 = payload_kg + s2_dry_kg + s2_prop_kg
    mf_s2 = payload_kg + s2_dry_kg
    dv2 = stage_delta_v(s2_isp_s, m0_s2, mf_s2)

    m0_s1 = m0_s2 + s1_dry_kg + s1_prop_kg
    mf_s1 = m0_s2 + s1_dry_kg
    dv1 = stage_delta_v(s1_isp_s, m0_s1, mf_s1)

    return {
        "dv_stage1_m_s": round(dv1, 2),
        "dv_stage2_m_s": round(dv2, 2),
        "total_dv_m_s": round(dv1 + dv2, 2),
        "payload_fraction_pct": round(100.0 * payload_kg / m0_s1, 3),
    }


if __name__ == "__main__":
    print("2-Stage LEO Launcher Estimate:", two_stage_vehicle(15000, 390000, 26000, 311, 105000, 4500, 348))
