# esp_lcd RGB panels on ESP32-S3

Source: ESP-IDF v5.5.1 "RGB LCD Panel" API reference (esp32s3) plus the
`esp_lcd` RGB example. Quotes below are from that documentation.

## 1. Configuration surface

`esp_lcd_rgb_panel_config_t` fields that change behaviour rather than pinout:

| Field | Meaning / constraint |
|---|---|
| `data_width` | 8, 16 or 24 data lines |
| `bits_per_pixel` | defaults to `data_width`; set explicitly when they differ (8 lines carrying RGB888 → 24) |
| `num_fbs` | frame-buffer count, 0/1 = single, max 3 |
| `double_fb` | shorthand: "the driver will allocate two screen sized frame buffer, same as num_fbs=2" |
| `fb_in_psram` | frame buffer in PSRAM, read by EDMA |
| `bounce_buffer_size_px` | "If it's non-zero, the driver allocates two DRAM bounce buffers for DMA use" |
| `no_fb` | "the driver won't allocate frame buffer" — you fill bounce buffers in `on_bounce_empty` |
| `bb_invalidate_cache` | invalidates read data in bounce mode; "Can be dangerous if data is written from other core(s)" |
| `dma_burst_size` | must be a power of two |
| unused GPIOs | set to `-1` |

## 2. Bandwidth model

With `fb_in_psram`, EDMA reads the frame buffer while bypassing the cache, but
"the bandwidth is **shared** between them, meaning EDMA and the CPU each get
half". Two consequences the documentation states directly:

* heavy EDMA elsewhere plus a high PCLK risks "LCD peripheral starvation,
  leading to display corruption";
* flash and PSRAM share one SPI bus — "At any given time, there can only be one
  consumer of the SPI bus" — so serving a filesystem from the main flash corrupts
  the display for the same reason.

Mitigations: lower the clock at runtime with `esp_lcd_rgb_panel_set_pclk()` (the
new value is applied at the next VSYNC), reduce colour depth, or move to bounce
buffers.

## 3. Bounce buffers

Two small internal-RAM buffers sit between PSRAM and the LCD: DMA drains one
while an ISR refills the other through the cache, then they swap. "The advantage
of this mode is achieving a higher pixel clock frequency", and it is "more robust
against short bandwidth spikes" because the buffers are deeper than the EDMA
FIFO.

Costs, verbatim from the docs:

* "a significant increase in CPU usage";
* the LCD "**CANNOT** function if the external memory cache is disabled, such as
  during OTA or NVS writes to the main flash";
* if both cores hit PSRAM at once, the ISR copy misses its deadline and you get
  "a screen shift", possibly with visible flicker even after auto-recovery.

For bounce mode the documentation recommends `CONFIG_SPIRAM_XIP_FROM_PSRAM`:
"This allows the CPU to fetch instructions and read-only data directly from PSRAM
instead of the main flash", which keeps the cache alive during flash writes — the
reason an OTA progress bar can stay on screen.

## 4. Drift versus tearing

**Drift (permanent shift).** If DMA starves, "the LCD will display dummy bytes"
and the read pointer desynchronises from the output position, "leading to a
**permanently** shifted image". Remedies: `CONFIG_LCD_RGB_RESTART_IN_VSYNC`,
which restarts DMA in the VBlank interrupt, or `esp_lcd_rgb_panel_restart()`
(also deferred to the next VSYNC; returns `ESP_ERR_INVALID_STATE` under
refresh-on-demand).

**Tearing.** "the simplest method is to use two screen-sized frame buffers" in
PSRAM: the CPU-written and EDMA-read buffers stay distinct and EDMA swaps only
after a full frame has shipped. The cost is "the need to maintain synchronization
between the two frame buffers".

## 5. Callbacks and IRAM

Available: `on_color_trans_done`, `on_vsync`, `on_bounce_empty`,
`on_bounce_frame_finish`, `on_frame_buf_complete`. "The callbacks are all running
under ISR environment", and "When CONFIG_LCD_RGB_ISR_IRAM_SAFE is enabled, the
callback itself and functions called by it should be placed in IRAM". Each
returns a bool saying whether it woke a higher-priority task.

## 6. Checklist for a new RGB panel

1. Compute `bytes_per_frame` and scan-out bandwidth; confirm the PSRAM interface
   (octal vs quad) can serve it — see the `esp32` skill's
   `references/esp32-s3/memory-bus.md`.
2. Validate the pin map (`esp32` skill); RGB data lines on strapping pins are
   fine only if the board guarantees the reset level.
3. Start at a conservative PCLK, two frame buffers, `RESTART_IN_VSYNC` on.
4. Only then trade up: higher PCLK via bounce buffers, accepting the CPU cost and
   the cache-disabled limitation.
5. Verify under load — write to flash/NVS while the panel runs; that is where
   starvation shows up, not in a static demo.
