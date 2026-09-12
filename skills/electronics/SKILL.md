---
name: electronics
description: Practical electronics for embedded boards — current and voltage limits, pull-up/pull-down sizing, level shifting between 1.8/3.3/5 V domains, decoupling and power budgeting, bus protocol selection and wiring (I2C, SPI, UART, PWM, 1-Wire, CAN, ADC, DAC), and pinout/wiring notes for common sensors, modules and breakouts. Use when the question is about wiring, electrical limits, bus timing, or a named sensor/breakout rather than about firmware APIs.
---

# Embedded Electronics

Chip-agnostic electrical and bus engineering: what is safe to wire, to what, and
at what speed. MCU-specific pin legality belongs to the `esp32` skill; vendor
register detail to `datasheets`.

## 1. Reference loading

| File | Load when |
|---|---|
| `references/electrical-constraints.md` | current limits, voltage levels, pull resistor values, power supply and decoupling |
| `references/protocol-quick-ref.md` | I2C, SPI, UART, PWM, 1-Wire, CAN, ADC or DAC is in play |
| `references/common-devices.md` | a specific sensor, display module or breakout is named |

## 2. Rules that prevent most hardware damage

* **Budget current per pin and per rail.** A pin's absolute maximum is not an
  operating point; design to roughly half. Sum every output before claiming a
  design is fine, and remember LEDs, relays and motors need their own driver.
* **Never drive a 3.3 V input from 5 V** without a level shifter or a divider,
  and never assume an input is 5 V tolerant because it worked once.
* **1.8 V domains hide in plain sight.** Some memory rails and SPI clock pins run
  at 1.8 V on specific part numbers; check before tying them to 3.3 V logic.
* **Pull-ups are a calculation, not a habit.** 4.7 kΩ at 100 kHz on a short bus,
  2.2 kΩ at 400 kHz or with several devices; internal ~45 kΩ pull-ups are too
  weak for I2C. Strapping/boot pins need their reset level guaranteed by the
  board, not by software.
* **Open-drain means both ends must release.** I2C and 1-Wire cannot be driven
  push-pull; an output-only pin cannot host them.
* **Decouple per device.** 100 nF at each supply pin plus bulk capacitance near
  the regulator; radios and motors want their own bulk capacitors.

## 3. Bus selection

| Need | Bus | Watch out for |
|---|---|---|
| Several slow sensors, few pins | I2C | address collisions, pull-up sizing, total capacitance, clock stretching |
| High throughput to one device | SPI | chip-select discipline, mode (CPOL/CPHA), trace length at >20 MHz |
| Point-to-point link, long wire | UART / RS-485 | level conversion, common ground, flow control |
| Many dumb actuators | PWM | channel count on the MCU, frequency vs resolution trade-off |
| One or two temperature probes | 1-Wire | parasite power, strong pull-up timing |
| Vehicle/industrial bus | CAN | transceiver required, termination, bit timing |
| Analogue measurement | ADC | reference and attenuation, input impedance, sampling vs noise |

State the pull-up value, the clock, and the expected bus capacitance when
proposing I2C — "just add pull-ups" is not an answer.

## 4. Before signing off a wiring proposal

1. Every signal's voltage domain matches at both ends.
2. Every bidirectional bus line is open-drain capable on both sides.
3. Total current per rail and per pin computed, with headroom.
4. Boot/strapping pins have a defined level at reset from the board itself.
5. Decoupling and bulk capacitance named explicitly for each active device.
6. For anything that moves power (motors, heaters, relays): a driver stage,
   flyback/snubber protection, and a separate ground return path.
