#!/usr/bin/env python3
"""
Economic Order Quantity (EOQ) & Stochastic Safety Stock Calculator
Module: 050_INTERNATIONAL_SUPPLY_CHAINS | EVERYTHING FUTURE (v2.0.0)
"""

import math
from typing import Dict


def inventory_policy(
    annual_demand: float,
    order_cost: float,
    holding_cost_per_unit: float,
    daily_demand_std: float,
    lead_time_days: float,
    z_service: float = 1.645,
) -> Dict[str, float]:
    """Compute EOQ, safety stock, and reorder point for a 95% (z=1.645) service level."""
    if annual_demand <= 0 or order_cost <= 0 or holding_cost_per_unit <= 0 or lead_time_days < 0:
        raise ValueError("Invalid inventory parameters.")
    eoq = math.sqrt((2.0 * annual_demand * order_cost) / holding_cost_per_unit)
    safety_stock = z_service * daily_demand_std * math.sqrt(lead_time_days)
    reorder_pt = (annual_demand / 365.0) * lead_time_days + safety_stock
    return {
        "eoq_units": round(eoq, 1),
        "safety_stock_units": round(safety_stock, 1),
        "reorder_point_units": round(reorder_pt, 1),
    }


if __name__ == "__main__":
    print("Supply Chain Policy:", inventory_policy(10000.0, 250.0, 5.0, 8.0, 14.0))
