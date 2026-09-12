---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "4.2 Peripherals"
pdf_pages: 51
retrieved: 2026-09-12
redistribute: false
---

# 4.2 Peripherals

```text
4 Functional Description



4.2       Peripherals
This section describes the chip’s peripheral capabilities, covering connectivity interfaces and on-chip sensors
that extend its functionality.


4.2.1     Connectivity Interface
This subsection describes the connectivity interfaces on the chip that enable communication and interaction
with external devices and networks.


4.2.1.1 UART Controller

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

   • Special character AT_CMD detection

   • RS485 protocol

   • IrDA protocol

   • High-speed data communication using GDMA

   • UART as wake-up source

   • Software and hardware flow control

For details, see ESP32-S3 Technical Reference Manual > Chapter UART Controller.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.


4.2.1.2    I2C Interface

ESP32-S3 has two I2C bus interfaces which are used for I2C master mode or slave mode, depending on the
user’s configuration.



Espressif Systems                                     51                      ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
```
