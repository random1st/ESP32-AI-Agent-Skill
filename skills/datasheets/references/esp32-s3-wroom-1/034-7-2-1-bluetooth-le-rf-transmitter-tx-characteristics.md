---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "7.2.1 Bluetooth LE RF Transmitter (TX) Characteristics"
pdf_pages: 35
retrieved: 2026-09-12
redistribute: false
---

# 7.2.1 Bluetooth LE RF Transmitter (TX) Characteristics

```text
5 Peripherals



7.2.1 Bluetooth LE RF Transmitter (TX) Characteristics

                        Table 7-8. Bluetooth LE - Transmitter Characteristics - 1 Mbps

  Parameter                            Description                     Min        Typ        Max        Unit
                                       Max |fn |n=0, 1, 2, ..k               —     2.50            —    kHz
                                       Max |f0 − fn |                        —     2.00            —    kHz
  Carrier frequency offset and drift
                                       Max |fn − fn−5 |                      —      1.40           —    kHz
                                       |f1 − f0 |                            —      1.00           —    kHz
                                       ∆ f 1avg                              —   249.00            —    kHz
                                       Min ∆ f 2max (for at least
  Modulation characteristics                                                 —   198.00            —    kHz
                                       99.9% of all ∆ f 2max )
                                       ∆ f 2avg /∆ f 1avg                    —      0.86           —     —
                                       ±2 MHz offset                         —   –37.00            —    dBm
  In-band spurious emissions           ±3 MHz offset                         —   –42.00            —    dBm
                                       >±3 MHz offset                        —   –44.00            —    dBm


                       Table 7-9. Bluetooth LE - Transmitter Characteristics - 2 Mbps

  Parameter                            Description                     Min        Typ        Max        Unit
                                       Max |fn |n=0, 1, 2, ..k               —     2.50            —    kHz
                                       Max |f0 − fn |                        —     2.00            —    kHz
  Carrier frequency offset and drift
                                       Max |fn − fn−5 |                      —      1.40           —    kHz
                                       |f1 − f0 |                            —      1.00           —    kHz
                                       ∆ f 1avg                              —   499.00            —    kHz
                                       Min ∆ f 2max (for at least
  Modulation characteristics                                                 —   416.00            —    kHz
                                       99.9% of all ∆ f 2max )
                                       ∆ f 2avg /∆ f 1avg                    —      0.89           —     —
                                       ±4 MHz offset                         —   –42.00            —    dBm
  In-band spurious emissions           ±5 MHz offset                         —   –44.00            —    dBm
                                       >±5 MHz offset                        —   –47.00            —    dBm

                      Table 7-10. Bluetooth LE - Transmitter Characteristics - 125 Kbps

  Parameter                            Description                     Min        Typ        Max        Unit
                                       Max |fn |n=0, 1, 2, ..k               —     0.80            —    kHz
                                       Max |f0 − fn |                        —      1.00           —    kHz
  Carrier frequency offset and drift
                                       |fn − fn−3 |                          —     0.30            —    kHz
                                       |f0 − f3 |                            —      1.00           —    kHz
                                       ∆ f 1avg                              —   248.00            —    kHz
  Modulation characteristics           Min ∆ f 1max (for at least
                                                                             —   222.00            —    kHz
                                       99.9% of all∆ f 1max )
                                       ±2 MHz offset                         —   –37.00            —    dBm
  In-band spurious emissions           ±3 MHz offset                         —   –42.00            —    dBm
                                       >±3 MHz offset                        —   –44.00            —    dBm




Espressif Systems                                           35         ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
```
