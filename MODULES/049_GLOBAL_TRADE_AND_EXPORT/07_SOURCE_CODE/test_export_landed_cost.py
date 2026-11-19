import unittest
from export_landed_cost import compute_landed_cost


class TestExportLandedCost(unittest.TestCase):
    def test_cif_and_taxes(self):
        r = compute_landed_cost(10000.0, 800.0, 200.0, 10.0, 18.0, port_handling_usd=100.0)
        self.assertEqual(r["cif_value_usd"], 11000.0)
        self.assertEqual(r["customs_duty_usd"], 1100.0)
        self.assertEqual(r["igst_vat_usd"], 2178.0)
        self.assertEqual(r["total_landed_cost_usd"], 14378.0)


if __name__ == "__main__":
    unittest.main()
