---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "4.4 JTAG Signal Source Control"
pdf_pages: 15
retrieved: 2026-09-12
redistribute: false
---

# 4.4 JTAG Signal Source Control

```text
4 Boot Configurations


In SPI Boot mode, the ROM bootloader loads and executes the program from SPI flash to boot the
system.

In Joint Download Boot mode, users can download binary files into flash using UART0 or USB interface. It is
also possible to download binary files into SRAM and execute it from SRAM.

In addition to SPI Boot and Joint Download Boot modes, ESP32-S3 also supports SPI Download Boot mode.
For details, please see ESP32-S3 Technical Reference Manual > Chapter Chip Boot Control.


4.2       VDD_SPI Voltage Control
Depending on the value of EFUSE_VDD_SPI_FORCE, the voltage can be controlled in two ways.

                                      Table 4-4. VDD_SPI Voltage Control

      VDD_SPI power source 2      Voltage      EFUSE_VDD_SPI_FORCE          GPIO45    EFUSE_VDD_SPI_TIEH
      VDD3P3_RTC via RSP I         3.3 V                                      0
                                                           0                                Ignored
      Flash Voltage Regulator       1.8 V                                      1
      Flash Voltage Regulator       1.8 V                                                       0
                                                              1             Ignored
      VDD3P3_RTC via RSP I         3.3 V                                                        1
      1 Bold marks the default value and configuration.
      2 See ESP32-S3 Series Datasheet > Section Power Scheme.



4.3       ROM Messages Printing Control
During boot process the messages by the ROM code can be printed to:

   • (Default) UART0 and USB Serial/JTAG controller

   • USB Serial/JTAG controller

   • UART0

The ROM messages printing to UART or USB Serial/JTAG controller can be respectively disabled by configuring
registers and eFuse. For detailed information, please refer to ESP32-S3 Technical Reference Manual >
Chapter Chip Boot Control.


4.4       JTAG Signal Source Control
The strapping pin GPIO3 can be used to control the source of JTAG signals during the early boot process. This
pin does not have any internal pull resistors and the strapping value must be controlled by the external circuit
that cannot be in a high impedance state.

As Table 4-5 shows, GPIO3 is used in combination with EFUSE_DIS_PAD_JTAG, EFUSE_DIS_USB_JTAG, and
EFUSE_STRAP_JTAG_SEL.




Espressif Systems                                        15             ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                            Submit Documentation Feedback
```
