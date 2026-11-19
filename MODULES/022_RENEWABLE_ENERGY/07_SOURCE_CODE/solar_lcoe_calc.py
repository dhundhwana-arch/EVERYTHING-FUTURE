#!/usr/bin/env python3
"""
Solar PV Levelized Cost of Electricity (LCOE) Calculator (Pure Python)
Module: 022_RENEWABLE_ENERGY | EVERYTHING FUTURE (v1.0.0)
"""

from typing import Dict


def calculate_solar_lcoe(
    capex_per_kw: float,
    opex_per_kw_yr: float,
    capacity_factor: float,
    discount_rate: float = 0.06,
    lifetime_years: int = 25,
    annual_degradation: float = 0.005,
) -> Dict[str, float]:
    """Compute discounted LCOE ($/kWh) and lifetime energy yield per kW installed."""
    if not (0 < capacity_factor <= 1.0) or lifetime_years <= 0:
        raise ValueError("Invalid capacity factor or lifetime.")
    pv_costs = capex_per_kw
    pv_energy_kwh = 0.0
    total_kwh = 0.0
    for yr in range(1, lifetime_years + 1):
        df = (1.0 + discount_rate) ** yr
        pv_costs += opex_per_kw_yr / df
        yr_kwh = 8760.0 * capacity_factor * ((1.0 - annual_degradation) ** (yr - 1))
        total_kwh += yr_kwh
        pv_energy_kwh += yr_kwh / df
    return {
        "lcoe_usd_per_kwh": round(pv_costs / pv_energy_kwh, 5),
        "lifetime_kwh_per_kw": round(total_kwh, 1),
    }


if __name__ == "__main__":
    print("Utility Solar PV LCOE:", calculate_solar_lcoe(800.0, 12.0, 0.22))
