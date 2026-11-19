#!/usr/bin/env python3
"""
Seawater Osmotic Pressure (van 't Hoff) & Thermodynamic Minimum Desalination Energy
Module: 037_WATER_ENGINEERING | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict

R_GAS = 8.314462618


def osmotic_min_energy(salinity_g_per_l: float = 35.0, temp_c: float = 25.0) -> Dict[str, float]:
    """Compute osmotic pressure (bar) and ideal minimum separation energy (kWh/m^3) for NaCl seawater."""
    if salinity_g_per_l < 0:
        raise ValueError("Salinity must be non-negative.")
    # NaCl molar mass ~58.44 g/mol, van 't Hoff factor i ~ 2
    molarity_mol_m3 = (salinity_g_per_l / 58.44) * 1000.0
    temp_k = temp_c + 273.15
    pi_pa = 2.0 * molarity_mol_m3 * R_GAS * temp_k
    pi_bar = pi_pa / 1e5
    min_kwh_m3 = pi_pa / 3.6e6
    return {"osmotic_pressure_bar": round(pi_bar, 2), "ideal_min_kwh_per_m3": round(min_kwh_m3, 3)}


if __name__ == "__main__":
    print("Seawater (35 g/L, 25 C):", osmotic_min_energy(35.0, 25.0))
