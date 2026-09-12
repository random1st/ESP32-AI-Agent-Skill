---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "2 Block Diagram"
pdf_pages: 9
retrieved: 2026-09-12
redistribute: false
---

# 2 Block Diagram

```text
                                             QSPI Flash
2 Block Diagram



2 Block Diagram

                                                                 ESP32-S3-WROOM-1
                                              40 MHz
            3V3                               Crystal                              Antenna


                                          ESP32-S3
                                          ESP32-S3R2                RF Matching
                                          ESP32-S3R8
                            EN            ESP32-S3R16V                   GPIOs
                                                   PSRAM(opt.)
                                                   (QSPI/OSPI)
                                          SPICS0
                                          SPICLK
                                          SPID
                                          SPIQ
                                          SPIHD
                                          SPIWP
                                          VDD_SPI


                                            QSPI Flash



                                 Figure 2-1. ESP32-S3-WROOM-1 Block Diagram




                                                                 ESP32-S3-WROOM-1U
                                               40 MHz
            3V3                                Crystal                                         Antenna


                                          ESP32-S3
                                          ESP32-S3R2                 RF Matching
                                          ESP32-S3R8
                            EN            ESP32-S3R16V                   GPIOs
                                                   PSRAM(opt.)
                                                   (QSPI/OSPI)
                                          SPICS0
                                          SPICLK
                                          SPID
                                          SPIQ
                                          SPIHD
                                          SPIWP
                                          VDD_SPI


                                             QSPI Flash



                                 Figure 2-2. ESP32-S3-WROOM-1U Block Diagram

  Note:
  For the pin mapping between the chip and the in-package PSRAM, please refer to ESP32-S3 Series Datasheet > Table
  Pin Mapping Between Chip and In-package Flash/PSRAM.
                                                                 ESP32-S3-WROOM-1
                                              40 MHz
           3V3                                Crystal                              Antenna


                                         ESP32-S3
                                         ESP32-S3R2                 RF Matching
                                         ESP32-S3R8
                            EN           ESP32-S3R16V                    GPIOs
                                                  PSRAM(opt.)
                                                  (QSPI/OSPI)
                                          SPICS0
                                          SPICLK
                                          SPID
                                          SPIQ
                                          SPIHD
                                          SPIWP
                                          VDD_SPI
Espressif Systems                                         9               ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                         Submit Documentation Feedback
                                           QSPI Flash
```
