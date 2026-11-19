#!/usr/bin/env python3
"""
Factory Overall Equipment Effectiveness (OEE) & Little's Law Analyzer
Module: 042_INDUSTRIAL_AUTOMATION | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict


def compute_oee_and_wip(
    availability: float,
    performance: float,
    quality: float,
    throughput_per_hr: float,
    lead_time_hr: float,
) -> Dict[str, float]:
    """Compute OEE (%) and steady-state Work-In-Progress (WIP = Throughput * Lead Time)."""
    for val in (availability, performance, quality):
        if not (0.0 <= val <= 1.0):
            raise ValueError("OEE factors must lie in [0, 1].")
    oee = availability * performance * quality
    wip = throughput_per_hr * lead_time_hr
    return {"oee_pct": round(100.0 * oee, 2), "steady_state_wip_units": round(wip, 2)}


if __name__ == "__main__":
    print("Factory Line Metrics:", compute_oee_and_wip(0.90, 0.92, 0.98, 45.0, 2.5))
