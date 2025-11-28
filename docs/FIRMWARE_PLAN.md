# Firmware Plan

## High-Level Architecture

loop:
read_thermocouple()
pid_output = PID(target, measured)
duty = clamp(pid_output, 0.0, 1.0)
drive_SSR(duty)
update_display()

---

## PID Timing Details

- Use **time-proportional control**
- 200ms windows
- SSR ON for (duty * window)
- SSR OFF for remainder
- Avoid high-frequency PWM (SSR cannot switch fast)

---

## UI Flow

- Encoder rotates to change target temp
- Push to toggle run/stop
- OLED displays:
  - Current temp
  - Target temp
  - Duty cycle %
  - System status

---

## Libraries

- Arduino or ESP-IDF
- Adafruit MAX31856
- PID library or custom PID

---

## Future Upgrades
- WiFi logging (Influx/Grafana)
- Web UI
- Pan thermal mass modeling
- Auto-tune PID

