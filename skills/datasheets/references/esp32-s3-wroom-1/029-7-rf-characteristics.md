---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "7 RF Characteristics"
pdf_pages: 32
retrieved: 2026-09-12
redistribute: false
---

# 7 RF Characteristics

```text
5 Peripherals



7 RF Characteristics
This section contains tables with RF characteristics of the Espressif product.

The RF data is measured at the antenna port, where RF cable is connected, including the front-end loss. The
external antennas used for the tests on the modules with external antenna connectors have an impedance of
50 Ω.
Devices should operate in the center frequency range allocated by regional regulatory authorities. The target
center frequency range and the target transmit power are configurable by software. See ESP RF Test Tool and
Test Guide for instructions.

Unless otherwise stated, the RF tests are conducted with a 3.3 V (±5%) supply at 25 ºC ambient temperature.




7.1 Wi-Fi Radio

                                        Table 7-1. Wi-Fi RF Characteristics

                  Name                                               Description
                  Center frequency range of operating channel        2412 ~ 2484 MHz
                  Wi-Fi wireless standard                            IEEE 802.11b/g/n



7.1.1 Wi-Fi RF Transmitter (TX) Characteristics

                 Table 7-2. TX Power with Spectral Mask and EVM Meeting 802.11 Standards

                                                                   Min         Typ      Max
                      Rate
                                                                  (dBm)       (dBm)     (dBm)
                      802.11b, 1 Mbps                                  —        20.5        —
                      802.11b, 11 Mbps                                 —        20.5        —
                      802.11g, 6 Mbps                                  —       20.0         —
                      802.11g, 54 Mbps                                 —        18.0        —
                      802.11n, HT20, MCS 0                             —        19.0        —
                      802.11n, HT20, MCS 7                             —         17.5       —
                      802.11n, HT40, MCS 0                             —        18.5        —
                      802.11n, HT40, MCS 7                             —         17.0       —


                                             Table 7-3. TX EVM Test1

                                                                   Min         Typ      Limit
                      Rate
                                                                   (dB)        (dB)     (dB)
                      802.11b, 1 Mbps, @20.5 dBm                       —      –24.5       –10
                      802.11b, 11 Mbps, @20.5 dBm                      —      –24.5       –10
                      802.11g, 6 Mbps, @20 dBm                         —      –23.0        –5
                      802.11g, 54 Mbps, @18 dBm                        —      –29.5       –25
                                                                       Cont’d on next page


Espressif Systems                                       32                 ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                          Submit Documentation Feedback
```
