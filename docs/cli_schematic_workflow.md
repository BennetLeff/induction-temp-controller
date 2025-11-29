# CLI Schematic Workflow

This repo now includes a purely scriptable path for generating and validating the induction temperature controller schematic. Follow the steps below to stay aligned with the plan and keep the schematic reproducible.

## Prerequisites

- **Python**: 3.10+ (the repo’s tools were last exercised with Python 3.13.2).
- **KiCad CLI**: Available via the standard KiCad 9 installation (`kicad-cli`).
- **Local symbol caches**: The checked-in `kicad-symbols-repo/`, `temp-espressif-library/`, and `temp-oled-library/` directories contain all required symbols.

## Generate the Schematic

```bash
python3 generate_full_schematic_cli.py
```

This script will:

1. Pull symbol definitions from the bundled KiCad/Espressif/OLED libraries.
2. Lay out every component in the DC, isolation, and AC blocks using the coordinates defined in the plan.
3. Emit `controller/controller-generated.kicad_sch` with annotations, labels, and current wiring.

## Run ERC from the CLI

```bash
kicad-cli sch erc controller/controller-generated.kicad_sch \
  --output erc_generated.rpt --exit-code-violations
```

Notes:

- The command currently reports ~150 violations (largely dangling labels/pins) because wiring is still being expanded per the plan. Treat this as the working baseline.
- `--exit-code-violations` bubbles ERC failures up to the shell so CI or scripts can gate on pass/fail later.

## Iteration Tips

- Work in **small iterations**: tweak `generate_full_schematic_cli.py`, regenerate, and re-run ERC each time.
- When adding new symbols, prefer extracting them with `extract_symbol_from_lib.py` so future regenerations stay deterministic.
- Avoid GUI edits on `controller/controller-generated.kicad_sch`; regenerate instead so the schematic remains source-controlled via Python.

## Next Steps in the Plan

- **Component placement clean-up**: adjust coordinates/offsets in the generator for tighter alignment.
- **Complete wiring + net labels**: continue filling in the nets defined in `SCHEMATIC_GENERATION_PLAN.md` until ERC passes cleanly.
- **Assign and verify footprints**: see [`docs/footprint_plan.md`](footprint_plan.md) for the current mapping; keep it updated as footprint choices evolve.
- **Add safety callouts/graphics**: once KiCad accepts the primitives, re-introduce isolation rectangles (likely via `polyline` instead of `gr_rect`).
- **Documentation**: keep this file updated as the flow evolves, and summarize major milestones in `SCHEMATIC_STATUS.md`.

## Supporting CLI Toolbox

- `tools/check_footprints.py`: ensures every symbol instance carries a footprint and flags unknown libraries.
- `tools/check_nets.py`: exports the netlist and verifies that plan-critical nets (SPI/I2C/AC) exist.
- `tools/check_layout.py`: enforces spatial rules for DC/isolation/AC blocks and grid alignment.
- `tools/run_checks.py`: wraps `kicad-cli sch erc` with a JSON allowlist to spotlight new violations.
- `tools/gen_bom.py`: produces `bom/generated_bom.md` using KiCad’s BOM exporter plus a local supplier map.
- `tools/simulate_ssr_drive.py`: quick sanity check for SSR LED current through R1.
- `tools/render_status.py`: re-renders `docs/status_snapshot.md` with symbol counts and ERC stats.
- `tools/extract_symbol_from_lib.py` / `tools/extract_footprint_from_lib.py`: grab individual assets from upstream libraries for reproducibility.
- `tools/test_libraries.py`: smoke-test local `.kicad_sym` / `.kicad_mod` files for syntax issues.
- `config/placements.json`: central source-of-truth for component coordinates/footprints used by `generate_full_schematic_cli.py`.

Keeping the workflow CLI-first ensures the schematic can always be regenerated from source, which is essential before moving into PCB layout or automated checks.
