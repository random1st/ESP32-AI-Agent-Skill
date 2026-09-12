---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Guidelines"
pdf_pages: 29
retrieved: 2026-09-12
redistribute: true
---

# Guidelines

```text
                                                                                                                                     TCA9554
www.ti.com                                                                                 SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


11 Layout

11.1 Layout Guidelines
For printed circuit board (PCB) layout of the TCA9554, common PCB layout practices must be followed but
additional concerns related to high-speed data transfer such as matched impedances and differential pairs are
not a concern for I2C signal speeds.
In all PCB layouts, it is a best practice to avoid right angles in signal traces, to fan out signal traces away from
each other upon leaving the vicinity of an integrated circuit (IC), and to use thicker trace widths to carry higher
amounts of current that commonly pass through power and ground traces. By-pass and de-coupling capacitors
are commonly used to control the voltage on the VCC pin, using a larger capacitor to provide additional power in
the event of a short power supply glitch and a smaller capacitor to filter out high-frequency ripple. These
capacitors must be placed as close to the TCA9554 as possible. These best practices are shown in Figure 34.
For the layout example provided in Figure 34, it is possible to fabricate a PCB with only 2 layers by using the top
layer for signal routing and the bottom layer as a split plane for power (VCC) and ground (GND). However, a 4
layer board is preferable for boards with higher density signal routing. On a 4 layer PCB, it is common to route
signals on the top and bottom layer, dedicate one internal layer to a ground plane, and dedicate the other internal
layer to a power plane. In a board layout using planes or split planes for power and ground, vias are placed
directly next to the surface mount component pad which needs to attach to VCC or GND and the via is connected
electrically to the internal layer or the other side of the board. Vias are also used when a signal trace needs to be
routed to the opposite side of the board, but this technique is not demonstrated in Figure 34.

11.2 Layout Example
                        LEGEND
                     Power or GND Plane
                                                                                                           To I2C Master
                     VIA to Power Plane                                              VCC
                     VIA to GND Plane

                                                              By-pass/De-coupling
                                                                   capacitors




                                                  1         A0                 VCC         16

                                                  2         A1                 SDA         15




                                                                     TCA9554
                                                  3         A2                 SCL         14

                                                  4         P0                 INT         13

                                                  5         P1                  P7         12



           To I/Os
                                                  6         P2                  P6         11



                                                                                                                           To I/Os
                                                  7         P3                  P5         10

                                                  8         GND                 P4         9



                                             GND



                                                        Figure 34. TCA9554 Layout


Copyright © 2012–2017, Texas Instruments Incorporated                                             Submit Documentation Feedback           29
                                                         Product Folder Links: TCA9554
```
