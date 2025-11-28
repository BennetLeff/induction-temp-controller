#!/usr/bin/env python3
"""
STEP 3: Add capacitor C1 between +5V and GND
Real component with real connections - this should satisfy ERC
"""

import uuid

def guid():
    return str(uuid.uuid4())

def grid(n):
    """Convert grid units to mm (2.54mm = 100 mil)"""
    return n * 2.54

# Add capacitor and PWR_FLAG symbols
SYMBOLS = """
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

# Layout: vertical stack
cap_x = grid(40)
cap_y = grid(35)

vcc_x = cap_x
vcc_y = cap_y - grid(5)  # Above capacitor

gnd_x = cap_x
gnd_y = cap_y + grid(5)  # Below capacitor

schematic = f"""(kicad_sch
  (version 20231120)
  (generator "step3-capacitor")
  (generator_version "1.0")
  (uuid "{guid()}")
  (paper "A4")
  (title_block
    (title "Step 3: Add Capacitor")
    (date "2025-01-01")
    (rev "1.0")
  )

  (lib_symbols
{SYMBOLS}
  )

  (text "STEP 3: Capacitor\\nC1 connects +5V to GND" (exclude_from_sim no)
    (at {grid(20)} {grid(15)} 0)
    (effects (font (size 3 3) bold) (justify left))
    (uuid "{guid()}")
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

  (symbol (lib_id "Device:C") (at {cap_x} {cap_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "C1" (at {cap_x + 2} {cap_y + 2} 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100µF" (at {cap_x + 2} {cap_y - 2} 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at {cap_x} {cap_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {cap_x} {cap_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
    (pin "2" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:PWR_FLAG") (at {vcc_x} {vcc_y} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#FLG01" (at {vcc_x} {vcc_y + 1.905} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "PWR_FLAG" (at {vcc_x + 5} {vcc_y - 3} 0) (effects (font (size 1.27 1.27))))
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
    (property "Value" "PWR_FLAG" (at {gnd_x + 5} {gnd_y + 3} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {gnd_x} {gnd_y} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {gnd_x} {gnd_y} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (wire (pts (xy {vcc_x} {vcc_y}) (xy {cap_x} {cap_y - 3.81}))
    (stroke (width 0) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy {cap_x} {cap_y + 3.81}) (xy {gnd_x} {gnd_y}))
    (stroke (width 0) (type default))
    (uuid "{guid()}")
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""

with open("controller/controller.kicad_sch", "w") as f:
    f.write(schematic)

print("✅ STEP 3: Capacitor added!")
print(f"\nCircuit:")
print(f"  +5V → C1 pin 1 → C1 pin 2 → GND")
print(f"\nComponent positions:")
print(f"  +5V: ({vcc_x}, {vcc_y})")
print(f"  C1:  ({cap_x}, {cap_y})")
print(f"  GND: ({gnd_x}, {gnd_y})")
print(f"\nCapacitor pins:")
print(f"  Pin 1 at ({cap_x}, {cap_y - 3.81}) - connects to +5V")
print(f"  Pin 2 at ({cap_x}, {cap_y + 3.81}) - connects to GND")
