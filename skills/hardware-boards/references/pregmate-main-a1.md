# Pregmate MAIN A1 (ESP32-S3 + ST7701S + GT911)

Custom analyzer board. Firmware: `pregmate-analyzer`, `TARGET_BOARD PREGMATE_MAIN_A1`
in `main/LCD_Driver/ST7701S.h`. The second board in that header,
`WAVESHARE_DEVKIT`, is the Waveshare ESP32-S3 Touch LCD devkit this design grew
out of — pin numbers are shared, the differences are called out below.

## 1. Platform

| Item | Value | Where it is pinned |
|---|---|---|
| MCU | ESP32-S3, dual Xtensa LX7 @ 240 MHz | `CONFIG_IDF_TARGET="esp32s3"` |
| PSRAM | Octal (8-line), 80 MHz, XIP enabled | `CONFIG_SPIRAM_MODE_OCT`, `CONFIG_SPIRAM_SPEED_80M` |
| Flash | 16 MB declared in defaults, quad SPI, DIO @ 80 MHz | `CONFIG_ESPTOOLPY_FLASHSIZE_16MB` |
| ESP-IDF | 5.5.1 | `dependencies.lock` |
| LVGL | 8.3.11 (registry component `lvgl/lvgl`) | `dependencies.lock` |
| Display | ST7701S, 480×640, RGB565, 16-bit parallel, PCLK 30 MHz | `ST7701S.h` |
| Frame buffers | 2 × 480×640×2 B = 1.17 MB in PSRAM | `CONFIG_EXAMPLE_DOUBLE_FB` |
| Touch | GT911 on I2C0 @ 400 kHz, address 0x5D | `GT911.h`, `I2C_Driver.h` |
| Expander | TCA9554 on the same I2C0 bus | `EXIO/TCA9554PWR.h` |
| Radio | BLE only, NimBLE peripheral, MTU 512, 1 bond | `sdkconfig.defaults` |
| Console | USB Serial/JTAG (GPIO19/20) | `CONFIG_ESP_CONSOLE_USB_SERIAL_JTAG` |

Wi-Fi is not enabled, so the ADC2/Wi-Fi restriction does not apply to this board —
validate with `"wifi_enabled": false`.

## 2. Pin map

The machine-readable copy lives in
`tests/fixtures/board_pregmate_main_a1.json` and is asserted by
`tests/test_esp32s3_memory_bus.py::TestPregmateBoardFixture`. Validate it with:

```bash
python scripts/validate_pinmap.py --format text \
  tests/fixtures/board_pregmate_main_a1.json
```

| GPIO | Function | Notes |
|---|---|---|
| 1 | ST7701S config SPI MOSI | 3-wire panel init only, not the pixel path |
| 2 | ST7701S config SPI SCLK | |
| 42 | ST7701S config SPI CS | On the Waveshare devkit this is an expander pin (`LCD_CS -1`) |
| 6 | Backlight PWM | LEDC low-speed, 4 kHz, 13-bit |
| 38 / 39 / 40 / 41 | HSYNC / VSYNC / DE / PCLK | DE mode, PCLK 30 MHz |
| 5, 45, 48, 47, 21 | B0..B4 | 45 and 47/48 carry caveats — see §3 |
| 14, 13, 12, 11, 10, 9 | G0..G5 | GPIO12 has no flash-voltage trap on S3 (that is ESP32-classic) |
| 46, 3, 8, 18, 17 | R0..R4 | 46 and 3 are strapping pins |
| 15 / 7 | I2C0 SDA / SCL | shared by GT911 + TCA9554, external pull-ups on board |
| 16 | GT911 INT | GT911 RST is not wired (`I2C_Touch_RST_IO -1`) |

Not native GPIO: the buzzer (`TCA9554_EXIO6`) and the panel reset both hang off
the TCA9554 expander, so they never appear in a pin-map validation.

## 3. Board-specific hazards

**Three strapping pins are used as RGB data lines — by design, but fragile.**
GPIO45 (B1), GPIO46 (R0) and GPIO3 (R1) are sampled at reset; the RGB peripheral
only drives them afterwards. The board must keep GPIO45 and GPIO46 LOW through
reset (the chip's internal weak pull-down does this, per the ESP32-S3 datasheet
pin table: both are `WPD, IE` at reset). Anything added to these nets — a probe,
a test point with a pull-up, a connector — risks either a 1.8 V VDD_SPI
selection (GPIO45) or a download-mode boot (GPIO46).

**GPIO47/48 are 1.8 V on "V" parts.** They are SPICLK_N/SPICLK_P, and the
ESP32-S3-WROOM-1 datasheet (pin-table footnote c) states that on modules built
around ESP32-S3R16V the VDD_SPI rail is 1.8 V, so these two pins swing 1.8 V
while every other GPIO stays at 3.3 V. This board uses GPIO47 and GPIO48 as the
panel's B3 and B2 bits. **Verify the fitted part number is a 3.3 V R8 and not an
R8V/R16V** — with a 1.8 V driver the two blue bits sit near the panel's input
threshold. Check with `esptool.py flash_id` / the module marking, not from
`sdkconfig`, which cannot tell the two apart.

**GPIO33-37 are never available for expansion.** In-package octal PSRAM takes
GPIO35/36/37 (SPIIO6, SPIIO7, SPIDQS), and WROOM-1/1U does not bond GPIO33/34
out at all. The validator enforces both, so a future sensor cannot be parked
there by accident.

**`sdkconfig` and `sdkconfig.defaults` disagree on flash size.** The committed
`sdkconfig` says `CONFIG_ESPTOOLPY_FLASHSIZE_8MB`, the defaults file says 16 MB.
`partitions_two_ota.csv` needs ~6.1 MB, so an 8 MB part still boots and both OTA
slots fit — the mismatch is latent rather than breaking, but regenerate
`sdkconfig` from the defaults before trusting the 16 MB figure anywhere.

## 4. RGB bandwidth budget

480 × 640 × 16 bpp at 30 MHz PCLK is 60 MB/s of PSRAM reads for the scan-out
alone, against a frame rate of 30 MHz / (480 × 640) ≈ 97 Hz worth of pixel clock
(the panel's real refresh depends on the porch settings in `ST7701S.c`). With
two full frame buffers in octal PSRAM at 80 MHz, the headroom is adequate but
not generous: this is why `CONFIG_SPIRAM_FETCH_INSTRUCTIONS`,
`CONFIG_SPIRAM_RODATA`, `CONFIG_LCD_RGB_ISR_IRAM_SAFE` and
`CONFIG_LCD_RGB_RESTART_IN_VSYNC` are all enabled — see
`references/esp32-s3/rgb-lcd.md` for what each one buys and what breaks without
it.

## 5. When touching this board

1. Re-validate the pin map after any wiring change (command in §2).
2. Keep `tests/fixtures/board_pregmate_main_a1.json` in sync with
   `ST7701S.h`, `I2C_Driver.h` and `GT911.h` — the fixture is the regression
   test, so a stale fixture silently stops protecting the board.
3. New peripheral? Prefer the TCA9554 expander over a native GPIO: almost every
   free S3 pin on this design is either a strapping pin or part of the RGB bus.
