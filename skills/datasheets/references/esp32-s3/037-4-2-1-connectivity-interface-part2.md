---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "4.2.1 Connectivity Interface"
pdf_pages: 51-58
retrieved: 2026-09-12
redistribute: false
---

# 4.2.1 Connectivity Interface

```text

Espressif Systems                                         56                ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
4 Functional Description


Feature List

   • Secure Digital (SD) memory version 3.0 and version 3.01

   • Secure Digital I/O (SDIO) version 3.0

   • Consumer Electronics Advanced Transport Architecture (CE-ATA) version 1.1

   • Multimedia Cards (MMC version 4.41, eMMC version 4.5 and version 4.51)

   • Up to 80 MHz clock output

   • Three data bus modes:

          – 1-bit

          – 4-bit (supports two SD/SDIO/MMC 4.41 cards, and one SD card operating at 1.8 V in 4-bit mode)

          – 8-bit

  Note:
  When working at 80 MHz, the clock phase adjustment is limited and only phase 0° and 180° are supported. The PCB
  layout should be optimized accordingly to ensure timing closure.



For details, see ESP32-S3 Technical Reference Manual > Chapter SD/MMC Host Controller.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.

Feature List

   • Can generate a digital waveform with configurable periods and duty cycle. The duty cycle resolution can
     be up to 14 bits within a 1 ms period

   • Multiple clock sources, including APB clock and external main crystal clock

   • Can operate when the CPU is in Light-sleep mode

   • Gradual increase or decrease of duty cycle, useful for the LED RGB color-fading generator

For details, see ESP32-S3 Technical Reference Manual > Chapter LED PWM Controller.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.


4.2.1.10 Motor Control PWM (MCPWM)

ESP32-S3 integrates two MCPWMs that can be used to drive digital motors and smart light. Each MCPWM
peripheral has one clock divider (prescaler), three PWM timers, three PWM operators, and a capture module.
PWM timers are used for generating timing references. The PWM operators generate desired waveform based
on the timing references. Any PWM operator can be configured to use the timing references of any PWM
timers. Different PWM operators can use the same PWM timer’s timing references to produce related PWM




Espressif Systems                                         57                    ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
4 Functional Description


signals. PWM operators can also use different PWM timers’ values to produce the PWM signals that work
alone. Different PWM timers can also be synchronized together.

For details, see ESP32-S3 Technical Reference Manual > Chapter Motor Control PWM.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.


4.2.1.11 Remote Control Peripheral (RMT)

The Remote Control Peripheral (RMT) is designed to send and receive infrared remote control signals.

Feature List

   • Four TX channels

   • Four RX channels

   • Support multiple channels (programmable) transmitting data simultaneously

   • Eight channels share a 384 x 32-bit RAM

   • Support modulation on TX pulses

   • Support filtering and demodulation on RX pulses

   • Wrap TX mode

   • Wrap RX mode

   • Continuous TX mode

   • DMA access for TX mode on channel 3

   • DMA access for RX mode on channel 7

For details, see ESP32-S3 Technical Reference Manual > Chapter Remote Control Peripheral.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.


4.2.1.12 Pulse Count Controller (PCNT)

The pulse count controller (PCNT) captures pulse and counts pulse edges through multiple modes.

Feature List

   • Four independent pulse counters (units) that count from 1 to 65535

   • Each unit consists of two independent channels sharing one pulse counter

   • All channels have input pulse signals (e.g. sig_ch0_un) with their corresponding control signals (e.g.
     ctrl_ch0_un)

   • Independently filter glitches of input pulse signals (sig_ch0_un and sig_ch1_un) and control signals
     (ctrl_ch0_un and ctrl_ch1_un) on each unit


Espressif Systems                                    58                      ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
```
