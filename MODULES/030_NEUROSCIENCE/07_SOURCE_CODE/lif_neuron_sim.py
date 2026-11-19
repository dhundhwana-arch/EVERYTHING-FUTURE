#!/usr/bin/env python3
"""
Leaky Integrate-and-Fire (LIF) Computational Neuron Simulator (Pure Python)
Module: 030_NEUROSCIENCE | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict


def simulate_lif(
    input_current_na: float,
    duration_ms: float = 100.0,
    dt_ms: float = 0.5,
    r_mohm: float = 10.0,
    tau_ms: float = 10.0,
    v_rest_mv: float = -65.0,
    v_thresh_mv: float = -50.0,
) -> Dict[str, float]:
    """Simulate a single LIF neuron and return spike count and firing rate (Hz)."""
    v = v_rest_mv
    spikes = 0
    steps = int(duration_ms / dt_ms)
    for _ in range(steps):
        dv = (-(v - v_rest_mv) + r_mohm * input_current_na) * (dt_ms / tau_ms)
        v += dv
        if v >= v_thresh_mv:
            spikes += 1
            v = v_rest_mv
    rate_hz = spikes / (duration_ms / 1000.0)
    return {"spikes": float(spikes), "firing_rate_hz": round(rate_hz, 2)}


if __name__ == "__main__":
    print("LIF Neuron (I=2.5 nA, 100ms):", simulate_lif(2.5, 100.0))
