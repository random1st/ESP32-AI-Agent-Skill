---
name: esp32
description: Expert ESP32 firmware and hardware guidance — chip selection (S3, C3, C6, S2, ...), GPIO pin-map validation with anti-bricking checks, memory/PSRAM layout, ESP-IDF 5.x and PlatformIO tooling, and Arduino/ESP-IDF init code generation. Use when the user mentions ESP32, ESP-IDF, idf.py, PlatformIO, GPIO assignment, strapping pins, PSRAM, or embedded C/C++ for Espressif chips.
---

# ESP32 Embedded Engineering

Expert-level guidance for the Espressif ESP32 family: ESP-IDF and PlatformIO
firmware, pin assignment, and hardware safety. Companion skills:

| Need | Skill |
|---|---|
| LVGL GUI code, widgets, migrations | `lvgl` |
| Panels, touch controllers, bus choice, tearing | `display-panels` |
| Board pinouts (Waveshare, Pregmate MAIN A1) | `hardware-boards` |
| Wiring, electrical limits, sensors, bus protocols | `electronics` |
| Datasheet / TRM lookup by section | `datasheets` |

## 1. Non-negotiables

**Never state a pin fact from memory.** Every GPIO claim is variant-specific and
the failure mode is a dead board. Load the reference, or run the validator.

**Chip-gate every safety rule.** The classic ESP32 rules are wrong on newer
variants, and that is the most common source of bad advice:

| Rule | Applies to | Does NOT apply to |
|---|---|---|
| GPIO12 MTDI sets flash voltage to 1.8 V → brick risk | original ESP32 | S2, S3, C3, C6 (on S3 GPIO12 is an ordinary IO, used as an RGB data line on real boards) |
| GPIO34-39 are input-only, no internal pulls | original ESP32 | S3 (no input-only pins at all), C3, C6. On S2 only GPIO46 is input-only |
| GPIO6-11 are flash pins | original ESP32 | S2/S3 use GPIO26-32, C3 uses 12-17, C6 uses 24-29 |
| GPIO16/17 reserved for PSRAM | ESP32 WROVER modules | S2/S3 (quad PSRAM shares the flash pins) |
| VDD_SPI select pin must stay LOW at boot | GPIO12 on ESP32, GPIO45 on S2/S3 | — |

Authority order: ESP-IDF `soc_caps.h` for the silicon → chip datasheet →
module datasheet → board schematic. Vendor summaries and blog posts lose.

## 2. Reference loading

All paths are relative to this skill directory.

| File | Load when |
|---|---|
| `references/platforms/esp32-pins.md` | any GPIO work (original-ESP32-centric pin database) |
| `references/platforms/esp32-specifics.md` | strapping pins, deep sleep, flash/PSRAM, ADC2, boot failures, memory layout |
| `references/esp32-s3/specs.md` | ESP32-S3 selected |
| `references/esp32-s3/gpio-iomux.md` | S3 pin assignment, strapping, reserved pins, drive strength, power domains |
| `references/esp32-s3/memory-bus.md` | S3 flash/PSRAM bus, octal vs quad, module part numbers, XIP, cache |
| `references/esp32/specs.md`, `references/esp32-s2/specs.md`, `references/esp32-c3/specs.md`, `references/esp32-c6/specs.md`, `references/esp32-c2/specs.md`, `references/esp32-c5/specs.md`, `references/esp32-h2/specs.md`, `references/esp32-p4/specs.md` | that variant is selected |

Protocol wiring, electrical limits and device pinouts moved to the `electronics`
skill; panel and touch hardware to `display-panels`.

## 3. Pin-map workflow

1. **Parse** the request: variant, module part number (`ESP32-S3-WROOM-1-N16R8`),
   protocols, framework, whether Wi-Fi is enabled.
2. **Load** the triggered references; for a known board load the profile from
   `hardware-boards` instead of inventing pins.
3. **Assign** pins — the GPIO matrix makes most choices free, so prefer the
   conventional default and move only to resolve a conflict.
4. **Validate** before presenting anything:

```bash
python scripts/validate_pinmap.py --format text pinmap.json
# exit 0 = valid, 1 = has errors, 2 = bad input
```

5. **Generate** init code when asked:

```bash
python scripts/generate_config.py --framework espidf pinmap.json   # or --framework arduino
```

6. **Report** the assignment table, the validator's warnings verbatim, and the
   `sdkconfig` / `platformio.ini` lines that matter.

### Input schema

```json
{
  "platform": "esp32",
  "variant": "esp32|esp32s2|esp32s3|esp32c3|esp32c6",
  "module": "WROOM | WROVER | ESP32-S3-WROOM-1-N16R8 | ...",
  "psram": "none|quad|octal",
  "flash": "quad|octal",
  "wifi_enabled": false,
  "pins": [
    {"gpio": 15, "function": "I2C_SDA", "protocol_bus": "i2c", "device": "GT911",
     "direction": "inout", "pull": "external_up", "speed_hz": 400000, "notes": ""}
  ]
}
```

`module` and `psram` are what make S2/S3 answers trustworthy: `psram` wins when
given, otherwise the memory suffix of the module name decides (`N16R8` → octal,
`N8R2` → quad, `N8` → none). With neither, the validator stays undecided and
**warns** about the octal-PSRAM pins instead of silently approving them. Pass
`wifi_enabled: true` only when Wi-Fi is actually used — it gates the ADC2 check.
`flash` is optional and quad unless stated; `"octal"` extends the reserved set to
all of GPIO33-37, since an octal flash drives SPIIO4/SPIIO5 as well.
Validation and code generation cover esp32, esp32s2, esp32s3, esp32c3 and
esp32c6; the remaining variants are reference-only.

## 4. What the validator catches

Errors: flash-pin use, in-package octal-PSRAM pins (GPIO35-37 on S3 R8/R16
parts), pins absent from the silicon (GPIO22-25 on S2/S3, 24/28-31 on ESP32),
pins not bonded out on the module (GPIO33/34 on WROOM-1), duplicate assignment,
output on an input-only pin, ADC2 with Wi-Fi, total GPIO current over 200 mA.

Warnings: strapping pins, UART0/USB-serial pins, 1.8 V SPICLK pins on "V"
parts, missing external I2C/1-Wire pull-ups, more PWM pins than the variant has
LEDC channels (8 on S2/S3, 16 on ESP32, 6 on C3/C6), current approaching the
limit.

A warning is not noise — repeat it to the user with the mitigation.

## 5. Firmware standards

- **Memory:** capability-based allocation (`MALLOC_CAP_DMA`, `MALLOC_CAP_SPIRAM`,
  `MALLOC_CAP_INTERNAL`). ISRs and anything that runs with the cache disabled
  must live in IRAM. Large framebuffers belong in PSRAM, DMA descriptors do not.
- **Reliability:** interrupt handlers short and IRAM-safe, task watchdog on,
  every `esp_err_t` handled (`ESP_ERROR_CHECK` or an explicit branch).
- **C++:** RAII throughout, no raw `new`/`delete`, prefer static or pool
  allocation in long-running firmware.
- **ESP-IDF 5.x CLI:** `idf.py set-target esp32s3`, `menuconfig`, `build`,
  `flash`, `monitor`, `size-components`, `erase-flash`. `set-target` wipes the
  build directory and rewrites `sdkconfig`. Pin component versions in
  `idf_component.yml`; `dependencies.lock` records what was resolved.
- **PlatformIO:** one `[env:...]` per board in `platformio.ini`; switching
  `framework = espidf|arduino` changes the whole API surface, so say which one
  the generated code targets.
