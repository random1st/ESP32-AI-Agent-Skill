---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "of Contents"
pdf_pages: 2
retrieved: 2026-09-12
redistribute: true
---

# of Contents

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                                                                      www.ti.com


                                                                            Table of Contents
    1    Features .................................................................. 1                          8.4 Device Functional Modes........................................ 17
    2    Applications ........................................................... 1                             8.5 Programming........................................................... 17
    3    Description ............................................................. 1                            8.6 Register Maps ......................................................... 19
    4    Revision History..................................................... 2                         9     Application and Implementation ........................ 24
                                                                                                                9.1 Application Information............................................ 24
    5    Pin Configuration and Functions ......................... 4
                                                                                                                9.2 Typical Application ................................................. 24
    6    Specifications......................................................... 5
         6.1     Absolute Maximum Ratings ..................................... 5                        10 Power Supply Recommendations ..................... 27
                                                                                                                10.1 Power-On Reset Requirements ........................... 27
         6.2     ESD Ratings ............................................................ 5
         6.3     Recommended Operating Conditions....................... 5                               11 Layout................................................................... 29
         6.4     Thermal Information .................................................. 6                       11.1 Layout Guidelines ................................................. 29
         6.5     Electrical Characteristics........................................... 6                        11.2 Layout Example .................................................... 29
         6.6     I2C Interface Timing Requirements........................... 8                          12 Device and Documentation Support ................. 30
         6.7     Switching Characteristics .......................................... 8                         12.1     Documentation Support ........................................ 30
         6.8     Typical Characteristics .............................................. 9                       12.2     Receiving Notification of Documentation Updates 30
    7    Parameter Measurement Information ................ 11                                                  12.3     Community Resources.......................................... 30
                                                                                                                12.4     Trademarks ........................................................... 30
    8    Detailed Description ............................................ 14
                                                                                                                12.5     Electrostatic Discharge Caution ............................ 30
         8.1 Overview ................................................................. 14
                                                                                                                12.6     Glossary ................................................................ 30
         8.2 Functional Block Diagram ....................................... 15
         8.3 Feature Description................................................. 16                     13 Mechanical, Packaging, and Orderable
                                                                                                            Information ........................................................... 30



4 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

Changes from Revision D (August 2015) to Revision E                                                                                                                                         Page

•   Added DW package................................................................................................................................................................ 1
•   Added Maximum junction temperature to the Absolute Maximum Ratings table .................................................................. 5
•   Added IOL for different Tj to the Recommended Operating Conditions table.......................................................................... 5
•   Changed ICC standby into different input states, with increased maximums ......................................................................... 7
•   Changed Cio, Ci maximum ..................................................................................................................................................... 7
•   Removed ΔICC spec from the Electrical Characteristics table, added ΔICC typical characteristics graph .............................. 7
•   Clarified interrupt reset time (tir) with respect to falling edge of ACK related SCL pulse. ................................................... 12
•   Made changes to the Interrupt Output (INT) section............................................................................................................ 16
•   Made changes to the Reads section ................................................................................................................................... 22
•   Added the Calculating Junction Temperature and Power Dissipation section..................................................................... 25
•   Changed recommended supply sequencing values ............................................................................................................ 27
•   Power on reset requirements relaxed ................................................................................................................................. 27


Changes from Revision C (May 2015) to Revision D                                                                                                                                            Page

•   Added DB package................................................................................................................................................................. 1


Changes from Revision B (October 2014) to Revision C                                                                                                                                        Page

•   Added standby mode current for VI = VCC test condition........................................................................................................ 7
•   Changed ΔICC for one P-port input at VI = VCC - 0.6, and other P-port I/O at VI = VCC or GND. ............................................ 7
•   Added clarification in datasheet that raising voltage above VCC on P-port I/O will result in current flow from P-port to
    VCC. ...................................................................................................................................................................................... 16



2        Submit Documentation Feedback                                                                                       Copyright © 2012–2017, Texas Instruments Incorporated

                                                                          Product Folder Links: TCA9554
```
