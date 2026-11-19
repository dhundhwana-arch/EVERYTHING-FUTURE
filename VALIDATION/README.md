# EVERYTHING FUTURE — Automated Validation Suite

**Dependencies:** Python 3.8+ Standard Library only (offline-safe).

## Run Validation
```bash
python3 VALIDATION/run_validation.py
```

## Checks Performed
1. Zero empty folders across the entire repository.
2. Required governance, documentation, and ownership files present.
3. CSV schema integrity, duplicate ID checks, URL format validation, and status-label validation (`VERIFIED`, `PARTIALLY_VERIFIED`, `UNVERIFIED`, `UNDER_RESEARCH`, `OUTDATED`).
4. YAML metadata integrity and owner attribution across all 70 built modules.
5. Internal relative Markdown link resolution across all `.md` files.
6. Python syntax compilation (`py_compile`) across every `.py` file.
7. Full automated `unittest` execution across all 16 Flagship Deep Module test suites.
