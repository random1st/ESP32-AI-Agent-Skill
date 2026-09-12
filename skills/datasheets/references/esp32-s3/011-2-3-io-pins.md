---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.3 IO Pins"
pdf_pages: 20
retrieved: 2026-09-12
redistribute: false
---

# 2.3 IO Pins

```text
2 Pins



2.3 IO Pins
2.3.1 IO MUX Functions
The IO MUX allows multiple input/output signals to be connected to a single input/output pin. Each IO pin of
ESP32-S3 can be connected to one of the five signals (IO MUX functions, i.e., F0-F4), as listed in Table 2-4 IO
MUX Functions.

Among the five sets of signals:

   • Some are routed via the GPIO Matrix (GPIO0, GPIO1, etc.), which incorporates internal signal routing
     circuitry for mapping signals programmatically. It gives the pin access to almost any peripheral signals.
     However, the flexibility of programmatic mapping comes at a cost as it might affect the latency of routed
     signals. For details about connecting to peripheral signals via GPIO Matrix, see
     ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

   • Some are directly routed from certain peripherals (U0TXD, MTCK, etc.), including UART0/1, JTAG,
     SPI0/1, and SPI2 - see Table 2-3 Peripheral Signals Routed via IO MUX.

                                  Table 2-3. Peripheral Signals Routed via IO MUX

 Pin Function         Signal                   Description
 U…TXD                Transmit data
 U…RXD                Receive data
                                               UART0/1 interface
 U…RTS                Request to send
 U…CTS                Clear to send
 MTCK                 Test clock
 MTDO                 Test Data Out
                                               JTAG interface for debugging
 MTDI                 Test Data In
 MTMS                 Test Mode Select
 SPIQ                 Master in, slave out
 SPID                 Master out, slave in     SPI0/1 interface (powered by VDD_SPI) for connection to in-package or
 SPIHD                Hold                     off-package flash/PSRAM via the SPI bus. It supports 1-, 2-, 4-line SPI
 SPIWP                Write protect            modes. See also Section 2.6 Pin Mapping Between Chip and
 SPICLK               Clock                    Flash/PSRAM
 SPICS…               Chip select
 SPIIO…               Data                     SPI0/1 interface (powered by VDD_SPI or VDD3P3_CPU) for the higher
 SPIDQS               Data strobe/data mask    4 bits data line interface and DQS interface in 8-line SPI mode
 SPICLK_N_DIFF        Negative clock signal    Differential clock negative/positive for the SPI bus
 SPICLK_P_DIFF        Positive clock signal
 SUBSPIQ              Master in, slave out
 SUBSPID              Master out, slave in
                                               SPI0/1 interface (powered by VDD3P3_RTC or VDD3V3_CPU) for
 SUBSPIHD             Hold
                                               connection to in-package or off-package flash/PSRAM via the SUBSPI
 SUBSPIWP             Write protect
                                               bus. It supports 1-, 2-, 4-line SPI modes
 SUBSPICLK            Clock
 SUBSPICS…            Chip select
 SUBSPICLK_N_DIFF     Negative clock signal    Differential clock negative/positive for the SUBSPI bus
 SUBSPICLK_P_DIFF     Positive clock signal
                                                                                                      Cont’d on next page




Espressif Systems                                       20                         ESP32-S3 Series Datasheet v2.2
                                          Submit Documentation Feedback
```
