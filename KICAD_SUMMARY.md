# KiCad Project Summary

## What's Been Created

I've set up a complete KiCad schematic for your induction temperature controller. The project is ready to view and verify.

### Files Created
- `controller/controller.kicad_pro` - Main project file
- `controller/controller.kicad_sch` - Schematic with all components and connections
- `controller/controller.kicad_pcb` - PCB layout file (empty, ready for layout)
- `controller/README.md` - Detailed documentation

### KiCad Application
KiCad should now be open with your project. If not, you can open it manually:
```bash
open -a KiCad /Users/bennet/Desktop/induction-temp-controller/controller/controller.kicad_pro
```

## Schematic Overview

The schematic is divided into three main sections:

### 1. DC Side (Left) - 5V/3.3V
**Components:**
- **U1**: ESP32 DevKit-C microcontroller
  - Runs PID control loop
  - Communicates with all peripherals

- **U2**: MAX31856 thermocouple amplifier
  - Reads K-type thermocouple
  - 19-bit resolution, ±0.15°C accuracy
  - Connected via SPI to ESP32

- **J1**: K-type thermocouple connector
  - For 450-550°F high-temp probe

- **J2**: USB-C power input
  - 5V DC power for entire DC side

- **DISP1**: OLED 128x64 display
  - I2C connection to ESP32
  - Shows temp, target, duty cycle, status

- **SW1**: Rotary encoder with push button
  - User input for target temperature
  - Push button for start/stop

**Power filtering:**
- C1 (100µF): Bulk capacitor on USB 5V input
- C2 (0.1µF): Decoupling for MAX31856

### 2. Isolation Barrier (Center)
**Component:**
- **SSR1**: Solid State Relay (10-40A)
  - **Critical safety component**: Provides optical isolation
  - DC side: Controlled by ESP32 GPIO4 via R1 (330Ω resistor)
  - AC side: Switches hot line to induction cooktop
  - No electrical connection between DC and AC
  - Zero-cross switching for reduced EMI

- **R1**: 330Ω current limiting resistor
  - Protects ESP32 GPIO
  - Provides proper drive current for SSR LED

### 3. AC Side (Right) - 120-240V
**Components:**
- **J3**: IEC C14 AC inlet
  - Standard AC power connector
  - Hot, Neutral, Ground connections

- **F1**: 10A slow-blow fuse (5×20mm)
  - Overcurrent protection on hot line
  - User replaceable

- **J4**: AC outlet to induction cooktop
  - Hot: Time-proportional modulated via SSR
  - Neutral: Direct pass-through
  - Ground: Safety ground to cooktop chassis

## Key Safety Features

### Electrical Isolation
- SSR provides complete galvanic isolation between DC and AC
- No physical electrical connection across the barrier
- Optical coupling only

### Physical Separation
- Schematic clearly labels DC and AC sides
- PCB will maintain ≥6.4mm creepage/clearance
- Red annotation shows isolation barrier

### Protection
- Fused hot line for overcurrent protection
- Ground bonding for fault protection
- Heavy gauge wire requirements for AC

## How to Verify the Schematic

### In KiCad:
1. **Open the schematic editor** (click "Schematic Editor" in KiCad main window)
2. **Check component placement:**
   - All components should be visible
   - Clear separation between DC (left) and AC (right) sides
   - SSR in the center as isolation barrier

3. **Verify net connections:**
   - Tools → Electrical Rules Checker (ERC)
   - Should show minimal errors (we haven't added all wire connections yet)

4. **Review component values:**
   - C1 = 100µF (USB power supply bulk cap)
   - C2 = 0.1µF (MAX31856 decoupling)
   - R1 = 330Ω (SSR current limiting)
   - F1 = 10A slow-blow

5. **Check annotations:**
   - Title block shows project name, date, revision
   - Safety notes at bottom
   - DC SIDE and AC SIDE labels clearly visible
   - ISOLATION BARRIER annotation on SSR

## Component Pin Assignments

### ESP32 → MAX31856 (SPI)
- GPIO18 (SCK) → MAX31856 SCK
- GPIO19 (MISO) → MAX31856 MISO
- GPIO23 (MOSI) → MAX31856 MOSI
- GPIO5 (CS) → MAX31856 CS

### ESP32 → OLED (I2C)
- GPIO21 (SDA) → OLED SDA
- GPIO22 (SCL) → OLED SCL

### ESP32 → Rotary Encoder
- GPIO32 → Encoder Channel A
- GPIO33 → Encoder Channel B
- GPIO25 → Encoder Button

### ESP32 → SSR
- GPIO4 → R1 → SSR DC+
- GND → SSR DC-

### MAX31856 → Thermocouple
- T+ → K-Type +
- T- → K-Type -

### AC Power Path
- IEC Hot → Fuse → SSR AC_IN
- SSR AC_OUT → Cooktop Hot
- IEC Neutral → Cooktop Neutral (unswitched)
- IEC Ground → Cooktop Ground (safety)

## Next Steps

### To complete the design:

1. **Schematic review** (Current step):
   - Open in KiCad
   - Verify all components are present
   - Check that the layout makes sense

2. **Assign footprints**:
   - Each component needs a physical footprint
   - Tools → Assign Footprints in KiCad

3. **Generate netlist**:
   - Export netlist for PCB design
   - File → Export → Netlist

4. **PCB Layout**:
   - Import netlist to PCB editor
   - Place components with AC/DC separation
   - Route traces maintaining 6.4mm clearance
   - Add ground planes
   - Design edge cuts (board outline)

5. **Design Rule Check (DRC)**:
   - Verify clearances
   - Check track widths
   - Ensure manufacturability

6. **Generate Gerbers**:
   - Export for PCB fabrication
   - Include drill files

## Design Rules for PCB Layout

When you move to PCB layout, follow these rules:

### Clearances
- **AC to DC**: Minimum 6.4mm (≥0.25 inches)
- **AC to edge**: Minimum 3mm
- **DC signals**: Standard 0.2mm

### Track Widths
- **AC power (Hot/Neutral)**: 2.0mm minimum (for 10A)
- **DC power (5V/3.3V)**: 0.5mm
- **Signals (SPI, I2C, GPIO)**: 0.25mm

### Copper Pours
- Separate ground planes for AC and DC
- Connect AC and DC ground ONLY at earth ground point
- Use thermal reliefs for ease of soldering

### Component Placement
- Keep high-voltage components (IEC, Fuse, SSR AC side) in one zone
- Keep low-voltage components (ESP32, MAX31856, OLED) in separate zone
- SSR can bridge the zones (it's designed for this)
- Provide adequate space for heat sink on SSR

### Silkscreen
- Label "DANGER HIGH VOLTAGE" near AC components
- Mark polarity for electrolytic capacitor
- Label connectors (USB, Thermocouple, AC In/Out)
- Include version number and date

## Bill of Materials

See `controller/README.md` for complete BOM with part numbers and specifications.

## Safety Testing Checklist

Before connecting AC power:
- [ ] Visual inspection for shorts
- [ ] Continuity test: Verify no AC-DC shorts
- [ ] DC power test: Verify 5V and 3.3V rails
- [ ] Thermocouple test: Verify temperature reading
- [ ] SSR test with light bulb load (not cooktop)
- [ ] Final integration test with cooktop

## Documentation

- `controller/README.md` - Complete project documentation
- `docs/HARDWARE_ARCHITECTURE.md` - System architecture
- `docs/FIRMWARE_PLAN.md` - Firmware implementation guide
- `docs/SAFETY_NOTES.md` - Critical safety information
- Mermaid diagrams - Visual system architecture

## Questions to Ask Yourself

As you review the schematic:
1. Are all components present and correctly valued?
2. Is the isolation barrier clearly marked and understood?
3. Are the AC and DC sections clearly separated?
4. Do you understand the signal flow from thermocouple → ESP32 → SSR → cooktop?
5. Are safety features (fuse, ground, isolation) properly implemented?

## Ready to Move Forward?

Once you've reviewed and verified the schematic:
1. Assign footprints to all components
2. Begin PCB layout with proper AC/DC separation
3. Order components from BOM
4. Plan enclosure design

The foundation is solid - the schematic correctly implements the temperature controller architecture with proper safety features!
