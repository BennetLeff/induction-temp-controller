#!/usr/bin/env python3
"""
Generate schematic matching the mermaid diagram flow:
USB → ESP32 → SSR → AC Power → Cooktop
With MAX31856, OLED, Encoder all connected to ESP32
"""

import uuid

def guid():
    return str(uuid.uuid4())

# Same symbol library as before
SYMBOLS = """
    (symbol "Device:R" (pin_numbers hide) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254)) (fill (type none))))
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))))
    (symbol "Device:C" (pin_numbers hide) (pin_names (offset 0.254))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0.635 2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "C" (at 0.635 -2.54 0) (effects (font (size 1.27 1.27)) (justify left)))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "C_0_1"
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508)) (fill (type none)))
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508)) (fill (type none))))
      (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))))
    (symbol "Connector:Conn_01x02" (pin_names (offset 1.016) hide)
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
      (property "Value" "Conn_01x02" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Conn_01x02_1_1"
        (rectangle (start -1.27 -2.413) (end 0 -2.667) (stroke (width 0.1524)) (fill (type none)))
        (rectangle (start -1.27 0.127) (end 0 -0.127) (stroke (width 0.1524)) (fill (type none)))
        (rectangle (start -1.27 1.27) (end 1.27 -3.81) (stroke (width 0.254)) (fill (type background)))
        (pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))))
    (symbol "Device:Fuse" (pin_numbers hide) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "F" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "Fuse" (at -1.905 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "Fuse_0_1"
        (rectangle (start -0.762 -2.54) (end 0.762 2.54) (stroke (width 0.254)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0 -2.54)) (stroke (width 0)) (fill (type none))))
      (symbol "Fuse_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))))
    (symbol "power:+5V" (power) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+5V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+5V_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0)) (fill (type none))))
      (symbol "+5V_1_1"
        (pin input line (at 0 0 90) (length 0) hide (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
    (symbol "power:+3V3" (power) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "+3V3" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "+3V3_0_1"
        (polyline (pts (xy -0.762 1.27) (xy 0 2.54)) (stroke (width 0)) (fill (type none)))
        (polyline (pts (xy 0 0) (xy 0 2.54)) (stroke (width 0)) (fill (type none)))
        (polyline (pts (xy 0 2.54) (xy 0.762 1.27)) (stroke (width 0)) (fill (type none))))
      (symbol "+3V3_1_1"
        (pin input line (at 0 0 90) (length 0) hide (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
    (symbol "power:GND" (power) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "GND_0_1"
        (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0)) (fill (type none))))
      (symbol "GND_1_1"
        (pin input line (at 0 0 270) (length 0) hide (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
"""

# Layout matching mermaid flow:
# Row 1 (y=60): USB-C → ESP32 → SSR (control) → IEC Inlet
# Row 2 (y=100): OLED connects to ESP32
# Row 3 (y=140): Encoder connects to ESP32
# Row 4 (y=180): MAX31856 → ESP32, SSR → Cooktop
# Row 5 (y=220): K-Type Probe → MAX31856

schematic = f"""(kicad_sch
  (version 20231120)
  (generator "python-flow")
  (generator_version "3.0")
  (uuid "{guid()}")
  (paper "A3")
  (title_block
    (title "Induction Temperature Controller - Signal Flow")
    (date "2024-01-01")
    (rev "1.0")
    (comment 1 "External PID Temperature Controller for Induction Cooktops")
    (comment 2 "Flow: USB → ESP32 → SSR → AC Power → Cooktop")
    (comment 3 "DC SIDE: 5V/3.3V | AC SIDE: 120-240V")
    (comment 4 "Maintain >=6.4mm creepage/clearance between AC and DC on PCB")
  )
  (lib_symbols
{SYMBOLS}
  )

  (text "DC SIDE - 5V/3.3V" (exclude_from_sim no)
    (at 60 30 0)
    (effects (font (size 5 5) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "ISOLATION\\nBARRIER" (exclude_from_sim no)
    (at 245 30 0)
    (effects (font (size 4 4) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "AC SIDE - 120-240V\\n⚡ DANGER ⚡" (exclude_from_sim no)
    (at 340 30 0)
    (effects (font (size 5 5) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "Power Flow →" (exclude_from_sim no)
    (at 50 55 0)
    (effects (font (size 2 2)) (justify left))
    (uuid "{guid()}")
  )

  (text "SPI: Temp Data" (exclude_from_sim no)
    (at 145 195 0)
    (effects (font (size 1.5 1.5)) (justify left))
    (uuid "{guid()}")
  )

  (text "I2C: Display" (exclude_from_sim no)
    (at 70 115 0)
    (effects (font (size 1.5 1.5)) (justify left))
    (uuid "{guid()}")
  )

  (text "GPIO: Encoder" (exclude_from_sim no)
    (at 70 155 0)
    (effects (font (size 1.5 1.5)) (justify left))
    (uuid "{guid()}")
  )

  (text "PWM Control\\n(Optically Isolated)" (exclude_from_sim no)
    (at 235 105 0)
    (effects (font (size 1.5 1.5)) (justify left))
    (uuid "{guid()}")
  )

  (text "Time-Proportional AC" (exclude_from_sim no)
    (at 310 165 0)
    (effects (font (size 1.5 1.5)) (justify left))
    (uuid "{guid()}")
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 60 70 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J1" (at 63 68 0) (effects (font (size 2 2) bold) (justify left)))
    (property "Value" "USB-C 5V" (at 63 72 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 60 70 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60 70 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:C") (at 90 80 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "C1" (at 92 78 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "100µF" (at 92 82 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 90 80 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 90 80 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 140 130 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "U1" (at 143 128 0) (effects (font (size 2.5 2.5) bold) (justify left)))
    (property "Value" "ESP32-DevKit-C" (at 143 132 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 140 130 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 140 130 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 60 120 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "DISP1" (at 63 118 0) (effects (font (size 1.8 1.8)) (justify left)))
    (property "Value" "OLED 128x64" (at 63 122 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 60 120 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60 120 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 60 160 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "SW1" (at 63 158 0) (effects (font (size 1.8 1.8)) (justify left)))
    (property "Value" "Rotary Encoder" (at 63 162 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 60 160 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 60 160 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 180 200 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "U2" (at 183 198 0) (effects (font (size 2 2) bold) (justify left)))
    (property "Value" "MAX31856" (at 183 202 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 180 200 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 180 200 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:C") (at 210 200 90) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "C2" (at 210 195 90) (effects (font (size 1.5 1.5))))
    (property "Value" "0.1µF" (at 210 205 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 210 200 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 210 200 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 120 230 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J2" (at 123 228 0) (effects (font (size 1.8 1.8)) (justify left)))
    (property "Value" "K-Type Probe" (at 123 232 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 120 230 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 120 230 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:R") (at 240 130 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "R1" (at 243 130 90) (effects (font (size 1.8 1.8))))
    (property "Value" "330Ω" (at 237 130 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 240 130 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 240 130 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 280 150 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "SSR1" (at 283 148 0) (effects (font (size 2.5 2.5) bold) (justify left)))
    (property "Value" "SSR 10-40A" (at 283 152 0) (effects (font (size 1.8 1.8)) (justify left)))
    (property "Footprint" "" (at 280 150 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 280 150 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 350 90 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J3" (at 353 88 0) (effects (font (size 2 2) bold) (justify left)))
    (property "Value" "IEC C14" (at 353 92 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 350 90 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 350 90 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:Fuse") (at 380 90 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "F1" (at 383 90 90) (effects (font (size 1.8 1.8))))
    (property "Value" "10A" (at 377 90 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 380 90 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 380 90 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 380 180 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J4" (at 383 178 0) (effects (font (size 2 2) bold) (justify left)))
    (property "Value" "To Cooktop" (at 383 182 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Footprint" "" (at 380 180 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 380 180 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:+5V") (at 55 70 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR01" (at 51 70 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 50 70 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 55 70 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 55 70 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 55 72.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR02" (at 48 72.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 50 72.54 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 55 72.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 55 72.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:+5V") (at 135 130 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR03" (at 131 130 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 130 130 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 135 130 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 135 130 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 135 132.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR04" (at 128 132.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 130 132.54 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 135 132.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 135 132.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:+3V3") (at 175 200 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR05" (at 171 200 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 170 200 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 175 200 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 175 200 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 175 202.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR06" (at 168 202.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 170 202.54 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 175 202.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 175 202.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 275 152.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR07" (at 268 152.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 270 152.54 90) (effects (font (size 1.5 1.5))))
    (property "Footprint" "" (at 275 152.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 275 152.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (wire (pts (xy 55 70) (xy 90 76.19))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 90 76.19) (xy 110 70))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 110 70) (xy 135 130))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 55 72.54) (xy 90 83.81))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 90 83.81) (xy 110 90))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 110 90) (xy 135 132.54))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 65 120) (xy 100 120))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 100 120) (xy 135 130))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 65 160) (xy 100 160))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 100 160) (xy 135 140))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 125 230) (xy 150 220))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 150 220) (xy 175 200))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 185 200) (xy 206.19 200))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 213.81 200) (xy 220 200))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 220 200) (xy 220 170))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 220 170) (xy 145 145))
    (stroke (width 0.8) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 195 130) (xy 236.19 130))
    (stroke (width 1.2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 243.81 130) (xy 260 130))
    (stroke (width 1.2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 260 130) (xy 275 150))
    (stroke (width 1.2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 345 90) (xy 376.19 90))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 383.81 90) (xy 400 90))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 400 90) (xy 400 130))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 400 130) (xy 315 145))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 315 145) (xy 285 150))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 285 152.54) (xy 315 175))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 315 175) (xy 375 180))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 345 92.54) (xy 345 220))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 345 220) (xy 375 182.54))
    (stroke (width 2) (type default))
    (uuid "{guid()}")
  )

  (label "+5V" (at 115 70 0) (fields_autoplaced yes)
    (effects (font (size 2 2) bold) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "I2C_SDA" (at 80 120 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "I2C_SCL" (at 80 122 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "ENC_A" (at 80 160 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "ENC_B" (at 80 162 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_SCK" (at 200 180 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_MISO" (at 200 182 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_MOSI" (at 200 184 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_CS" (at 200 186 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SSR_CTRL\\nPWM 3.3V" (at 220 130 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8) bold) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "TC+" (at 140 228 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "TC-" (at 140 232 0) (fields_autoplaced yes)
    (effects (font (size 1.8 1.8)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "AC_HOT\\nSWITCHED" (at 320 140 0) (fields_autoplaced yes)
    (effects (font (size 2 2) bold) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "AC_NEUTRAL" (at 360 210 0) (fields_autoplaced yes)
    (effects (font (size 2 2)) (justify left bottom))
    (uuid "{guid()}")
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""

# Write the file
output_file = "controller/controller.kicad_sch"
with open(output_file, "w") as f:
    f.write(schematic)

print("✅ FLOW-BASED schematic generated matching mermaid diagram!")
print("\nSignal Flow (left to right):")
print("  USB-C → ESP32 (with OLED + Encoder) → R1 → SSR → AC Power → Cooktop")
print("  Probe → MAX31856 → ESP32 (SPI)")
print("\nLayout:")
print("  • Power flow: horizontal left to right")
print("  • Peripherals connect vertically to ESP32")
print("  • SSR in center as isolation barrier")
print("  • AC path on right side")
print("  • Actual wires showing connections!")
print(f"\nSaved to: {output_file}")
