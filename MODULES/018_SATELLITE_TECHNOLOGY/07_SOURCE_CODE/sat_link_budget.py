#!/usr/bin/env python3
"""
Satellite Communications Free-Space Path Loss (FSPL) & Link Budget Calculator
Module: 018_SATELLITE_TECHNOLOGY | EVERYTHING FUTURE (v2.0.0)
"""

import math
from typing import Dict

C_LIGHT = 299792458.0


def compute_link_budget(
    tx_power_dbw: float,
    tx_gain_dbi: float,
    rx_gain_dbi: float,
    distance_km: float,
    freq_ghz: float,
    atm_loss_db: float = 1.5,
) -> Dict[str, float]:
    """Compute FSPL (dB) and received signal power (dBW) for a satellite RF link."""
    if distance_km <= 0 or freq_ghz <= 0:
        raise ValueError("Distance and frequency must be positive.")
    d_m = distance_km * 1000.0
    f_hz = freq_ghz * 1e9
    fspl_db = 20.0 * math.log10(4.0 * math.pi * d_m * f_hz / C_LIGHT)
    rx_power_dbw = tx_power_dbw + tx_gain_dbi + rx_gain_dbi - fspl_db - atm_loss_db
    return {"fspl_db": round(fspl_db, 2), "rx_power_dbw": round(rx_power_dbw, 2)}


if __name__ == "__main__":
    print("LEO 600km Ka-Band (20 GHz):", compute_link_budget(10.0, 30.0, 35.0, 600.0, 20.0))
