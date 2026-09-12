---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Curves"
pdf_pages: 26
retrieved: 2026-09-12
redistribute: true
---

# Curves

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                                                         www.ti.com


Typical Application (continued)

                                                                             3.3 V                       5V




                                                                             VCC              LED


                                                                              LEDx




                                                   Figure 28. Device Supplied by a Lower Voltage

9.2.2 Detailed Design Procedure
The pull-up resistors, RP, for the SCL and SDA lines need to be selected appropriately and take into
consideration the total capacitance of all slaves on the I2C bus. The minimum pull-up resistance is a function of
VCC, VOL,(max), and IOL as shown in Equation 5.
                VCC - VOL(max)
     Rp(min) =
                      IOL                                                                                      (5)
The maximum pull-up resistance is a function of the maximum rise time, tr (300 ns for fast-mode operation, fSCL =
400 kHz) and bus capacitance, Cb as shown in Equation 6.
                   tr
     Rp(max) =
               0.8473 ´ Cb                                                                                     (6)
The maximum bus capacitance for an I2C bus must not exceed 400 pF for standard-mode or fast-mode
operation. The bus capacitance can be approximated by adding the capacitance of the TCA9554, Ci for SCL or
Cio for SDA, the capacitance of wires, connections, traces, and the capacitance of additional slaves on the bus.

9.2.3 Application Curves

                  25                                                                                     1.8
                                                               Standard-mode
                                                               Fast-mode                                 1.6
                  20                                                                                     1.4

                                                                                                         1.2



 Rp(max) (kOhm)                                                                         Rp(min) (kOhm)
                  15
                                                                                                          1

                                                                                                         0.8
                  10
                                                                                                         0.6

                   5                                                                                     0.4

                                                                                                         0.2                                                      VCC > 2V
                                                                                                                                                                  VCC <= 2
                   0                                                                                      0
                       0   50    100   150   200   250   300   350     400     450                             0   0.5   1     1.5   2    2.5  3     3.5   4    4.5   5   5.5
                                              Cb (pF)                            D008
                                                                                                                                          VCC (V)                            D009
         Standard-mode                           Fast-mode                                       VOL = 0.2 × VCC, IOL = 2 mA when VCC ≤ 2 V
         (fSCL= 100 kHz, tr = 1 µs)              (fSCL = 400 kHz, tr = 300 ns)                   VOL = 0.4 V, IOL = 3 mA when VCC > 2 V
                       Figure 29. Maximum Pull-Up Resistance (Rp(max)) vs Bus                             Figure 30. Minimum Pull-Up Resistance (Rp(min)) vs Pull-Up
                                         Capacitance (Cb)                                                                  Reference Voltage (VCC)




26                     Submit Documentation Feedback                                                                         Copyright © 2012–2017, Texas Instruments Incorporated

                                                                     Product Folder Links: TCA9554
```
