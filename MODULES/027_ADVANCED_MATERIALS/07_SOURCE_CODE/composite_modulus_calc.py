#!/usr/bin/env python3
"""
Composite Elastic Modulus Voigt (Upper) & Reuss (Lower) Bounds Calculator
Module: 027_ADVANCED_MATERIALS | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict


def composite_bounds(e_fiber_gpa: float, e_matrix_gpa: float, vol_frac_fiber: float) -> Dict[str, float]:
    """Compute longitudinal (Voigt) and transverse (Reuss) composite elastic moduli (GPa)."""
    if not (0.0 <= vol_frac_fiber <= 1.0) or e_fiber_gpa <= 0 or e_matrix_gpa <= 0:
        raise ValueError("Invalid material parameters.")
    vm = 1.0 - vol_frac_fiber
    e_voigt = vol_frac_fiber * e_fiber_gpa + vm * e_matrix_gpa
    e_reuss = 1.0 / (vol_frac_fiber / e_fiber_gpa + vm / e_matrix_gpa)
    return {"voigt_upper_gpa": round(e_voigt, 3), "reuss_lower_gpa": round(e_reuss, 3)}


if __name__ == "__main__":
    print("Carbon/Epoxy (60% fiber):", composite_bounds(230.0, 3.5, 0.6))
