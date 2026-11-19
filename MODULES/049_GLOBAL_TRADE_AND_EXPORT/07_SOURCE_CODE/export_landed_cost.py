#!/usr/bin/env python3
"""
International Trade CIF/FOB Landed Import Cost Calculator (Pure Python)
Module: 049_GLOBAL_TRADE_AND_EXPORT | EVERYTHING FUTURE (v1.0.0)
"""

from typing import Dict


def compute_landed_cost(
    fob_value_usd: float,
    freight_usd: float,
    insurance_usd: float,
    basic_customs_duty_pct: float,
    igst_or_vat_pct: float,
    port_handling_usd: float = 150.0,
) -> Dict[str, float]:
    """Compute CIF value, customs duty, IGST/VAT on (CIF + Duty), and total landed cost."""
    if fob_value_usd < 0 or freight_usd < 0 or insurance_usd < 0:
        raise ValueError("Cost inputs must be non-negative.")
    cif = fob_value_usd + freight_usd + insurance_usd
    duty = cif * (basic_customs_duty_pct / 100.0)
    taxable_val = cif + duty
    vat = taxable_val * (igst_or_vat_pct / 100.0)
    total = cif + duty + vat + port_handling_usd
    return {
        "cif_value_usd": round(cif, 2),
        "customs_duty_usd": round(duty, 2),
        "igst_vat_usd": round(vat, 2),
        "total_landed_cost_usd": round(total, 2),
    }


if __name__ == "__main__":
    print("Sample Export/Import Landed Cost:", compute_landed_cost(10000.0, 800.0, 100.0, 10.0, 18.0))
