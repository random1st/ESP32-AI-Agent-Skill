---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Reset Requirements"
pdf_pages: 27-28
retrieved: 2026-09-12
redistribute: true
---

# Reset Requirements

```text
                                                                                                                            TCA9554
www.ti.com                                                                                SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


10 Power Supply Recommendations

10.1 Power-On Reset Requirements
In the event of a glitch or data corruption, the TCA9554 can be reset to its default conditions by using the power-
on reset feature. Power-on reset requires that the device go through a power cycle to be completely reset. This
reset also happens when the device is powered on for the first time in an application.
The power-on reset is shown in Figure 31.
VCC

                                        Ramp-Down                                           Ramp-Up

                                                                  VCC_TRR

      VCC drops below VPORF – 50 mV


                                                                                                                                    Time
                                                              Time to Re-Ramp
                                          VCC_FT                                            VCC_RT

               Figure 31. VCC is Lowered Below the POR Threshold, Then Ramped Back Up to VCC

Table 8 specifies the performance of the power-on reset feature for the TCA9554.

                                 Table 8. Recommended Supply Sequencing and Ramp Rates (1)
                                                   PARAMETER                                                      MIN    MAX      UNIT
VCC_FT               Fall rate                                                        See Figure 31                 1    2000     ms
VCC_RT               Rise rate                                                        See Figure 31                0.1   2000     ms
                     Time to re-ramp (when VCC drops to VPOR_MIN – 50 mV or
VCC_TRR                                                                               See Figure 31                 2              μs
                     when VCC drops to GND)
                     Level that VCCP can glitch down to, but not cause a functional
VCC_GH                                                                                See Figure 32                       1.2      V
                     disruption when VCC_GW = 1 µs
                     The minimum voltage that VCC can glitch down to without
VCC_MV                                                                                See Figure 32                1.5             V
                     causing a reset (VCC_GH must not be violated)
                     Glitch width that does not cause a functional disruption when
VCC_GW                                                                                See Figure 32                        10      μs
                     VCC_GH = 0.5 × VCC

(1)   All supply sequencing and ramp rate values are measured at TA = 25°C

Glitches in the power supply can also affect the power-on reset performance of this device. The glitch width
(VCC_GW) and height (VCC_GH) are dependent on each other. The bypass capacitance, source impedance, and
device impedance are factors that affect power-on reset performance. Figure 32 and Table 8 provide more
information on how to measure these specifications.
VCC




             VCC_GH



                                                                             VCC_MV
                                                                                                                                    Time
                                            VCC_GW

                                             Figure 32. Glitch Width and Glitch Height




Copyright © 2012–2017, Texas Instruments Incorporated                                             Submit Documentation Feedback         27
                                                        Product Folder Links: TCA9554
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                           www.ti.com


VPORR is critical to the power-on reset. VPORR is the voltage level at which the reset condition is released and all
the registers and the I2C/SMBus state machine are initialized to their default states. The value of power-on-reset
voltage differs based on the VCC being lowered to or from 0 (VPORR or VPORF). Figure 33 and Table 8 provide
more details on this specification.




VPORR




        Figure 33. Waveform Describing VCC Voltage Level at Which Power-On-Reset (POR) Occurs




28     Submit Documentation Feedback                                            Copyright © 2012–2017, Texas Instruments Incorporated

                                                Product Folder Links: TCA9554
```
