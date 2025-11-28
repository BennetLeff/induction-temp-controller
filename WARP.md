# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project overview

This repository contains an early-stage KiCad 9 project for an induction temperature controller. The electrical design and PCB layout are managed entirely via KiCad project files; there is currently no firmware, simulation code, or custom build tooling checked into this repo.

## Repository layout (big picture)

- `README.md` – top-level project name only; there is no additional documentation yet.
- `controller/` – main KiCad project directory.
  - `controller.kicad_pro` – KiCad project configuration (net classes, board settings, and project-level metadata). Currently uses the default net class configuration.
  - `controller.kicad_sch` – root schematic file for the controller. At present it only contains project metadata and an empty sheet definition (no symbols or nets yet).
  - `controller.kicad_pcb` – PCB layout file. At present it is effectively empty (just the KiCad 9 PCB header).
  - `controller-backups/` – KiCad-created backup ZIP archives of the project.

There are **no** source files, scripts, or build/test automation outside of the KiCad artifacts.

## Working with the KiCad project

Most development work happens inside the KiCad GUI rather than via command-line tools.

### Opening the project

- Open the project in KiCad by loading `controller/controller.kicad_pro`.
- On macOS from the terminal, you can use:
  - `open controller/controller.kicad_pro` – opens the project in the default associated application (KiCad).

Once the project is open in KiCad:

- Use the Schematic Editor on `controller.kicad_sch` to add symbols, nets, and hierarchical sheets for the induction temperature controller.
- Use the PCB Editor on `controller.kicad_pcb` to create and route the PCB.

### Design checks and validation

There are no repo-defined "build" or test commands. Validation is performed inside KiCad:

- **ERC (Electrical Rules Check)** is run from the Schematic Editor to validate the schematic.
- **DRC (Design Rules Check)** is run from the PCB Editor to validate the board layout.

If command-line or scripted checks are added in the future (for example, using KiCad CLI or custom scripts), update this section with the exact commands.

### Fabrication outputs

Fabrication outputs (Gerbers, drill files, BOM, pick-and-place) are currently expected to be generated via KiCad's built-in exporters from the GUI. There are no automation scripts or CI pipelines defined in this repository for generating manufacturing data.

## Notes for future Warp agents

- Treat `.kicad_sch` and `.kicad_pcb` as KiCad 9 files:
  - `.kicad_sch` is an S-expression-based schematic format.
  - `.kicad_pcb` is an S-expression-based PCB board format.
  - Changes must preserve valid KiCad syntax; prefer small, localized textual edits when asked to modify these files, and avoid large restructurings without clear instructions.
- The `.kicad_pro` file is JSON and primarily contains project configuration. Be cautious when editing net class or board settings; keep the structure consistent with KiCad's expectations.
- Do not modify files in `controller/controller-backups/` unless explicitly requested; they are automatic snapshots created by KiCad.
- If firmware, simulations, or additional tooling are added later (e.g., microcontroller code for the controller, Python scripts, or CI configs), expand this file to document:
  - How to build and flash firmware.
  - How to run any simulations or tests.
  - Any new build/lint/test commands or project-specific workflows.
