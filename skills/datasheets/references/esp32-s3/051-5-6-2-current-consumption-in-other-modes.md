---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "5.6.2 Current Consumption in Other Modes"
pdf_pages: 67
retrieved: 2026-09-12
redistribute: false
---

# 5.6.2 Current Consumption in Other Modes

```text
5 Electrical Characteristics


                      Table 5-8. Current Consumption for Bluetooth LE in Active Mode

       Work Mode                RF Condition         Description                                 Peak (mA)
                                                     Bluetooth LE @ 21.0 dBm                            335
                                TX                   Bluetooth LE @ 9.0 dBm                              193
       Active (RF working)                           Bluetooth LE @ 0 dBm                                176
                                                     Bluetooth LE @ –15.0 dBm                            116
                                RX                   Bluetooth LE                                         93



5.6.2 Current Consumption in Other Modes
The measurements below are applicable to ESP32-S3 and ESP32-S3FH8. Since ESP32-S3R2, ESP32-S3RH2,
ESP32-S3R8, ESP32-S3R8V, ESP32-S3R16V, and ESP32-S3FN4R2 are embedded with PSRAM, their current
consumption might be higher.

                               Table 5-9. Current Consumption in Modem-sleep Mode

                    Frequency                                                                         Typ1     Typ2
 Work mode            (MHz)          Description                                                      (mA)     (mA)
                                     WAITI (Dual core in idle state)                                   13.2     18.8
                                     Single core running 32-bit data access instructions, the
                                                                                                       16.2     21.8
                                     other core in idle state
                               40    Dual core running 32-bit data access instructions                 18.7     24.4
                                     Single core running 128-bit data access instructions, the
                                                                                                       19.9     25.4
                                     other core in idle state
                                     Dual core running 128-bit data access instructions                23.0     28.8
                                     WAITI                                                             22.0     36.1
                                     Single core running 32-bit data access instructions, the
                                                                                                       28.4     42.6
                                     other core in idle state
                               80    Dual core running 32-bit data access instructions                 33.1     47.3
                                     Single core running 128-bit data access instructions, the
                                                                                                       35.1     49.6
                                     other core in idle state
                                     Dual core running 128-bit data access instructions                41.8    56.3
 Modem-sleep3
                                     WAITI                                                             27.6     42.3
                                     Single core running 32-bit data access instructions, the
                                                                                                       39.9     54.6
                                     other core in idle state
                               160   Dual core running 32-bit data access instructions                 49.6     64.1
                                     Single core running 128-bit data access instructions, the
                                                                                                       54.4     69.2
                                     other core in idle state
                                     Dual core running 128-bit data access instructions                66.7      81.1
                                     WAITI                                                             32.9     47.6
                                     Single core running 32-bit data access instructions, the
                                                                                                       51.2     65.9
                                     other core in idle state
                             240     Dual core running 32-bit data access instructions                 66.2     81.3
                                     Single core running 128-bit data access instructions, the
                                                                                                       72.4     87.9
                                     other core in idle state
                                                                                                 Cont’d on next page


Espressif Systems                                         67                    ESP32-S3 Series Datasheet v2.2
                                             Submit Documentation Feedback
```
