#!/usr/bin/env python3
"""Generate a reproducible KiCad schematic directly from Python + CLI tooling."""

from __future__ import annotations

import textwrap
import uuid
from collections import OrderedDict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent


def repo_path(*parts: str) -> Path:
    return REPO_ROOT.joinpath(*parts)


def guid() -> str:
    return str(uuid.uuid4())


def extract_symbol(symbol_name: str, library_file: Path) -> str:
    """Return the full s-expression for `symbol_name` from `library_file`."""

    if not library_file.exists():
        raise FileNotFoundError(f"Missing KiCad library: {library_file}")

    content = library_file.read_text(encoding="utf-8")
    needle = f'(symbol "{symbol_name}"'
    start = content.find(needle)
    if start == -1:
        raise ValueError(f"Symbol '{symbol_name}' not found in {library_file}")

    depth = 0
    for idx in range(start, len(content)):
        char = content[idx]
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth == 0:
                return content[start : idx + 1]

    raise ValueError(f"Unbalanced parentheses while parsing {symbol_name} from {library_file}")


CUSTOM_SYMBOLS = {
    "Custom:Thermocouple_Connector": textwrap.dedent(
        """
        (symbol "Custom:Thermocouple_Connector"
          (property "Reference" "J" (at 0 2.921 0)
            (effects (font (size 1.27 1.27)))
          )
          (property "Value" "Thermocouple_Connector" (at 0 -2.921 0)
            (effects (font (size 1.27 1.27)))
          )
          (property "Footprint" "" (at 0 0 0)
            (effects (font (size 1.27 1.27)) hide)
          )
          (property "Datasheet" "~" (at 0 0 0)
            (effects (font (size 1.27 1.27)) hide)
          )
          (symbol "Thermocouple_Connector_1_1"
            (pin passive line (at 0 2.54 270) (length 2.54)
              (name "T+" (effects (font (size 1.27 1.27))))
              (number "1" (effects (font (size 1.27 1.27))))
            )
            (pin passive line (at 0 -2.54 90) (length 2.54)
              (name "T-" (effects (font (size 1.27 1.27))))
              (number "2" (effects (font (size 1.27 1.27))))
            )
          )
        )
        """
    ).strip(),
    "Custom:AC_Outlet_Connector": textwrap.dedent(
        """
        (symbol "Custom:AC_Outlet_Connector"
          (property "Reference" "J" (at 0 2.921 0)
            (effects (font (size 1.27 1.27)))
          )
          (property "Value" "AC_Outlet_Connector" (at 0 -2.921 0)
            (effects (font (size 1.27 1.27)))
          )
          (property "Footprint" "" (at 0 0 0)
            (effects (font (size 1.27 1.27)) hide)
          )
          (property "Datasheet" "~" (at 0 0 0)
            (effects (font (size 1.27 1.27)) hide)
          )
          (symbol "AC_Outlet_Connector_1_1"
            (pin power_in line (at 0 2.54 270) (length 2.54)
              (name "Hot" (effects (font (size 1.27 1.27))))
              (number "1" (effects (font (size 1.27 1.27))))
            )
            (pin power_in line (at 0 0 270) (length 2.54)
              (name "Neutral" (effects (font (size 1.27 1.27))))
              (number "2" (effects (font (size 1.27 1.27))))
            )
            (pin power_in line (at 0 -2.54 270) (length 2.54)
              (name "Ground" (effects (font (size 1.27 1.27))))
              (number "3" (effects (font (size 1.27 1.27))))
            )
          )
        )
        """
    ).strip(),
}


SYMBOL_SOURCES = OrderedDict(
    (
        ("Device:R", (repo_path("kicad-symbols-repo", "Device.kicad_sym"), "R")),
        ("Device:C", (repo_path("kicad-symbols-repo", "Device.kicad_sym"), "C")),
        ("Device:Fuse", (repo_path("kicad-symbols-repo", "Device.kicad_sym"), "Fuse")),
        ("Device:RotaryEncoder_Switch", (repo_path("kicad-symbols-repo", "Device.kicad_sym"), "RotaryEncoder_Switch")),
        ("Relay_SolidState:ASSR-1218", (repo_path("kicad-symbols-repo", "Relay_SolidState.kicad_sym"), "ASSR-1218")),
        ("Connector:USB_C_Receptacle", (repo_path("kicad-symbols-repo", "Connector.kicad_sym"), "USB_C_Receptacle")),
        ("Connector:IEC_60320_C14_Receptacle", (repo_path("kicad-symbols-repo", "Connector.kicad_sym"), "IEC_60320_C14_Receptacle")),
        ("Sensor_Temperature:MAX31856", (repo_path("kicad-symbols-repo", "Sensor_Temperature.kicad_sym"), "MAX31856")),
        ("Espressif:ESP32-DevKitC", (repo_path("temp-espressif-library", "symbols", "Espressif.kicad_sym"), "ESP32-DevKitC")),
        ("SSD1306_OLED:SSD1306", (repo_path("temp-oled-library", "SSD1306_OLED-0.91-128x32.kicad_sym"), "SSD1306")),
        ("power:+5V", (repo_path("kicad-symbols-repo", "power.kicad_sym"), "+5V")),
        ("power:+3V3", (repo_path("kicad-symbols-repo", "power.kicad_sym"), "+3V3")),
        ("power:GND", (repo_path("kicad-symbols-repo", "power.kicad_sym"), "GND")),
        ("power:PWR_FLAG", (repo_path("kicad-symbols-repo", "power.kicad_sym"), "PWR_FLAG")),
    )
)

FOOTPRINT_MAP = {
    "J1": "Connector_USB:USB_C_Receptacle_GCT_USB4085",
    "C1": "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm",
    "U1": "Espressif:ESP32-DevKitC",
    "DISP1": "SSD1306_OLED:SSD1306_OLED-0.91-128x32",
    "SW1": "Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical",
    "U2": "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm",
    "J2": "Connector_Wire:Screw_Terminal_01x02",
    "R1": "Resistor_SMD:R_1206_3216Metric",
    "SSR1": "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
    "J3": "Connector_AC:IEC_60320_C14_PanelMount",
    "F1": "Fuse:Fuseholder_Cylinder-5x20mm_Schurter_0031_8003_Straight",
    "J4": "TerminalBlock:TerminalBlock_bornier-3_P5.08mm",
}


def load_symbol_definitions() -> OrderedDict[str, str]:
    symbols = OrderedDict()
    for lib_id, (library_path, lookup_name) in SYMBOL_SOURCES.items():
        definition = extract_symbol(lookup_name, library_path)
        if lib_id != lookup_name:
            definition = definition.replace(f'(symbol "{lookup_name}"', f'(symbol "{lib_id}"', 1)
        definition = definition.replace("\t", "  ")
        symbols[lib_id] = definition

    for lib_id, definition in CUSTOM_SYMBOLS.items():
        symbols[lib_id] = definition.replace("\t", "  ")

    return symbols


def format_symbol_instance(
    *,
    lib_id: str,
    reference: str,
    value: str,
    position: tuple[float, float, float],
    footprint: str | None = "",
    ref_offset: tuple[float, float, float] = (0.635, 2.54, 0),
    val_offset: tuple[float, float, float] = (0.635, -2.54, 0),
    justify: str = "left",
) -> str:
    x, y, rot = position
    ref_dx, ref_dy, ref_rot = ref_offset
    val_dx, val_dy, val_rot = val_offset
    footprint_text = footprint or ""
    return textwrap.dedent(
        f"""
        (symbol (lib_id "{lib_id}") (at {x} {y} {rot}) (unit 1)
          (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
          (uuid "{guid()}")
          (property "Reference" "{reference}" (at {x + ref_dx} {y + ref_dy} {ref_rot})
            (effects (font (size 1.27 1.27)) (justify {justify}))
          )
          (property "Value" "{value}" (at {x + val_dx} {y + val_dy} {val_rot})
            (effects (font (size 1.27 1.27)) (justify {justify}))
          )
          (property "Footprint" "{footprint_text}" (at {x} {y} {rot})
            (effects (font (size 1.27 1.27)) (hide yes))
          )
          (property "Datasheet" "" (at {x} {y} {rot})
            (effects (font (size 1.27 1.27)) (hide yes))
          )
        )
        """
    ).strip()


def format_power_symbol(
    lib_id: str,
    *,
    reference: str,
    value: str,
    position: tuple[float, float, float],
    ref_offset: tuple[float, float, float] = (0.0, -3.81, 0),
    val_offset: tuple[float, float, float] = (0.0, 1.27, 0),
) -> str:
    x, y, rot = position
    ref_dx, ref_dy, ref_rot = ref_offset
    val_dx, val_dy, val_rot = val_offset
    return textwrap.dedent(
        f"""
        (symbol (lib_id "{lib_id}") (at {x} {y} {rot}) (unit 1)
          (exclude_from_sim no) (in_bom no) (on_board no) (dnp no)
          (uuid "{guid()}")
          (property "Reference" "{reference}" (at {x + ref_dx} {y + ref_dy} {ref_rot})
            (effects (font (size 1.27 1.27)) (hide yes))
          )
          (property "Value" "{value}" (at {x + val_dx} {y + val_dy} {val_rot})
            (effects (font (size 1.27 1.27)))
          )
          (property "Footprint" "" (at {x} {y} {rot})
            (effects (font (size 1.27 1.27)) (hide yes))
          )
          (property "Datasheet" "" (at {x} {y} {rot})
            (effects (font (size 1.27 1.27)) (hide yes))
          )
        )
        """
    ).strip()


def format_wire(pt1: tuple[float, float], pt2: tuple[float, float]) -> str:
    x1, y1 = pt1
    x2, y2 = pt2
    return textwrap.dedent(
        f"""
        (wire
          (pts
            (xy {x1} {y1}) (xy {x2} {y2})
          )
          (stroke
            (width 0.2032)
            (type default)
          )
          (uuid "{guid()}")
        )
        """
    ).strip()


def format_label(name: str, position: tuple[float, float], justify: str = "left") -> str:
    x, y = position
    return textwrap.dedent(
        f"""
        (label "{name}" (at {x} {y} 0)
          (effects (font (size 1.27 1.27)) (justify {justify}))
          (uuid "{guid()}")
        )
        """
    ).strip()


def format_text(
    text: str,
    position: tuple[float, float],
    font_size: float,
    *,
    bold: bool = False,
    justify: tuple[str, ...] | None = ("left",),
) -> str:
    x, y = position
    bold_str = "yes" if bold else "no"
    justify_tokens = tuple(justify) if justify else ()
    justify_section = ""
    if justify_tokens:
        joined = " ".join(justify_tokens)
        justify_section = f" (justify {joined})"
    return textwrap.dedent(
        f"""
        (text "{text}" (exclude_from_sim no)
          (at {x} {y} 0)
          (effects (font (size {font_size} {font_size}) (bold {bold_str})){justify_section})
          (uuid "{guid()}")
        )
        """
    ).strip()


def format_rect(start: tuple[float, float], end: tuple[float, float]) -> str:
    x1, y1 = start
    x2, y2 = end
    return textwrap.dedent(
        f"""
        (gr_rect (start {x1} {y1}) (end {x2} {y2}) (stroke (width 0.254) (type solid) (color 0 0 0 0)) (fill (type none))
          (uuid "{guid()}")
        )
        """
    ).strip()


def main() -> None:
    symbol_definitions = load_symbol_definitions()
    lib_symbols = "\n".join(symbol_definitions.values())
    lib_symbols_block = "\n    ".join(lib_symbols.splitlines())

    dc_instances = [
        format_symbol_instance(
            lib_id="Connector:USB_C_Receptacle",
            reference="J1",
            value="USB-C",
            position=(50.8, 63.5, 0),
            footprint=FOOTPRINT_MAP["J1"],
        ),
        format_symbol_instance(
            lib_id="Device:C",
            reference="C1",
            value="100µF",
            position=(63.5, 76.2, 0),
            footprint=FOOTPRINT_MAP["C1"],
        ),
        format_symbol_instance(
            lib_id="Espressif:ESP32-DevKitC",
            reference="U1",
            value="ESP32-DevKitC",
            position=(101.6, 101.6, 0),
            footprint=FOOTPRINT_MAP["U1"],
        ),
        format_symbol_instance(
            lib_id="SSD1306_OLED:SSD1306",
            reference="DISP1",
            value="SSD1306 OLED",
            position=(76.2, 50.8, 0),
            footprint=FOOTPRINT_MAP["DISP1"],
        ),
        format_symbol_instance(
            lib_id="Device:RotaryEncoder_Switch",
            reference="SW1",
            value="Rotary Encoder",
            position=(76.2, 76.2, 0),
            footprint=FOOTPRINT_MAP["SW1"],
        ),
        format_symbol_instance(
            lib_id="Sensor_Temperature:MAX31856",
            reference="U2",
            value="MAX31856",
            position=(127.0, 152.4, 0),
            footprint=FOOTPRINT_MAP["U2"],
        ),
        format_symbol_instance(
            lib_id="Custom:Thermocouple_Connector",
            reference="J2",
            value="Thermocouple",
            position=(139.7, 182.88, 0),
            footprint=FOOTPRINT_MAP["J2"],
        ),
    ]

    isolation_instances = [
        format_symbol_instance(
            lib_id="Device:R",
            reference="R1",
            value="330",
            position=(177.8, 127.0, 0),
            footprint=FOOTPRINT_MAP["R1"],
        ),
        format_symbol_instance(
            lib_id="Relay_SolidState:ASSR-1218",
            reference="SSR1",
            value="ASSR-1218",
            position=(203.2, 127.0, 0),
            footprint=FOOTPRINT_MAP["SSR1"],
        ),
    ]

    ac_instances = [
        format_symbol_instance(
            lib_id="Connector:IEC_60320_C14_Receptacle",
            reference="J3",
            value="IEC C14",
            position=(279.4, 63.5, 0),
            footprint=FOOTPRINT_MAP["J3"],
        ),
        format_symbol_instance(
            lib_id="Device:Fuse",
            reference="F1",
            value="10A",
            position=(304.8, 63.5, 0),
            footprint=FOOTPRINT_MAP["F1"],
        ),
        format_symbol_instance(
            lib_id="Custom:AC_Outlet_Connector",
            reference="J4",
            value="Cooktop",
            position=(330.2, 63.5, 0),
            footprint=FOOTPRINT_MAP["J4"],
        ),
    ]

    power_instances = [
        format_power_symbol("power:+5V", reference="#PWR0101", value="+5V", position=(45.72, 91.44, 270)),
        format_power_symbol("power:+3V3", reference="#PWR0102", value="+3V3", position=(114.3, 86.36, 270)),
        format_power_symbol("power:GND", reference="#PWR0103", value="GND", position=(45.72, 104.14, 90)),
        format_power_symbol("power:GND", reference="#PWR0104", value="GND", position=(152.4, 172.72, 90)),
    ]

    power_flag_instances = [
        format_power_symbol("power:PWR_FLAG", reference="#FLG0101", value="PWR_FLAG", position=(53.34, 91.44, 0)),
        format_power_symbol("power:PWR_FLAG", reference="#FLG0102", value="PWR_FLAG", position=(53.34, 104.14, 0)),
        format_power_symbol("power:PWR_FLAG", reference="#FLG0103", value="PWR_FLAG", position=(101.6, 86.36, 0)),
    ]

    wires = []
    wire_points = [
        ((53.34, 63.5), (53.34, 76.2)),
        ((53.34, 76.2), (53.34, 91.44)),
        ((53.34, 91.44), (101.6, 91.44)),
        ((53.34, 66.04), (53.34, 104.14)),
        ((53.34, 104.14), (101.6, 104.14)),
        ((101.6, 104.14), (127.0, 104.14)),
        ((101.6, 86.36), (127.0, 86.36)),
        ((101.6, 91.44), (101.6, 116.84)),
        ((101.6, 104.14), (101.6, 78.74)),
        ((177.8, 127.0), (203.2, 127.0)),
        ((203.2, 127.0), (330.2, 127.0)),
        ((279.4, 66.04), (304.8, 66.04)),
        ((304.8, 66.04), (304.8, 63.5)),
        ((304.8, 60.96), (203.2, 60.96)),
        ((203.2, 60.96), (203.2, 127.0)),
        ((279.4, 63.5), (330.2, 63.5)),
        ((279.4, 60.96), (330.2, 60.96)),
    ]
    for start, end in wire_points:
        wires.append(format_wire(start, end))

    labels = [
        format_label("+5V", (43.18, 91.44)),
        format_label("+3V3", (111.76, 86.36)),
        format_label("GND", (43.18, 104.14)),
        format_label("SPI_SCK", (96.52, 91.44)),
        format_label("SPI_MISO", (96.52, 88.9)),
        format_label("SPI_MOSI", (96.52, 86.36)),
        format_label("SPI_CS", (96.52, 93.98)),
        format_label("I2C_SDA", (73.66, 83.82)),
        format_label("I2C_SCL", (73.66, 81.28)),
        format_label("ENC_A", (73.66, 109.22)),
        format_label("ENC_B", (73.66, 111.76)),
        format_label("ENC_SW", (73.66, 106.68)),
        format_label("SSR_CTRL", (170.18, 127.0)),
        format_label("AC_HOT", (271.78, 66.04)),
        format_label("AC_NEUTRAL", (271.78, 63.5)),
        format_label("AC_GND", (271.78, 60.96)),
    ]

    text_entries = [
        format_text("DC SIDE - LOW VOLTAGE (5V/3V3)", (101.6, 40.64), 2.54, bold=True, justify=None),
        format_text("ISOLATION BARRIER >=6.4mm", (203.2, 40.64), 2.54, bold=True, justify=None),
        format_text("AC SIDE - HIGH VOLTAGE (120-240V) ⚡", (304.8, 40.64), 2.54, bold=True, justify=None),
    ]

    graphic_entries: list[str] = []

    schematic = textwrap.dedent(
        f"""
        (kicad_sch
          (version 20231120)
          (generator "cli-python-pipeline")
          (uuid "{guid()}")
          (paper "A3")
          (title_block
            (title "Induction Temperature Controller")
            (date "2025-02-20")
            (rev "1.0")
            (comment 1 "Generated via generate_full_schematic.py")
            (comment 2 "DC + AC isolation with SSR")
          )
          (lib_symbols
            {lib_symbols_block}
          )
          
          {"\n".join(text_entries + graphic_entries)}
          {"\n".join(dc_instances + isolation_instances + ac_instances + power_instances + power_flag_instances)}
          {"\n".join(wires)}
          {"\n".join(labels)}
          (sheet_instances
            (path "/" (page "1"))
          )
          (embedded_fonts no)
        )
        """
    ).strip() + "\n"

    output_path = repo_path("controller", "controller-generated.kicad_sch")
    output_path.write_text(schematic, encoding="utf-8")
    print(f"✅ Wrote schematic to {output_path}")


if __name__ == "__main__":
    main()
