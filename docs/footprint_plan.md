# Footprint Assignment Plan

The schematic generator now records the intended PCB footprints for each reference designator. This table documents the chosen land patterns and the rationale behind them so PCB layout can proceed without guesswork.

| Ref  | Component                        | Selected Footprint Library ID                                              | Notes |
|------|----------------------------------|---------------------------------------------------------------------------|-------|
| J1   | USB-C Power Input                | `Connector_USB:USB_C_Receptacle_GCT_USB4085`                              | Reversible 16-pin USB-C receptacle with through-hole shell tabs, rated for 5 A. Matches the common GCT USB4085 footprint used in many KiCad templates. |
| C1   | 100 µF Bulk Capacitor            | `Capacitor_THT:CP_Radial_D8.0mm_P3.50mm`                                  | Radial electrolytic (8 mm body, 3.5 mm pitch). Sized for easy sourcing and enough ripple handling on the 5 V input. |
| U1   | ESP32 DevKitC Module             | `Espressif:ESP32-DevKitC`                                                 | Directly from Espressif’s official KiCad library so the pin header spacing and USB position line up with the module. |
| DISP1| SSD1306 0.91" OLED               | `SSD1306_OLED:SSD1306_OLED-0.91-128x32`                                   | Footprint provided with the temporary OLED library bundled in the repo. |
| SW1  | Rotary Encoder w/ Push Switch    | `Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical`                 | Alps EC11 vertical encoder with integrated momentary switch; common for UI knobs. |
| U2   | MAX31856 (SOIC-20W)              | `Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm`                                  | Matches the TI/ADI wide SOIC package used by the MAX31856. |
| J2   | Thermocouple Connector           | `Connector_Wire:Screw_Terminal_01x02`                                     | 2-position pluggable/screw terminal for the probe, giving robust wire retention. |
| R1   | 330 Ω SSR Gate Resistor          | `Resistor_SMD:R_1206_3216Metric`                                          | 1206 size for elevated power dissipation margin and easy hand assembly. |
| SSR1 | ASSR-1218 Solid State Relay      | `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm`                                     | Matches the SSR’s SOIC-8 package. |
| J3   | IEC C14 AC Inlet                 | `Connector_AC:IEC_60320_C14_PanelMount`                                   | Right-angle panel mount inlet available in KiCad’s connector library, suitable for board-edge mounting. |
| F1   | 10 A Fuse                        | `Fuse:Fuseholder_Cylinder-5x20mm_Schurter_0031_8003_Straight`             | Horizontal 5×20 mm cartridge fuse holder rated for 10 A. |
| J4   | Cooktop Outlet (Hot/Neutral/GND) | `TerminalBlock:TerminalBlock_bornier-3_P5.08mm`                           | 3-position 5.08 mm pitch terminal block to route AC hot, neutral, and protective earth to the cooktop. |

### How to Update

- Modify `FOOTPRINT_MAP` inside `generate_full_schematic_cli.py` to change any assignment.
- Re-run `python3 generate_full_schematic_cli.py` and check `controller/controller-generated.kicad_sch` to confirm each `Footprint` property updated.
- If a new footprint library is required, add it to the project’s footprint library table so PCB editors can resolve it without extra configuration.

### Validation

After editing the footprint map:

```bash
python3 generate_full_schematic_cli.py
kicad-cli sch erc controller/controller-generated.kicad_sch --output erc_generated.rpt --exit-code-violations
```

The ERC run still reports the known dangling-label violations, but the schematic now loads cleanly with footprint metadata embedded for every physical part.
