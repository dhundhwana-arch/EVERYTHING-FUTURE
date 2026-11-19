#!/usr/bin/env python3
"""
Photolithography Rayleigh Resolution (CD) & Depth of Focus (DOF) Calculator
Module: 011_EUV_LITHOGRAPHY | EVERYTHING FUTURE (v1.0.0)
"""

from typing import Dict


def rayleigh_lithography(wavelength_nm: float, na: float, k1: float = 0.28, k2: float = 0.5) -> Dict[str, float]:
    """Compute Critical Dimension (CD) and Depth of Focus (DOF) in nanometers."""
    if wavelength_nm <= 0 or na <= 0 or k1 < 0.25:
        raise ValueError("Invalid optical parameters (note physical single-exposure limit k1 >= 0.25).")
    cd_nm = k1 * wavelength_nm / na
    dof_nm = k2 * wavelength_nm / (na ** 2)
    return {"cd_nm": round(cd_nm, 3), "dof_nm": round(dof_nm, 3), "wavelength_nm": wavelength_nm, "na": na}


if __name__ == "__main__":
    print("193i DUV (1.35 NA):", rayleigh_lithography(193.0, 1.35))
    print("0.33 NA EUV (13.5nm):", rayleigh_lithography(13.5, 0.33))
    print("0.55 NA High-NA EUV:", rayleigh_lithography(13.5, 0.55))
