# EVERYTHING FUTURE — Offline CLI Tools

**Dependencies:** Python 3.8+ Standard Library only (works offline on Linux, macOS, Windows, and Android Termux).

## Usage Examples
```bash
# Search any keyword across modules, verified resources, and paper DOIs
python3 TOOLS/ef_cli.py search "quantum"

# List all Tier-1 Flagship Deep Modules
python3 TOOLS/ef_cli.py list --tier 1

# Export Module 009 (Semiconductor Design) as a standalone ZIP with OWNERSHIP policy
python3 TOOLS/ef_cli.py pack 009 --out semiconductor_design_module.zip
```
