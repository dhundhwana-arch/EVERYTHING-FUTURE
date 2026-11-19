#!/usr/bin/env python3
"""
CMOS Dynamic Power, Static Power & RC Elmore Delay Calculator (Pure Python)
Module: 009_SEMICONDUCTOR_DESIGN | EVERYTHING FUTURE (v1.0.0)
"""

from typing import Dict


def cmos_metrics(
    activity_factor: float,
    capacitance_pf: float,
    voltage_v: float,
    freq_ghz: float,
    leakage_current_ma: float = 10.0,
    wire_resistance_ohm: float = 100.0,
) -> Dict[str, float]:
    """Calculate CMOS dynamic power (W), static power (W), and RC delay (ps)."""
    if voltage_v <= 0 or freq_ghz <= 0 or capacitance_pf <= 0:
        raise ValueError("Voltage, frequency, and capacitance must be positive.")
    c_farads = capacitance_pf * 1e-12
    f_hz = freq_ghz * 1e9
    p_dyn = activity_factor * c_farads * (voltage_v ** 2) * f_hz
    p_stat = voltage_v * (leakage_current_ma * 1e-3)
    rc_delay_ps = wire_resistance_ohm * c_farads * 1e12
    return {
        "dynamic_power_w": round(p_dyn, 6),
        "static_power_w": round(p_stat, 6),
        "total_power_w": round(p_dyn + p_stat, 6),
        "rc_delay_ps": round(rc_delay_ps, 4),
    }


if __name__ == "__main__":
    print("CMOS Metrics:", cmos_metrics(0.2, 5000.0, 0.75, 3.0, leakage_current_ma=25.0))
