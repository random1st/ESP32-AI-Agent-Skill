---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "1.2 Comparison"
pdf_pages: 13
retrieved: 2026-09-12
redistribute: false
---

# 1.2 Comparison

```text
1 ESP32-S3 Series Comparison



1 ESP32-S3 Series Comparison

1.1 Nomenclature

         ESP32-S3        F      H/N         x         R        H     x          V


                                                                                           1.8 V external SPI flash only



                                                                                           PSRAM size (MB)


                                                                                           PSRAM temperature
                                                                                           H: High temperature


                                                                                           PSRAM



                                                                                           Flash size (MB)

                                                                                           Flash temperature
                                                                                           H: High temperature
                                                                                           N: Normal temperature

                                                                                           Flash



                                                                                           Chip series


                                      Figure 1-1. ESP32-S3 Series Nomenclature

1.2      Comparison
                                       Table 1-1. ESP32-S3 Series Comparison

 Part Number1            In-Package Flash 2 In-Package PSRAM Ambient Temp. 3 VDD_SPI Voltage 4 Chip Revision
 ESP32-S3                        —                        —           –40 ∼ 105 °C        3.3 V/1.8 V           v0.1/v0.2
 ESP32-S3FN8             8 MB (Quad SPI)5                 —              –40 ∼ 85 °C        3.3 V               v0.1/v0.2
 ESP32-S3RH2                     —                2 MB (Quad SPI)     –40 ∼ 105 °C          3.3 V                  v0.2
 ESP32-S3R8                      —                8 MB (Octal SPI)       –40 ∼ 65 °C        3.3 V               v0.1/v0.2
 ESP32-S3R16V                    —               16 MB (Octal SPI)       –40 ∼ 65 °C         1.8 V                 v0.2
 ESP32-S3FH4R2            4 MB (Quad SPI)         2 MB (Quad SPI)        –40 ∼ 85 °C        3.3 V               v0.1/v0.2
 ESP32-S3R8V (EOL)               —                8 MB (Octal SPI)       –40 ∼ 65 °C         1.8 V              v0.1/v0.2
 ESP32-S3R2 (EOL)6               —                2 MB (Quad SPI)        –40 ∼ 85 °C        3.3 V               v0.1/v0.2
  1 For details on chip marking and packing, see Section 7 Packaging.
  2 For information about in-package flash, see also Section 4.1.2.1 Internal Memory. By default, the SPI flash on the

      chip operates at a maximum clock frequency of 80 MHz and does not support the auto suspend feature. If you have
      a requirement for a higher flash clock frequency of 120 MHz or if you need the flash auto suspend feature, please
      contact us.
  3 Ambient temperature specifies the recommended temperature range of the environment immediately outside an

      Espressif chip. For chips with Octal SPI PSRAM (ESP32-S3R8, ESP32-S3R8V, and ESP32-S3R16V), if the PSRAM ECC
      function is enabled, the maximum ambient temperature can be improved to 85 °C, while the usable size of PSRAM will
    be reduced by 1/16.
  4 For more information on VDD_SPI, see Section 2.5 Power Supply.
  5 For details about SPI modes, see Section 2.6 Pin Mapping Between Chip and Flash/PSRAM.
  6 ESP32-S3R2 has been upgraded to ESP32-S3RH2. For more information, see PCN.



Espressif Systems                                             13                       ESP32-S3 Series Datasheet v2.2
                                                Submit Documentation Feedback
```
