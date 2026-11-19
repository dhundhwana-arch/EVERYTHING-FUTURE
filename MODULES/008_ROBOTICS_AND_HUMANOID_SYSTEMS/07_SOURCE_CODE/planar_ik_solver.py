#!/usr/bin/env python3
"""
2-Link Planar Robotic Arm Forward & Inverse Kinematics Solver (Pure Python)
Module: 008_ROBOTICS_AND_HUMANOID_SYSTEMS | EVERYTHING FUTURE (v1.0.0)
"""

import math
from typing import Tuple


def forward_kinematics(l1: float, l2: float, theta1_rad: float, theta2_rad: float) -> Tuple[float, float]:
    """Return end-effector (x, y) given link lengths and joint angles in radians."""
    x = l1 * math.cos(theta1_rad) + l2 * math.cos(theta1_rad + theta2_rad)
    y = l1 * math.sin(theta1_rad) + l2 * math.sin(theta1_rad + theta2_rad)
    return x, y


def inverse_kinematics(l1: float, l2: float, x: float, y: float, elbow_up: bool = False) -> Tuple[float, float]:
    """Analytical 2-DOF inverse kinematics returning (theta1_rad, theta2_rad)."""
    r_sq = x * x + y * y
    r = math.sqrt(r_sq)
    if r > (l1 + l2) + 1e-9 or r < abs(l1 - l2) - 1e-9:
        raise ValueError("Target (x, y) lies outside the manipulator reachable workspace.")
    cos_t2 = max(-1.0, min(1.0, (r_sq - l1 * l1 - l2 * l2) / (2.0 * l1 * l2)))
    sin_t2 = math.sqrt(max(0.0, 1.0 - cos_t2 * cos_t2))
    if elbow_up:
        sin_t2 = -sin_t2
    theta2 = math.atan2(sin_t2, cos_t2)
    theta1 = math.atan2(y, x) - math.atan2(l2 * math.sin(theta2), l1 + l2 * math.cos(theta2))
    return theta1, theta2


if __name__ == "__main__":
    t1, t2 = inverse_kinematics(1.0, 1.0, 1.0, 1.0)
    x, y = forward_kinematics(1.0, 1.0, t1, t2)
    print(f"IK Angles (deg): ({math.degrees(t1):.2f}, {math.degrees(t2):.2f}) -> FK: ({x:.4f}, {y:.4f})")
