import unittest
from bioinformatics_seq import analyze_dna


class TestBioinformaticsSeq(unittest.TestCase):
    def test_valid_sequence(self):
        r = analyze_dna("ATGGCTAAATAA")
        self.assertEqual(r["length"], 12)
        self.assertEqual(r["translation"], "MAK*")
        self.assertEqual(r["reverse_complement"], "TTATTTAGCCAT")

    def test_invalid_base(self):
        with self.assertRaises(ValueError):
            analyze_dna("ATGZ")


if __name__ == "__main__":
    unittest.main()
