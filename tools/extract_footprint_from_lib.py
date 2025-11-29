#!/usr/bin/env python3
"""Extract a footprint module definition from a .kicad_mod file."""

from __future__ import annotations

import argparse
from pathlib import Path


def extract_module(text: str, name: str) -> str | None:
    needle = f"(module {name}"
    start = text.find(needle)
    if start == -1:
        return None
    depth = 0
    for idx in range(start, len(text)):
        char = text[idx]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return text[start : idx + 1]
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("library", type=Path)
    parser.add_argument("footprint_name")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    text = args.library.read_text(encoding="utf-8")
    module = extract_module(text, args.footprint_name)
    if module is None:
        print(f"Footprint '{args.footprint_name}' not found in {args.library}")
        return 1
    args.output.write_text(module + "\n", encoding="utf-8")
    print(f"Saved footprint '{args.footprint_name}' to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())