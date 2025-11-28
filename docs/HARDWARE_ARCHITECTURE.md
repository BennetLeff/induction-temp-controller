# Hardware Architecture

## Top-Level Block Diagram

ESP32 → PWM (200ms windows) → SSR → AC Hot → Induction Cooker
↑
│
MAX31856 → K-Type Probe
OLED UI + Encoder

## Major Components

### 1. **ESP32 (DevKit-C or similar)**
- Reads thermocouple temperature
- Runs PID loop
- Outputs SSR control signal
- Drives OLED and encoder

### 2. **MAX31856**
- Thermocouple amplifier
- SPI interface
- Accurate to ±0.1–0.5°C

### 3. **SSR (Solid State Relay)**
- AC switching
- Optocoupled (safety)
- Zero-cross recommended
- 10A–40A rating

### 4. **K-type High-Temp Probe**
- 450–550°F capable
- Stainless braided sheath
- Screw-lock or bare-wire

### 5. **AC Side**
- IEC C14 or screw terminals
- Fuse holder (5×20mm)
- Earth-grounded chassis

### 6. **DC Side**
- USB-C 5V input
- 3.3V regulated rails
- DC ground plane

---

## KiCad Requirements

We will design:
- A PCB with separated **AC** and **DC** zones
- Wide copper for AC traces
- Creepage/clearance >= 6.4mm
- TVS diodes optional
- Mounting holes for SSR
