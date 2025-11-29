#!/usr/bin/env python3
"""Basic sanity checks for local KiCad symbol and footprint libraries."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        default=["controller"],
        help="Directories to scan for .kicad_sym / .kicad_mod files",
    )
    return parser.parse_args()


def balanced_parentheses(text: str) -> bool:
    stripped = text.lstrip()
    if stripped.startswith("symbol"):
        opens = text.count("(")
        closes = text.count(")")
        return opens - closes in (0, 1)
    start = text.find("(")
    if start == -1:
        return True
    text = text[start:]
    depth = 0
    for char in text:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def main() -> int:
    args = parse_args()
    failures: list[Path] = []
    for root in args.paths:
        for path in Path(root).rglob("*.kicad_sym"):
            if not balanced_parentheses(path.read_text(encoding="utf-8")):
                failures.append(path)
        for path in Path(root).rglob("*.kicad_mod"):
            if not balanced_parentheses(path.read_text(encoding="utf-8")):
                failures.append(path)
    if failures:
        print("[ERROR] Unbalanced parentheses detected in:")
        for path in failures:
            print(f"  - {path}")
        return 1
    print("✅ Library files passed structural checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())