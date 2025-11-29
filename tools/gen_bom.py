#!/usr/bin/env python3
"""Generate a markdown BOM and highlight missing supplier data."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import tempfile
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schematic", type=Path)
    parser.add_argument(
        "--parts",
        type=Path,
        default=Path("tools/bom_parts.json"),
        help="JSON mapping of Value -> supplier data",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("bom/generated_bom.md"),
        help="Output markdown file",
    )
    return parser.parse_args()


def export_bom(schematic: Path) -> Path:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    tmp.close()
    subprocess.run(
        [
            "kicad-cli",
            "sch",
            "export",
            "bom",
            str(schematic),
            "--output",
            tmp.name,
            "--labels",
            "Refs,Value,Footprint,Qty,DNP",
        ],
        check=True,
    )
    return Path(tmp.name)


def parse_bom_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        return [row for row in reader]


def load_parts_map(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_markdown(rows: list[dict[str, str]], parts: dict[str, dict[str, str]], dest: Path) -> list[str]:
    missing = []
    lines = ["| Refs | Value | Footprint | Qty | MPN | Status |", "|------|-------|-----------|-----|-----|--------|"]
    for row in rows:
        value = row.get("Value", "")
        info = parts.get(value)
        if not info:
            missing.append(value)
            mpn = "-"
            status = "missing"
        else:
            mpn = info.get("mpn", "-")
            status = info.get("status", "unknown")
        lines.append(
            f"| {row.get('Refs','')} | {value} | {row.get('Footprint','')} | {row.get('Qty','')} | {mpn} | {status} |"
        )
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return missing


def main() -> int:
    args = parse_args()
    csv_path = export_bom(args.schematic)
    rows = parse_bom_csv(csv_path)
    csv_path.unlink(missing_ok=True)
    parts = load_parts_map(args.parts)
    missing = write_markdown(rows, parts, args.output)
    if missing:
        print("[WARN] Missing supplier data for values:")
        for val in sorted(set(missing)):
            print(f"  - {val}")
    else:
        print("✅ BOM generated with complete supplier info ->", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())