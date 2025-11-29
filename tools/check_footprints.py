#!/usr/bin/env python3
"""Lint footprints referenced inside a KiCad schematic."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "schematic",
        type=Path,
        help="Path to the .kicad_sch file to inspect",
    )
    parser.add_argument(
        "--footprint-root",
        type=Path,
        default=Path.cwd(),
        help="Root directory containing *.pretty footprint libraries (defaults to CWD)",
    )
    parser.add_argument(
        "--ignore-prefix",
        action="append",
        default=["#PWR", "#FLG"],
        help="Reference prefix to ignore when checking for missing footprints (repeatable)",
    )
    return parser.parse_args()


REF_RE = re.compile(r'\(property "Reference" "([^"]+)"')
FOOTPRINT_RE = re.compile(r'\(property "Footprint" "([^"]*)"')


def iter_symbol_instances(text: str) -> list[tuple[str, str]]:
    """Yield (reference, footprint) tuples for every symbol instance."""

    results: list[tuple[str, str]] = []
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
        ref_match = REF_RE.search(block)
        fp_match = FOOTPRINT_RE.search(block)
        if not ref_match:
            continue
        reference = ref_match.group(1)
        footprint = fp_match.group(1) if fp_match else ""
        results.append((reference, footprint))
        idx = end
    return results


def collect_known_libs(root: Path) -> set[str]:
    libs: set[str] = set()
    for pretty in root.rglob("*.pretty"):
        libs.add(pretty.stem)
    return libs


def main() -> int:
    args = parse_args()
    text = args.schematic.read_text(encoding="utf-8")
    symbols = iter_symbol_instances(text)
    known_libs = collect_known_libs(args.footprint_root)

    missing = []
    unknown = []

    for ref, footprint in symbols:
        if any(ref.startswith(prefix) for prefix in args.ignore_prefix):
            continue
        if not footprint:
            missing.append(ref)
            continue
        if ":" in footprint:
            library, _ = footprint.split(":", 1)
            if library and library not in known_libs:
                unknown.append((ref, footprint))

    if missing:
        print("[ERROR] Symbols missing footprints:")
        for ref in sorted(missing):
            print(f"  - {ref}")

    if unknown:
        print("[WARN] Footprints with unknown libraries (relative to footprint-root):")
        for ref, fp in sorted(unknown):
            print(f"  - {ref}: {fp}")

    if not missing and not unknown:
        print("✅ All symbol footprints present and libraries discovered under", args.footprint_root)
        return 0

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())