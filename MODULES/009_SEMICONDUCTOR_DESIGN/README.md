# Module 009: Semiconductor Design

**Cluster:** C03 | **Tier:** 1 | **Status:** `VERIFIED` | **Last Verified:** 2026-11-19  
**Original Creator & Project Owner:** DIVYESH BAMBHANIYA

## Overview
Integrated circuit architecture, CMOS physics, RTL design, EDA verification, and open ISA ecosystems (RISC-V).

## Three-Level Learning Pathway
- **LEVEL 1 (Beginner):** Start with [`01_FUNDAMENTALS/GLOSSARY.md`](01_FUNDAMENTALS/GLOSSARY.md) to master core vocabulary and conceptual intuition.
- **LEVEL 2 (Intermediate):** Review engineering frameworks, verified institutions (`13_INDUSTRY_DATABASE/ORGANIZATIONS.csv`), and executable simulations (where provided in `07_SOURCE_CODE/`).
- **LEVEL 3 (Advanced Research):** Examine primary references (`11_RESEARCH_PAPERS/KEY_REFERENCES.md`), open bottlenecks (`19_RESEARCH_GAPS/OPEN_PROBLEMS.md`), and adapt `RESEARCH_INTELLIGENCE/TEMPLATES/` for reproducible inquiry.

## Executable Engineering Module (`07_SOURCE_CODE/`)
- **Script:** [`07_SOURCE_CODE/cmos_power_delay.py`](07_SOURCE_CODE/cmos_power_delay.py)
- **Dependencies:** Python 3.8+ Standard Library only (zero external packages required).
- **Run & Test:**
  ```bash
  python3 07_SOURCE_CODE/cmos_power_delay.py
  python3 -m unittest discover -s 07_SOURCE_CODE -p "test_*.py"
  ```

## Scientific Research Intelligence (8-Point Synthesis)
1. **What Is Currently Known:** CMOS scaling physics, RTL-to-GDSII EDA flows, and modular SoC verification are mature industrial disciplines.
2. **What Has Already Been Achieved:** Multi-billion-transistor SoCs, open royalty-free RISC-V ecosystems, and nanosheet gate-all-around (GAA) transistor designs.
3. **What Remains Unsolved:** Overcoming the end of Dennard scaling, interconnect RC bottleneck, and rising verification complexity.
4. **Major Limitations:** Multi-million-dollar mask/NRE costs at leading nodes and dark-silicon thermal density limits.
5. **Promising Research Directions:** Open-source RISC-V silicon, AI-assisted place-and-route, backside power delivery, and 2D channel transistors.
6. **Resources Needed:** Open RISC-V specifications, open-source RTL simulators, and EDA verification tools.
7. **Safe Conductable Experiments:** Calculate CMOS dynamic power, RC delay, and frequency scaling tradeoffs across supply voltages.
8. **Active Institutions & Ecosystems:** RISC-V International, Synopsys, IMEC, TSMC, NVIDIA

## Verified Primary References
- [RISC-V International](https://riscv.org/)
- [Synopsys RISC-V Solutions](https://www.synopsys.com/solutions/risc-v.html)
- [IMEC](https://www.imec-int.com/en)
