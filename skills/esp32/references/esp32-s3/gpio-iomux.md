# ESP32-S3 GPIO, IO MUX and pin hazards

Sources: ESP32-S3 Series Datasheet §2 (Pins), §5 (Electrical Characteristics);
ESP32-S3-WROOM-1/1U Datasheet §3.2 (Pin Description);
ESP-IDF v5.5.1 `components/soc/esp32s3/include/soc/soc_caps.h` and the
ESP32-S3 GPIO API reference. Full text: `esp32-datasheets` skill.

## 1. What exists

| Fact | Value | Authority |
|---|---|---|
| Valid GPIOs | 0-21 and 26-48 (45 pins) | `SOC_GPIO_VALID_GPIO_MASK` excludes BIT22-BIT25 |
| GPIO22-25 | **do not exist** | same mask |
| Input-only pins | **none** | `SOC_GPIO_VALID_OUTPUT_GPIO_MASK == SOC_GPIO_VALID_GPIO_MASK` |
| Strapping pins | GPIO0, GPIO3, GPIO45, GPIO46 | datasheet §2.3.2, IDF GPIO reference |
| SPI0/1 flash pins | GPIO26-32 | "GPIO26 ~ GPIO32 are usually used for SPI flash and PSRAM and not recommended for other uses" |
| Octal memory pins | GPIO33-37 = SPIIO4..SPIIO7 + SPIDQS | datasheet §2.3.5; see `memory-bus.md` for which ones a given module loses |
| USB-Serial/JTAG | GPIO19 (D-), GPIO20 (D+) | repurposing them disables USB-JTAG |
| ADC1 / ADC2 | ADC1: GPIO1-10, ADC2: GPIO11-20 | ADC2 is unreliable while Wi-Fi runs |
| Touch channels | 14 (GPIO1-14) | datasheet §1 |
| LEDC channels | 8 (low-speed group only) | `SOC_LEDC_CHANNEL_NUM` |

Unlike the original ESP32, **GPIO12 carries no flash-voltage trap on the S3**,
and GPIO34-39 are ordinary bidirectional IOs. Advice copied from ESP32 articles
is wrong here; real S3 boards drive GPIO12-14 and GPIO46 as display data lines.

## 2. Reset-time state worth knowing

From the datasheet pin table (columns "At Reset" / "After Reset"):

| Pin | At reset | Consequence |
|---|---|---|
| GPIO0 | WPU (weak pull-up) | held LOW at reset → download mode |
| GPIO3 | floating | JTAG signal source select; has a default pull-up on many boards |
| GPIO45 | WPD (weak pull-down) | **VDD_SPI select.** HIGH at reset selects 1.8 V and can destroy a 3.3 V flash/PSRAM |
| GPIO46 | WPD (weak pull-down) | boot mode + ROM log; must be LOW for SPI boot |
| GPIO19, GPIO20 | USB_PU | USB pull-up enabled by default; both show a ~2 ms HIGH glitch during power-up (datasheet Table 2-2) |
| GPIO26-32 (SPI) | WPU, IE | driven by the flash controller |
| GPIO33-37 | IE | input enabled, no pull |

Using a strapping pin as a peripheral output is legitimate — the peripheral only
drives it after reset — but the board must guarantee the reset level. State that
requirement whenever you assign one.

## 3. Power domains and voltage

| Pins | Rail | Note |
|---|---|---|
| GPIO0-21 | VDD3P3_RTC | 3.3 V |
| GPIO26-32 | VDD_SPI | flash/PSRAM rail; 1.8 V on "V" parts |
| GPIO33-37 | VDD_SPI **or** VDD3P3_CPU | selected by eFuse `EFUSE_PIN_POWER_SELECTION` |
| GPIO38-48 | VDD3P3_CPU | 3.3 V |
| GPIO47, GPIO48 | VDD_SPI (SPICLK_N/P) | **1.8 V on ESP32-S3R8V / R16V parts** while every other GPIO stays 3.3 V (WROOM-1 datasheet footnote c) |

That last row bites boards that use GPIO47/48 as general IO or display data:
the levels differ from the rest of the bus on 1.8 V parts.

## 4. DC limits (3.3 V, 25 °C — datasheet §5.4)

| Parameter | Value |
|---|---|
| VIH | ≥ 0.75 × VDD |
| VIL | ≤ 0.25 × VDD |
| IOH (max drive, `PAD_DRIVER = 3`, VOH ≥ 2.64 V) | 40 mA |
| IOL (max sink, `PAD_DRIVER = 3`, VOL ≤ 0.495 V) | 28 mA |
| GPIO19/GPIO20 source capability | 40 mA |

Design to ~20 mA per pin and keep the total under 200 mA; the absolute numbers
above are limits, not operating points. Drive strength is per-pin
(`gpio_set_drive_capability()`), and raising it on a long RGB data line trades
edge rate for EMI.

## 5. IO MUX vs GPIO matrix

Most peripherals route through the GPIO matrix, so pin choice is nearly free —
with two exceptions worth stating to the user:

* **Direct IO MUX pins are faster.** For SPI above ~40 MHz and for the RGB/LCD
  interface, use the pins' native IO MUX function (datasheet §2.3.1) instead of
  a matrix route; the matrix adds propagation delay and skew.
* **Clear the previous function when remapping.** `gpio_func_sel(pin,
  PIN_FUNC_GPIO)` (or `gpio_reset_pin()` then configure) detaches a pin from its
  boot-time IO MUX function. Skipping this is the usual cause of "the pin toggles
  but the peripheral also drives it".

Per-pin alternate functions and the peripheral signal list live in the
datasheet chunk `2.3.1 IO MUX Functions` and TRM chapter 6 (IO MUX and GPIO
Matrix) — both available through the `esp32-datasheets` skill.
