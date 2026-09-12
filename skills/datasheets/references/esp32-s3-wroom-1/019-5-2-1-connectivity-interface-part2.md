---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "5.2.1 Connectivity Interface"
pdf_pages: 17-24
retrieved: 2026-09-12
redistribute: false
---

# 5.2.1 Connectivity Interface

```text


   • Internal PHY, so no or very few external components needed to connect to a host computer.

   • CDC-ACM adherent serial port emulation is plug-and-play on most modern OSes.

   • JTAG interface allows fast communication with CPU debug core using a compact representation of JTAG
     instructions.

   • CDC-ACM supports host controllable chip reset and entry into download mode.

For details, see ESP32-S3 Technical Reference Manual > Chapter USB Serial/JTAG Controller.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.9 SD/MMC Host Controller

ESP32-S3 has an SD/MMC Host controller.

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

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.

Feature List

   • Can generate a digital waveform with configurable periods and duty cycle. The duty cycle resolution can
     be up to 14 bits within a 1 ms period

   • Multiple clock sources, including APB clock and external main crystal clock

   • Can operate when the CPU is in Light-sleep mode


Espressif Systems                                         23             ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
5 Peripherals


   • Gradual increase or decrease of duty cycle, useful for the LED RGB color-fading generator

For details, see ESP32-S3 Technical Reference Manual > Chapter LED PWM Controller.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.10   Motor Control PWM (MCPWM)

ESP32-S3 integrates two MCPWMs that can be used to drive digital motors and smart light. Each MCPWM
peripheral has one clock divider (prescaler), three PWM timers, three PWM operators, and a capture module.
PWM timers are used for generating timing references. The PWM operators generate desired waveform based
on the timing references. Any PWM operator can be configured to use the timing references of any PWM
timers. Different PWM operators can use the same PWM timer’s timing references to produce related PWM
signals. PWM operators can also use different PWM timers’ values to produce the PWM signals that work
alone. Different PWM timers can also be synchronized together.

For details, see ESP32-S3 Technical Reference Manual > Chapter Motor Control PWM.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.11 Remote Control Peripheral (RMT)

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

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


Espressif Systems                                   24              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                       Submit Documentation Feedback
```
