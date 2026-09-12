---
name: hardware-boards
description: Pinouts and board profiles for ESP32 hardware — Waveshare dev boards, LCD/e-paper/round display modules, display and touch controller wiring, plus the custom Pregmate MAIN A1 analyzer board (ESP32-S3 + ST7701S + GT911 + TCA9554). Use when a specific board or display module is named, when asking "which pin is X on this board", or before changing wiring on a known board.
---

# ESP32 Board Profiles

Never infer a board's pinout from the chip datasheet — boards reassign, expand
and strap pins. Load the profile, and if no profile exists, say so and ask for
the schematic instead of guessing.

## 1. Profile index

| File | Load when |
|---|---|
| `references/pregmate-main-a1.md` | the Pregmate analyzer board, or `TARGET_BOARD PREGMATE_MAIN_A1` in the firmware |
| `references/waveshare-overview.md` | a Waveshare board or display is named, model unknown |
| `references/dev-boards/README.md` | Waveshare dev board, family unknown |
| `references/dev-boards/esp32-s3-touch-lcd.md` | ESP32-S3 Touch LCD boards (1.28/1.69/2.1/4.3 inch) |
| `references/dev-boards/esp32-s3-lcd.md` | ESP32-S3 LCD boards without touch |
| `references/dev-boards/esp32-c6-lcd.md` | ESP32-C6 LCD boards |
| `references/dev-boards/esp32-e-paper.md` | e-paper driver boards |
| `references/dev-boards/esp32-camera.md` | camera boards |
| `references/dev-boards/esp32-general.md` | plain dev boards without a display |
| `references/lcd-boards/README.md` | a standalone display module (not a dev board) |
| `references/lcd-boards/spi-displays.md`, `parallel-displays.md`, `round-displays.md`, `i2c-displays.md`, `e-paper.md` | that display bus/form factor |

Controller behaviour (ST7701S, GT911, bus choice) lives in the `display-panels`
skill; GUI code in `lvgl`; pin legality in `esp32`.

## 2. How to use a profile

1. Identify the board from the firmware (`TARGET_BOARD`, board headers,
   `sdkconfig` target) or from what the user names — not from the display size.
2. Read the profile and keep its pin table as the single source of truth.
3. Run any change through the validator in the `esp32` skill with the board's
   real module part number and `psram` mode; a board profile that ships a JSON
   fixture (Pregmate) can be validated directly.
4. When a pin is driven by an IO expander rather than the MCU, say so — it will
   never appear in a GPIO validation, and it cannot be used from an ISR with the
   cache disabled.

## 3. Board-level hazards to check every time

- **Strapping pins reused as data lines.** Legal, but the board must hold the
  reset level; anything you add to that net (probe, test point, pull-up) can
  change the boot mode or the VDD_SPI voltage.
- **Module part number.** `…-N16R8` vs `…-N16R16V` changes which pins exist and
  whether GPIO47/48 are 3.3 V or 1.8 V. Read the marking, not the config.
- **Shared I2C bus.** Touch controller plus IO expander plus EEPROM on one bus
  means address conflicts and a shared bandwidth budget.
- **Display reset and backlight paths.** Frequently behind an expander or a
  transistor, sometimes inverted; check the profile before writing init code.
