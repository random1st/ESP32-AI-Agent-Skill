---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Block Diagram"
pdf_pages: 15
retrieved: 2026-09-12
redistribute: true
---

# Block Diagram

```text
                                                                                                                              TCA9554
www.ti.com                                                                                 SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


8.2 Functional Block Diagram


                13                                                                         Interrupt
      INT                                          LP Filter
                                                                                             Logic


                 1
       A0
                 2
       A1
                                                                                                                              P7−P0
                 3
       A2

                14
     SCL                       Input                    I2C Bus
                                                                              Shift                          I/O
                15             Filter                   Control                                 8 Bits
     SDA                                                                     Register                        Port




                                                                                  Write Pulse

                16                 Power-On                                       Read Pulse
     VCC                             Reset
                 8
     GND


            Pin numbers shown are for the PW package.

                                                Figure 14. Functional Block Diagram




Copyright © 2012–2017, Texas Instruments Incorporated                                                Submit Documentation Feedback    15
                                                          Product Folder Links: TCA9554
```
