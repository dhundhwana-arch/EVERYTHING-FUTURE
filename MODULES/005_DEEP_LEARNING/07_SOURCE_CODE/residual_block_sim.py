#!/usr/bin/env python3
"""
Residual Skip-Connection vs Plain Deep Chain Gradient Flow Simulator (Pure Python)
Module: 005_DEEP_LEARNING | EVERYTHING FUTURE (v2.0.0)
"""

from typing import Dict


def compare_gradient_flow(depth: int, layer_gain: float = 0.8) -> Dict[str, float]:
    """Compare scalar backprop gradient magnitude through plain vs residual (1 + gain) chains."""
    if depth <= 0:
        raise ValueError("depth must be positive.")
    plain_grad = layer_gain ** depth
    residual_grad = (1.0 + layer_gain * 0.1) ** depth
    return {
        "depth": float(depth),
        "plain_chain_grad": round(plain_grad, 8),
        "residual_chain_grad": round(residual_grad, 6),
        "vanished_plain": 1.0 if plain_grad < 1e-4 else 0.0,
    }


if __name__ == "__main__":
    print("Depth-50 Gradient Flow:", compare_gradient_flow(50, 0.8))
