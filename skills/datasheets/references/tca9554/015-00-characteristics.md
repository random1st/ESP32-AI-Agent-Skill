---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Characteristics"
pdf_pages: 9-10
retrieved: 2026-09-12
redistribute: true
---

# Characteristics

```text
                                                                                                                                                                                                                        TCA9554
www.ti.com                                                                                                                                                                   SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


6.8 Typical Characteristics
TA = 25°C (unless otherwise noted)

                                   22                                                                                                                        1.8
                                                                                                     1.8 V
                                   20                                                                                                                        1.6
                                                                                                     2.5 V
                                   18                                                                3.3 V
                                                                                                                                                             1.4




   ICC - Supply Current (µA)                                                                                            ICC - Supply Current (µA)
                                                                                                     5V
                                   16
                                                                                                                                                             1.2
                                   14
                                   12                                                                                                                         1
                                   10                                                                                                                        0.8                                                        1.8 V
                                    8                                                                                                                                                                                   2.5 V
                                                                                                                                                             0.6                                                        3.3 V
                                    6                                                                                                                                                                                   5V
                                                                                                                                                             0.4
                                    4
                                    2                                                                                                                        0.2

                                    0                                                                                                                         0
                                    -40             -15           10         35              60          85                                                   -40          -15            10         35            60        85
                                                          TA - Free-Air Temperature (°C)                     D001
                                                                                                                                                                                  TA - Free-Air Temperature (°C)                 D002
                                        fSCL = 400 kHz             I/Os = High or Low Inputs                                                                       fSCL = 0 kHz       I/Os = High Inputs

                                            Figure 1. Supply Current (ICC, Operating Mode) vs                                                                        Figure 2. Supply Current (ICC, Standby Mode) vs
                                                Temperature (TA) at Four Supply Voltages                                                                                Temperature (TA) at Four Supply Voltages
                                   25                                                                                                                        250




                                                                                                                    VOL - Output Low Voltage (mV)
                                   20                                                                                                                        200




  ICC - Supply Current (µA)
                                   15                                                                                                                        150


                                   10                                                                                                                        100


                                                                                                                                                                                                      VCC = 1.8 V, IOL = 8 mA
                                    5                                                                                                                         50                                      VCC = 5 V, IOL = 8 mA
                                                                                                                                                                                                      VCC = 1.8 V, IOL = 10 mA
                                                                                                                                                                                                      VCC = 5 V, IOL = 10 mA
                                    0                                                                                                                          0
                                        0   0.5     1     1.5      2   2.5    3   3.5    4   4.5     5   5.5                                                   -40         -15            10         35            60           85
                                                                VCC - Supply Voltage (V)                     D003
                                                                                                                                                                                  TA - Free-Air Temperature (°C)                 D004
                                        fSCL = 400 kHz           I/Os = High or Low                  TA = 25°C                                                                       I/Os = High or Low Inputs
                                                                              Inputs
                                                                                                                                                              Figure 4. Output Low Voltage (VOL) vs Temperature (TA) for
                                        Figure 3. Supply Current (ICC, Operating Mode) vs Supply                                                                                     P-Port I/Os
                                                             Voltage (VCC)
                                   80                                                                                                                        500
                                               1.8 V                                                                                                                    VCC = 1.8 V, IOH = 8 mA




                                                                                                                    (VCC - VOH) - Output High Voltage (mV)
                                   70          2.5 V                                                                                                         450        VCC = 5 V, IOH = 8 mA




  IOL - Output Sink Current (mA)
                                               3.3 V                                                                                                         400        VCC = 1.65 V, IOH = 10 mA
                                   60          5V                                                                                                                       VCC = 5 V, IOH = 10 mA
                                                                                                                                                             350
                                   50
                                                                                                                                                             300
                                   40                                                                                                                        250

                                   30                                                                                                                        200
                                                                                                                                                             150
                                   20
                                                                                                                                                             100
                                   10                                                                                                                         50
                                    0                                                                                                                          0
                                        0     0.1       0.2     0.3    0.4    0.5      0.6         0.7   0.8                                                   -40         -15            10         35            60           85
                                                          VOL - Output Low Voltage - (V)                     D005
                                                                                                                                                                                  TA - Free-Air Temperature (°C)                 D006
                                            TA = 25°C

                                    Figure 5. Sink Current (IOL) vs Output Low Voltage (VOL) for                                                               Figure 6. Output High Voltage (VCC – VOH) vs Temperature
                                                  P-Ports at Four Supply Voltages                                                                                                   (TA) for P-Ports




Copyright © 2012–2017, Texas Instruments Incorporated                                                                                                                                   Submit Documentation Feedback                9
                                                                                               Product Folder Links: TCA9554
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                                                                                                                       www.ti.com


Typical Characteristics (continued)
TA = 25°C (unless otherwise noted)
                                      70                                                                                                                       6
                                                  1.8 V
                                                  2.5 V




   IOH - Output Source Current (mA)
                                      60
                                                                                                                                                               5




                                                                                                                       VOH - Output High Voltage (V)
                                                  3.3 V
                                                  5V
                                      50
                                                                                                                                                               4
                                      40
                                                                                                                                                               3
                                      30
                                                                                                                                                               2
                                      20

                                      10                                                                                                                       1
                                                                                                                                                                                                                           IOH = -8 mA
                                                                                                                                                                                                                           IOH = -10 mA
                                       0                                                                                                                       0
                                           0     0.1        0.2    0.3     0.4    0.5     0.6      0.7     0.8                                                          0             1          2         3         4          5         6
                                                          (VCC - VOH) - Output High Voltage (V)                 D007
                                                                                                                                                                                                VCC - Supply Voltage (V)                    D008
                                                TA = 25°C                                                                                                                         TA = 25°C

                                       Figure 7. Source Current (IOH) vs Output High Voltage (VOH)                                                              Figure 8. Output High Voltage (VOH) vs Supply Voltage (VCC)
                                                   for P-Ports at Four Supply Voltages                                                                                                  for P-Ports
                                      600                                                                                                                               18
                                      550                                                                                                                                             1.65 V       3.3 V
                                                                                                                                                                                      1.8 V        5V
                                      500                                                                                                                               15            2.5 V        5.5 V




 ICC Supply Current (PA)
                                      450
                                      400                                                                                                                               12



                                                                                                                                                       Delta ICC (µA)
                                      350
                                      300                                                                                                                                   9
                                      250
                                      200                                                                                                                                   6
                                      150
                                      100                                                               25qC
                                                                                                        85qC                                                                3
                                       50                                                               -40qC
                                        0
                                            0      1         2       3        4      5       6      7           8                                                           0
                                                                 Number of I/Os Held Low (#)                                                                                -40           -15         10         35        60          85
                                                                                                                D001                                                                              TA - Temperature (°C)                D019
                                                       VCC = 5 V

                                       Figure 9. Supply Current (ICC) vs Number of I/Os Held Low
                                                                                                                                                                                Figure 10. Δ ICC vs Temperature for Different VCC
                                                                   (#)
                                                                                                                                                                                                 (VI = VCC – 0.6 V)




10                                         Submit Documentation Feedback                                                                                                                  Copyright © 2012–2017, Texas Instruments Incorporated

                                                                                                  Product Folder Links: TCA9554
```
