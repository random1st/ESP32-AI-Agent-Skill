---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "7.2.2 Bluetooth LE RF Receiver (RX) Characteristics"
pdf_pages: 36-38
retrieved: 2026-09-12
redistribute: false
---

# 7.2.2 Bluetooth LE RF Receiver (RX) Characteristics

```text
5 Peripherals


                      Table 7-11. Bluetooth LE - Transmitter Characteristics - 500 Kbps

  Parameter                            Description                       Min            Typ         Max       Unit
                                       Max |fn |n=0, 1, 2, ..k                 —         0.80             —   kHz
                                       Max |f0 − fn |                          —         1.00             —   kHz
  Carrier frequency offset and drift
                                       |fn − fn−3 |                            —         0.85             —   kHz
                                       |f0 − f3 |                              —         0.34             —   kHz
                                       ∆ f 2avg                                —       213.00             —   kHz
  Modulation characteristics           Min ∆ f 2max (for at least
                                                                               —       196.00             —   kHz
                                       99.9% of all ∆ f 2max )
                                       ±2 MHz offset                           —       –37.00             —   dBm
  In-band spurious emissions           ±3 MHz offset                           —       –42.00             —   dBm
                                       >±3 MHz offset                          —       –44.00             —   dBm




7.2.2   Bluetooth LE RF Receiver (RX) Characteristics

                        Table 7-12. Bluetooth LE - Receiver Characteristics - 1 Mbps

  Parameter                                       Description                  Min        Typ        Max      Unit
  Sensitivity @30.8% PER                          —                                —     –96.5            —   dBm
  Maximum received signal @30.8% PER              —                                —            8         —   dBm
  Co-channel C/I                                  F = F0 MHz                       —            8         —   dB
                                                  F = F0 + 1 MHz                   —            4         —   dB
                                                  F = F0 – 1 MHz                   —            4         —   dB
                                                  F = F0 + 2 MHz                   —          –23         —   dB
                                                  F = F0 – 2 MHz                   —          –23         —   dB
  Adjacent channel selectivity C/I
                                                  F = F0 + 3 MHz                   —          –34         —   dB
                                                  F = F0 – 3 MHz                   —          –34         —   dB
                                                  F > F0 + 3 MHz                   —          –36         —   dB
                                                  F > F0 – 3 MHz                   —          –37         —   dB
  Image frequency                                 —                                —          –36         —   dB
                                                  F = Fimage + 1 MHz               —          –39         —   dB
  Adjacent channel to image frequency
                                                  F = Fimage – 1 MHz               —          –34         —   dB
                                                  30 MHz ~ 2000 MHz                —          –12         —   dBm
                                                  2003 MHz ~ 2399 MHz              —          –18         —   dBm
  Out-of-band blocking performance
                                                  2484 MHz ~ 2997 MHz              —          –16         —   dBm
                                                  3000 MHz ~ 12.75 GHz             —          –10         —   dBm
  Intermodulation                                 —                                —          –29         —   dBm


                        Table 7-13. Bluetooth LE - Receiver Characteristics - 2 Mbps

  Parameter                                       Description                  Min        Typ        Max      Unit
  Sensitivity @30.8% PER                          —                                —          –92         —   dBm
  Maximum received signal @30.8% PER              —                                —            3         —   dBm
                                                                                                Cont’d on next page


Espressif Systems                                           36           ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
5 Peripherals


                                     Table 7-13 – cont’d from previous page
  Parameter                                  Description                  Min        Typ        Max       Unit
  Co-channel C/I                             F = F0 MHz                        —           8          —    dB
                                             F = F0 + 2 MHz                    —           4          —    dB
                                             F = F0 – 2 MHz                    —           4          —    dB
                                             F = F0 + 4 MHz                    —      –27             —    dB
                                             F = F0 – 4 MHz                    —      –27             —    dB
  Adjacent channel selectivity C/I
                                             F = F0 + 6 MHz                    —      –38             —    dB
                                             F = F0 – 6 MHz                    —      –38             —    dB
                                             F > F0 + 6 MHz                    —      –41             —    dB
                                             F > F0 – 6 MHz                    —      –41             —    dB
  Image frequency                            —                                 —      –27             —    dB
                                             F = Fimage + 2 MHz                —      –38             —    dB
  Adjacent channel to image frequency
                                             F = Fimage – 2 MHz                —           4          —    dB
                                             30 MHz ~ 2000 MHz                 —      –15             —   dBm
                                             2003 MHz ~ 2399 MHz               —      –21             —   dBm
  Out-of-band blocking performance
                                             2484 MHz ~ 2997 MHz               —      –21             —   dBm
                                             3000 MHz ~ 12.75 GHz              —        –9            —   dBm
  Intermodulation                            —                                 —      –29             —   dBm


                       Table 7-14. Bluetooth LE - Receiver Characteristics - 125 Kbps

  Parameter                                  Description                  Min        Typ        Max       Unit
  Sensitivity @30.8% PER                     —                                 —    –103.5            —   dBm
  Maximum received signal @30.8% PER         —                                 —           8          —   dBm
  Co-channel C/I                             F = F0 MHz                        —           4          —    dB
                                             F = F0 + 1 MHz                    —            1         —    dB
                                             F = F0 – 1 MHz                    —           2          —    dB
                                             F = F0 + 2 MHz                    —      –26             —    dB
                                             F = F0 – 2 MHz                    —      –26             —    dB
  Adjacent channel selectivity C/I
                                             F = F0 + 3 MHz                    —      –36             —    dB
                                             F = F0 – 3 MHz                    —      –39             —    dB
                                             F > F0 + 3 MHz                    —      –42             —    dB
                                             F > F0 – 3 MHz                    —      –43             —    dB
  Image frequency                            —                                 —      –42             —    dB
                                             F = Fimage + 1 MHz                —      –43             —    dB
  Adjacent channel to image frequency
                                             F = Fimage – 1 MHz                —      –36             —    dB



                      Table 7-15. Bluetooth LE - Receiver Characteristics - 500 Kbps

   Parameter                                  Description                     Min    Typ        Max       Unit
   Sensitivity @30.8% PER                     —                                 —   –100          —       dBm
   Maximum received signal @30.8% PER         —                                 —       8         —       dBm
   Co-channel C/I                             F = F0 MHz                        —       4         —       dB
                                                                                        Cont’d on next page



Espressif Systems                                     37              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                         Submit Documentation Feedback
5 Peripherals


                                      Table 7-15 – cont’d from previous page
   Parameter                                   Description                     Min   Typ      Max      Unit
                                               F = F0 + 1 MHz                    —       1       —      dB
                                               F = F0 – 1 MHz                    —      0        —      dB
                                               F = F0 + 2 MHz                    —    –24        —      dB
                                               F = F0 – 2 MHz                    —    –24        —      dB
   Adjacent channel selectivity C/I
                                               F = F0 + 3 MHz                    —    –37        —      dB
                                               F = F0 – 3 MHz                    —   –39         —      dB
                                               F > F0 + 3 MHz                    —    –38        —      dB
                                               F > F0 – 3 MHz                    —   –42         —      dB
   Image frequency                             —                                 —    –38        —      dB
                                               F = Fimage + 1 MHz                —   –42         —      dB
   Adjacent channel to image frequency
                                               F = Fimage – 1 MHz                —    –37        —      dB




Espressif Systems                                      38              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                          Submit Documentation Feedback
```
