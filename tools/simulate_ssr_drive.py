#!/usr/bin/env python3
"""Estimate SSR LED current through the drive resistor."""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--v-drive", type=float, default=3.3, help="Drive voltage in volts")
    parser.add_argument("--v-led", type=float, default=1.2, help="SSR LED forward voltage")
    parser.add_argument("--resistance", type=float, default=330.0, help="Series resistance in ohms")
    parser.add_argument("--imin", type=float, default=5e-3, help="Minimum desired current (A)")
    parser.add_argument("--imax", type=float, default=15e-3, help="Maximum desired current (A)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    voltage_drop = args.v_drive - args.v_led
    current = voltage_drop / args.resistance if args.resistance else 0.0
    print(f"Drive current ≈ {current * 1e3:.2f} mA (drop {voltage_drop:.2f} V across resistor)")
    if current < args.imin:
        print("[WARN] Current below recommended minimum")
        return 1
    if current > args.imax:
        print("[WARN] Current above recommended maximum")
        return 1
    print("✅ Current within recommended window")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())