#!/usr/bin/env python3
"""
Deterministic BB84 Quantum Key Distribution Basis Reconciliation & QBER Simulator
Module: 014_QUANTUM_COMMUNICATION | EVERYTHING FUTURE (v2.0.0)
"""

from typing import List, Dict


def bb84_sift_and_qber(
    alice_bits: List[int],
    alice_bases: List[str],
    bob_bases: List[str],
    bob_measured: List[int],
) -> Dict[str, float]:
    """Perform BB84 basis sifting and compute Quantum Bit Error Rate (QBER)."""
    n = len(alice_bits)
    if not (len(alice_bases) == len(bob_bases) == len(bob_measured) == n) or n == 0:
        raise ValueError("All BB84 input lists must be non-empty and equal length.")
    sifted_a, sifted_b = [], []
    for ab, abas, bbas, bm in zip(alice_bits, alice_bases, bob_bases, bob_measured):
        if abas == bbas:
            sifted_a.append(ab)
            sifted_b.append(bm)
    if not sifted_a:
        return {"sifted_len": 0.0, "qber_pct": 0.0, "eavesdropper_alert": 0.0}
    errors = sum(1 for a, b in zip(sifted_a, sifted_b) if a != b)
    qber = 100.0 * errors / len(sifted_a)
    return {
        "sifted_len": float(len(sifted_a)),
        "qber_pct": round(qber, 2),
        "eavesdropper_alert": 1.0 if qber > 11.0 else 0.0,
    }


if __name__ == "__main__":
    print("Clean Channel:", bb84_sift_and_qber([0, 1, 1, 0], ["+", "x", "+", "x"], ["+", "+", "+", "x"], [0, 0, 1, 0]))
