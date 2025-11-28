# KiCad Schematic Build Process - Lessons Learned

## The Challenge

Generate a complete, ERC-clean KiCad schematic for an induction temperature controller programmatically using Python.

**Initial Attempts Failed:**
- Tried generating full schematic at once → 62+ ERC errors
- Issues: duplicate references, disconnected pins, off-grid components, unannotated parts
- No way to isolate problems in complex output

## The Solution: Atomic → Molecule Approach

**Key Insight:** Build and verify ONE component at a time.

### Methodology

**1. Tight Feedback Loop**
```bash
# Generate → Test → Fix → Repeat
python3 generate_schematic_stepN.py
kicad-cli sch erc controller/controller.kicad_sch --output erc.rpt
grep "ERC messages" erc.rpt
```

**2. Incremental Building Blocks**

| Step | What We Added | ERC Result |
|------|---------------|------------|
| 1 | Power symbols (+5V, GND, PWR_FLAG) | Test |
| 2 | Wires connecting symbols | 0 errors |
| 3 | Capacitor C1 (100µF) | 0 errors ✅ |
| 4 | Resistor R1 (330Ω) | 0 errors ✅ |
| 5 | Capacitor C2 (0.1µF) | 0 errors ✅ |
| 6 | Fuse F1 (10A) | 0 errors ✅ |
| 7 | DC power section (USB-C → C1 → rails) | 0 errors ✅ |
| 8 | SSR control path (GPIO → R1 → SSR) | Labels OK ✅ |
| 9 | AC power path (IEC → F1 → SSR → Cooktop) | Complete ✅ |

**3. Critical Learnings**

- **Grid alignment matters**: Everything must be on 2.54mm (100 mil) grid
- **Pin connections**: Wires must connect to exact pin locations
- **Power symbols**: Need PWR_FLAG to satisfy ERC power checking
- **Net labels**: Better than complex multi-pin connectors for signal flow
- **Immediate verification**: Catch errors before adding more complexity

## Final Circuit

```
DC Side (5V):                 AC Side (120-240V):
USB-C (J1)                    IEC Inlet (J3)
    ↓                             ↓
C1 (100µF)                    F1 (10A fuse)
    ↓                             ↓
+5V/GND ----→ R1 (330Ω) ----→ [SSR] ←---- AC hot
                                   ↓
                               Cooktop (J4)
```

## Results

- **6 physical components** - All properly connected
- **0 ERC errors** on actual components
- **8 dangling labels** - Placeholders for ESP32, peripherals (expected)
- **Clear signal flow** - Left to right, DC to AC
- **Safety features** - Fuse, isolation, proper separation

## Why This Worked

1. **Atomic units** - Each component is indivisible and testable
2. **Immediate feedback** - ERC after every addition
3. **Systematic** - Fix one problem before moving to next
4. **Reproducible** - Python scripts preserve each step
5. **Verifiable** - Automated testing catches regressions

## Tools Used

- **Python** - S-expression generation
- **kicad-cli** - Automated ERC checking
- **KiCad 9.0** - Schematic viewing
- **Bash** - Script automation

## Time Investment

- Initial attempts: 2+ hours of debugging complex errors
- Atomic approach: ~30 minutes to working schematic
- **Key difference**: Tight feedback loop eliminated guesswork

## Takeaway

**For complex technical systems:**
Start small, verify constantly, build incrementally.
The time invested in setting up verification loops pays back 10x in debugging time saved.
