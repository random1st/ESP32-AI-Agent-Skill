---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Measurement Information"
pdf_pages: 11-13
retrieved: 2026-09-12
redistribute: true
---

# Measurement Information

```text
                                                                                                                                  TCA9554
www.ti.com                                                                                  SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


7 Parameter Measurement Information




       A.   CL includes probe and jig capacitance.
       B.   All inputs are supplied by generators having the following characteristics: PRR ≤ 10 MHz, ZO = 50 Ω, tr/tf ≤ 30 ns.
       C.   All parameters and waveforms are not applicable to all devices.

                               Figure 11. I2C Interface Load Circuit and Voltage Waveforms




Copyright © 2012–2017, Texas Instruments Incorporated                                                Submit Documentation Feedback     11
                                                        Product Folder Links: TCA9554
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                             www.ti.com


                                        Parameter Measurement Information (continued)
                                                                             VCC


                                                                                   RL = 4.7 kΩ

                                                                         INT
                                                              DUT

                                                                                   CL = 100 pF
                                                                                   (see Note A)



                                                              Interupt Load Configuration




      SCL               1    2     3    4   5   6   7     8
                                 Slave Address                           Data From Port                     Data From Port


      SDA           S    0   1     0     0 A2 A1 A0 1         A                Data 1             A             Data 4               NA P

                     Start                          R/W           ACK From                        ACK From               NACK From          Stop
                     Condition                                    Slave                           Master                    Master          Condition
Read From
      Port

 Data Into
                                   Data 1                           Data 2         Data 3                Data 4                        Data 5
     Port
                                                        tph                                 tps



       INT

            tiv                                         tir




                                                0.7 × VCC                                                                              0.7 × VCC
     INT                                                                     SCL
                                                                                            R/W            A
                                                0.3 × VCC                                                                              0.3 × VCC

                             tiv                                                                               tir

                                                0.7 × VCC                                                                              0.7 × VCC
Data Into                                                                    INT
Port (Pn)                                                                                                                              0.3 × VCC
                                                0.3 × VCC
      A.     CL includes probe and jig capacitance.
      B.     All inputs are supplied by generators having the following characteristics: PRR ≤ 10 MHz, ZO = 50 Ω, tr/tf ≤ 30 ns.
      C.     All parameters and waveforms are not applicable to all devices.

                                       Figure 12. Interrupt Load Circuit and Voltage Waveforms




12     Submit Documentation Feedback                                                              Copyright © 2012–2017, Texas Instruments Incorporated

                                                              Product Folder Links: TCA9554
                                                                                                                                     TCA9554
www.ti.com                                                                                         SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


                                     Parameter Measurement Information (continued)
                                                         Pn                                500 Ω
                                         DUT                                                             2 × VCC

                                                                CL = 50 pF
                                                                                     500
                                                                (see Note A)




                                                               P-Port Load Configuration




                                                                                                               0.7 × VCC
                              SCL
                                               P0                       A                   P3
                                                                                                               0.3 × VCC
                                                                       Slave
                                                                       ACK

                              SDA

                                                                                  tpv
                                                                                  (see Note B)

                                Pn

                                                                                       Last Stable Bit
                                                                     Unstable
                                                                      Data


                                                                  Write Mode (R/W = 0)




                                                                                                               0.7 × VCC
                              SCL
                                               P0                       A                   P3
                                                                                                               0.3 × VCC
                                                                            tph
                                                        tps
                                                                                                               0.7 × VCC
                              Pn
                                                                                                               0.3 × VCC

                                                                  Read Mode (R/W = 1)
       A.   CL includes probe and jig capacitance.
       B.   tpv is measured from 0.7 × VCC on SCL to 50% I/O (Pn) output.
       C.   All inputs are supplied by generators having the following characteristics: PRR ≤ 10 MHz, ZO = 50 Ω, tr/tf ≤ 30 ns.
       D.   The outputs are measured one at a time, with one transition per measurement.
       E.   All parameters and waveforms are not applicable to all devices.

                                     Figure 13. P-Port Load Circuit and Voltage Waveforms




Copyright © 2012–2017, Texas Instruments Incorporated                                                      Submit Documentation Feedback     13
                                                              Product Folder Links: TCA9554
```
