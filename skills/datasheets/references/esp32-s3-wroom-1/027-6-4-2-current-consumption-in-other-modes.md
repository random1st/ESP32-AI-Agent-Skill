---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "6.4.2 Current Consumption in Other Modes"
pdf_pages: 29
retrieved: 2026-09-12
redistribute: false
---

# 6.4.2 Current Consumption in Other Modes

```text
5 Peripherals



  Note:
  The content below is excerpted from Section Current Consumption in Other Modes in ESP32-S3 Series Datasheet.




6.4.2     Current Consumption in Other Modes
Please note that if the chip embedded has in-package PSRAM, the current consumption of the module might
be higher compared to the measurements below.

                            Table 6-6. Current Consumption in Modem-sleep Mode

                    Frequency                                                                       Typ1     Typ2
 Work mode            (MHz)        Description                                                     (mA)      (mA)
                                   WAITI (Dual core in idle state)                                   13.2        18.8
                                   Single core running 32-bit data access instructions, the
                                                                                                     16.2        21.8
                                   other core in idle state
                              40   Dual core running 32-bit data access instructions                 18.7        24.4
                                   Single core running 128-bit data access instructions, the
                                                                                                     19.9        25.4
                                   other core in idle state
                                   Dual core running 128-bit data access instructions                23.0        28.8
                                   WAITI                                                             22.0        36.1
                                   Single core running 32-bit data access instructions, the
                                                                                                     28.4        42.6
                                   other core in idle state
                              80   Dual core running 32-bit data access instructions                 33.1        47.3
                                   Single core running 128-bit data access instructions, the
                                                                                                     35.1        49.6
                                   other core in idle state
                                   Dual core running 128-bit data access instructions                41.8        56.3
 Modem-sleep3
                                   WAITI                                                             27.6        42.3
                                   Single core running 32-bit data access instructions, the
                                                                                                     39.9        54.6
                                   other core in idle state
                            160    Dual core running 32-bit data access instructions                 49.6        64.1
                                   Single core running 128-bit data access instructions, the
                                                                                                     54.4        69.2
                                   other core in idle state
                                   Dual core running 128-bit data access instructions                66.7         81.1
                                   WAITI                                                             32.9        47.6
                                   Single core running 32-bit data access instructions, the
                                                                                                     51.2        65.9
                                   other core in idle state
                            240    Dual core running 32-bit data access instructions                66.2         81.3
                                   Single core running 128-bit data access instructions, the
                                                                                                     72.4         87.9
                                   other core in idle state
                                   Dual core running 128-bit data access instructions                91.7        107.9
 1 Current consumption when all peripheral clocks are disabled.
 2 Current consumption when all peripheral clocks are enabled. In practice, the current consumption might be
   different depending on which peripherals are enabled.
 3 In Modem-sleep mode, Wi-Fi is clock gated, and the current consumption might be higher when accessing
   flash. For a flash rated at 80 Mbit/s, in SPI 2-line mode the consumption is 10 mA.



Espressif Systems                                       29              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
```
