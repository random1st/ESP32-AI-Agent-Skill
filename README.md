# ESP32 Agent Skills

Six agent skills for embedded work on the Espressif ESP32 family and the hardware
around it. They run in **Claude Code** (as a plugin or as project/user skills) and
in **Codex** (as `.agents/skills`), from the same files.

| Skill | Covers |
|---|---|
| `esp32` | ESP-IDF 5.x / PlatformIO firmware, GPIO pin-map validation with anti-bricking checks, code generation, memory and PSRAM |
| `lvgl` | LVGL 8.2-9.5 APIs, widgets, the v8→v9 migration, draw buffers, performance |
| `display-panels` | display and touch controllers, bus choice (RGB/I80/SPI/QSPI/I2C), tearing and image-drift diagnosis, esp_lcd RGB configuration |
| `hardware-boards` | board pinouts — Waveshare dev boards and display modules, plus the Pregmate MAIN A1 analyzer board |
| `electronics` | wiring and electrical limits, pull-ups and level shifting, bus protocols, sensor/breakout pinouts |
| `datasheets` | downloads vendor PDFs and splits them into per-section chunks with an index, so hardware claims can be cited |

## Install

**Claude Code, as a plugin:**

```bash
claude /install-plugin https://github.com/random1st/ESP32-AI-Agent-Skill
```

**Claude Code, as project or user skills** — symlink (or copy) the skill
directories into `.claude/skills/` or `~/.claude/skills/`:

```bash
git clone https://github.com/random1st/ESP32-AI-Agent-Skill
for s in esp32 lvgl display-panels hardware-boards electronics datasheets; do
  ln -sfn "$PWD/ESP32-AI-Agent-Skill/skills/$s" ~/.claude/skills/$s
done
```

**Codex** — the repo already carries `.agents/skills/<name>` links, so a clone
works as-is inside a project; for global use:

```bash
for s in esp32 lvgl display-panels hardware-boards electronics datasheets; do
  ln -sfn "$PWD/ESP32-AI-Agent-Skill/skills/$s" ~/.agents/skills/$s
done
```

Each skill is self-contained: `SKILL.md` plus its own `references/`, and for
`esp32`/`datasheets` also `scripts/` and `tests/`. Nothing resolves outside its
own directory, which is what makes one tree work for both hosts.

Prerequisites: Python 3.9+ for the scripts; `pdftotext` (poppler) or `pypdf` for
the datasheet chunker.

## Using the scripts

```bash
cd skills/esp32

# Validate a pin map (exit 0 valid, 1 errors, 2 bad input)
python scripts/validate_pinmap.py --format text pinmap.json

# Real-board example shipped with the repo
python scripts/validate_pinmap.py --format text tests/fixtures/board_pregmate_main_a1.json

# Generate init code
python scripts/generate_config.py pinmap.json --framework espidf   # or arduino

# Regression suite (75 tests)
python -m pytest -q
```

Input format:

```json
{
  "platform": "esp32",
  "variant": "esp32s3",
  "module": "ESP32-S3-WROOM-1-N16R8",
  "psram": "octal",
  "wifi_enabled": false,
  "pins": [
    {"gpio": 15, "function": "I2C_SDA", "protocol_bus": "i2c", "device": "GT911",
     "direction": "inout", "pull": "external_up", "speed_hz": 400000}
  ]
}
```

`module` and `psram` are what make S2/S3 answers correct. `psram` wins when given;
otherwise the module's memory suffix decides (`N16R8` → octal, `N8R2` → quad,
`N8` → none). With neither, the validator stays undecided and warns about the
octal-memory pins instead of silently approving them. An optional
`"flash": "octal"` reserves the same group when only the flash is octal.

## Datasheet corpus

```bash
cd skills/datasheets
python scripts/fetch_datasheets.py --list
python scripts/fetch_datasheets.py esp32-s3            # chip datasheet
python scripts/fetch_datasheets.py --depth 3 esp32-s3-trm
```

Sectioning follows the PDF outline when the document has one (ESP32-S3 datasheet
→ 66 chunks, the TRM → 463), falling back to a numbered-heading heuristic.
Every chunk carries front matter naming the source URL, document, section and PDF
pages; `INDEX.md` maps sections to chunk files. PDFs are never committed, and
chunks whose `redistribute:` flag is false stay local.

## Supported variants

| Variant | Validation | Code gen | Reference docs | Best for |
|---------|:----------:|:--------:|:--------------:|----------|
| ESP32   | Yes | Yes | Yes | Bluetooth Classic, legacy projects |
| ESP32-S2 | Yes | Yes | Yes | Ultra-low power, USB OTG/HID |
| ESP32-S3 | Yes | Yes | Yes | AI/ML, complex GUIs, cameras |
| ESP32-C3 | Yes | Yes | Yes | Budget IoT nodes (RISC-V) |
| ESP32-C6 | Yes | Yes | Yes | Wi-Fi 6, Matter/Thread, Zigbee |
| ESP32-C2, C5, H2, P4 | - | - | Yes | reference only |

## Safety checks

Chip-gated, because the classic ESP32 rules are wrong on newer variants:

| Check | What it catches |
|---|---|
| **Flash pins** | GPIO6-11 (ESP32), 12-17 (C3), 24-29 (C6), 26-32 (S2/S3) |
| **Octal flash/PSRAM pins** | GPIO33-37 on ESP32-S3 R8/R16 parts (SPIIO4-SPIIO7 + SPIDQS) — a boot failure, not a warning |
| **Non-existent GPIOs** | GPIO22-25 on S2/S3, GPIO24/28-31 on ESP32 |
| **Pins absent on the module** | GPIO33/34 on ESP32-S3-WROOM-1/1U, GPIO20/24/28-31/37/38 on WROOM-32 |
| **Input-only pins** | GPIO34-39 on ESP32, GPIO46 on S2 — and explicitly *not* on S3, which has none |
| **VDD_SPI strapping** | GPIO12 (ESP32) / GPIO45 (S2/S3) high at boot selects 1.8 V and can destroy 3.3 V memory |
| **1.8 V SPI clock pins** | GPIO47/48 on "V" parts swing 1.8 V while the rest of the IO stays 3.3 V |
| **ADC2 vs Wi-Fi** | ADC2 readings are invalid while Wi-Fi runs (ESP32/S2/S3) |
| **LEDC channel count** | 8 channels on S2/S3, 16 on ESP32, 6 on C3/C6 |
| **Current budget** | warns as the estimated GPIO current approaches 200 mA |

The pin model is pinned to ESP-IDF v5.5.1 `soc_caps.h` masks and the vendor
datasheets, with the regression tests citing the exact source for each claim.

## Reference documentation

- **ESP32 hardware** — per-variant pin databases, strapping behaviour, ESP32-S3
  deep dives for IO MUX/GPIO and the flash/PSRAM bus.
- **LVGL 8.2-9.5** — per-version API references, widget catalogues, the v8→v9
  migration with its renamed functions, ESP32 integration.
- **Boards** — Waveshare dev boards, LCD/e-paper/round display modules, and a
  complete profile for the Pregmate MAIN A1 (ESP32-S3 + ST7701S + GT911 + TCA9554)
  with a machine-readable pin map used as a test fixture.
- **Electronics** — electrical constraints, protocol quick reference, common
  device pinouts.

## Credits

Fork of [ezrover/ESP32-AI-Agent-Skill](https://github.com/ezrover/ESP32-AI-Agent-Skill),
restructured into per-subject skills with a corrected ESP32-S3 model, Codex
support, a datasheet corpus and board profiles.

## License

See `LICENSE`.
