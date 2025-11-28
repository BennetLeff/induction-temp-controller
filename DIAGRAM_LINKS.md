# Mermaid Diagram Links - Induction Temperature Controller

All diagrams are now enhanced with detailed annotations explaining what each component does.

## 1. Hardware Architecture Diagram
**What's annotated:**
- **ESP32**: Runs PID, reads temp via SPI, drives SSR, WiFi capable
- **MAX31856**: Cold junction compensation, 19-bit ADC, ±0.15°C accuracy, SPI interface
- **K-Type Probe**: Measures pan/liquid temp, 450-550°F, stainless steel, fast response
- **SSR (Solid State Relay)**: AC/DC isolation barrier, zero-cross switching, optocoupled
- **OLED Display**: Shows current/target temp, duty cycle %, system status
- **Rotary Encoder**: Rotate to adjust target, push to start/stop
- **AC Components**: IEC inlet, fuse protection, hot/neutral/ground connections
- **Induction Cooktop**: Receives modulated AC, internal safety systems intact

**Connection annotations explain:**
- SPI communication (19-bit temp data)
- Critical optical isolation between ESP32 and SSR
- Time-proportional AC power delivery
- Ground safety connections

[Open Hardware Architecture Diagram](http://localhost:8000/edit#pako:eNqNV_9u2zYQfhXCRYEWqBrZqYPG2AoottMYzQ_Ddtptzv6gJdriKokaSSX1mgJ7i_6_J-heoX2TPck-krIsyylQIXGiO5J3x_vuu_PHVigi1uq1VpLmMZmd3GQEjyoWTnDTOqMyuqOSkUCGMdcs1IVkNy23rrF20CdTHjHypPv24PD54dun9XXmGU7Hh525_SQXPJQiFJmWIkmY_GkhD155nmf__vf3P2RSZIqMRwNSriGJEPlWy2ikiGZpTm45JdPxqFINJL9likynE3LHdUzG7y4q3RnNogTK69EBy0zokvAsL3S14B0_5SSkOV0kjCyFhNXVvier33cDuQh-OWy_7B7NN__YA2YxkyliKnJsDtJ8L6a-SCLyR5GFmosMgaU5yxQ1L9WS9rG34JoEuEvJlEiKHe3Xf_3n7e7XL31Cw7CQNFxXKlwBYtFMLmnIKuk5zxiV_C_E_MbT65wRUWgE3Ijn6nw4mJsPMuAqT-h6z_VpLO4UgU3JMm0vvqHSVK7Yg5qo0GsSrkNcyuOGSq0VNhClqS5UpRt1-gc74TS8HbrUzScCRteb130EQa1Zj9Doj0Lp0sFKOy5U3DOWpT5QugatCvERWwjkCtnfemY8kkWuvcigLHPoabh3PT2Z49frk-5b7NjAq-7aWNwxqVw9NIVRLQPWJlCAOCKylCIlQX8LlYCkPONpkRIJEO2AlGXRTfZgkU4BOSGblTmWYsHmb7yZgYh9sWZedH2v2_W_fjndC-GCUQUqUCSn2UHC_yx41Ei-pjxDsSHLmrGEqJhRHVfqU4qcYH8uMsWI5ukWtAMuwTO28Cn-KnhcT8IZX8WeLX1p7uWHog421NTu-F7nhb_PTaNhf45f0m-_-E7SEFAWARzIATGRbbEUhCHLtcLeQ5InxdbV00IhcbkUhjjrhfxaAlqRCTFraNq-1-4G-xk1jzlubj5I99vnjp-mez5e3TK5KdIHzLb9gKhE3HkLfGyB5xYq8KWsX_SULpkpXfBUwmlWo5VrBeaUDDgNmaHKhp_g3vlUJEDE1JQg2HoD6KtclwQZmUhf-MFeCEH_AOTHLeoNTS6olLwsb6P_jUnhoXcYYIHg0ZVqLl8KkopbSABLqdUu2qrl5EnH91P1dAspQJMAZO8RFJAsd1BlnjOh50g7_qBFSLaPDXs0glqsTfSVfAZce0hELqQJhiabdlY3fbsmK1qsmLl_Vs9KzmSyBtZUkTSQbp5LVmhJE-NX-e8-z1ClUKI6BtxWMUFLLf2stSQkl2ksCjmQw3WtxaLVZxXnN4w7AM-HuOW4fNm_FIef1VZrLcZwiiuyEFlUT90pLZIHQTspU2L7sbJn_lDNnwsaNau8L8R7kP18lEWF68Kl5PvVjoSpIgXei6x2O7YTmHyC_tApmj5XaoGCtFzlHK8FFTI7p6QictmtU3uAXRSAyE1LINWUtMd1jQt4_JigdPoVqSgnRjMinvfKtRsnshRvhZsJxsk3b0Z1jx7cIzM4D2fM2Eciqqn1sZxSIr7iGkFKTGNIpSs3M50gUegZ5axxXzdshwxzeNnke5uJw9BMiit3h7w2OeShIkUOo8wJp3ZMQD0sxc6Z5QBgj309Hl31XOs32c2LRJW7TwqtjQQ9xwmqZo7KXyFXqjq0us1-OXtO7QLikdnZaErwMzsbkv5kNBv1g3O8X50Hs9HVJTkJJpPRcFK6Zedc7zm8MtOwGUQbB1o3LBXZBoj6zyKMRVY82E5N6Ai-70anq7E1ef5raXQ4uDd8U3M5eAAApq-ZXJvW4SS2iRgRGK0hKblkd6ercCczJGjhseE8IzCDpvPwEgOfaSO1uc8pTk83GslSzAZIWel82TPsqZYxx3XGLOvioioUVxURS1BA0pXUbsH87Gx_-0xS-uF-U-LOThmetXVd8WHJdiBMHTc2lK3aRuwIrUZ3VeukK0SEHrM0LKZqR5TfqPQaiTQxLnmS9B4tl8d4nimA4T3rPQpDH0_56t3xSMe9w_xDfa9Dk9t9fByGy2W12_ePjsJwd3dnd7er943tMKzZXi6Pjpq2G7vLKyiN-8PhsV9t73RennQ6D2xvPWuBNZHoCN8vP960dMxSfHPs3bQiZm_ppvUJa2ihxXSdha2elgV71nIFP-AUNJ464af_AUgr_Y8)

---

## 2. Firmware Control Flow Diagram
**What's annotated:**
- **Initialize**: Configure SPI, I2C, GPIO, set PID parameters (Kp, Ki, Kd), load saved target
- **Main Loop**: Runs continuously, ~100ms cycle time, non-blocking execution
- **Read Thermocouple**: SPI read command, 19-bit temp data, cold junction compensation, fault detection
- **PID Calculation**: error = target - current, P/I/D terms, anti-windup for integral
- **Clamp Output**: Limits to 0.0-1.0 range, maps to duty cycle percentage
- **Calculate Duty Cycle**: 200ms window, ON_time = duty × 200ms, example: 60% = 120ms ON / 80ms OFF
- **Drive SSR**: GPIO HIGH for ON_time (AC flows), GPIO LOW for OFF_time (AC blocked)
- **Update Display**: Shows current/target temp, duty %, RUN/STOP status
- **Check Input**: Interrupt-driven encoder reading with debouncing
- **Adjust Target**: Rotate CW/CCW, step size 0.5-1°C, clamp to safe limits (60-250°C)
- **Toggle Run/Stop**: Enable/disable PID & SSR, safety checks before start

[Open Firmware Control Flow Diagram](http://localhost:8000/edit#pako:eNqFVlFuGzcQvcpAQYoW9caSCwux0KQwpDgWIluCV66LykFAcWclxrvkguTaUZ0U_eoBigL9by-QM6T_PURO0iGp3ZViBxEgieQMhzNvZh552-IqwVavlWbqhi-ZtjAdXEqgT2xp9vUsXhmLeZi9_Aai6CkMpbAz9yNYJn7B7-d692kURf7_429_Q1_JVCxKjRBPhpAqDSeHP33XebzfrVVitGUBw73-bqUyHj0b3GMBpXNQw_PJcAyFkGbTBEyGAyiYZjla1AZeFDvwQtA3qbVGiiVg2DUmQBEsaA9FU3zix-TiBFRpi9J6V-L47OWlDCi4MH3QI6WK2xMmpB9txXxWSgNcSStkqUqTrfzqr512O6f1Fc8QrMgDTqdKRvNM8SshF4BvkJdWKPmuOs7Z9sedIUum5OnMDWC6RJ0rrsoiC2auBdsGdRP_GGXiodduL1d5zmSDyBlyFNcInYNoLgIckDDLaoXDoshWtC1L4HUpufPPGSlQGuYmm1m6RqoYq-DD-z4Qch_eHzVeWEX5Y4RAqTVK-2oL-P4S-ZVH25Bd-ktZmVlT417F78GgNM9cqvss42XWOFEFjVqThSdVhqO7R05I-qKAf_8Cr-vXhm5NuLX__gnLbpxYLxw4YeKFf3rZ7lqwrpMnMIFvYUjfULWHlP3oRsiEyslFJaTFhWYZ4avzOioXhAuonzFKrf-FsTfojbQftR2YnUftOzkdiZyStT6cdK6p9RLQTC6w1nHbn0D7IRTqhlpmfNQko-NFVJGV8Oh8NKqlE43XBJcBRfl0TFBLTlhh3HFJaVehlOtYgvc-GkrLgBRmVX4Q3BT6Tt-b8tsJyz3fEg6m9RmbIV74ZXIzaFllWVYLx6evXA-RdMtWIz86qhQ60f0qz96Qwxn2oEsofPz9D-jsuXPGpzvw2A828DovqCXQOCpwvUvN2sS9jtaHPtDUSqQ08wOnfk832sBex8Pnx4HqQiyNBh1C9JGUnFJw2Hd4c6WurCruGhmNL4KNdbxbRjyxeBOpVvkdIz-jVhHXyhgwN8LypeOgQmNKBY4NQTxHidpH7w6ICq0KpV3PUTX74qmhqKL3UATIzoezMICBMEXGVnfwGGh2UzVoYJ_MtS1FJe220gZhU83YJTVVIjiz6_6t9ZridHTz0BHRnDU68ZKq6uz8dDeejidgLLOl-STRQPWvV65eov2tmjkm5iSzhmtECfMyJayIVlONZlnDUEUemsER21BSm94-W99dfvbDFhCB_hxJaF0WdO1kbBFO9XyvqfY97zpvsVmfl9ZurQ5wroijkUzRGaa-RxovnFNvz5w9fAuHyevS2KnHdRYmEGYwrahyK1d0r3LbuJMIjXz7DrigjhOS8GEG1xlrhF6a4P3S2GIBhh4QPWKu_Ygoim6RZq-nF2oFw1KEzNFfk5ZuO9rbd-pgVwWVRMMTMV31bleOudKrl5_BY1Ka5VuYqsUiQ7q9Z2EENNyNrbqLw1EmCtDlGnmfreY-PT_t0TOFzcmA4_evahbw_lDN9Qg3U8l3fKduck2dw3V2qSNNE-qPwpTUeCliMmdUM6Sw9VSKCR5X_r6g5pi6S9f4x9pnYqcXCFWCe2gE8WZN1C-dIKoB2lgPEmNX63BTkWW9BwcHaXpwsGOsVlfYe9Buc95ur6d0LSZ22dsr3mzurbkjGHDbNwy47V8wUL8QKgOcbxhI0273Cwb8065yn_M03XC_2-X8ns2tnVZO9zkTCT2Zby9bdok5XrZ6l60E_QPmsvWOdFhpVbySvNWzusSdVukJYiAYvQjysPjuf5PjBTo)

---

## 3. Development Roadmap Gantt Chart
**What's annotated:**

**Phase 1 - Breadboard Prototype:**
- Wire ESP32 to MAX31856, test SPI communication
- Connect SSR to test load (light bulb), verify 3.3V control works
- Implement basic PID loop, tune Kp, Ki, Kd parameters

**Phase 2 - KiCad Schematic:**
- Design AC/DC isolation with proper creepage/clearance (≥6.4mm)
- Select and place components (connectors, fuse holder, terminals)

**Phase 3 - PCB Layout:**
- Route traces with wide copper for AC, proper ground planes
- Design 3D enclosure in CAD, ensure PCB fits with mounting holes

**Phase 4 - Firmware:**
- Implement OLED UI with real-time temp display and menus
- Auto-tune PID using Ziegler-Nichols or relay method
- Add diagnostics (sensor fault detection, thermal runaway protection)

**Phase 5 - Testing:**
- Water bath tests at 60-100°C, measure overshoot and stability
- High-temp oil tests 150-200°C, verify long-term accuracy

**Phase 6 - Advanced Features:**
- Add IR or contact pan sensor to detect thermal mass changes
- Implement WiFi logging to InfluxDB/Grafana for temp graphs
- Create temperature profiles (ramp rates, multi-step cooking)

[Open Development Roadmap Diagram](http://localhost:8000/edit#pako:eNp9VduO2zYQ_ZWBHooWlbK-t_Cb18q2xmZbY502beGXsTiWiVAkQVLrGkH-qd-QL8tQkr3K1glhGJA4PJxz5szoQ1IYQck8KVGHsNXAK8igCHJ6ImVsRTrAo0FRoYUMVlrURZBGw1uqLDkMtSNYGh2cUYpciyAw0J1xFQb4m1f28JDl-Va3m55agPUBPcGQQW8dodgZdALWzgQTTpba2Gs78LzmdpjCaDCaZIMh_1IYTkR78J3ktF5v1uMRBAMPi7_Gw5-nM-BrdxfIFAL5AJv1CgpTVbWWBTaZzS8wTExzurDZPEacJl6xGPC9kuUhwK5Wux9SeCIn9ycYvxr_yVCNFnA07r2H-U8d0qqyihoxd-hlAetVzkjGgtSwcKKW2nA-tSa4t3Av4V6ARYcVBXIdzDX5RizfvVxyRpviQCw4Q-fkZdlFv9z7cs3tKAXc8xVg--q1CLBY3uRLkN6oVpejDAewznDdoXBEFku6KRRxnrogmL2aVNWPz5Q3pKJ2qJmKQg5gla3RrIHnrItWWuN8CvuaqRyMEuRiUVwlNapvsB7z-fXyFt7gydSda5-f4cqa2_GF6ajH9JHjCYLj9HzL7yhFzNRGknvjWIT0zLl0pm7JaOqVtlNrnAPpQhkfO4KrulzkKb9pHmNyexm6KyqGCVKXkTJ9g-aEad5JVx3RfdGPbey1nT7hyYUwUx8N_-fD39-8zuGPVZsSN4XKgqxYC-5rENIzy1NTOw6ue2wXdTBZY9Ro4dpHHv9IKrn5s99kwZQ8sGyO4nm278GI3mEhGBtLbTy7MdrAs0IcvsdaBRDs9kYAdsGBbYAKXK3xyEhcgm7v63pNGe8tt2hMKWa-RCV3rvFuG37e_K6_1ZNsepFs0p8lGF_tkGWKA8ADj7XZIBsOBp_-Y3NUhE2NDU8BfzCmdbwPuJNKhtMz-V95ZGSNvEaqDmo4HWSjDqibIsroMotNAFgUNTvz9HXGM2a8EE-x_QTcUTON_VnqF69f9MPswnXas0cs0OoxFjDOMeT2tajPReIJ2FboUp0KvYfigLqkq7PunbyTTKgso-p8fKX3qv43v735xeEeNTYd1khSOrSHHsaSHRlaN56_MmyBvYwNkwEPRst_rCHrz86RmQ9kOWfzPt7UoCRpUsUspeDP24dtwjlXtE3m20RQY7dt8pFjkP28OekimQdXU5rUNn69cjYpX9K-_PgZWrpUPA)

---

## Opening Diagrams

To open any diagram in the local Mermaid editor, use the provided script:

```bash
# Open hardware architecture diagram
node open-diagram.js hardware-diagram.mmd

# Open firmware flow diagram
node open-diagram.js firmware-flow.mmd

# Open roadmap diagram
node open-diagram.js roadmap.mmd
```

The script will automatically encode the diagram and open it in your browser.

## Local Server Info
The Mermaid Live Editor is running at: **http://localhost:8000**

To stop the server:
```bash
docker stop mermaid-live
```

To restart the server:
```bash
docker start mermaid-live
```

## Diagram Files
The `.mmd` source files are saved in your project directory:
- `hardware-diagram.mmd` - Hardware architecture with component annotations
- `firmware-flow.mmd` - Firmware control flow with step-by-step details
- `roadmap.mmd` - Development roadmap with phase descriptions

You can edit these files directly and use `open-diagram.js` to view changes.
