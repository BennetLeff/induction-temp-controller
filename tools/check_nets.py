#!/usr/bin/env python3
"""Verify that critical nets exist in the KiCad netlist."""

from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from pathlib import Path


EXPECTED_NETS = (
    "SPI_SCK",
    "SPI_MISO",
    "SPI_MOSI",
    "SPI_CS",
    "I2C_SDA",
    "I2C_SCL",
    "SSR_CTRL",
    "AC_HOT",
    "AC_NEUTRAL",
    "AC_GND",
)


NET_RE = re.compile(r'\(net\s+\(code\s+"?\d+"?\)\s+\(name\s+"([^"]+)"')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schematic", type=Path, help=".kicad_sch file to inspect")
    parser.add_argument(
        "--expected",
        nargs="*",
        default=EXPECTED_NETS,
        help="Override the list of required net names",
    )
    return parser.parse_args()


def export_netlist(path: Path) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".kicad_net") as tmp:
        out_path = Path(tmp.name)
    try:
        subprocess.run(
            [
                "kicad-cli",
                "sch",
                "export",
                "netlist",
                str(path),
                "--format",
                "kicadsexpr",
                "--output",
                str(out_path),
            ],
            check=True,
            capture_output=True,
        )
        return out_path.read_text(encoding="utf-8")
    finally:
        out_path.unlink(missing_ok=True)


def extract_nets(netlist_text: str) -> set[str]:
    raw = {match.group(1) for match in NET_RE.finditer(netlist_text)}
    normalized = set()
    for name in raw:
        normalized.add(name)
        if name.startswith("/"):
            normalized.add(name[1:])
    return normalized


def main() -> int:
    args = parse_args()
    netlist = export_netlist(args.schematic)
    nets = extract_nets(netlist)

    missing = [net for net in args.expected if net not in nets]

    if missing:
        print("[ERROR] Expected nets not found:")
        for net in missing:
            print(f"  - {net}")
        return 1

    print("✅ All expected nets present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())