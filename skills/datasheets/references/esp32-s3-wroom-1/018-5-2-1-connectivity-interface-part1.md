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
5 Peripherals


   • Special character AT_CMD detection

   • RS485 protocol

   • IrDA protocol

   • High-speed data communication using GDMA

   • UART as wake-up source

   • Software and hardware flow control

For details, see ESP32-S3 Technical Reference Manual > Chapter UART Controller.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.2   I2C Interface

ESP32-S3 has two I2C bus interfaces which are used for I2C master mode or slave mode, depending on the
user’s configuration.

Feature List

   • Standard mode (100 kbit/s)

   • Fast mode (400 kbit/s)

   • Up to 800 kbit/s (constrained by SCL and SDA pull-up strength)

   • 7-bit and 10-bit addressing mode

   • Double addressing mode (slave addressing and slave register addressing)

The hardware provides a command abstraction layer to simplify the usage of the I2C peripheral.

For details, see ESP32-S3 Technical Reference Manual > Chapter I2C Controller.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.3 I2S Interface

ESP32-S3 includes two standard I2S interfaces. They can operate in master mode or slave mode, in
full-duplex mode or half-duplex communication mode, and can be configured to operate with an 8-bit, 16-bit,
24-bit, or 32-bit resolution as an input or output channel. BCK clock frequency, from 10 kHz up to 40 MHz, is
supported.

The I2S interface has a dedicated DMA controller. It supports TDM PCM, TDM MSB alignment, TDM LSB
alignment, TDM Phillips, and PDM interface.

For details, see ESP32-S3 Technical Reference Manual > Chapter I2S Controller.




Espressif Systems                                     18              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                        Submit Documentation Feedback
5 Peripherals


Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.4     LCD and Camera Controller

The LCD and Camera controller of ESP32-S3 consists of a LCD module and a camera module.

The LCD module is designed to send parallel video data signals, and its bus supports 8-bit ~ 16-bit parallel
RGB, I8080, and MOTO6800 interfaces. These interfaces operate at 40 MHz or lower, and support conversion
among RGB565, YUV422, YUV420, and YUV411.

The camera module is designed to receive parallel video data signals, and its bus supports an 8-bit ~ 16-bit
DVP image sensor, with clock frequency of up to 40 MHz. The camera interface supports conversion among
RGB565, YUV422, YUV420, and YUV411.

For details, see ESP32-S3 Technical Reference Manual > Chapter LCD and Camera Controller.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.5     Serial Peripheral Interface (SPI)

ESP32-S3 has the following SPI interfaces:

   • SPI0 used by ESP32-S3’s GDMA controller and cache to access in-package or off-package flash/PSRAM

   • SPI1 used by the CPU to access in-package or off-package flash/PSRAM

   • SPI2 is a general purpose SPI controller with access to a DMA channel allocated by the GDMA controller

   • SPI3 is a general purpose SPI controller with access to a DMA channel allocated by the GDMA controller

Feature List

   • SPI0 and SPI1:

          – Supports Single SPI, Dual SPI, Quad SPI, Octal SPI, QPI, and OPI modes

          – 8-line SPI mode supports single data rate (SDR) and double data rate (DDR)

          – Configurable clock frequency with a maximum of 120 MHz for 8-line SPI SDR/DDR modes

          – Data transmission is in bytes

   • SPI2:

          – Supports operation as a master or slave

          – Connects to a DMA channel allocated by the GDMA controller

          – Supports Single SPI, Dual SPI, Quad SPI, Octal SPI, QPI, and OPI modes

          – Configurable clock polarity (CPOL) and phase (CPHA)

          – Configurable clock frequency

          – Data transmission is in bytes


Espressif Systems                                        19             ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                            Submit Documentation Feedback
5 Peripherals


        – Configurable read and write data bit order: most-significant bit (MSB) first, or least-significant bit
          (LSB) first

        – As a master

             * Supports 2-line full-duplex communication with clock frequency up to 80 MHz

             * Full-duplex 8-line SPI mode supports single data rate (SDR) only

             * Supports 1-, 2-, 4-, 8-line half-duplex communication with clock frequency up to 80 MHz

             * Half-duplex 8-line SPI mode supports both single data rate (up to 80 MHz) and double data rate
                (up to 40 MHz)

             * Provides six SPI_CS pins for connection with six independent SPI slaves

             * Configurable CS setup time and hold time

        – As a slave

             * Supports 2-line full-duplex communication with clock frequency up to 60 MHz

             * Supports 1-, 2-, 4-line half-duplex communication with clock frequency up to 60 MHz

             * Full-duplex and half-duplex 8-line SPI mode supports single data rate (SDR) only

   • SPI3:

        – Supports operation as a master or slave

        – Connects to a DMA channel allocated by the GDMA controller

        – Supports Single SPI, Dual SPI, Quad SPI, and QPI modes

        – Configurable clock polarity (CPOL) and phase (CPHA)

        – Configurable clock frequency

        – Data transmission is in bytes

        – Configurable read and write data bit order: most-significant bit (MSB) first, or least-significant bit
          (LSB) first

        – As a master

             * Supports 2-line full-duplex communication with clock frequency up to 80 MHz

             * Supports 1-, 2-, 4-line half-duplex communication with clock frequency up to 80 MHz

             * Provides three SPI_CS pins for connection with three independent SPI slaves

             * Configurable CS setup time and hold time

        – As a slave

             * Supports 2-line full-duplex communication with clock frequency up to 60 MHz

             * Supports 1-, 2-, 4-line half-duplex communication with clock frequency up to 60 MHz

For details, see ESP32-S3 Technical Reference Manual > Chapter SPI Controller.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


Espressif Systems                                       20               ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                          Submit Documentation Feedback
5 Peripherals



5.2.1.6 Two-Wire Automotive Interface (TWAI® )

The Two-Wire Automotive Interface (TWAI® ) is a multi-master, multi-cast communication protocol with error
detection and signaling as well as inbuilt message priorities and arbitration.

Feature List

   • Compatible with ISO 11898-1 protocol (CAN Specification 2.0)

   • Standard frame format (11-bit ID) and extended frame format (29-bit ID)

   • Bit rates from 1 Kbit/s to 1 Mbit/s

   • Multiple modes of operation:

        – Normal

        – Listen Only

        – Self-Test (no acknowledgment required)

   • 64-byte receive FIFO

   • Acceptance filter (single and dual filter modes)

   • Error detection and handling:

        – Error counters

        – Configurable error interrupt threshold

        – Error code capture

        – Arbitration lost capture

For details, see ESP32-S3 Technical Reference Manual > Chapter Two-wire Automotive Interface.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.7 USB 2.0 OTG Full-Speed Interface

ESP32-S3 features a full-speed USB OTG interface along with an integrated transceiver. The USB OTG
interface complies with the USB 2.0 specification.

General Features

   • FS and LS data rates

   • HNP and SRP as A-device or B-device

   • Dynamic FIFO (DFIFO) sizing

   • Multiple modes of memory access

        – Scatter/Gather DMA mode

        – Buffer DMA mode



Espressif Systems                                       21              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
5 Peripherals


        – Slave mode

   • Can choose integrated transceiver or external transceiver

   • Utilizing integrated transceiver with USB Serial/JTAG by time-division multiplexing when only integrated
     transceiver is used

   • Support USB OTG using one of the transceivers while USB Serial/JTAG using the other one when both
     integrated transceiver or external transceiver are used

Device Mode Features

   • Endpoint number 0 always present (bi-directional, consisting of EP0 IN and EP0 OUT)

   • Six additional endpoints (endpoint numbers 1 to 6), configurable as IN or OUT

   • Maximum of five IN endpoints concurrently active at any time (including EP0 IN)

   • All OUT endpoints share a single RX FIFO

   • Each IN endpoint has a dedicated TX FIFO

Host Mode Features

   • Eight channels (pipes)

        – A control pipe consists of two channels (IN and OUT), as IN and OUT transactions must be handled
             separately. Only Control transfer type is supported.

        – Each of the other seven channels is dynamically configurable to be IN or OUT, and supports Bulk,
             Isochronous, and Interrupt transfer types.

   • All channels share an RX FIFO, non-periodic TX FIFO, and periodic TX FIFO. The size of each FIFO is
     configurable.

For details, see ESP32-S3 Technical Reference Manual > Chapter USB On-The-Go.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.1.8 USB Serial/JTAG Controller

ESP32-S3 integrates a USB Serial/JTAG controller.

Feature List

   • USB Full-speed device.

   • Can be configured to either use internal USB PHY of ESP32-S3 or external PHY via GPIO matrix.

   • Fixed function device, hardwired for CDC-ACM (Communication Device Class - Abstract Control Model)
     and JTAG adapter functionality.

   • Two OUT Endpoints, three IN Endpoints in addition to Control Endpoint 0; Up to 64-byte data payload
     size.



Espressif Systems                                         22           ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
5 Peripherals
```
