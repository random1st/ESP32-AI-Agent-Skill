---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "6.2.1 Bluetooth LE RF Transmitter (TX) Characteristics"
pdf_pages: 73
retrieved: 2026-09-12
redistribute: false
---

# 6.2.1 Bluetooth LE RF Transmitter (TX) Characteristics

```text
6 RF Characteristics



6.2.1 Bluetooth LE RF Transmitter (TX) Characteristics

                        Table 6-8. Transmitter Characteristics - Bluetooth LE 1 Mbps

  Parameter                            Description                     Min          Typ           Max       Unit
                                       RF power control range         –24.00              0       20.00     dBm
  RF transmit power
                                       Gain control step                     —       3.00               —   dB
                                       Max |fn |n=0, 1, 2, ..k               —       2.50               —   kHz
                                       Max |f0 − fn |                        —       2.00               —   kHz
  Carrier frequency offset and drift
                                       Max |fn − fn−5 |                      —        1.39              —   kHz
                                       |f1 − f0 |                            —       0.80               —   kHz
                                       ∆ f 1avg                              —     249.00               —   kHz
                                       Min ∆ f 2max (for at least
  Modulation characteristics                                                 —     198.00               —   kHz
                                       99.9% of all ∆ f 2max )
                                       ∆ f 2avg /∆ f 1avg                    —       0.86               —    —
                                       ±2 MHz offset                         —     –37.00               —   dBm
  In-band spurious emissions           ±3 MHz offset                         —     –42.00               —   dBm
                                       >±3 MHz offset                        —     –44.00               —   dBm



                        Table 6-9. Transmitter Characteristics - Bluetooth LE 2 Mbps

  Parameter                            Description                     Min          Typ           Max       Unit
                                       RF power control range         –24.00              0       20.00     dBm
  RF transmit power
                                       Gain control step                     —       3.00               —   dB
                                       Max |fn |n=0, 1, 2, ..k               —       2.50               —   kHz
                                       Max |f0 − fn |                        —        1.90              —   kHz
  Carrier frequency offset and drift
                                       Max |fn − fn−5 |                      —        1.40              —   kHz
                                       |f1 − f0 |                            —        1.10              —   kHz
                                       ∆ f 1avg                              —     499.00               —   kHz
                                       Min ∆ f 2max (for at least
  Modulation characteristics                                                 —     416.00               —   kHz
                                       99.9% of all ∆ f 2max )
                                       ∆ f 2avg /∆ f 1avg                    —       0.89               —    —
                                       ±4 MHz offset                         —     –43.80               —   dBm
  In-band spurious emissions           ±5 MHz offset                         —     –45.80               —   dBm
                                       >±5 MHz offset                        —     –47.00               —   dBm


                       Table 6-10. Transmitter Characteristics - Bluetooth LE 125 Kbps

  Parameter                            Description                     Min          Typ           Max       Unit
                                       RF power control range         –24.00              0       20.00     dBm
  RF transmit power
                                       Gain control step                     —       3.00               —   dB
                                       Max |fn |n=0, 1, 2, ..k               —       0.80               —   kHz
                                       Max |f0 − fn |                        —       0.98               —   kHz
  Carrier frequency offset and drift
                                       |fn − fn−3 |                          —       0.30               —   kHz
                                       |f0 − f3 |                            —        1.00              —   kHz
                                                                                              Cont’d on next page


Espressif Systems                                           73                   ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
```
