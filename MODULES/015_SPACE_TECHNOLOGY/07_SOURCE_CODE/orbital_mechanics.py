#!/usr/bin/env python3
"""
Orbital Mechanics & Hohmann Transfer Delta-V Calculator (Pure Python)
Module: 015_SPACE_TECHNOLOGY | EVERYTHING FUTURE (v1.0.0)
"""

import math
from typing import Dict

MU_EARTH_KM3_S2 = 398600.4418
R_EARTH_KM = 6378.137


def hohmann_transfer(alt1_km: float, alt2_km: float) -> Dict[str, float]:
    """Compute circular velocities, transfer time, and total Hohmann delta-v (km/s) around Earth."""
    if alt1_km < 0 or alt2_km < 0:
        raise ValueError("Altitudes must be non-negative.")
    r1 = R_EARTH_KM + alt1_km
    r2 = R_EARTH_KM + alt2_km
    v1 = math.sqrt(MU_EARTH_KM3_S2 / r1)
    v2 = math.sqrt(MU_EARTH_KM3_S2 / r2)
    a_tx = 0.5 * (r1 + r2)
    v_tx1 = math.sqrt(MU_EARTH_KM3_S2 * (2.0 / r1 - 1.0 / a_tx))
    v_tx2 = math.sqrt(MU_EARTH_KM3_S2 * (2.0 / r2 - 1.0 / a_tx))
    dv1 = abs(v_tx1 - v1)
    dv2 = abs(v2 - v_tx2)
    transfer_time_hr = (math.pi * math.sqrt((a_tx ** 3) / MU_EARTH_KM3_S2)) / 3600.0
    return {
        "v_circ_1_km_s": round(v1, 4),
        "v_circ_2_km_s": round(v2, 4),
        "dv1_km_s": round(dv1, 4),
        "dv2_km_s": round(dv2, 4),
        "total_dv_km_s": round(dv1 + dv2, 4),
        "transfer_time_hr": round(transfer_time_hr, 3),
    }


if __name__ == "__main__":
    print("LEO (400 km) to GEO (35786 km):", hohmann_transfer(400.0, 35786.0))
