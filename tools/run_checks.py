#!/usr/bin/env python3
"""Run ERC with a simple allowlist to gate regressions."""

from __future__ import annotations

import argparse
import json
import subprocess
import tempfile
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schematic", type=Path)
    parser.add_argument(
        "--allowlist",
        type=Path,
        default=Path("tools/erc_allowlist.json"),
        help="JSON file listing allowed ERC violation types",
    )
    parser.add_argument(
        "--keep-report",
        action="store_true",
        help="Persist the ERC JSON report alongside the schematic",
    )
    return parser.parse_args()


def load_allowlist(path: Path) -> set[str]:
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    return set(data.get("allowed_types", []))


def run_erc(schematic: Path) -> tuple[dict, Path | None]:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    tmp.close()
    out_path = Path(tmp.name)
    subprocess.run(
        [
            "kicad-cli",
            "sch",
            "erc",
            str(schematic),
            "--format",
            "json",
            "--output",
            str(out_path),
        ],
        check=True,
    )
    data = json.loads(out_path.read_text(encoding="utf-8"))
    return data, out_path


def collect_violation_types(report: dict) -> list[tuple[str, str]]:
    violations: list[tuple[str, str]] = []
    for sheet in report.get("sheets", []):
        for violation in sheet.get("violations", []):
            violations.append((violation.get("type", "unknown"), violation.get("description", "")))
    return violations


def main() -> int:
    args = parse_args()
    allowlist = load_allowlist(args.allowlist)
    report, path = run_erc(args.schematic)
    violations = collect_violation_types(report)

    unexpected = [v for v in violations if v[0] not in allowlist]

    if unexpected:
        print("[ERROR] Unexpected ERC violations:")
        for vtype, desc in unexpected:
            print(f"  - {vtype}: {desc}")
    else:
        print("✅ ERC contains only allowlisted violations")

    if args.keep_report:
        dest = args.schematic.with_suffix(".erc.json")
        dest.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("Saved report to", dest)
    else:
        path.unlink(missing_ok=True)

    return 1 if unexpected else 0


if __name__ == "__main__":
    raise SystemExit(main())