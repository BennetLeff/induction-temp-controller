# Induction Temperature Controller (External PID System)

This project builds an **external, PID-driven temperature controller** for consumer induction cooktops by using:

- A high-temp **K-type thermocouple**
- A **MAX31856** thermocouple amplifier
- An **ESP32** microcontroller
- A **Solid State Relay (SSR)**
- A custom **KiCad-designed PCB**
- A safe, grounded AC enclosure
- A PID control loop that performs **time-proportional AC power modulation**

This system allows precise control of pan or liquid temperature (±0.3–1°C) on any induction cooktop without modifying the cooktop itself.

---

## 🚀 Features
- External, safe, isolated AC power modulation with SSR
- PID loop controlling duty cycle of AC bursts
- OLED UI + rotary encoder input
- Support for high-temp probes (450–550°F)
- AC/DC isolation following best practices
- Upgrade path toward a fully custom Control-Freak-class cooker

---

## 📄 Documentation

All documentation lives in the `docs/` folder:

- [Project Overview](docs/PROJECT_OVERVIEW.md)
- [Hardware Architecture](docs/HARDWARE_ARCHITECTURE.md)
- [Firmware Plan](docs/FIRMWARE_PLAN.md)
- [KiCad Getting Started Guide](docs/KICAD_GETTING_STARTED.md)
- [Safety Notes](docs/SAFETY_NOTES.md)
- [Development Roadmap](docs/DEVELOPMENT_ROADMAP.md)
- [Glossary](docs/GLOSSARY.md)

---

## 🛠️ Quick Start

```bash
git clone https://github.com/YOURNAME/induction-temp-controller
cd induction-temp-controller
open docs/PROJECT_OVERVIEW.md

## 📜 License

MIT License.



---

# 📁 **FILE 2 — `docs/PROJECT_OVERVIEW.md`**

```markdown
# Project Overview

## What Are We Building?

We are building a **precision temperature controller** for induction cooktops using:

- Time-proportional **AC control** via SSR
- A microcontroller running **PID logic**
- High-temp K-type thermocouples
- Safe AC/DC isolation
- A custom PCB designed in KiCad

The idea:  
Control an induction cooker's heat output by modulating its AC input in small, rapid time windows (e.g., 200ms), turning the cooker into a PID-driven precision heating device similar to a Breville Control Freak.

---

## Why This Works

Induction cookers already regulate power internally using on/off bursts.  
By controlling how long AC is available during each window, we effectively control the **average power** delivered to the induction coil.

### Example (time-proportional control):

| Duty Cycle | Behavior |
|-----------|----------|
| 20% | Very low heat |
| 50% | Medium heat |
| 80% | High heat |

The PID loop adjusts duty cycle to match target temperature.

---

## Safety Model

- DC side (ESP32, sensors) is isolated from AC using an **optocoupled SSR**
- Only **hot** wire is switched
- Neutral + Ground pass through safely
- Enclosure separates AC and DC sections
- Cooktop’s internal safety systems remain active (pan detection, overheat protection)

---

## Build Phases

1. **Breadboard prototype**
2. **KiCad schematic + PCB design**
3. **Enclosure and AC wiring**
4. **Firmware development**
5. **Testing + calibration**
6. (Optional) Smart additions: WiFi logging, pan sensor, ramp profiles


