---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "5 Peripherals"
pdf_pages: 17
retrieved: 2026-09-12
redistribute: false
---

# 5 Peripherals

```text
5 Peripherals



5 Peripherals

5.1       Peripheral Overview
ESP32-S3 integrates a rich set of peripherals including SPI, LCD, Camera interface, UART, I2C, I2S, remote
control, pulse counter, LED PWM, USB Serial/JTAG, MCPWM, SD/MMC host controller, TWAI® controller
(compatible with ISO 11898-1, i.e., CAN Specification 2.0), ADC, touch sensor, and temperature sensor. It also
includes a full-speed USB 2.0 On-The-Go (OTG) interface to enable USB communication.

To learn more about on-chip components, please refer to ESP32-S3 Series Datasheet > Section Functional
Description.

  Note:
  The content below is sourced from ESP32-S3 Series Datasheet > Section Peripherals. Some information may not be
  applicable to ESP32-S3-WROOM-1 and ESP32-S3-WROOM-1U as not all the IO signals are exposed on the module.
  To learn more about peripheral signals, please refer to ESP32-S3 Technical Reference Manual > Section Peripheral
  Signals via GPIO Matrix.




5.2       Peripheral Description
This section describes the chip’s peripheral capabilities, covering connectivity interfaces and on-chip sensors
that extend its functionality.


5.2.1     Connectivity Interface
This subsection describes the connectivity interfaces on the chip that enable communication and interaction
with external devices and networks.


5.2.1.1    UART Controller

ESP32-S3 has three UART (Universal Asynchronous Receiver Transmitter) controllers, i.e., UART0, UART1, and
UART2, which support IrDA and asynchronous communication (RS232 and RS485) at a speed of up to 5
Mbps.

Feature List

   • Three clock sources that can be divided

   • Programmable baud rate

   • 1024 x 8-bit RAM shared by TX FIFOs and RX FIFOs of the three UART controllers

   • Full-duplex asynchronous communication

   • Automatic baud rate detection of input signals

   • Data bits ranging from 5 to 8

   • Stop bits of 1, 1.5, 2, or 3 bits

   • Parity bit


Espressif Systems                                       17               ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                         Submit Documentation Feedback
```
