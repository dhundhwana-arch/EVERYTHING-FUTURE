#!/usr/bin/env python3
"""
Safe Computational DNA Sequence Utility (GC-Content, Reverse Complement, Translation)
Module: 029_BIOTECHNOLOGY | EVERYTHING FUTURE (v1.0.0)
"""

from typing import Dict

COMP = {"A": "T", "T": "A", "G": "C", "C": "G"}
CODON_TABLE = {
    "ATG": "M", "GCT": "A", "GCC": "A", "GGA": "G", "GGT": "G",
    "AAA": "K", "AAG": "K", "TAA": "*", "TAG": "*", "TGA": "*",
}


def analyze_dna(seq: str) -> Dict[str, object]:
    """Compute length, GC%, reverse complement, and basic codon translation for a DNA string."""
    s = seq.strip().upper()
    if not s or any(ch not in COMP for ch in s):
        raise ValueError("Sequence must be non-empty and contain only A, T, G, C.")
    gc_pct = 100.0 * sum(1 for ch in s if ch in ("G", "C")) / len(s)
    rev_comp = "".join(COMP[ch] for ch in reversed(s))
    aa = "".join(CODON_TABLE.get(s[i:i+3], "X") for i in range(0, len(s) - 2, 3))
    return {"length": len(s), "gc_percent": round(gc_pct, 2), "reverse_complement": rev_comp, "translation": aa}


if __name__ == "__main__":
    print("Sequence Analysis:", analyze_dna("ATGGCTAAATAA"))
