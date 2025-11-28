#!/usr/bin/env python3
"""
STEP 9: AC Power Path
Add the high-voltage AC side:
- J3: IEC C14 power inlet
- F1: 10A fuse (safety)
- SSR switching (via labels)
- J4: AC outlet to cooktop
"""

import uuid

def guid():
    return str(uuid.uuid4())

def grid(n):
    """Convert grid units to mm (2.54mm = 100 mil)"""
    return n * 2.54

SYMBOLS = """
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
    (symbol "power:PWR_FLAG" (power) (pin_numbers hide) (pin_names (offset 0) hide)
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#FLG" (at 0 1.905 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "PWR_FLAG" (at 0 3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "PWR_FLAG_0_0"
        (pin power_out line (at 0 0 90) (length 0) (name "pwr" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27))))))
      (symbol "PWR_FLAG_0_1"
        (polyline (pts (xy 0 0) (xy 0 1.27) (xy -1.016 1.905) (xy 0 2.54) (xy 1.016 1.905) (xy 0 1.27)) (stroke (width 0)) (fill (type none)))))
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
        (pin power_in line (at 0 0 90) (length 0) hide (name "+5V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
    (symbol "power:GND" (power) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "GND_0_1"
        (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0)) (fill (type none))))
      (symbol "GND_1_1"
        (pin power_in line (at 0 0 270) (length 0) hide (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))))
"""

# Layout - DC side on left, AC side on right
# DC components
j1_x = grid(25)
j1_y = grid(30)
c1_x = grid(35)
c1_y = grid(30)
r1_x = grid(70)
r1_y = grid(30)
vcc_x = grid(45)
vcc_y = grid(25)
gnd_x = grid(45)
gnd_y = grid(40)

# AC components - right side
j3_x = grid(110)  # IEC inlet
j3_y = grid(25)
f1_x = grid(120)  # Fuse
f1_y = grid(25)
j4_x = grid(140)  # Cooktop outlet
j4_y = grid(30)

schematic = f"""(kicad_sch
  (version 20231120)
  (generator "step9-ac-path")
  (generator_version "1.0")
  (uuid "{guid()}")
  (paper "A3")
  (title_block
    (title "Induction Temp Controller - Step 9")
    (date "2025-01-01")
    (rev "1.0")
    (comment 1 "Complete Power Path: DC + AC")
  )

  (lib_symbols
{SYMBOLS}
  )

  (text "DC SIDE - 5V" (exclude_from_sim no)
    (at {grid(20)} {grid(15)} 0)
    (effects (font (size 4 4) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "USB-C" (exclude_from_sim no)
    (at {grid(20)} {grid(28)} 0)
    (effects (font (size 2 2)) (justify left))
    (uuid "{guid()}")
  )

  (text "SSR Control" (exclude_from_sim no)
    (at {grid(65)} {grid(22)} 0)
    (effects (font (size 2 2)) (justify left))
    (uuid "{guid()}")
  )

  (text "ISOLATION\\nBARRIER" (exclude_from_sim no)
    (at {grid(90)} {grid(15)} 0)
    (effects (font (size 3 3) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "AC SIDE\\n120-240V ⚡" (exclude_from_sim no)
    (at {grid(105)} {grid(15)} 0)
    (effects (font (size 4 4) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "IEC Inlet" (exclude_from_sim no)
    (at {grid(105)} {grid(23)} 0)
    (effects (font (size 2 2)) (justify left))
    (uuid "{guid()}")
  )

  (text "To Cooktop" (exclude_from_sim no)
    (at {grid(135)} {grid(28)} 0)
    (effects (font (size 2 2)) (justify left))
    (uuid "{guid()}")
  )

  (symbol (lib_id "Connector:Conn_01x02") (at {j1_x} {j1_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J1" (at {j1_x + 3} {j1_y + 2} 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "USB-C 5V" (at {j1_x + 3} {j1_y - 2} 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at {j1_x} {j1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {j1_x} {j1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
    (pin "2" (uuid "{guid()}"))
  )

  (symbol (lib_id "Device:C") (at {c1_x} {c1_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "C1" (at {c1_x + 2} {c1_y - 2} 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100µF" (at {c1_x + 2} {c1_y + 2} 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at {c1_x} {c1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {c1_x} {c1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
    (pin "2" (uuid "{guid()}"))
  )

  (symbol (lib_id "Device:R") (at {r1_x} {r1_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "R1" (at {r1_x + 2} {r1_y} 90) (effects (font (size 1.27 1.27))))
    (property "Value" "330Ω" (at {r1_x - 2} {r1_y} 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {r1_x} {r1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {r1_x} {r1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
    (pin "2" (uuid "{guid()}"))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at {j3_x} {j3_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J3" (at {j3_x + 3} {j3_y + 2} 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "IEC C14" (at {j3_x + 3} {j3_y - 2} 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at {j3_x} {j3_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {j3_x} {j3_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
    (pin "2" (uuid "{guid()}"))
  )

  (symbol (lib_id "Device:Fuse") (at {f1_x} {f1_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "F1" (at {f1_x + 2} {f1_y} 90) (effects (font (size 1.27 1.27))))
    (property "Value" "10A" (at {f1_x - 2} {f1_y} 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {f1_x} {f1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {f1_x} {f1_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
    (pin "2" (uuid "{guid()}"))
  )

  (symbol (lib_id "Connector:Conn_01x02") (at {j4_x} {j4_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "J4" (at {j4_x + 3} {j4_y + 2} 0) (effects (font (size 1.5 1.5)) (justify left)))
    (property "Value" "Cooktop" (at {j4_x + 3} {j4_y - 2} 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at {j4_x} {j4_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {j4_x} {j4_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
    (pin "2" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:+5V") (at {vcc_x} {vcc_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR01" (at {vcc_x} {vcc_y - 3.81} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at {vcc_x} {vcc_y + 3.5} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {vcc_x} {vcc_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {vcc_x} {vcc_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:PWR_FLAG") (at {vcc_x} {vcc_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#FLG01" (at {vcc_x} {vcc_y + 1.905} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "PWR_FLAG" (at {vcc_x + 5} {vcc_y - 2} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {vcc_x} {vcc_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {vcc_x} {vcc_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:GND") (at {gnd_x} {gnd_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR02" (at {gnd_x} {gnd_y + 6.35} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at {gnd_x} {gnd_y + 3.8} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {gnd_x} {gnd_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {gnd_x} {gnd_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:PWR_FLAG") (at {gnd_x} {gnd_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#FLG02" (at {gnd_x} {gnd_y + 1.905} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "PWR_FLAG" (at {gnd_x + 5} {gnd_y + 2} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {gnd_x} {gnd_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {gnd_x} {gnd_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (wire (pts (xy {j1_x - 5.08} {j1_y}) (xy {c1_x} {c1_y - 3.81}))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {c1_x} {c1_y - 3.81}) (xy {vcc_x} {vcc_y}))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {j1_x - 5.08} {j1_y + 2.54}) (xy {c1_x} {c1_y + 3.81}))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {c1_x} {c1_y + 3.81}) (xy {gnd_x} {gnd_y}))
    (stroke (width 0.5) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {r1_x - grid(5)} {r1_y - 3.81}) (xy {r1_x} {r1_y - 3.81}))
    (stroke (width 0.3) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {r1_x} {r1_y + 3.81}) (xy {r1_x + grid(5)} {r1_y + 3.81}))
    (stroke (width 0.3) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {j3_x - 5.08} {j3_y}) (xy {f1_x} {f1_y - 3.81}))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {f1_x} {f1_y + 3.81}) (xy {f1_x + grid(5)} {f1_y + 3.81}))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {f1_x + grid(10)} {f1_y + 3.81}) (xy {j4_x - 5.08} {j4_y}))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {j3_x - 5.08} {j3_y + 2.54}) (xy {j4_x - 5.08} {j4_y + 2.54}))
    (stroke (width 1) (type default))
    (uuid "{guid()}")
  )

  (label "ESP32_GPIO4" (at {r1_x - grid(5)} {r1_y - 3.81} 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SSR_CTRL" (at {r1_x + grid(5)} {r1_y + 3.81} 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27) bold) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SSR_HOT_IN" (at {f1_x + grid(5)} {f1_y + 3.81} 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5) bold) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SSR_HOT_OUT" (at {f1_x + grid(10)} {f1_y + 3.81} 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5) bold) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "AC_HOT" (at {j3_x - 2} {j3_y} 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5) bold) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "AC_NEUTRAL" (at {j3_x - 2} {j3_y + 2.54} 0) (fields_autoplaced yes)
    (effects (font (size 1.5 1.5)) (justify left bottom))
    (uuid "{guid()}")
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""

with open("controller/controller.kicad_sch", "w") as f:
    f.write(schematic)

print("✅ STEP 9: AC Power Path Added!")
print(f"\nAC Signal flow:")
print(f"  AC_HOT → F1 (10A fuse) → SSR_HOT_IN → SSR → SSR_HOT_OUT → Cooktop")
print(f"  AC_NEUTRAL → Cooktop (direct)")
print(f"\nComplete circuit now has:")
print(f"  • DC power: USB-C → C1 → +5V/GND")
print(f"  • SSR control: ESP32_GPIO4 → R1 → SSR_CTRL")
print(f"  • AC power: IEC → F1 → SSR → Cooktop")
print(f"\nNet labels show connections for SSR (to be visualized)")
