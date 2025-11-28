# KiCad Schematic Generation Plan

## Tools Discovered

### 1. kicad-skip (Recommended)
- **Purpose**: Python library for manipulating KiCad S-expression files
- **Capabilities**: Load, modify, and generate KiCad schematics programmatically
- **Link**: https://github.com/psychogenic/kicad-skip
- **Status**: Active development (2024)

### 2. SKiDL
- **Purpose**: Python-based schematic design language
- **Capabilities**: Programmatic circuit design, generates netlists
- **Link**: https://pypi.org/project/skidl/
- **Note**: Currently supports KiCad V5 format (may need updates for V9)

### 3. Official KiCad Documentation
- **S-Expression Format**: https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/index.html
- **File Format Guide**: Complete specification for .kicad_sch files

## Step-by-Step Implementation Plan

### Phase 1: Setup and Research (Current)
1. ✅ Install Python 3 (available: 3.13.2)
2. ⏳ Install kicad-skip library
3. ⏳ Study KiCad symbol definitions for our components

### Phase 2: Component Library
Extract or define symbols for:
- USB-C connector (power input)
- ESP32-DevKit-C module (microcontroller)
- MAX31856 (thermocouple amplifier)
- OLED display (I2C)
- Rotary encoder (user input)
- SSR (solid state relay)
- Resistor (330Ω current limiting)
- Capacitors (100µF, 0.1µF)
- IEC C14 connector (AC inlet)
- Fuse holder (10A)
- AC outlet connector (to cooktop)
- Thermocouple connector (K-type)

### Phase 3: Schematic Structure
Create base schematic with:
- Version: 20231120 (KiCad 9.0)
- Paper: A3
- Title block with project info
- Empty lib_symbols section (will populate)

### Phase 4: Component Placement

#### DC Side (Left, x=50-150mm)
- J1 (USB-C): Position at (50, 60)
- C1 (100µF): Near J1 at (60, 70)
- U1 (ESP32): Center at (100, 120)
- U2 (MAX31856): Position at (120, 180)
- J2 (Thermocouple): Below MAX31856 at (120, 200)
- C2 (0.1µF): Near MAX31856 at (130, 180)
- DISP1 (OLED): Above ESP32 at (80, 80)
- SW1 (Encoder): Above ESP32 at (80, 100)

#### Isolation Barrier (Center, x=190-210mm)
- R1 (330Ω): At (190, 140)
- SSR1: At (200, 140)

#### AC Side (Right, x=260-350mm)
- J3 (IEC C14): At (280, 60)
- F1 (Fuse): At (300, 60)
- J4 (Cooktop): At (330, 60)

### Phase 5: Wiring Connections

#### Power Distribution
- USB-C VBUS → +5V net
- USB-C GND → GND net
- ESP32 3V3 → +3V3 net
- All component power pins to appropriate nets

#### SPI Bus (ESP32 ↔ MAX31856)
- ESP32 GPIO18 → MAX31856 SCK
- ESP32 GPIO19 → MAX31856 MISO
- ESP32 GPIO23 → MAX31856 MOSI
- ESP32 GPIO5 → MAX31856 CS

#### I2C Bus (ESP32 ↔ OLED)
- ESP32 GPIO21 → OLED SDA
- ESP32 GPIO22 → OLED SCL

#### User Input (Encoder)
- ESP32 GPIO32 → Encoder A
- ESP32 GPIO33 → Encoder B
- ESP32 GPIO25 → Encoder Button

#### SSR Control
- ESP32 GPIO4 → R1 pin 1
- R1 pin 2 → SSR DC+
- GND → SSR DC-

#### AC Power Path
- IEC HOT → F1 → SSR AC_IN
- SSR AC_OUT → Cooktop HOT
- IEC NEUTRAL → Cooktop NEUTRAL (direct)
- IEC GROUND → Cooktop GROUND (safety)

### Phase 6: Component Annotation
Assign reference designators:
- C1, C2 (capacitors)
- R1 (resistor)
- U1 (ESP32)
- U2 (MAX31856)
- J1, J2, J3, J4 (connectors)
- DISP1 (OLED)
- SW1 (encoder)
- SSR1 (relay)
- F1 (fuse)

### Phase 7: Validation
1. Write complete .kicad_sch file
2. Open in KiCad
3. Run ERC (Electrical Rules Checker)
4. Fix any errors
5. Verify all connections

## Implementation Approach

### Option A: kicad-skip Library (Preferred)
```python
from kicad_skip import Schematic, Symbol, Wire, Net

# Create schematic
sch = Schematic("controller.kicad_sch")
sch.set_title_block(title="Induction Temperature Controller", ...)

# Add components
esp32 = sch.add_symbol("ESP32-DevKit-C", ref="U1", x=100, y=120)
max31856 = sch.add_symbol("MAX31856", ref="U2", x=120, y=180)

# Connect with wires
sch.add_wire(esp32.pin("GPIO18"), max31856.pin("SCK"))
```

### Option B: Direct S-Expression Generation
- Manually construct S-expression strings
- Use templates for components
- Generate UUIDs for all elements
- Write complete file structure

### Option C: Hybrid Approach (Most Practical)
1. Use kicad-skip for structure
2. Manually define complex symbols if needed
3. Generate core components programmatically
4. Validate and refine in KiCad

## Sources

- [Scripting for KiCad Schematics in Python](https://inductive-kickback.com/2024/02/scripting-for-kicad-schematics-in-python/)
- [kicad-skip GitHub](https://github.com/psychogenic/kicad-skip)
- [SKiDL Documentation](https://devbisme.github.io/skidl/)
- [KiCad S-Expression Format](https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/index.html)
- [KiCad File Formats](https://dev-docs.kicad.org/en/file-formats/)
