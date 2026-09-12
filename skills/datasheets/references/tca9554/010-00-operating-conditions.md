---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Operating Conditions"
pdf_pages: 5
retrieved: 2026-09-12
redistribute: true
---

# Operating Conditions

```text
                                                                                                                                        TCA9554
www.ti.com                                                                                    SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


6 Specifications
6.1 Absolute Maximum Ratings
over operating free-air temperature range (unless otherwise noted) (1)
                                                                                                              MIN           MAX              UNIT
VCC         Supply voltage                                                                                   –0.5             6                V
                            (2)
VI          Input voltage                                                                                    –0.5             6                V
VO          Output voltage (2)                                                                               –0.5             6                V
IIK         Input clamp current                                         VI < 0                                               –20              mA
IOK         Output clamp current                                        VO < 0                                               –20              mA
IIOK        Input-output clamp current                                  VO < 0 or VO > VCC                                   ±20              mA
IOL         Continuous output low current through a single P-port       VO = 0 to VCC                                        50               mA
IOH         Continuous output high current through a single P-port      VO = 0 to VCC                                        –50              mA
            Continuous current through GND by all P-ports                                                                    250
ICC                                                                                                                                           mA
            Continuous current through VCC                                                                                  –160
Tj(MAX)     Maximum junction temperature                                                                                     100              °C
Tstg        Storage temperature                                                                               –65            150              °C

(1)    Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings
       only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended
       Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2)    The input negative-voltage and output voltage ratings may be exceeded if the input and output current ratings are observed.

6.2 ESD Ratings
                                                                                                                       VALUE                 UNIT
                                            Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1)                         ±2000
V(ESD)      Electrostatic discharge         Charged-device model (CDM), per JEDEC specification JESD22-                                       V
                                                                                                                           ±1000
                                            C101 (2)

(1)    JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. Manufacturing with
       less than 500-V HBM is possible with the necessary precautions.
(2)    JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. Manufacturing with
       less than 250-V CDM is possible with the necessary precautions.

6.3 Recommended Operating Conditions
                                                                                                                    MIN             MAX       UNIT
VCC          Supply voltage                                                                                         1.65              5.5      V
                                                    SCL, SDA                     VCC = 1.65 V to 5.5 V       0.7 × VCC             VCC (1)
VIH          High-level input voltage                                            VCC = 1.65 V to 2.7 V       0.7 × VCC                5.5      V
                                                    A0, A1, A2, P7–P0
                                                                                 VCC = 3 V to 5.5 V          0.8 × VCC                5.5
                                                    SCL, SDA                     VCC = 1.65 V to 5.5 V              –0.5     0.3 × VCC
VIL          Low-level input voltage                                             VCC = 1.65 V to 2.7 V              –0.5     0.3 × VCC         V
                                                    A0, A1, A2, P7–P0
                                                                                 VCC = 3 V to 5.5 V                 –0.5     0.2 × VCC
                                                                                 Tj ≤ 65°C                                             25
                                                    P00–P07, P10–P17             Tj ≤ 85°C                                             18
IOL          Low-level output current (2)                                        Tj ≤ 100°C                                             9     mA
                                                                                 Tj ≤ 85°C                                              6
                                                    INT, SDA
                                                                                 Tj ≤ 100°C                                             3
IOH          High-level output current              Any P-port, P7–P0                                                                –10      mA
             Continuous current through GND         All P-ports P7-P0, INT, and SDA                                                  200
ICC                                                                                                                                           mA
             Continuous current through VCC         All P-ports P7-P0                                                                –80


(1)    For voltages applied above VCC, an increase in ICC will result.
(2)    The values shown apply to specific junction temperatures, which depend on the RθJA of the package used. See the Calculating Junction
       Temperature and Power Dissipation section on how to calculate the junction temperature.
Copyright © 2012–2017, Texas Instruments Incorporated                                                 Submit Documentation Feedback                  5
                                                         Product Folder Links: TCA9554
```
