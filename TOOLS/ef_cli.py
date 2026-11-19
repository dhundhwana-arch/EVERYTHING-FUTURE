#!/usr/bin/env python3
"""
EVERYTHING FUTURE — Offline CLI Navigator & Standalone Module Packager
Original Creator & Project Owner: DIVYESH BAMBHANIYA
Dependencies: Python 3.8+ Standard Library only.
"""

import argparse
import csv
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_csv(rel_path: str):
    with (ROOT / rel_path).open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cmd_search(query: str) -> None:
    q = query.lower()
    print(f"=== Search Results for '{query}' ===")
    mods = [
        m for m in load_csv("MODULE_CATALOG.csv")
        if q in m["module_name"].lower() or q in m["module_id"]
    ]
    print(f"\nModules ({len(mods)}):")
    for m in mods[:20]:
        print(f"  [{m['module_id']}] {m['module_name']} ({m['tier']} | {m['verification_status']}) -> {m['path']}")

    res = [
        r for r in load_csv("RESOURCE_DATABASE.csv")
        if q in r["organization_name"].lower() or q in r["description"].lower()
    ]
    print(f"\nGlobal Resources ({len(res)}):")
    for r in res[:15]:
        print(f"  [{r['resource_id']}] {r['organization_name']} ({r['country_or_region']}) -> {r['official_url']}")

    papers = [
        p for p in load_csv("RESEARCH_INTELLIGENCE/RESEARCH_PAPERS_DATABASE.csv")
        if q in p["title"].lower() or q in p["key_contribution"].lower()
    ]
    print(f"\nVerified Papers ({len(papers)}):")
    for p in papers:
        print(f"  [{p['paper_id']}] {p['title']} ({p['year']}) | DOI: {p['doi']}")


def cmd_list(tier: str = None, status: str = None) -> None:
    rows = load_csv("MODULE_CATALOG.csv")
    for m in rows:
        if tier and m["tier"].lower() != f"tier {tier}".lower():
            continue
        if status and m["verification_status"].upper() != status.upper():
            continue
        print(
            f"[{m['module_id']}] {m['module_name']} | {m['cluster']} | "
            f"{m['tier']} | {m['verification_status']} | code={m['has_executable_code']}"
        )


def cmd_pack(module_id: str, output_zip: str) -> None:
    rows = [m for m in load_csv("MODULE_CATALOG.csv") if m["module_id"] == module_id.zfill(3)]
    if not rows or not rows[0]["path"].startswith("MODULES/"):
        print(f"Module {module_id} is not built locally yet (check MODULE_CATALOG.csv).", file=sys.stderr)
        sys.exit(1)
    mod_dir = ROOT / rows[0]["path"]
    out_path = Path(output_zip)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(mod_dir.rglob("*")):
            if file_path.is_file():
                zf.write(file_path, file_path.relative_to(ROOT))
        for own_file in sorted((ROOT / "OWNERSHIP").rglob("*")):
            if own_file.is_file():
                zf.write(own_file, own_file.relative_to(ROOT))
    print(f"Created standalone module package: {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="EVERYTHING FUTURE Offline CLI Navigator")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Search modules, resources, and verified papers")
    p_search.add_argument("query", help="Keyword to search")

    p_list = sub.add_parser("list", help="List modules by tier or status")
    p_list.add_argument("--tier", help="Filter by tier number (1, 2, or 3)")
    p_list.add_argument("--status", help="Filter by verification status")

    p_pack = sub.add_parser("pack", help="Export a single built module as a standalone ZIP")
    p_pack.add_argument("module_id", help="3-digit module ID (e.g. 009)")
    p_pack.add_argument("--out", default="module_pack.zip", help="Output ZIP path")

    args = parser.parse_args()
    if args.command == "search":
        cmd_search(args.query)
    elif args.command == "list":
        cmd_list(tier=args.tier, status=args.status)
    elif args.command == "pack":
        cmd_pack(args.module_id, args.out)


if __name__ == "__main__":
    main()
