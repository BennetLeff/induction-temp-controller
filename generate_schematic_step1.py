#!/usr/bin/env python3
"""
STEP 1: Minimal test schematic
- Just power symbols (+5V, GND)
- PWR_FLAG to satisfy ERC
- One simple connection
This MUST load without errors before we proceed.
"""

import uuid

def guid():
    return str(uuid.uuid4())

def mm(millimeters):
    """Convert millimeters to KiCad internal units"""
    return millimeters

# Minimal symbol library - only what we need for this step
SYMBOLS = """
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
"""

schematic = f"""(kicad_sch
  (version 20231120)
  (generator "step1-minimal")
  (generator_version "1.0")
  (uuid "{guid()}")
  (paper "A4")
  (title_block
    (title "Step 1: Minimal Test")
    (date "2025-01-01")
    (rev "1.0")
  )

  (lib_symbols
{SYMBOLS}
  )

  (text "STEP 1: Minimal Test\\nJust power symbols" (exclude_from_sim no)
    (at {mm(50)} {mm(40)} 0)
    (effects (font (size 3 3) bold) (justify left))
    (uuid "{guid()}")
  )

  (symbol (lib_id "power:+5V") (at {mm(100)} {mm(80)} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR01" (at {mm(100)} {mm(76.19)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at {mm(100)} {mm(83.5)} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {mm(100)} {mm(80)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {mm(100)} {mm(80)} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:GND") (at {mm(100)} {mm(120)} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR02" (at {mm(100)} {mm(126.35)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at {mm(100)} {mm(123.8)} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {mm(100)} {mm(120)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {mm(100)} {mm(120)} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:PWR_FLAG") (at {mm(100)} {mm(80)} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#FLG01" (at {mm(100)} {mm(81.905)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "PWR_FLAG" (at {mm(100)} {mm(76)} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {mm(100)} {mm(80)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {mm(100)} {mm(80)} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
  )

  (symbol (lib_id "power:PWR_FLAG") (at {mm(100)} {mm(120)} 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#FLG02" (at {mm(100)} {mm(121.905)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "PWR_FLAG" (at {mm(100)} {mm(116)} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at {mm(100)} {mm(120)} 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at {mm(100)} {mm(120)} 0) (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{guid()}"))
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

print("✅ STEP 1: Minimal schematic generated")
print("\nContents:")
print("  • +5V power symbol")
print("  • GND power symbol")
print("  • PWR_FLAG for +5V (tells ERC power is driven)")
print("  • PWR_FLAG for GND (tells ERC ground is driven)")
print("\nExpected result:")
print("  ✓ Should load in KiCad without errors")
print("  ✓ Should pass ERC with 0 errors")
print("\nNext: Verify this loads, then we'll add C1")
print(f"\nSaved to: {output_file}")
