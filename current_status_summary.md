# Current Status Summary

## TL;DR

- The **CLI-first schematic pipeline** is the source of truth. `generate_full_schematic_cli.py` now instantiates every production symbol using the checked-in KiCad/Espressif/OLED libraries and the coordinates in `config/placements.json`.
- `tools/render_status.py` reports **20 symbol instances** in `controller/controller-generated.kicad_sch` with **140 ERC violations** (mostly dangling labels/power pins) as of the latest regeneration.
- All block-level annotations, net labels, and section callouts are emitted from Python so the schematic can be regenerated deterministically without touching the GUI.

## What’s Been Completed

1. **Library + symbol provenance locked down** via the bundled `kicad-symbols-repo/`, `temp-espressif-library/`, and `temp-oled-library/` directories plus the `extract_symbol_from_lib.py` helper.
2. **Placement data centralized** in `config/placements.json`, covering USB-C power, ESP32 control, MAX31856, rotary input, SSR drive, thermocouple, and AC-side protection/connector hardware.
3. **Programmatic annotations**: the generator stamps DC/Isolation/AC callouts, net labels for SPI/I²C/SSR control, and safety text, matching the schematic generation plan.
4. **Automated status capture** through `tools/render_status.py`, which refreshes `docs/status_snapshot.md` after each ERC run to keep metrics visible.

## In Flight / Blockers

- **ERC cleanup**: Wiring serialization is good enough for KiCad to parse, but large portions of nets are still missing, leaving dangling pins and undriven power rails. This is the primary source of the 140 open violations.
- **Footprint validation**: Every instantiated symbol now carries a footprint, but we still need to run the footprint checker scripts before sign-off.
- **Graphic primitives**: Isolation rectangles and safety arrows still need to be reintroduced once we verify the syntax KiCad expects from generated drawings.

## Next Steps

1. Keep iterating inside `generate_full_schematic_cli.py` to finish the remaining wiring + power flag placement until `kicad-cli sch erc` reaches zero violations.
2. Add the outstanding graphic primitives (isolation bar, HV warning blocks) via the generator so they survive regeneration.
3. After the ERC noise floor drops, hand the schematic to the footprint + BOM tooling (`tools/check_footprints.py`, `tools/gen_bom.py`) to validate the library choices before PCB layout work begins.

This document should be updated whenever we cut the ERC violation count or change the CLI workflow so newcomers can immediately see the project’s true status.
