---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "6.1.1 Wi-Fi RF Transmitter (TX) Characteristics"
pdf_pages: 70
retrieved: 2026-09-12
redistribute: false
---

# 6.1.1 Wi-Fi RF Transmitter (TX) Characteristics

```text
6 RF Characteristics



6 RF Characteristics
This section contains tables with RF characteristics of the Espressif product.

The RF data is measured at the antenna port, where RF cable is connected, including the front-end loss. The
front-end circuit is a 0 Ω resistor.

Devices should operate in the center frequency range allocated by regional regulatory authorities. The target
center frequency range and the target transmit power are configurable by software. See ESP RF Test Tool and
Test Guide for instructions.

Unless otherwise stated, the RF tests are conducted with a 3.3 V (±5%) supply at 25 ºC ambient temperature.




6.1    Wi-Fi Radio

                                         Table 6-1. Wi-Fi RF Characteristics

                   Name                                               Description
                   Center frequency range of operating channel        2412 ~ 2484 MHz
                   Wi-Fi wireless standard                            IEEE 802.11b/g/n



6.1.1 Wi-Fi RF Transmitter (TX) Characteristics

                  Table 6-2. TX Power with Spectral Mask and EVM Meeting 802.11 Standards

                                                                    Min         Typ      Max
                       Rate                                        (dBm)       (dBm)    (dBm)
                       802.11b, 1 Mbps                                  —        21.0       —
                       802.11b, 11 Mbps                                 —        21.0       —
                       802.11g, 6 Mbps                                  —       20.5        —
                       802.11g, 54 Mbps                                 —        19.0       —
                       802.11n, HT20, MCS0                              —        19.5       —
                       802.11n, HT20, MCS7                              —        18.5       —
                       802.11n, HT40, MCS0                              —        19.5       —
                       802.11n, HT40, MCS7                              —        18.0       —



                                              Table 6-3. TX EVM Test1

                                                                    Min         Typ      Limit
                       Rate                                         (dB)       (dB)      (dB)
                       802.11b, 1 Mbps, @21 dBm                         —      –24.5       –10
                       802.11b, 11 Mbps, @21 dBm                        —      –24.5       –10
                       802.11g, 6 Mbps, @20.5 dBm                       —       –21.5       –5
                       802.11g, 54 Mbps, @19 dBm                        —      –28.0      –25
                                                                        Cont’d on next page



Espressif Systems                                        70                        ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
```
