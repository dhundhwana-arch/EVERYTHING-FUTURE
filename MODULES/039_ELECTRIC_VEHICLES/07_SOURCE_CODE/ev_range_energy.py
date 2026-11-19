#!/usr/bin/env python3
"""
Electric Vehicle Aerodynamic + Rolling Resistance Consumption & Range Estimator
Module: 039_ELECTRIC_VEHICLES | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict

G0 = 9.80665
RHO_AIR = 1.225


def estimate_ev_range(
    battery_kwh: float,
    mass_kg: float,
    speed_kmh: float,
    cd: float = 0.24,
    frontal_area_m2: float = 2.3,
    crr: float = 0.009,
    drivetrain_eff: float = 0.88,
) -> Dict[str, float]:
    """Estimate steady highway EV consumption (Wh/km) and range (km)."""
    if battery_kwh <= 0 or mass_kg <= 0 or speed_kmh <= 0:
        raise ValueError("Parameters must be positive.")
    v = speed_kmh / 3.6
    f_roll = crr * mass_kg * G0
    f_aero = 0.5 * RHO_AIR * cd * frontal_area_m2 * (v ** 2)
    wheel_power_w = (f_roll + f_aero) * v
    batt_power_w = wheel_power_w / drivetrain_eff
    wh_per_km = batt_power_w / speed_kmh
    range_km = (battery_kwh * 1000.0) / wh_per_km
    return {"wh_per_km": round(wh_per_km, 2), "estimated_range_km": round(range_km, 1)}


if __name__ == "__main__":
    print("60 kWh EV at 90 km/h:", estimate_ev_range(60.0, 1800.0, 90.0))
