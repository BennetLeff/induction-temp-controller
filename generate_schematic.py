import uuid

def generate_uuid():
    return str(uuid.uuid4())

# Read symbol definitions
# Note: These files are expected to be in the controller/ directory
# and contain the raw symbol definitions.
with open("controller/symbols.kicad_sym", "r") as f:
    resistor_symbol = f.read()
with open("controller/capacitor.kicad_sym", "r") as f:
    capacitor_symbol = f.read()
with open("controller/esp32.kicad_sym", "r") as f:
    esp32_symbol = f.read()
with open("controller/max31856.kicad_sym", "r") as f:
    max31856_symbol = f.read()
with open("controller/oled.kicad_sym", "r") as f:
    oled_symbol = f.read()
with open("controller/rotary_encoder.kicad_sym", "r") as f:
    rotary_encoder_symbol = f.read()
with open("controller/ssr.kicad_sym", "r") as f:
    ssr_symbol = f.read()
with open("controller/usb_c.kicad_sym", "r") as f:
    usb_c_symbol = f.read()
with open("controller/iec_c14.kicad_sym", "r") as f:
    iec_c14_symbol = f.read()
with open("controller/fuse.kicad_sym", "r") as f:
    fuse_symbol = f.read()
with open("controller/ac_outlet.kicad_sym", "r") as f:
    ac_outlet_symbol = f.read()
with open("controller/thermocouple_conn.kicad_sym", "r") as f:
    thermocouple_conn_symbol = f.read()


# Main schematic template
schematic_template = """(kicad_sch (version 20231120) (generator "gemini-script")
  (uuid "{uuid}")
  (paper "A3")
  (title_block
    (title "Induction Temperature Controller")
    (company "Project Author")
    (rev "1")
    (date "2025-11-27")
  )
  (lib_symbols
    {lib_symbols}
  )
  {symbols}
)
"""

# Symbol instance template
symbol_template = """
  (symbol (lib_id "{lib_id}") (at {x} {y} 0) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid "{uuid}")
    (property "Reference" "{reference}" (at {x_ref} {y_ref} 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "{value}" (at {x_val} {y_val} 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
  )
"""

# Generate the final schematic
lib_symbols = (resistor_symbol + "\n" + capacitor_symbol + "\n" + esp32_symbol + 
               "\n" + max31856_symbol + "\n" + oled_symbol + "\n" + rotary_encoder_symbol + 
               "\n" + ssr_symbol + "\n" + usb_c_symbol + "\n" + iec_c14_symbol + 
                "\n" + fuse_symbol + "\n" + ac_outlet_symbol + "\n" + thermocouple_conn_symbol)

resistor_instance = symbol_template.format(
    lib_id="R",
    x=190,
    y=140,
    uuid=generate_uuid(),
    reference="R1",
    x_ref=190.635,
    y_ref=142.54,
    value="330",
    x_val=190.635,
    y_val=137.46,
)

capacitor_instance = symbol_template.format(
    lib_id="C",
    x=60,
    y=70,
    uuid=generate_uuid(),
    reference="C1",
    x_ref=60.635,
    y_ref=72.54,
    value="100µF",
    x_val=60.635,
    y_val=67.46,
)

esp32_instance = symbol_template.format(
    lib_id="ESP32-DevKitC",
    x=100,
    y=120,
    uuid=generate_uuid(),
    reference="U1",
    x_ref=100.635,
    y_ref=122.54,
    value="ESP32-DevKitC",
    x_val=100.635,
    y_val=117.46,
)

max31856_instance = symbol_template.format(
    lib_id="MAX31856",
    x=120,
    y=180,
    uuid=generate_uuid(),
    reference="U2",
    x_ref=120.635,
    y_ref=182.54,
    value="MAX31856",
    x_val=120.635,
    y_val=177.46,
)

oled_instance = symbol_template.format(
    lib_id="SSD1306",
    x=80,
    y=80,
    uuid=generate_uuid(),
    reference="DISP1",
    x_ref=80.635,
    y_ref=82.54,
    value="SSD1306",
    x_val=80.635,
    y_val=77.46,
)

rotary_encoder_instance = symbol_template.format(
    lib_id="RotaryEncoder_Switch",
    x=80,
    y=100,
    uuid=generate_uuid(),
    reference="SW1",
    x_ref=80.635,
    y_ref=102.54,
    value="Rotary Encoder",
    x_val=80.635,
    y_val=97.46,
)

ssr_instance = symbol_template.format(
    lib_id="ASSR-1218",
    x=200,
    y=140,
    uuid=generate_uuid(),
    reference="SSR1",
    x_ref=200.635,
    y_ref=142.54,
    value="ASSR-1218",
    x_val=200.635,
    y_val=137.46,
)

usb_c_instance = symbol_template.format(
    lib_id="USB_C_Receptacle",
    x=50,
    y=60,
    uuid=generate_uuid(),
    reference="J1",
    x_ref=50.635,
    y_ref=62.54,
    value="USB-C",
    x_val=50.635,
    y_val=57.46,
)

iec_c14_instance = symbol_template.format(
    lib_id="IEC_60320_C14_Receptacle",
    x=280,
    y=60,
    uuid=generate_uuid(),
    reference="J3",
    x_ref=280.635,
    y_ref=62.54,
    value="IEC C14",
    x_val=280.635,
    y_val=57.46,
)

fuse_instance = symbol_template.format(
    lib_id="Fuse",
    x=300,
    y=60,
    uuid=generate_uuid(),
    reference="F1",
    x_ref=300.635,
    y_ref=62.54,
    value="10A",
    x_val=300.635,
    y_val=57.46,
)

ac_outlet_instance = symbol_template.format(
    lib_id="Conn_01x02",
    x=330,
    y=60,
    uuid=generate_uuid(),
    reference="J4",
    x_ref=330.635,
    y_ref=62.54,
    value="AC Outlet",
    x_val=330.635,
    y_val=57.46,
)

thermocouple_conn_instance = symbol_template.format(
    lib_id="Conn_01x02",
    x=120,
    y=200,
    uuid=generate_uuid(),
    reference="J2",
    x_ref=120.635,
    y_ref=202.54,
    value="Thermocouple",
    x_val=120.635,
    y_val=197.46,
)

symbols = (resistor_instance + "\n" + capacitor_instance + "\n" + esp32_instance + 
           "\n" + max31856_instance + "\n" + oled_instance + "\n" + rotary_encoder_instance + 
           "\n" + ssr_instance + "\n" + usb_c_instance + "\n" + iec_c14_instance + 
            "\n" + fuse_instance + "\n" + ac_outlet_instance + "\n" + thermocouple_conn_instance)

schematic_content = schematic_template.format(
    uuid=generate_uuid(),
    lib_symbols=lib_symbols,
    symbols=symbols
)

# Write the schematic to a file
output_file = "controller/controller-generated.kicad_sch"
with open(output_file, "w") as f:
    f.write(schematic_content)

print(f"Schematic written to {output_file}")
