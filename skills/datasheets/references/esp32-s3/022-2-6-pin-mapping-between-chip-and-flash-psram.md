---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.6 Pin Mapping Between Chip and Flash/PSRAM"
pdf_pages: 31
retrieved: 2026-09-12
redistribute: false
---

# 2.6 Pin Mapping Between Chip and Flash/PSRAM

```text
2 Pins



2.6 Pin Mapping Between Chip and Flash/PSRAM
Table 2-14 lists the pin mapping between the chip and flash/PSRAM for all SPI modes.

For chip variants with in-package flash/PSRAM (see Table 1-1 ESP32-S3 Series Comparison), the pins allocated
for communication with in-package flash/PSRAM can be identified depending on the SPI mode used.

For off-package flash/PSRAM, these are the recommended pin mappings.

For more information on SPI controllers, see also Section 4.2.1.5 Serial Peripheral Interface (SPI).

  Notice: Do not use the pins connected to in-package flash/PSRAM for any other purposes.



                          Table 2-14. Pin Mapping Between Chip and Flash or PSRAM

                               Single SPI               Dual SPI              Quad SPI/QPI        Octal SPI/OPI
 Pin No.   Pin Name      Flash       PSRAM        Flash        PSRAM     Flash       PSRAM     Flash      PSRAM
 28        SPICS1 2                  CE#                       CE#                   CE#                  CE#
 30        SPIHD         HOLD#       SIO3         HOLD#        SIO3      HOLD#       SIO3      DQ3        DQ3
 31        SPIWP         WP#         SIO2         WP#          SIO2      WP#         SIO2      DQ2        DQ2
 32        SPICS0 1      CS#                      CS#                    CS#                   CS#
 33        SPICLK        CLK         CLK          CLK          CLK       CLK         CLK       CLK        CLK
 34        SPIQ          DO          SO/SIO1      DO           SO/SIO1   DO          SO/SIO1   DQ1        DQ1
 35        SPID          DI          SI/SIO0      DI           SI/SIO0   DI          SI/SIO0   DQ0        DQ0
 38        GPIO33                                                                              DQ4        DQ4
 39        GPIO34                                                                              DQ5        DQ5
 40        GPIO35                                                                              DQ6        DQ6
 41        GPIO36                                                                              DQ7        DQ7
 42        GPIO37                                                                              DQS/DM     DQS/DM
 1 CS0 is for in-package flash
 2 CS1 is for in-package PSRAM




Espressif Systems                                         31                        ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
```
