#!/usr/bin/env python3
"""
2D Projectile Trajectory Simulator: Ideal Vacuum vs Quadratic Air Drag
Module: 054_PHYSICS | EVERYTHING FUTURE (v2.0.0)
"""

import math
from typing import Dict

G0 = 9.80665


def simulate_range(v0_m_s: float, angle_deg: float, drag_k_per_m: float = 0.005, dt: float = 0.005) -> Dict[str, float]:
    """Compare analytical vacuum range with numerical Euler-Cromer quadratic drag range."""
    if v0_m_s <= 0 or not (0.0 < angle_deg < 90.0):
        raise ValueError("Require v0 > 0 and 0 < angle_deg < 90.")
    rad = math.radians(angle_deg)
    vacuum_range = (v0_m_s ** 2) * math.sin(2.0 * rad) / G0
    x, y = 0.0, 0.0
    vx, vy = v0_m_s * math.cos(rad), v0_m_s * math.sin(rad)
    while y >= 0.0:
        speed = math.hypot(vx, vy)
        ax = -drag_k_per_m * speed * vx
        ay = -G0 - drag_k_per_m * speed * vy
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
    return {"vacuum_range_m": round(vacuum_range, 2), "drag_range_m": round(x, 2)}


if __name__ == "__main__":
    print("45-deg Launch (50 m/s):", simulate_range(50.0, 45.0, drag_k_per_m=0.004))
