---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "3 Boot Configurations"
pdf_pages: 32
retrieved: 2026-09-12
redistribute: false
---

# 3 Boot Configurations

```text
3 Boot Configurations



3     Boot Configurations
The chip allows for configuring the following boot parameters through strapping pins and eFuse parameters at
power-up or a hardware reset, without microcontroller interaction.

    • Chip boot mode

        – Strapping pin: GPIO0 and GPIO46

    • VDD_SPI voltage

        – Strapping pin: GPIO45

        – eFuse parameter: EFUSE_VDD_SPI_FORCE and EFUSE_VDD_SPI_TIEH

    • ROM message printing

        – Strapping pin: GPIO46

        – eFuse parameter: EFUSE_UART_PRINT_CONTROL and
           EFUSE_DIS_USB_SERIAL_JTAG_ROM_PRINT

    • JTAG signal source

        – Strapping pin: GPIO3

        – eFuse parameter: EFUSE_DIS_PAD_JTAG, EFUSE_DIS_USB_JTAG, and EFUSE_STRAP_JTAG_SEL

The default values of all the above eFuse parameters are 0, which means that they are not burnt. Given that
eFuse is one-time programmable, once programmed to 1, it can never be reverted to 0. For how to program
eFuse parameters, please refer to ESP32-S3 Technical Reference Manual > Chapter eFuse Controller.

The default values of the strapping pins, namely the logic levels, are determined by pins’ internal weak
pull-up/pull-down resistors at reset if the pins are not connected to any circuit, or connected to an external
high-impedance circuit.

                              Table 3-1. Default Configuration of Strapping Pins

                               Strapping Pin    Default Configuration    Bit Value
                               GPIO0                Weak pull-up             1
                               GPIO3                   Floating             –
                               GPIO45             Weak pull-down            0
                               GPIO46             Weak pull-down            0


To change the bit values, the strapping pins should be connected to external pull-down/pull-up resistances. If
the ESP32-S3 is used as a device by a host MCU, the strapping pin voltage levels can also be controlled by
the host MCU.

All strapping pins have latches. At Chip Reset, the latches sample the bit values of their respective strapping
pins and store them until the chip is powered down or shut down. The states of latches cannot be changed in
any other way. It makes the strapping pin values available during the entire chip operation, and the pins are
freed up to be used as regular IO pins after reset. For details on Chip Reset, see
ESP32-S3 Technical Reference Manual > Chapter Reset and Clock.




Espressif Systems                                      32                        ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
```
