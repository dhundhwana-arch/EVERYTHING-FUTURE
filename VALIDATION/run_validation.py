#!/usr/bin/env python3
"""
EVERYTHING FUTURE (v1.0.0) — Automated Quality Assurance & Validation Suite
Original Creator & Project Owner: DIVYESH BAMBHANIYA

Validates:
1. Empty folders (zero tolerance)
2. Required root & ownership documentation presence
3. CSV schema integrity, required fields & duplicate ID detection
4. YAML metadata integrity & allowed verification status labels
5. File path consistency in MODULE_CATALOG.csv
6. Internal Markdown relative link integrity & external URL format checks
7. Ownership & proprietary license consistency
8. Python syntax compilation across all .py scripts
9. Automated unit test execution across all executable flagship modules
10. Outdated resource detection
"""

import csv
import json
import py_compile
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
VALID_STATUSES = {"VERIFIED", "PARTIALLY_VERIFIED", "UNVERIFIED", "UNDER_RESEARCH", "OUTDATED"}

REQUIRED_FILES = [
    "README.md",
    "MASTER_INDEX.md",
    "MODULE_CATALOG.csv",
    "RESOURCE_DATABASE.csv",
    "RESEARCH_TRACKER.md",
    "GLOBAL_TECHNOLOGY_TIMELINE.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "SECURITY.md",
    "OWNERSHIP/COPYRIGHT.md",
    "OWNERSHIP/LICENSE.md",
    "OWNERSHIP/PERMISSION_POLICY.md",
    "OWNERSHIP/ATTRIBUTION_POLICY.md",
    "OWNERSHIP/OWNER_METADATA.yaml",
    "DOCUMENTATION/ARCHITECTURE.md",
    "DOCUMENTATION/TAXONOMY_SPEC.md",
    "DOCUMENTATION/LEARNING_LEVELS_GUIDE.md",
    "DOCUMENTATION/QUALITY_AND_VERIFICATION_STANDARD.md",
    "DOCUMENTATION/RESUMABLE_MISSION_ROADMAP.md",
    "INDUSTRY_DATABASE/GLOBAL_INDUSTRY_DIRECTORY.csv",
    "RESEARCH_INTELLIGENCE/RESEARCH_PAPERS_DATABASE.csv",
    "RESEARCH_INTELLIGENCE/RESEARCH_GAPS_DATABASE.csv",
    "RESEARCH_INTELLIGENCE/BENCHMARK_DIRECTORY.csv",
]


def check_empty_folders(errors: list) -> int:
    count = 0
    for d in sorted(ROOT.rglob("*")):
        if d.is_dir() and "__pycache__" not in d.parts and ".git" not in d.parts:
            count += 1
            if not any(d.iterdir()):
                errors.append(f"EMPTY_FOLDER: {d.relative_to(ROOT)}")
    return count


def check_required_files(errors: list) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"MISSING_REQUIRED_FILE: {rel}")


def check_csv_integrity(errors: list, warnings: list) -> dict:
    stats = {}
    csv_files = sorted(ROOT.rglob("*.csv"))
    for cf in csv_files:
        rel = str(cf.relative_to(ROOT))
        with cf.open("r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
        if len(reader) < 2:
            errors.append(f"EMPTY_OR_HEADER_ONLY_CSV: {rel}")
            continue
        header = reader[0]
        seen_ids = set()
        for row_idx, row in enumerate(reader[1:], start=2):
            if len(row) != len(header):
                errors.append(f"CSV_COLUMN_MISMATCH: {rel}:{row_idx} expected {len(header)}, got {len(row)}")
                continue
            row_id = row[0].strip()
            if not row_id:
                errors.append(f"CSV_EMPTY_ID: {rel}:{row_idx}")
            elif row_id in seen_ids:
                errors.append(f"CSV_DUPLICATE_ID: {rel}:{row_idx} ({row_id})")
            else:
                seen_ids.add(row_id)
            for col_name, val in zip(header, row):
                if "url" in col_name.lower() or "website" in col_name.lower():
                    parsed = urlparse(val.strip())
                    if parsed.scheme not in ("http", "https") or not parsed.netloc:
                        errors.append(f"INVALID_URL: {rel}:{row_idx} -> {val}")
                if col_name == "verification_status":
                    st = val.strip()
                    if st not in VALID_STATUSES:
                        errors.append(f"INVALID_STATUS: {rel}:{row_idx} -> {st}")
                    elif st == "OUTDATED":
                        warnings.append(f"OUTDATED_ENTRY: {rel}:{row_idx} ({row_id})")
        stats[rel] = len(reader) - 1
    return stats


def check_module_catalog_and_metadata(errors: list) -> dict:
    built = 0
    roadmap = 0
    with (ROOT / "MODULE_CATALOG.csv").open("r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            p = row["path"].strip()
            if p.startswith("MODULES/"):
                built += 1
                mod_dir = ROOT / p
                if not mod_dir.is_dir():
                    errors.append(f"MISSING_MODULE_DIR: {p}")
                    continue
                meta_file = mod_dir / "METADATA.yaml"
                if not meta_file.is_file():
                    errors.append(f"MISSING_METADATA_YAML: {p}")
                else:
                    txt = meta_file.read_text(encoding="utf-8")
                    for req_key in ["module_id:", "name:", "verification_status:", "last_verified:", "owner:"]:
                        if req_key not in txt:
                            errors.append(f"INVALID_METADATA_YAML: {p} missing {req_key}")
                    if "DIVYESH BAMBHANIYA" not in txt:
                        errors.append(f"OWNERSHIP_MISSING_IN_METADATA: {p}")
                if not (mod_dir / "README.md").is_file():
                    errors.append(f"MISSING_MODULE_README: {p}")
            else:
                roadmap += 1
    return {"built_modules": built, "roadmap_modules": roadmap}


def check_markdown_links(errors: list) -> int:
    md_files = sorted(ROOT.rglob("*.md"))
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    checked = 0
    for mf in md_files:
        txt = mf.read_text(encoding="utf-8")
        for match in link_re.finditer(txt):
            target = match.group(1).strip()
            if not target or target.startswith("#") or target.startswith("mailto:"):
                continue
            checked += 1
            if target.startswith(("http://", "https://")):
                parsed = urlparse(target)
                if not parsed.netloc:
                    errors.append(f"MALFORMED_URL: {mf.relative_to(ROOT)} -> {target}")
            else:
                clean_target = target.split("#")[0]
                resolved = (mf.parent / clean_target).resolve()
                if not resolved.exists():
                    errors.append(f"BROKEN_INTERNAL_LINK: {mf.relative_to(ROOT)} -> {target}")
    return checked


def check_ownership_policy(errors: list) -> None:
    meta = (ROOT / "OWNERSHIP/OWNER_METADATA.yaml").read_text(encoding="utf-8")
    if "DIVYESH BAMBHANIYA" not in meta:
        errors.append("OWNERSHIP_POLICY_ERROR: Owner name missing in OWNER_METADATA.yaml")
    if "written_permission_required: true" not in meta:
        errors.append("OWNERSHIP_POLICY_ERROR: written_permission_required must be true")


def check_python_syntax_and_tests(errors: list) -> dict:
    py_files = [p for p in sorted(ROOT.rglob("*.py")) if "__pycache__" not in p.parts and ".git" not in p.parts]
    for pf in py_files:
        try:
            py_compile.compile(str(pf), doraise=True)
        except py_compile.PyCompileError as e:
            errors.append(f"PYTHON_SYNTAX_ERROR: {pf.relative_to(ROOT)} -> {e}")

    test_files = [p for p in py_files if p.name.startswith("test_")]
    passed_suites = 0
    for tf in test_files:
        proc = subprocess.run(
            [sys.executable, "-m", "unittest", tf.name],
            cwd=str(tf.parent),
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            errors.append(f"UNIT_TEST_FAILED: {tf.relative_to(ROOT)} -> {proc.stderr.strip()}")
        else:
            passed_suites += 1
    return {"python_files_checked": len(py_files), "test_suites_total": len(test_files), "test_suites_passed": passed_suites}


def run_all() -> dict:
    errors = []
    warnings = []
    folder_count = check_empty_folders(errors)
    check_required_files(errors)
    csv_stats = check_csv_integrity(errors, warnings)
    mod_stats = check_module_catalog_and_metadata(errors)
    links_checked = check_markdown_links(errors)
    check_ownership_policy(errors)
    py_stats = check_python_syntax_and_tests(errors)

    total_files = sum(1 for p in ROOT.rglob("*") if p.is_file() and "__pycache__" not in p.parts and ".git" not in p.parts)
    report = {
        "status": "PASSED" if not errors else "FAILED",
        "total_folders": folder_count,
        "total_files": total_files,
        "built_modules": mod_stats["built_modules"],
        "roadmap_modules": mod_stats["roadmap_modules"],
        "csv_files_validated": len(csv_stats),
        "links_checked": links_checked,
        "python_files_checked": py_stats["python_files_checked"],
        "test_suites_passed": py_stats["test_suites_passed"],
        "test_suites_total": py_stats["test_suites_total"],
        "errors_count": len(errors),
        "warnings_count": len(warnings),
        "errors": errors,
        "warnings": warnings,
    }
    return report


if __name__ == "__main__":
    result = run_all()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "PASSED" else 1)
