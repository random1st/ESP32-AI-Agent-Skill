---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "6.2.2 Bluetooth LE RF Receiver (RX) Characteristics"
pdf_pages: 74-76
retrieved: 2026-09-12
redistribute: false
---

# 6.2.2 Bluetooth LE RF Receiver (RX) Characteristics

```text
6 RF Characteristics


                                       Table 6-10 – cont’d from previous page
  Parameter                             Description                     Min            Typ           Max       Unit
                                        ∆ f 1avg                              —       248.00               —   kHz
  Modulation characteristics            Min ∆ f 1max (for at least
                                                                              —       222.00               —   kHz
                                        99.9% of all∆ f 1max )
                                        ±2 MHz offset                         —       –37.00               —   dBm
  In-band spurious emissions            ±3 MHz offset                         —       –42.00               —   dBm
                                        >±3 MHz offset                        —       –44.00               —   dBm


                       Table 6-11. Transmitter Characteristics - Bluetooth LE 500 Kbps

  Parameter                             Description                     Min            Typ           Max       Unit
                                        RF power control range          –24.00               0       20.00     dBm
  RF transmit power
                                        Gain control step                     —         3.00               —   dB
                                        Max |fn |n=0, 1, 2, ..k               —         0.70               —   kHz
                                        Max |f0 − fn |                        —         0.90               —   kHz
  Carrier frequency offset and drift
                                        |fn − fn−3 |                          —         0.85               —   kHz
                                        |f0 − f3 |                            —         0.34               —   kHz
                                        ∆ f 2avg                              —       213.00               —   kHz
  Modulation characteristics            Min ∆ f 2max (for at least
                                                                              —       196.00               —   kHz
                                        99.9% of all ∆ f 2max )
                                        ±2 MHz offset                         —       –37.00               —   dBm
  In-band spurious emissions            ±3 MHz offset                         —       –42.00               —   dBm
                                        >±3 MHz offset                        —       –44.00               —   dBm



6.2.2 Bluetooth LE RF Receiver (RX) Characteristics

                         Table 6-12. Receiver Characteristics - Bluetooth LE 1 Mbps

  Parameter                                        Description                Min        Typ          Max      Unit
  Sensitivity @30.8% PER                           —                              —      –97.5             —   dBm
  Maximum received signal @30.8% PER               —                              —              8         —   dBm
  Co-channel C/I                                   F = F0 MHz                     —              9         —   dB
                                                   F = F0 + 1 MHz                 —           –3           —   dB
                                                   F = F0 – 1 MHz                 —           –3           —   dB
                                                   F = F0 + 2 MHz                 —          –28           —   dB
                                                   F = F0 – 2 MHz                 —          –30           —   dB
  Adjacent channel selectivity C/I
                                                   F = F0 + 3 MHz                 —          –31           —   dB
                                                   F = F0 – 3 MHz                 —          –33           —   dB
                                                   F > F0 + 3 MHz                 —          –32           —   dB
                                                   F > F0 – 3 MHz                 —          –36           —   dB
  Image frequency                                  —                              —          –32           —   dB
                                                   F = Fimage + 1 MHz             —          –39           —   dB
  Adjacent channel to image frequency
                                                   F = Fimage – 1 MHz             —          –31           —   dB
                                                                                                 Cont’d on next page


Espressif Systems                                            74                   ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
6 RF Characteristics


                                     Table 6-12 – cont’d from previous page
  Parameter                                  Description                  Min      Typ       Max     Unit
                                             30 MHz ~ 2000 MHz                —       –9       —    dBm
                                             2003 MHz ~ 2399 MHz              —       –19      —    dBm
  Out-of-band blocking performance
                                             2484 MHz ~ 2997 MHz              —       –16      —    dBm
                                             3000 MHz ~ 12.75 GHz             —       –5       —    dBm
  Intermodulation                            —                                —       –31      —    dBm



                        Table 6-13. Receiver Characteristics - Bluetooth LE 2 Mbps

  Parameter                                  Description                  Min      Typ       Max     Unit
  Sensitivity @30.8% PER                     —                                —    –93.5       —    dBm
  Maximum received signal @30.8% PER         —                                —          3     —    dBm
  Co-channel C/I                             F = F0 MHz                       —       10       —     dB
                                             F = F0 + 2 MHz                   —       –8       —     dB
                                             F = F0 – 2 MHz                   —       –5       —     dB
                                             F = F0 + 4 MHz                   —       –31      —     dB
                                             F = F0 – 4 MHz                   —      –33       —     dB
  Adjacent channel selectivity C/I
                                             F = F0 + 6 MHz                   —      –37       —     dB
                                             F = F0 – 6 MHz                   —      –37       —     dB
                                             F > F0 + 6 MHz                   —      –40       —     dB
                                             F > F0 – 6 MHz                   —      –40       —     dB
  Image frequency                            —                                —       –31      —     dB
                                             F = Fimage + 2 MHz               —      –37       —     dB
  Adjacent channel to image frequency
                                             F = Fimage – 2 MHz               —       –8       —     dB
                                             30 MHz ~ 2000 MHz                —       –16      —    dBm
                                             2003 MHz ~ 2399 MHz              —      –20       —    dBm
  Out-of-band blocking performance
                                             2484 MHz ~ 2997 MHz              —       –16      —    dBm
                                             3000 MHz ~ 12.75 GHz             —       –16      —    dBm
  Intermodulation                            —                                —      –30       —    dBm


                       Table 6-14. Receiver Characteristics - Bluetooth LE 125 Kbps

  Parameter                                  Description                  Min      Typ       Max     Unit
  Sensitivity @30.8% PER                     —                                —   –104.5       —    dBm
  Maximum received signal @30.8% PER         —                                —          8     —    dBm
  Co-channel C/I                             F = F0 MHz                       —          6     —     dB
                                             F = F0 + 1 MHz                   —       –6       —     dB
                                             F = F0 – 1 MHz                   —       –5       —     dB
                                             F = F0 + 2 MHz                   —      –32       —     dB
                                             F = F0 – 2 MHz                   —      –39       —     dB
  Adjacent channel selectivity C/I
                                             F = F0 + 3 MHz                   —      –35       —     dB
                                             F = F0 – 3 MHz                   —      –45       —     dB
                                             F > F0 + 3 MHz                   —      –35       —     dB
                                                                                       Cont’d on next page


Espressif Systems                                     75                      ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
6 RF Characteristics


                                     Table 6-14 – cont’d from previous page
  Parameter                                  Description                  Min      Typ       Max    Unit
                                             F > F0 – 3 MHz                   —      –48       —     dB
  Image frequency                            —                                —      –35       —     dB
                                             F = Fimage + 1 MHz               —      –49       —     dB
  Adjacent channel to image frequency
                                             F = Fimage – 1 MHz               —      –32       —     dB



                       Table 6-15. Receiver Characteristics - Bluetooth LE 500 Kbps

  Parameter                                  Description                  Min      Typ       Max    Unit
  Sensitivity @30.8% PER                     —                                —     –101       —    dBm
  Maximum received signal @30.8% PER         —                                —          8     —    dBm
  Co-channel C/I                             F = F0 MHz                       —          4     —     dB
                                             F = F0 + 1 MHz                   —       –5       —     dB
                                             F = F0 – 1 MHz                   —       –5       —     dB
                                             F = F0 + 2 MHz                   —      –28       —     dB
                                             F = F0 – 2 MHz                   —      –36       —     dB
  Adjacent channel selectivity C/I
                                             F = F0 + 3 MHz                   —      –36       —     dB
                                             F = F0 – 3 MHz                   —      –38       —     dB
                                             F > F0 + 3 MHz                   —      –37       —     dB
                                             F > F0 – 3 MHz                   —      –41       —     dB
  Image frequency                            —                                —      –37       —     dB
                                             F = Fimage + 1 MHz               —      –44       —     dB
  Adjacent channel to image frequency
                                             F = Fimage – 1 MHz               —      –28       —     dB




Espressif Systems                                     76                      ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
```
