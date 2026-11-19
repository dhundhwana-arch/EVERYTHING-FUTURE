#!/usr/bin/env python3
"""
FAO-Style Daily Soil-Water Balance & Irrigation Scheduler (Pure Python)
Module: 033_AGRICULTURAL_TECHNOLOGY | EVERYTHING FUTURE (v1.0.0)
"""

from typing import List, Dict


def simulate_irrigation(
    et0_mm_list: List[float],
    rain_mm_list: List[float],
    kc: float = 1.05,
    taw_mm: float = 100.0,
    raw_fraction: float = 0.5,
) -> Dict[str, float]:
    """Simulate daily root-zone soil water deficit and trigger irrigation when deficit > RAW."""
    if len(et0_mm_list) != len(rain_mm_list):
        raise ValueError("ET0 and rainfall lists must match in length.")
    raw_mm = taw_mm * raw_fraction
    deficit = 0.0
    total_irrigation = 0.0
    events = 0
    for et0, rain in zip(et0_mm_list, rain_mm_list):
        etc = et0 * kc
        deficit = max(0.0, deficit + etc - rain)
        if deficit >= raw_mm:
            total_irrigation += deficit
            deficit = 0.0
            events += 1
    return {
        "total_irrigation_mm": round(total_irrigation, 2),
        "irrigation_events": float(events),
        "final_deficit_mm": round(deficit, 2),
    }


if __name__ == "__main__":
    et0 = [5.5] * 14
    rain = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15.0, 0.0, 0.0, 0.0, 0.0]
    print("14-Day Irrigation Schedule:", simulate_irrigation(et0, rain))
