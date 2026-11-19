#!/usr/bin/env python3
"""
4th-Order Runge-Kutta (RK4) Numerical ODE Solver (Pure Python)
Module: 053_MATHEMATICAL_SCIENCES | EVERYTHING FUTURE (v1.0.0)
"""

import math
from typing import Callable, List, Tuple


def rk4_integrate(
    f: Callable[[float, float], float],
    t0: float,
    y0: float,
    t_end: float,
    steps: int,
) -> List[Tuple[float, float]]:
    """Integrate dy/dt = f(t, y) from t0 to t_end using classic 4th-order Runge-Kutta."""
    if steps <= 0:
        raise ValueError("steps must be positive.")
    h = (t_end - t0) / steps
    t, y = t0, y0
    traj = [(t, y)]
    for _ in range(steps):
        k1 = f(t, y)
        k2 = f(t + 0.5 * h, y + 0.5 * h * k1)
        k3 = f(t + 0.5 * h, y + 0.5 * h * k2)
        k4 = f(t + h, y + h * k3)
        y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        t = t + h
        traj.append((t, y))
    return traj


if __name__ == "__main__":
    # dy/dt = -y, y(0) = 1 => exact y(1) = e^-1
    res = rk4_integrate(lambda t, y: -y, 0.0, 1.0, 1.0, 100)
    print(f"RK4 y(1) = {res[-1][1]:.8f} | Exact = {math.exp(-1.0):.8f}")
