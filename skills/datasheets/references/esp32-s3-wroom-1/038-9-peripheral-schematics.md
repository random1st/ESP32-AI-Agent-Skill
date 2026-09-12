---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "9 Peripheral Schematics"
pdf_pages: 41
retrieved: 2026-09-12
redistribute: false
---

# 9 Peripheral Schematics

```text
    9 Peripheral Schematics



    9         Peripheral Schematics
    This is the typical application circuit of the module connected with peripheral components (for example,
    power supply, antenna, reset button, JTAG interface, and UART interface).

     VDD33                                                      GND                                           GND                VDD33
                                                                                                                                               JP1
                                                                        ESP32-S3-WROOM-1/ESP32-S3-WROOM-1U                                 1
                                                                                                        41                                 2    1
         C1            C3                       R1       TBD             1                        EPAD 40                                  3    2
                                                                         2 GND                     GND 39         IO1                      4    3
         22uF          0.1uF                    C2       TBD     EN      3 3V3                      IO1 38        IO2                           4
                                    GND                                     EN                      IO2 37
                                                                 IO4     4                                        TXD0                         UART
     GND          GND                                            IO5     5 IO4                    TXD0 36         RXD0            GND          JP2
                  C4 12pF(NC)                                    IO6     6 IO5                    RXD0 35         IO42            TMS      1
     GND
                                     R2   X1: ESR = Max. 70 K    IO7     7 IO6                     IO42 34        IO41            TDI      2    1
                                                                         8 IO7                     IO41 33                                      2
                            1
                   X1                         R3      0(NC)      IO15                                             IO40            TDO      3
                                              R5      0(NC)      IO16    9 IO15                    IO40 32        IO39            TCK      4    3
        32.768KHz(NC)
                                                                 IO17   10 IO16                    IO39 31        IO38                          4
                                     NC                                 11 IO17                    IO38 30                        GND
                            2
                                                                 IO18                                             IO37                         JTAG
     GND
                  C7    12pF(NC)                                 IO8    12 IO18                    IO37 29        IO36                          JP4
                                                                 IO19   13 IO8                     IO36 28        IO35                     2
                                                                 IO20   14 IO19                    IO35 27        IO0                      1    2
     JP3                                                                    IO20                    IO0                                         1
              1        USB_D-               R6           0                                                                              Boot Option
        1
                                                                             IO3
                       USB_D+
                                                                             IO46
              2
                                                                             IO9
                                            R4           0
                                                                             IO10
                                                                             IO11
                                                                             IO12
        2
                                                                             IO13
                                                                             IO14
                                                                                                                       SW1
                                                                             IO21
                                                                             IO47
                                                                             IO48
                                                                             IO45
     USB OTG                   C6         C5 NC: No component.              15
                                                                            16
                                                                            17
                                                                            18
                                                                            19
                                                                            20                         U1                        R7        0 EN
                                                                            21
                                                                            22
                                                                            23
                                                                            24
                                                                            25
                                                                            26
                            TBD           TBD                                                                     C8     0.1uF
                                                                            IO3
                                                                            IO46
                                                                            IO9
                                                                            IO10
                                                                            IO11
                                                                            IO12
                                                                            IO13
                               GNDGND                                                                       GND
                                                                            IO14
                                                                            IO21
                                                                            IO47
                                                                            IO48
                                                                            IO45

                               For ESP32-S3-WROOM-1-N16R16V and ESP32-S3-WROOM-1U-N16R16V, IO47/IO48 operates in the 1.8V voltage domain.


                                                               Figure 9-1. Peripheral Schematics


        • Soldering the EPAD to the ground of the base board is not a must, however, it can optimize thermal
            performance. If you choose to solder it, please apply the correct amount of soldering paste. Too much
            soldering paste may increase the gap between the module and the baseboard. As a result, the adhesion
            between other pins and the baseboard may be poor.

        • To ensure that the power supply to the ESP32-S3 chip is stable during power-up, it is advised to add an
            RC delay circuit at the EN pin. The recommended setting for the RC delay circuit is usually R = 10 kΩ and
            C = 1 µF. However, specific parameters should be adjusted based on the power-up timing of the module
            and the power-up and reset sequence timing of the chip. For ESP32-S3’s power-up and reset sequence
            timing diagram, please refer Section 4.5 Chip Power-up and Reset.




5                                                    4                                             3                                                  2




    Espressif Systems                                                         41              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                                                Submit Documentation Feedback
```
