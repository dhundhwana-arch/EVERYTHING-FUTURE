#!/usr/bin/env python3
"""
Pure-Python 2-Qubit State-Vector Quantum Simulator (Hadamard, Pauli-X, CNOT -> Bell State)
Module: 013_QUANTUM_COMPUTING | EVERYTHING FUTURE (v1.0.0)
"""

import cmath
import math
from typing import List, Dict


def apply_single_qubit_gate(state: List[complex], gate: List[List[complex]], target: int) -> List[complex]:
    """Apply a 2x2 unitary gate to qubit 0 (MSB) or qubit 1 (LSB) of a 2-qubit state vector."""
    out = [0j] * 4
    for i in range(4):
        bit = (i >> (1 - target)) & 1
        partner = i ^ (1 << (1 - target))
        if bit == 0:
            out[i] = gate[0][0] * state[i] + gate[0][1] * state[partner]
            out[partner] = gate[1][0] * state[i] + gate[1][1] * state[partner]
    return out


def apply_cnot_0_to_1(state: List[complex]) -> List[complex]:
    """Apply CNOT with control=qubit 0 and target=qubit 1."""
    return [state[0], state[1], state[3], state[2]]


def bell_state_probabilities() -> Dict[str, float]:
    """Prepare |Phi+> = (|00> + |11>) / sqrt(2) and return basis measurement probabilities."""
    inv_s2 = 1.0 / math.sqrt(2.0)
    H = [[inv_s2, inv_s2], [inv_s2, -inv_s2]]
    state = [1.0 + 0j, 0j, 0j, 0j]  # |00>
    state = apply_single_qubit_gate(state, H, target=0)
    state = apply_cnot_0_to_1(state)
    labels = ["00", "01", "10", "11"]
    return {lbl: round(abs(amp) ** 2, 6) for lbl, amp in zip(labels, state)}


if __name__ == "__main__":
    print("Bell State |Phi+> Probabilities:", bell_state_probabilities())
