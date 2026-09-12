---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "3.2 VDD_SPI Voltage Control"
pdf_pages: 34
retrieved: 2026-09-12
redistribute: false
---

# 3.2 VDD_SPI Voltage Control

```text
3 Boot Configurations


For details, please see ESP32-S3 Technical Reference Manual > Chapter Chip Boot Control.


3.2     VDD_SPI Voltage Control
The required VDD_SPI voltage for the chips of the ESP32-S3 Series can be found in Table 1-1 ESP32-S3 Series
Comparison.

The VDD_SPI voltage can be:

   • (Default) 3.3 V supplied by VDD3P3_RTC via RSP I

   • 1.8V supplied by the Flash Voltage Regulator

The voltage is determined by EFUSE_VDD_SPI_FORCE, GPIO45, and EFUSE_VDD_SPI_TIEH.

                                      Table 3-4. VDD_SPI Voltage Control

      VDD_SPI power source 2      Voltage      EFUSE_VDD_SPI_FORCE          GPIO45     EFUSE_VDD_SPI_TIEH
                                                           0                  0               Ignored
      VDD3P3_RTC via RSP I         3.3 V
                                                           1                Ignored              1
                                                           0                   1              Ignored
      Flash Voltage Regulator       1.8 V
                                                           1                Ignored              0
      1 Bold marks the default value and configuration.
      2 See Section 2.5.2 Power Scheme.



3.3     ROM Messages Printing Control
During the boot process, the messages by the ROM code can be printed to:

   • (Default) UART0 and USB Serial/JTAG controller

   • USB Serial/JTAG controller

   • UART0

The ROM messages printing to UART or USB Serial/JTAG controller can be respectively disabled by configuring
registers and eFuse. For detailed information, please refer to ESP32-S3 Technical Reference Manual >
Chapter Chip Boot Control.


3.4     JTAG Signal Source Control
The strapping pin GPIO3 can be used to control the source of JTAG signals during the early boot process. This
pin does not have any internal pull resistors and the strapping value must be controlled by the external circuit
that cannot be in a high impedance state.

As Table 3-5 JTAG Signal Source Control shows, GPIO3 is used in combination with EFUSE_DIS_PAD_JTAG,
EFUSE_DIS_USB_JTAG, and EFUSE_STRAP_JTAG_SEL.




Espressif Systems                                        34                        ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
```
