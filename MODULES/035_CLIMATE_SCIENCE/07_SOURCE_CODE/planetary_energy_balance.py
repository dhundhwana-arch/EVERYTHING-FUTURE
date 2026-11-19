#!/usr/bin/env python3
"""
0D Planetary Radiative Equilibrium & Greenhouse Emissivity Model (Pure Python)
Module: 035_CLIMATE_SCIENCE | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict

SIGMA = 5.670374419e-8


def equilibrium_temperature(solar_constant_w_m2: float = 1361.0, albedo: float = 0.30, emissivity: float = 0.612) -> Dict[str, float]:
    """Compute effective radiative temperature (no atmosphere) and surface temperature (K & C)."""
    if not (0.0 <= albedo < 1.0) or not (0.0 < emissivity <= 1.0):
        raise ValueError("Invalid albedo or emissivity.")
    absorbed = solar_constant_w_m2 * (1.0 - albedo) / 4.0
    t_eff_k = (absorbed / SIGMA) ** 0.25
    t_surf_k = (absorbed / (emissivity * SIGMA)) ** 0.25
    return {
        "absorbed_flux_w_m2": round(absorbed, 2),
        "t_effective_k": round(t_eff_k, 2),
        "t_surface_k": round(t_surf_k, 2),
        "t_surface_c": round(t_surf_k - 273.15, 2),
    }


if __name__ == "__main__":
    print("Earth 0D Radiative Balance:", equilibrium_temperature())
