#!/usr/bin/env python3
"""
Educational Radioactive Decay & Half-Life Calculator (Pure Python)
Module: 020_NUCLEAR_SCIENCE | EVERYTHING FUTURE (v2.0.0)
"""

import math
from typing import Dict


def decay_remaining(initial_atoms: float, half_life_s: float, elapsed_s: float) -> Dict[str, float]:
    """Compute remaining nuclei and decay constant lambda = ln(2) / t_half."""
    if initial_atoms < 0 or half_life_s <= 0 or elapsed_s < 0:
        raise ValueError("Invalid decay parameters.")
    lam = math.log(2.0) / half_life_s
    remaining = initial_atoms * math.exp(-lam * elapsed_s)
    return {
        "decay_constant_s_inv": lam,
        "remaining_atoms": round(remaining, 4),
        "fraction_remaining": round(remaining / initial_atoms, 6) if initial_atoms > 0 else 0.0,
    }


if __name__ == "__main__":
    print("After 3 Half-Lives:", decay_remaining(1000.0, 10.0, 30.0))
