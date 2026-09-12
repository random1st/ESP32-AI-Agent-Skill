---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Configuration and Functions"
pdf_pages: 4
retrieved: 2026-09-12
redistribute: true
---

# Configuration and Functions

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                   www.ti.com


5 Pin Configuration and Functions

                                                    PW, DB, DBQ, or DW Package
                                                     16-Pin TSSOP, SSOP, SOIC
                                                              Top View

                                                                          VCC




                                                          Pin Functions
                PIN
                                            I/O                                          DESCRIPTION
      NAME                NO.
A0                         1                    I        Address input. Connect directly to VCC or ground
A1                         2                    I        Address input. Connect directly to VCC or ground
A2                         3                    I        Address input. Connect directly to VCC or ground
GND                        8                —            Ground
INT                       13                O            Interrupt output. Connect to VCC through a pull-up resistor
                                                         P-port input-output. Push-pull design structure. At power on, P0 is configured
P0                         4                I/O
                                                         as an input
                                                         P-port input-output. Push-pull design structure. At power on, P1 is configured
P1                         5                I/O
                                                         as an input
                                                         P-port input-output. Push-pull design structure. At power on, P2 is configured
P2                         6                I/O
                                                         as an input
                                                         P-port input-output. Push-pull design structure. At power on, P3 is configured
P3                         7                I/O
                                                         as an input
                                                         P-port input-output. Push-pull design structure. At power on, P4 is configured
P4                         9                I/O
                                                         as an input
                                                         P-port input-output. Push-pull design structure. At power on, P5 is configured
P5                        10                I/O
                                                         as an input
                                                         P-port input-output. Push-pull design structure. At power on, P6 is configured
P6                        11                I/O
                                                         as an input
                                                         P-port input-output. Push-pull design structure. At power on, P7 is configured
P7                        12                I/O
                                                         as an input
SCL                       14                    I        Serial clock bus. Connect to VCC through a pull-up resistor
SDA                       15                I/O          Serial data bus. Connect to VCC through a pull-up resistor
VCC                       16                —            Supply voltage




4      Submit Documentation Feedback                                                    Copyright © 2012–2017, Texas Instruments Incorporated

                                                    Product Folder Links: TCA9554
```
