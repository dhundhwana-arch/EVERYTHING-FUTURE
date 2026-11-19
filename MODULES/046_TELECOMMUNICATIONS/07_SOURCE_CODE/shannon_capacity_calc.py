#!/usr/bin/env python3
"""
Shannon-Hartley Channel Capacity & Spectral Efficiency Calculator (Pure Python)
Module: 046_TELECOMMUNICATIONS | EVERYTHING FUTURE (v2.0.0)
"""

import math
from typing import Dict


def shannon_capacity(bandwidth_mhz: float, snr_db: float) -> Dict[str, float]:
    """Compute theoretical error-free capacity (Mbps) and spectral efficiency (bps/Hz)."""
    if bandwidth_mhz <= 0:
        raise ValueError("Bandwidth must be positive.")
    snr_linear = 10.0 ** (snr_db / 10.0)
    spec_eff = math.log2(1.0 + snr_linear)
    cap_mbps = bandwidth_mhz * spec_eff
    return {"spectral_efficiency_bps_hz": round(spec_eff, 4), "capacity_mbps": round(cap_mbps, 2)}


if __name__ == "__main__":
    print("100 MHz 5G Channel at 20 dB SNR:", shannon_capacity(100.0, 20.0))
