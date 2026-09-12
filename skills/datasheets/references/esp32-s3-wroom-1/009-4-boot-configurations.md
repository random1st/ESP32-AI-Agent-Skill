---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "4 Boot Configurations"
pdf_pages: 13
retrieved: 2026-09-12
redistribute: false
---

# 4 Boot Configurations

```text
4 Boot Configurations



4 Boot Configurations
  Note:
  The content below is excerpted from ESP32-S3 Series Datasheet > Section Boot Configurations. For the strapping
  pin mapping between the chip and modules, please refer to Chapter 8 Module Schematics.



The chip allows for configuring the following boot parameters through strapping pins and eFuse bits at
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

                               Table 4-1. Default Configuration of Strapping Pins

                               Strapping Pin    Default Configuration    Bit Value
                               GPIO0                Weak pull-up             1
                               GPIO3                   Floating              –
                               GPIO45              Weak pull-down            0
                               GPIO46              Weak pull-down            0


To change the bit values, the strapping pins should be connected to external pull-down/pull-up resistances. If
the ESP32-S3 is used as a device by a host MCU, the strapping pin voltage levels can also be controlled by
the host MCU.

All strapping pins have latches. At system reset, the latches sample the bit values of their respective strapping
pins and store them until the chip is powered down or shut down. The states of latches cannot be changed in


Espressif Systems                                      13               ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                         Submit Documentation Feedback
```
