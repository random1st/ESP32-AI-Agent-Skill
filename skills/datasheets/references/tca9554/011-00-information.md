---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Information"
pdf_pages: 6
retrieved: 2026-09-12
redistribute: true
---

# Information

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                                      www.ti.com


Recommended Operating Conditions (continued)
                                                                                                                              MIN                MAX       UNIT
TA           Operating free-air temperature                                                                                    –40                85        °C


6.4 Thermal Information
                                                                                                    TCA9554
                          THERMAL METRIC (1)                                    PW (TSSOP)   DBQ (SSOP)        DB (SSOP)       DW (SOIC)               UNIT
                                                                                 16 PINS      16 PINS            16 PINS           16 PINS
RθJA           Junction-to-ambient thermal resistance                              122           121.7              113.2            84.7              °C/W
RθJC(top)      Junction-to-case (top) thermal resistance                           56.4          72.9                63.6            48                °C/W
RθJB           Junction-to-board thermal resistance                                67.1          64.2                 64             49.1              °C/W
ψJT            Junction-to-top characterization parameter                          10.8          24.4                21.2            22.7              °C/W
ψJB            Junction-to-board characterization parameter                        66.5          63.8                63.4            48.7              °C/W

(1)   For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
      report.

6.5 Electrical Characteristics
over operating free-air temperature range (unless otherwise noted)
                 PARAMETER                                           TEST CONDITIONS                          VCC           MIN       TYP (1)     MAX      UNIT
VIK            Input diode clamp voltage              II = –18 mA                                        1.65 V to 5.5 V    –1.2                             V
               Power-on reset voltage, VCC
VPORR                                                 VI = VCC or GND, IO = 0                                                             1.2      1.5       V
               rising
               Power-on reset voltage, VCC
VPORF                                                 VI = VCC or GND, IO = 0                                               0.75             1
               falling                                                                                                                                       V
                                                                                                             1.65 V          1.2
                                                                                                             2.3 V           1.8
                                                      IOH = –8 mA
                                                                                                              3V             2.6
                                                                                                             4.5 V           4.1
VOH            P-port high-level output voltage (2)
                                                                                                             1.65 V          1.1                             V
                                                                                                             2.3 V           1.7
                                                      IOH = –10 mA
                                                                                                              3V             2.5
                                                                                                             4.5 V            4
               SDA (3)                                VOL = 0.4 V                                        1.65 V to 5.5 V      3             11
                                                                                                             1.65 V           8             10
                                                                                                             2.3 V            8             13
                                                      VOL = 0.5 V
                                                                                                              3V              8             15

                        (4)
                                                                                                             4.5 V            8             17
IOL            P port                                                                                                                                       mA
                                                                                                             1.65 V          10             14
                                                                                                             2.3 V           10             17
                                                      VOL = 0.7 V
                                                                                                              3V             10             20
                                                                                                             4.5 V           10             24
               INT (5)                                VOL = 0.4 V                                        1.65 V to 5.5 V      3              7
               SCL, SDA                                                                                                                             ±1
II                                                    VI = VCC or GND                                    1.65 V to 5.5 V                                    µA
               A0, A1, A2                                                                                                                           ±1
IIH            P port                                 VI = VCC                                           1.65 V to 5.5 V                               1    µA
IIL            P port                                 VI = GND                                           1.65 V to 5.5 V                          –100      µA

(1)   All typical values are at nominal supply voltage (1.8-, 2.5-, 3.3-, or 5-V VCC) and TA = 25°C.
(2)   Each P-port I/O configured as a high output must be externally limited to a maximum of 10 mA, and the total current sourced by all I/Os
      (P-ports P7-P0) through VCC must be limited to a maximum current of 80 mA.
(3)   The SDA pin must be externally limited to a maximum of 12 mA, and the total current sunk by all I/Os (P-ports P7-P0, INT, and SDA)
      through GND must be limited to a maximum current of 200 mA.
(4)   Each P-port I/O configured as a low output must be externally limited to a maximum of 25 mA, and the total current sunk by all I/Os (P-
      ports P7-P0, INT, and SDA) through GND must be limited to a maximum current of 200 mA.
(5)   The INT pin must be externally limited to a maximum of 7 mA, and the total current sunk by all I/Os (P-ports P7-P0, INT, and SDA)
      through GND must be limited to a maximum current of 200 mA.
6        Submit Documentation Feedback                                                              Copyright © 2012–2017, Texas Instruments Incorporated

                                                                 Product Folder Links: TCA9554
```
