---
name: display-panels
description: Display and touch panel hardware — controller behaviour (ST7701S, ST7789, ILI9341, GC9A01, SSD1306, e-paper), touch controllers (GT911, FT6336, CST816S), bus choice (RGB/DE, I80/8080, SPI, QSPI, I2C), esp_lcd driver configuration, frame-buffer and bounce-buffer sizing, tearing and image-drift diagnosis. Use when a panel or touch controller is named, when a display shows tearing/shift/corruption, or when sizing pixel clock against memory bandwidth.
---

# Display and Touch Panels

Panel-side engineering: which bus, which controller, how much bandwidth, and why
the picture is torn or permanently shifted. GUI code belongs to the `lvgl`
skill, pin legality to `esp32`, per-board wiring to `hardware-boards`.

## 1. Reference loading

| File | Load when |
|---|---|
| `references/display-controllers.md` | a display controller is named, or choosing one |
| `references/touch-controllers.md` | a touch controller is named (GT911, FT6336, CST816S, …) |
| `references/interfaces.md` | choosing or wiring a bus: RGB, I80, SPI, QSPI, I2C |
| `references/rgb-lcd.md` | RGB/DE panels on ESP32-S3: esp_lcd config, bandwidth, bounce buffers, tearing, drift |

Register-level truth comes from the vendor PDF via the `datasheets` skill
(`st7701s`, `gt911`, `gt911-programming`), not from these summaries.

## 2. Choose the bus from the numbers, not the habit

```
bytes_per_frame   = width * height * bytes_per_pixel
scanout_bandwidth = bytes_per_frame * refresh_hz
refresh_hz        ≈ pclk / ((hres + hfp + hbp + hsync) * (vres + vfp + vbp + vsync))
```

| Bus | Practical ceiling | Notes |
|---|---|---|
| SPI / QSPI | small panels, partial updates | controller has its own GAM/RAM; cheap pins, low bandwidth |
| I80 (8080) | medium panels with internal RAM | parallel, still RAM-backed on the controller |
| RGB / DE | large panels, no controller RAM | the MCU must stream every pixel every frame — this is where bandwidth decides the design |
| I2C | monochrome OLED | tens of kB/s; fine for status displays only |

An RGB panel has no frame memory: starve the stream and the image breaks. A
480×640 RGB565 panel at 30 MHz PCLK needs ~60 MB/s of continuous reads, which
requires octal PSRAM (quad will not do it) — see `references/rgb-lcd.md`.

## 3. Diagnose the classic failures

| Symptom | Cause | Fix |
|---|---|---|
| Image shifted sideways, permanently, after a flash write or heavy load | DMA underran, read pointer desynchronised, panel consumed dummy bytes | `CONFIG_LCD_RGB_RESTART_IN_VSYNC` or `esp_lcd_rgb_panel_restart()`; then remove the starvation |
| Tearing along a moving edge | CPU writes the buffer the DMA is reading | two full frame buffers, or a VSYNC semaphore with one |
| Corruption only while writing flash/NVS/OTA | flash and PSRAM share the SPI bus and the cache | XIP from PSRAM, bounce buffers off the flash path, or pause drawing during the write |
| Colours wrong / channels swapped | RGB565 byte order or R/B swap in the panel wiring | check the panel's bit order against the data-line mapping before touching code |
| Dim or flickering backlight | PWM frequency too low, or the backlight is behind an expander/transistor with inverted polarity | check the board profile |
| Touch works only after a reset, or has the wrong address | GT911 latches its I2C address from INT/RST levels at power-on | drive the straps deliberately; if RST is unwired, read the address instead of assuming |

## 4. Panel bring-up order

1. Confirm the controller part number and the panel's timing sheet (porches,
   polarity, PCLK range) — porch values are panel-specific, not controller-wide.
2. Initialise the controller over its config bus (many RGB panels have a 3-wire
   SPI side channel, e.g. ST7701S) **before** starting the pixel stream.
3. Bring up the pixel bus at a conservative clock, one or two frame buffers,
   VSYNC restart enabled.
4. Verify under stress: flash write, Wi-Fi/BLE traffic, full-screen animation.
5. Only then optimise (higher PCLK, bounce buffers, colour depth), re-running the
   stress test after each step.
