# KiCad Getting Started

## 1. Create Project

Open KiCad → File → New Project  
Save into: `kicad/controller.kicad_pro`

---

## 2. Create Hierarchical Sheets

Suggested structure:

/Schematic
├── System_Block_Diagram
├── MCU_and_IO
├── SSR_and_AC
├── Power_5V_3V3
├── Thermocouple_Input
└── UI_Display_Encoder

---

## 3. Add Symbols

Use built-in libs for:
- ESP32 DevKit
- MAX31856 breakout
- Screw terminals
- SSR footprint (create custom if needed)

---

## 4. PCB Layout

Important:
- Keep AC and DC zones far apart
- Use thick traces for AC (≥2mm)
- Add isolation slots if needed
- Use ground pours for DC side
- Add standoffs for enclosure mounting

---

## 5. DRC + ERC

Run both early and often:
- ERC for schematic errors
- DRC for PCB spacing and routing

