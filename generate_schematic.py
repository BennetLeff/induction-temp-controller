import uuid
import re

def generate_uuid():
    return str(uuid.uuid4())

def extract_symbol_definition(library_content, symbol_name):
    """
    Extracts the s-expression definition of a specific symbol from the library content.
    """
    pattern = re.compile(r"\(symbol \"" + re.escape(symbol_name) + r"\"[\s\S]*?\)\s*\)", re.MULTILINE)
    match = pattern.search(library_content)
    if match:
        return match.group(0)
    return None

# Read full library files
with open("kicad-symbols-repo/Device.kicad_sym", "r", encoding="utf-8") as f:
    device_lib_content = f.read()
with open("kicad-symbols-repo/Sensor_Temperature.kicad_sym", "r", encoding="utf-8") as f:
    sensor_temp_lib_content = f.read()
with open("kicad-symbols-repo/Connector.kicad_sym", "r", encoding="utf-8") as f:
    connector_lib_content = f.read()
with open("kicad-symbols-repo/Relay_SolidState.kicad_sym", "r", encoding="utf-8") as f:
    relay_ss_lib_content = f.read()
with open("temp-espressif-library/symbols/Espressif.kicad_sym", "r", encoding="utf-8") as f:
    esp_lib_content = f.read()
with open("temp-oled-library/SSD1306_OLED-0.91-128x32.kicad_sym", "r", encoding="utf-8") as f:
    oled_lib_content = f.read()
with open("kicad-symbols-repo/power.kicad_sym", "r", encoding="utf-8") as f:
    power_lib_content = f.read()


# Extract specific symbol definitions
resistor_symbol = extract_symbol_definition(device_lib_content, "R")
capacitor_symbol = extract_symbol_definition(device_lib_content, "C")
rotary_encoder_symbol = extract_symbol_definition(device_lib_content, "RotaryEncoder_Switch")
fuse_symbol = extract_symbol_definition(device_lib_content, "Fuse")
max31856_symbol = extract_symbol_definition(sensor_temp_lib_content, "MAX31856")
usb_c_symbol = extract_symbol_definition(connector_lib_content, "USB_C_Receptacle")
iec_c14_symbol = extract_symbol_definition(connector_lib_content, "IEC_60320_C14_Receptacle")
ssr_symbol = extract_symbol_definition(relay_ss_lib_content, "ASSR-1218")
esp32_symbol = extract_symbol_definition(esp_lib_content, "ESP32-DevKitC")
oled_symbol = extract_symbol_definition(oled_lib_content, "SSD1306")

# Power Symbols
power_5v_symbol = extract_symbol_definition(power_lib_content, "+5V")
power_gnd_symbol = extract_symbol_definition(power_lib_content, "GND")
power_3v3_symbol = extract_symbol_definition(power_lib_content, "+3V3")


# Manually created symbols
thermocouple_connector_symbol = """(symbol \"Thermocouple_Connector\"
    (property \"Reference\" \"J\" (at 0 2.921 0)
      (effects (font (size 1.27 1.27)))
    )
    (property \"Value\" \"Thermocouple_Connector\" (at 0 -2.921 0)
      (effects (font (size 1.27 1.27)))
    )
    (property \"Footprint\" \"\" (at 0 0 0)
      (effects (font (size 1.27 1.27)) (hide))
    )
    (property \"Datasheet\" \"~\" (at 0 0 0)
      (effects (font (size 1.27 1.27)) (hide))
    )
    (symbol \"Thermocouple_Connector_1_1\"
      (pin passive line (at 0 2.54 270) (length 2.54)
        (name \"T+\" (effects (font (size 1.27 1.27))))
        (number \"1\" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -2.54 90) (length 2.54)
        (name \"T-\" (effects (font (size 1.27 1.27))))
        (number \"2\" (effects (font (size 1.27 1.27))))
      )
    )
  )"""

ac_outlet_connector_symbol = """(symbol \"AC_Outlet_Connector\"
    (property \"Reference\" \"J\" (at 0 2.921 0)
      (effects (font (size 1.27 1.27)))
    )
    (property \"Value\" \"AC_Outlet_Connector\" (at 0 -2.921 0)
      (effects (font (size 1.27 1.27)))
    )
    (property \"Footprint\" \"\" (at 0 0 0)
      (effects (font (size 1.27 1.27)) (hide))
    )
    (property \"Datasheet\" \"~\" (at 0 0 0)
      (effects (font (size 1.27 1.27)) (hide))
    )
    (symbol \"AC_Outlet_Connector_1_1\"
      (pin power_in line (at 0 2.54 270) (length 2.54)
        (name \"Hot\" (effects (font (size 1.27 1.27))))
        (number \"1\" (effects (font (size 1.27 1.27))))
      )
      (pin power_in line (at 0 0 270) (length 2.54)
        (name \"Neutral\" (effects (font (size 1.27 1.27))))
        (number \"2\" (effects (font (size 1.27 1.27))))
      )
      (pin power_in line (at 0 -2.54 270) (length 2.54)
        (name \"Ground\" (effects (font (size 1.27 1.27))))
        (number \"3\" (effects (font (size 1.27 1.27))))
      )
    )
  )"""

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
  {graphic_elements}
  {wires}
  {net_labels}
)
"""

# Symbol instance template
symbol_instance_template = """
  (symbol (lib_id "{lib_id}") (at {x} {y} {rotation}) (unit 1)
    (in_bom yes) (on_board yes)
    (uuid "{uuid}")
    (property "Reference" "{reference}" (at {x_ref} {y_ref} {ref_rot})
      (effects (font (size 1.27 1.27)) (justify {ref_justify}))
    )
    (property "Value" "{value}" (at {x_val} {y_val} {val_rot})
      (effects (font (size 1.27 1.27)) (justify {val_justify}))
    )
  )"""

# Text annotation template
text_template = """
  (text "{text}" (at {x} {y} {rotation})
    (effects (font (size {font_size} {font_size}) (bold {bold})) (justify {justify}))
  )"""

# Power symbol template (simplified as they usually don't have Ref/Value properties displayed)
power_symbol_template = """
  (symbol (lib_id "{lib_id}") (at {x} {y} {rotation}) (unit 1)
    (in_bom no) (on_board no)
    (uuid "{uuid}")
  )"""

# Wire template
wire_template = """
  (wire (pts (xy {x1} {y1}) (xy {x2} {y2}))
    (stroke (width 0.2032) (type default) (color 0 0 0 0))
  )"""

# Net label template
net_label_template = """
  (label "{label}" (at {x} {y} {rotation})
    (effects (font (size 1.27 1.27)) (justify {justify}))
  )"""

# Collect all unique symbol definitions
lib_symbols_content = "\n".join(filter(None, [
    resistor_symbol, capacitor_symbol, esp32_symbol, max31856_symbol, oled_symbol,
    rotary_encoder_symbol, ssr_symbol, usb_c_symbol, iec_c14_symbol, fuse_symbol,
    ac_outlet_connector_symbol, thermocouple_connector_symbol,
    power_5v_symbol, power_gnd_symbol, power_3v3_symbol
]))

# Create instances with refined coordinates
resistor_instance = symbol_instance_template.format(
    lib_id="R", x=177.8, y=127, rotation=0, uuid=generate_uuid(),
    reference="R1", x_ref=177.8+0.635, y_ref=127+2.54, ref_rot=0, ref_justify="left", 
    value="330", x_val=177.8+0.635, y_val=127-2.54, val_rot=0, val_justify="left",
)
capacitor_instance = symbol_instance_template.format(
    lib_id="C", x=50.8, y=76.2, rotation=0, uuid=generate_uuid(),
    reference="C1", x_ref=50.8+0.635, y_ref=76.2+2.54, ref_rot=0, ref_justify="left", 
    value="100µF", x_val=50.8+0.635, y_val=76.2-2.54, val_rot=0, val_justify="left",
)
esp32_instance = symbol_instance_template.format(
    lib_id="ESP32-DevKitC", x=101.6, y=101.6, rotation=0, uuid=generate_uuid(),
    reference="U1", x_ref=101.6+0.635, y_ref=101.6+2.54, ref_rot=0, ref_justify="left", 
    value="ESP32-DevKitC", x_val=101.6+0.635, y_val=101.6-2.54, val_rot=0, val_justify="left",
)
max31856_instance = symbol_instance_template.format(
    lib_id="MAX31856", x=127, y=152.4, rotation=0, uuid=generate_uuid(),
    reference="U2", x_ref=127+0.635, y_ref=152.4+2.54, ref_rot=0, ref_justify="left", 
    value="MAX31856", x_val=127+0.635, y_val=152.4-2.54, val_rot=0, val_justify="left",
)
oled_instance = symbol_instance_template.format(
    lib_id="SSD1306", x=76.2, y=50.8, rotation=0, uuid=generate_uuid(),
    reference="DISP1", x_ref=76.2+0.635, y_ref=50.8+2.54, ref_rot=0, ref_justify="left", 
    value="SSD1306", x_val=76.2+0.635, y_val=50.8-2.54, val_rot=0, val_justify="left",
)
rotary_encoder_instance = symbol_instance_template.format(
    lib_id="RotaryEncoder_Switch", x=76.2, y=76.2, rotation=0, uuid=generate_uuid(),
    reference="SW1", x_ref=76.2+0.635, y_ref=76.2+2.54, ref_rot=0, ref_justify="left", 
    value="Rotary Encoder", x_val=76.2+0.635, y_val=76.2-2.54, val_rot=0, val_justify="left",
)
ssr_instance = symbol_instance_template.format(
    lib_id="ASSR-1218", x=203.2, y=127, rotation=0, uuid=generate_uuid(),
    reference="SSR1", x_ref=203.2+0.635, y_ref=127+2.54, ref_rot=0, ref_justify="left", 
    value="ASSR-1218", x_val=203.2+0.635, y_val=127-2.54, val_rot=0, val_justify="left",
)
usb_c_instance = symbol_instance_template.format(
    lib_id="USB_C_Receptacle", x=50.8, y=63.5, rotation=0, uuid=generate_uuid(),
    reference="J1", x_ref=50.8+0.635, y_ref=63.5+2.54, ref_rot=0, ref_justify="left", 
    value="USB-C", x_val=50.8+0.635, y_val=63.5-2.54, val_rot=0, val_justify="left",
)
iec_c14_instance = symbol_instance_template.format(
    lib_id="IEC_60320_C14_Receptacle", x=279.4, y=63.5, rotation=0, uuid=generate_uuid(),
    reference="J3", x_ref=279.4+0.635, y_ref=63.5+2.54, ref_rot=0, ref_justify="left", 
    value="IEC C14", x_val=279.4+0.635, y_val=63.5-2.54, val_rot=0, val_justify="left",
)
fuse_instance = symbol_instance_template.format(
    lib_id="Fuse", x=304.8, y=63.5, rotation=0, uuid=generate_uuid(),
    reference="F1", x_ref=304.8+0.635, y_ref=63.5+2.54, ref_rot=0, ref_justify="left", 
    value="10A", x_val=304.8+0.635, y_val=63.5-2.54, val_rot=0, val_justify="left",
)
ac_outlet_instance = symbol_instance_template.format(
    lib_id="AC_Outlet_Connector", x=330.2, y=63.5, rotation=0, uuid=generate_uuid(),
    reference="J4", x_ref=330.2+0.635, y_ref=63.5+2.54, ref_rot=0, ref_justify="left", 
    value="AC Outlet Connector", x_val=330.2+0.635, y_val=63.5-2.54, val_rot=0, val_justify="left",
)
thermocouple_conn_instance = symbol_instance_template.format(
    lib_id="Thermocouple_Connector", x=127, y=177.8, rotation=0, uuid=generate_uuid(),
    reference="J2", x_ref=127+0.635, y_ref=177.8+2.54, ref_rot=0, ref_justify="left", 
    value="Thermocouple Connector", x_val=127+0.635, y_val=177.8-2.54, val_rot=0, val_justify="left",
)

# Power symbol instances
power_5v_instance = power_symbol_template.format(
    lib_id="+5V", x=45.72, y=91.44, rotation=270, uuid=generate_uuid(), # Near J1, ESP32
)
power_gnd_instance_1 = power_symbol_template.format(
    lib_id="GND", x=45.72, y=104.14, rotation=90, uuid=generate_uuid(), # Near J1, C1
)
power_gnd_instance_2 = power_symbol_template.format(
    lib_id="GND", x=101.6, y=190.5, rotation=90, uuid=generate_uuid(), # Near ESP32, MAX31856, J2
)
power_3v3_instance = power_symbol_template.format(
    lib_id="+3V3", x=114.3, y=86.36, rotation=270, uuid=generate_uuid(), # Near ESP32, MAX31856
)


all_symbol_instances = "\n".join(filter(None, [
    resistor_instance, capacitor_instance, esp32_instance, max31856_instance, oled_instance,
    rotary_encoder_instance, ssr_instance, usb_c_instance, iec_c14_instance, fuse_instance,
    ac_outlet_instance, thermocouple_conn_instance,
    power_5v_instance, power_gnd_instance_1, power_gnd_instance_2, power_3v3_instance
]))

# Text annotations
dc_side_text = text_template.format(
    text="DC SIDE - LOW VOLTAGE (5V/3V3)", x=101.6, y=40.64, rotation=0, font_size=2.54, bold="yes", justify="center"
)
isolation_text = text_template.format(
    text="ISOLATION BARRIER >=6.4mm clearance", x=203.2, y=40.64, rotation=0, font_size=2.54, bold="yes", justify="center"
)
ac_side_text = text_template.format(
    text="AC SIDE - HIGH VOLTAGE (120-240V) ⚡ DANGER ⚡", x=304.8, y=40.64, rotation=0, font_size=2.54, bold="yes", justify="center"
)

# Graphic elements (rectangles for visual delineation)
graphic_elements = f"""
  (gr_rect (start 38.1 30.48) (end 165.1 215.9) (stroke (width 0.254) (type solid) (color 0 0 0 0)) (fill (type none)))
  (gr_rect (start 177.8 30.48) (end 254 215.9) (stroke (width 0.254) (type solid) (color 0 0 0 0)) (fill (type none)))
  (gr_rect (start 266.7 30.48) (end 355.6 215.9) (stroke (width 0.254) (type solid) (color 0 0 0 0)) (fill (type none)))
"""

# Wires
wires = f"""
  {wire_template.format(x1=53.34, y1=63.5, x2=53.34, y2=76.2)} ; J1-1 to C1-1
  {wire_template.format(x1=53.34, y1=76.2, x2=53.34, y2=91.44)} ; C1-1 to +5V net
  {wire_template.format(x1=53.34, y1=91.44, x2=101.6, y2=91.44)} ; +5V net horizontal
  {wire_template.format(x1=101.6, y1=91.44, x2=101.6, y2=101.6)} ; +5V net to U1-19 (ESP32 5V)
  {wire_template.format(x1=53.34, y1=66.04, x2=53.34, y2=104.14)} ; J1-4 to GND net
  {wire_template.format(x1=53.34, y1=104.14, x2=101.6, y2=104.14)} ; GND net horizontal
  {wire_template.format(x1=101.6, y1=104.14, x2=101.6, y2=116.84)} ; GND net to U1-14 (ESP32 GND)
  {wire_template.format(x1=101.6, y1=101.6, x2=101.6, y2=86.36)} ; U1-1 (ESP32 3V3) to +3V3 net
  {wire_template.format(x1=101.6, y1=86.36, x2=127, y2=86.36)} ; +3V3 net to U2-5 (MAX31856 AVDD)
  {wire_template.format(x1=101.6, y1=104.14, x2=127, y2=104.14)} ; GND net to U2-1 (MAX31856 AGND)

  {wire_template.format(x1=101.6, y1=101.6-1.27*7, x2=127, y2=101.6-1.27*7)} ; ESP32 GPIO18 to SPI_SCK
  {wire_template.format(x1=101.6, y1=101.6-1.27*8, x2=127, y2=101.6-1.27*8)} ; ESP32 GPIO19 to SPI_MISO
  {wire_template.format(x1=101.6, y1=101.6-1.27*10, x2=127, y2=101.6-1.27*10)} ; ESP32 GPIO23 to SPI_MOSI
  {wire_template.format(x1=101.6, y1=101.6-1.27*4, x2=127, y2=101.6-1.27*4)} ; ESP32 GPIO5 to SPI_CS

  {wire_template.format(x1=101.6, y1=101.6-1.27*9, x2=76.2, y2=101.6-1.27*9)} ; ESP32 GPIO21 to I2C_SDA
  {wire_template.format(x1=101.6, y1=101.6-1.27*10, x2=76.2, y2=101.6-1.27*10)} ; ESP32 GPIO22 to I2C_SCL

  {wire_template.format(x1=101.6, y1=101.6+1.27*2, x2=76.2, y2=101.6+1.27*2)} ; ESP32 GPIO32 to ENC_A
  {wire_template.format(x1=101.6, y1=101.6+1.27*3, x2=76.2, y2=101.6+1.27*3)} ; ESP32 GPIO33 to ENC_B
  {wire_template.format(x1=101.6, y1=101.6-1.27*2, x2=76.2, y2=101.6-1.27*2)} ; ESP32 GPIO25 to ENC_SW

  {wire_template.format(x1=101.6, y1=101.6-1.27*5, x2=177.8, y2=101.6-1.27*5)} ; ESP32 GPIO4 to R1-1
  {wire_template.format(x1=177.8, y1=101.6-1.27*5, x2=177.8, y2=127)} ; R1-1 to R1
  {wire_template.format(x1=177.8, y1=127, x2=203.2, y2=127)} ; R1-2 to SSR1-1
  {wire_template.format(x1=203.2, y1=127, x2=203.2, y2=127+1.27*2)} ; SSR1-1 to SSR1
  {wire_template.format(x1=203.2, y1=127+1.27*3, x2=101.6, y2=127+1.27*3)} ; SSR1-2 to GND net

  {wire_template.format(x1=279.4, y1=63.5+1.27*2, x2=304.8, y2=63.5+1.27*2)} ; J3-1 to F1-1
  {wire_template.format(x1=304.8, y1=63.5+1.27*2, x2=304.8, y2=63.5)} ; F1-1 to F1
  {wire_template.format(x1=304.8, y1=63.5, x2=203.2, y2=63.5)} ; F1-2 to SSR1-3
  {wire_template.format(x1=203.2, y1=63.5, x2=203.2, y2=127)} ; SSR1-3 to SSR1
  {wire_template.format(x1=203.2, y1=127, x2=330.2, y2=127)} ; SSR1-4 to J4-1
  {wire_template.format(x1=279.4, y1=63.5, x2=330.2, y2=63.5)} ; J3-2 to J4-2
  {wire_template.format(x1=279.4, y1=63.5-1.27*2, x2=330.2, y2=63.5-1.27*2)} ; J3-3 to J4-3
"""

# Net Labels
net_labels = f"""
  {net_label_template.format(label="+5V", x=45.72-2.54, y=91.44, rotation=0, justify="left")}
  {net_label_template.format(label="GND", x=45.72-2.54, y=104.14, rotation=0, justify="left")}
  {net_label_template.format(label="+3V3", x=114.3-2.54, y=86.36, rotation=0, justify="left")}

  {net_label_template.format(label="SPI_SCK", x=101.6-2.54, y=101.6-1.27*7, rotation=0, justify="left")}
  {net_label_template.format(label="SPI_MISO", x=101.6-2.54, y=101.6-1.27*8, rotation=0, justify="left")}
  {net_label_template.format(label="SPI_MOSI", x=101.6-2.54, y=101.6-1.27*10, rotation=0, justify="left")}
  {net_label_template.format(label="SPI_CS", x=101.6-2.54, y=101.6-1.27*4, rotation=0, justify="left")}

  {net_label_template.format(label="I2C_SDA", x=76.2-2.54, y=101.6-1.27*9, rotation=0, justify="left")}
  {net_label_template.format(label="I2C_SCL", x=76.2-2.54, y=101.6-1.27*10, rotation=0, justify="left")}

  {net_label_template.format(label="ENC_A", x=76.2-2.54, y=101.6+1.27*2, rotation=0, justify="left")}
  {net_label_template.format(label="ENC_B", x=76.2-2.54, y=101.6+1.27*3, rotation=0, justify="left")}
  {net_label_template.format(label="ENC_SW", x=76.2-2.54, y=101.6-1.27*2, rotation=0, justify="left")}

  {net_label_template.format(label="SSR_CTRL", x=101.6-2.54, y=101.6-1.27*5, rotation=0, justify="left")}

  {net_label_template.format(label="AC_HOT", x=279.4-2.54, y=63.5+1.27*2, rotation=0, justify="left")}
  {net_label_template.format(label="AC_NEUTRAL", x=279.4-2.54, y=63.5, rotation=0, justify="left")}
  {net_label_template.format(label="AC_GND", x=279.4-2.54, y=63.5-1.27*2, rotation=0, justify="left")}
"""

schematic_content = schematic_template.format(
    uuid=generate_uuid(),
    lib_symbols=lib_symbols_content,
    symbols=all_symbol_instances,
    graphic_elements=f"{dc_side_text}{isolation_text}{ac_side_text}{graphic_elements}",
    wires=wires,
    net_labels=net_labels
)

# Write the schematic to a file
output_file = "controller/controller-generated.kicad_sch"
with open(output_file, "w") as f:
    f.write(schematic_content)

print(f"Schematic written to {output_file}")