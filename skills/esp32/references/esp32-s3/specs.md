# ESP32-S3 Specifications

Deep dives: `gpio-iomux.md` (pins, straps, drive, IO MUX),
`memory-bus.md` (flash/PSRAM bus, modules, XIP). Full datasheet text is
available through the `esp32-datasheets` skill.

## 1. Core Architecture
- **CPU:** Dual-core Xtensa® LX7, 240 MHz.
- **Wireless:** 802.11 b/g/n (Wi-Fi 4), BLE 5.0 (Mesh support). No Bluetooth Classic.
- **Acceleration:** PIE vector instructions for ML kernels and GUI blits.
- **Application:** High-performance IoT, AI on the edge, multimedia GUIs.

## 2. Memory & Storage
- **SRAM:** 512 KB internal, plus 16 KB RTC SRAM.
- **PSRAM:** quad or octal SPI, in-package on R-suffix parts (2-16 MB).
- **Flash:** quad SPI on all Espressif modules, 4-32 MB.
- Flash and PSRAM share one SPI bus and one cache — see `memory-bus.md` §3.

## 3. Peripheral Mapping
- **GPIOs:** 45 usable — GPIO0-21 and GPIO26-48. **GPIO22-25 do not exist.**
- **Input-only pins:** none; every valid GPIO can drive an output.
- **ADC:** 2 units — ADC1 on GPIO1-10, ADC2 on GPIO11-20 (20 channels).
- **DAC:** **None** (that is ESP32 and S2 only).
- **Touch:** 14 capacitive channels (GPIO1-14).
- **USB:** native USB OTG or USB-Serial/JTAG, both on GPIO19/20.
- **PWM:** LEDC with **8 channels** (low-speed group only — not 16 like the
  original ESP32), plus MCPWM for motor control.
- **LCD:** RGB (DE/HV), I80 (8080) and SPI panels via LCD_CAM.

## 4. Hardware Safety & Constraints
- **Flash pins:** GPIO26-32 — never available.
- **Octal PSRAM (R8/R16V parts):** GPIO35, GPIO36, GPIO37 are wired to the
  in-package PSRAM. GPIO33/34 are only taken by an octal *flash* and are not
  bonded out on WROOM-1/1U.
- **Strapping pins:** GPIO0, GPIO3, GPIO45, GPIO46. GPIO45 selects the VDD_SPI
  voltage — HIGH at reset means 1.8 V and can damage 3.3 V memory.
- **1.8 V pins on "V" parts:** GPIO47/48 (SPICLK_N/P) swing 1.8 V on R8V/R16V.
- **ADC2/Wi-Fi:** ADC2 readings are unusable while Wi-Fi is active. BLE-only
  designs are unaffected.
- **No GPIO12 flash-voltage trap** and no input-only pins: those are
  original-ESP32 rules that do not transfer to the S3.
