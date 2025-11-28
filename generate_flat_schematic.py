#!/usr/bin/env python3
"""
Generate a completely flat KiCad schematic (no hierarchical sheets)
"""

import uuid

def guid():
    return str(uuid.uuid4())

# Complete schematic with minimal components
schematic = f"""(kicad_sch
  (version 20231120)
  (generator "python-script")
  (generator_version "1.0")
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
    (symbol "Device:R" (pin_numbers hide) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at -1.778 0 90) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54)
          (stroke (width 0.254)) (fill (type none))))
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27)))))))

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
        (pin passive line (at 0 3.81 270) (length 2.794)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 2.794)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27)))))))

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
        (pin input line (at 0 0 90) (length 0) hide
          (name "+5V" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27)))))))

    (symbol "power:GND" (power) (pin_names (offset 0))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
      (property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "GND_0_1"
        (polyline (pts (xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)) (stroke (width 0)) (fill (type none))))
      (symbol "GND_1_1"
        (pin input line (at 0 0 270) (length 0) hide
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27)))))))
  )

  (text "DC SIDE - LOW VOLTAGE (5V/3.3V)" (exclude_from_sim no)
    (at 50 30 0)
    (effects (font (size 3 3) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "AC SIDE - HIGH VOLTAGE (120-240V) ⚡ DANGER ⚡" (exclude_from_sim no)
    (at 280 30 0)
    (effects (font (size 3 3) bold) (justify left))
    (uuid "{guid()}")
  )

  (text "ISOLATION BARRIER\\n>=6.4mm clearance required" (exclude_from_sim no)
    (at 190 100 0)
    (effects (font (size 2 2) bold) (justify left))
    (uuid "{guid()}")
  )

  (symbol (lib_id "Device:R") (at 190 110 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "R1" (at 192 110 90) (effects (font (size 1.27 1.27))))
    (property "Value" "330" (at 190 110 90) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 188.222 110 90) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 190 110 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "Device:C") (at 70 70 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "C1" (at 70.635 72.54 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Value" "100µF" (at 70.635 67.46 0) (effects (font (size 1.27 1.27)) (justify left)))
    (property "Footprint" "" (at 70 70 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 70 70 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:+5V") (at 70 65 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR01" (at 70 61.19 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "+5V" (at 70 68.556 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 70 65 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 70 65 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol (lib_id "power:GND") (at 70 75 0) (unit 1)
    (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
    (uuid "{guid()}")
    (property "Reference" "#PWR02" (at 70 81.35 0) (effects (font (size 1.27 1.27)) hide))
    (property "Value" "GND" (at 70 78.81 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "" (at 70 75 0) (effects (font (size 1.27 1.27)) hide))
    (property "Datasheet" "" (at 70 75 0) (effects (font (size 1.27 1.27)) hide))
  )

  (wire (pts (xy 70 65) (xy 70 66.19))
    (stroke (width 0) (type default))
    (uuid "{guid()}")
  )

  (wire (pts (xy 70 73.81) (xy 70 75))
    (stroke (width 0) (type default))
    (uuid "{guid()}")
  )

  (label "SPI_SCK" (at 120 100 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_MISO" (at 120 105 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_MOSI" (at 120 110 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SPI_CS" (at 120 115 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "I2C_SDA" (at 90 90 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "I2C_SCL" (at 90 95 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{guid()}")
  )

  (label "SSR_CTRL" (at 180 110 0) (fields_autoplaced yes)
    (effects (font (size 1.27 1.27)) (justify left bottom))
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

print(f"✅ Clean flat schematic generated: {output_file}")
print("   No hierarchical sheets - completely flat design")
print("\nTo open:")
print("  open -a KiCad controller/controller.kicad_sch")
