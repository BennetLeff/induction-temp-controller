#!/usr/bin/env python3
"""Render a quick Markdown snapshot of the schematic status."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


def count_symbols(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    return text.count("(symbol (lib_id")


def erc_summary(path: Path) -> tuple[int, set[str]]:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    tmp.close()
    subprocess.run(
        [
            "kicad-cli",
            "sch",
            "erc",
            str(path),
            "--format",
            "json",
            "--output",
            tmp.name,
        ],
        check=True,
    )
    data = json.loads(Path(tmp.name).read_text())
    Path(tmp.name).unlink(missing_ok=True)
    violations = []
    types: set[str] = set()
    for sheet in data.get("sheets", []):
        for viol in sheet.get("violations", []):
            violations.append(viol)
            types.add(viol.get("type", "unknown"))
    return len(violations), types


def main() -> int:
    schematic = Path("controller/controller-generated.kicad_sch")
    dest = Path("docs/status_snapshot.md")
    symbol_count = count_symbols(schematic)
    violation_count, types = erc_summary(schematic)
    content = """# Status Snapshot

- Schematic source: {schematic}
- Symbol instances: {symbols}
- ERC violations: {violations}
  - Types: {types_list}

Generated via `tools/render_status.py`.
""".format(
        schematic=schematic,
        symbols=symbol_count,
        violations=violation_count,
        types_list=", ".join(sorted(types)),
    )
    dest.write_text(content, encoding="utf-8")
    print("Updated", dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())