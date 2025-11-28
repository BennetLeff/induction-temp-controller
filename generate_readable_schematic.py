#!/usr/bin/env python3
"""
Generate READABLE KiCad schematic with proper spacing and organization
"""

import uuid

def guid():
    return str(uuid.uuid4())

# Symbol definitions (same as before but cleaner positioning)
SYMBOLS_LIB = """
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

# Build schematic with MUCH better spacing
schematic = f"""(kicad_sch
  (version 20231120)
  (generator "python-readable")
  (generator_version "2.0")
  (uuid "{guid()}")
  (paper "A3")
  (title_block
    (title "Induction Temperature Controller")
    (date "2024-01-01")
    (rev "1.0")
    (comment 1 "External PID Temperature Controller for Induction Cooktops")
    (comment 2 "ESP32 + MAX31856 + SSR Control")
    (comment 3 "DC SIDE: 5V/3.3V | AC SIDE: 120-240V")
    (comment 4 "Maintain >=6.4mm creepage/clearance between AC and DC on PCB")
  )

  (lib_symbols
{SYMBOLS_LIB}
  )

  (text "DC SIDE\\nLOW VOLTAGE\\n5V / 3.3V" (exclude_from_sim no)
    (at 80 40 0)
    (effects (font (size 4 4) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "ISOLATION\\nBARRIER\\n>=6.4mm" (exclude_from_sim no)
    (at 200 40 0)
    (effects (font (size 3 3) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "AC SIDE\\nHIGH VOLTAGE\\n120-240V\\n⚡ DANGER ⚡" (exclude_from_sim no)
    (at 320 40 0)
    (effects (font (size 4 4) bold) (justify left))
    (uuid "{guid()}")
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 70 80 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J1" (at 75 80 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "USB-C Power" (at 75 82.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 70 80 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 70 80 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:C") (at 70 110 90) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "C1" (at 70 105 90) (effects (font (size 1.5 1.5))))
    (property "Value" "100µF" (at 70 115 90) (effects (font (size 1.2 1.2))))
    (property "Footprint" "" (at 70 110 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 70 110 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 100 140 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "U1" (at 105 140 0) (effects (font (size 1.5 1.5) bold) (justify left)))
    (property "Value" "ESP32-DevKit-C" (at 105 142.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 100 140 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 100 140 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 40 170 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "DISP1" (at 45 170 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "OLED 128x64" (at 45 172.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 40 170 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 40 170 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 40 200 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "SW1" (at 45 200 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "Rotary Encoder" (at 45 202.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 40 200 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 40 200 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 130 170 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "U2" (at 135 170 0) (effects (font (size 1.5 1.5) bold) (justify left)))
    (property "Value" "MAX31856" (at 135 172.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 130 170 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 130 170 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:C") (at 160 170 90) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "C2" (at 160 165 90) (effects (font (size 1.5 1.5))))
    (property "Value" "0.1µF" (at 160 175 90) (effects (font (size 1.2 1.2))))
    (property "Footprint" "" (at 160 170 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 160 170 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 130 210 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J2" (at 135 210 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "K-Type TC" (at 135 212.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 130 210 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 130 210 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:R") (at 220 140 90) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "R1" (at 220 135 90) (effects (font (size 1.5 1.5))))
    (property "Value" "330Ω" (at 220 145 90) (effects (font (size 1.2 1.2))))
    (property "Footprint" "" (at 220 140 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 220 140 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 260 140 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "SSR1" (at 265 140 0) (effects (font (size 1.5 1.5) bold) (justify left)))
    (property "Value" "SSR 10-40A" (at 265 142.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 260 140 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 260 140 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 330 100 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J3" (at 335 100 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "IEC C14" (at 335 102.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 330 100 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 330 100 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:Fuse") (at 330 130 90) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "F1" (at 330 125 90) (effects (font (size 1.5 1.5))))
    (property "Value" "10A" (at 330 135 90) (effects (font (size 1.2 1.2))))
    (property "Footprint" "" (at 330 130 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 330 130 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at 330 170 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J4" (at 335 170 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "To Cooktop" (at 335 172.5 0) (effects (font (size 1.2 1.2)) (justify left)))
    (property "Footprint" "" (at 330 170 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 330 170 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:+5V") (at 65 80 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR01" (at 61.19 80 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 61 80 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 65 80 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 65 80 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 65 82.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR02" (at 58.65 82.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 61 82.54 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 65 82.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 65 82.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:+5V") (at 95 140 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR03" (at 91.19 140 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 91 140 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 95 140 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 95 140 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 95 142.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR04" (at 88.65 142.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 91 142.54 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 95 142.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 95 142.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:+3V3") (at 125 170 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR05" (at 121.19 170 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+3V3" (at 121 170 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 125 170 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 125 170 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 125 172.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR06" (at 118.65 172.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 121 172.54 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 125 172.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 125 172.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 255 142.54 270) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR07" (at 248.65 142.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 251 142.54 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 255 142.54 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 255 142.54 0) (effects (font (size 1.27 1.27)) hide))
  )

  (wire (pts (xy 65 80) (xy 70 106.19))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 70 113.81) (xy 65 142.54))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 95 140) (xy 95 140))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 95 142.54) (xy 95 142.54))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 200 140) (xy 216.19 140))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 223.81 140) (xy 255 140))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 255 142.54) (xy 255 142.54))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 325 100) (xy 330 126.19))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 330 133.81) (xy 325 170))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (label "+5V" (at 68 90 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "GND" (at 68 95 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_SCK" (at 115 155 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_MISO" (at 115 160 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_MOSI" (at 115 165 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_CS" (at 115 175 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "I2C_SDA" (at 50 165 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "I2C_SCL" (at 50 175 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "ENC_A" (at 50 195 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "ENC_B" (at 50 205 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SSR_CTRL" (at 190 140 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "TC+" (at 140 205 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "TC-" (at 140 215 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "AC_HOT" (at 340 110 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "AC_NEUTRAL" (at 340 180 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
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

print("✅ READABLE schematic generated with proper spacing!")
print("\nKey improvements:")
print("  • Components spread across full A3 sheet")
print("  • DC side: x=40-170mm")
print("  • Isolation: x=200-260mm")
print("  • AC side: x=320-400mm")
print("  • 30-40mm vertical spacing between components")
print("  • Larger text labels (1.5mm font)")
print("  • Clear section headers")
print("  • Organized layout")
print(f"\nSaved to: {output_file}")
print("Opening in KiCad...")
