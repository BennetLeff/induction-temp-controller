#!/usr/bin/env python3
"""Validate rough placement rules for the generated schematic."""

from __future__ import annotations

import argparse
from pathlib import Path


DC_REFS = {"J1", "C1", "U1", "DISP1", "SW1", "U2", "J2"}
ISOLATION_REFS = {"R1", "SSR1"}
AC_REFS = {"J3", "F1", "J4"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schematic", type=Path)
    return parser.parse_args()


def iter_symbol_positions(text: str) -> dict[str, tuple[float, float]]:
    data: dict[str, tuple[float, float]] = {}
    needle = "(symbol (lib_id"
    idx = 0
    while True:
        start = text.find(needle, idx)
        if start == -1:
            break
        depth = 0
        end = start
        for pos in range(start, len(text)):
            char = text[pos]
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    end = pos + 1
                    break
        block = text[start:end]
        ref_tag = 'property "Reference" "'
        ref_start = block.find(ref_tag)
        if ref_start == -1:
            idx = end
            continue
        ref_start += len(ref_tag)
        ref_end = block.find('"', ref_start)
        reference = block[ref_start:ref_end]
        at_tag = "(symbol (lib_id"
        at_idx = block.find("(at", len(at_tag))
        coords = block[at_idx:].split()
        try:
            x = float(coords[1])
            y = float(coords[2])
        except (ValueError, IndexError):
            idx = end
            continue
        data[reference] = (x, y)
        idx = end
    return data


def on_grid(value: float, pitch: float = 2.54) -> bool:
    remainder = abs(value) % pitch
    return remainder < 1e-3 or abs(remainder - pitch) < 1e-3


def check_blocks(locations: dict[str, tuple[float, float]]) -> list[str]:
    errors: list[str] = []
    for ref in DC_REFS & locations.keys():
        x, _ = locations[ref]
        if x > 165:
            errors.append(f"{ref} expected on DC side (x<=165) but is at {x}")
    for ref in ISOLATION_REFS & locations.keys():
        x, _ = locations[ref]
        if not (170 <= x <= 230):
            errors.append(f"{ref} expected near isolation barrier but is at {x}")
    for ref in AC_REFS & locations.keys():
        x, _ = locations[ref]
        if x < 260:
            errors.append(f"{ref} expected on AC side (x>=260) but is at {x}")
    for ref, (x, y) in locations.items():
        if ref.startswith("#"):
            continue
        if not (on_grid(x) and on_grid(y)):
            errors.append(f"{ref} not on 2.54 mm grid ({x}, {y})")
    return errors


def main() -> int:
    args = parse_args()
    text = args.schematic.read_text(encoding="utf-8")
    locations = iter_symbol_positions(text)
    issues = check_blocks(locations)
    if issues:
        print("[ERROR] Layout issues detected:")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print("✅ Placement rules satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())