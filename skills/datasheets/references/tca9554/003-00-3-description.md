---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "3 Description"
pdf_pages: 1
retrieved: 2026-09-12
redistribute: true
---

# 3 Description

```text
                                 Product          Order         Technical              Tools &          Support &
                                 Folder           Now           Documents              Software         Community



                                                                                                                               TCA9554
                                                                                             SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017

TCA9554 Low Voltage 8-Bit I2C and SMBus Low-Power I/O Expander With Interrupt Output
                             and Configuration Registers
1 Features                                                                3 Description
•
1
    2
    I C to Parallel Port Expander                                         The TCA9554 is a 16-pin device that provides 8 bits
                                                                          of general purpose parallel input and output (I/O)
•   Open-Drain Active-Low Interrupt Output                                expansion for the two-line bidirectional I2C bus (or
•   Operating Power-Supply Voltage Range of 1.65 V                        SMBus) protocol. The device can operate with a
    to 5.5 V                                                              power supply voltage ranging from 1.65 V to 5.5 V.
•   5-V Tolerant I/O Ports                                                The device supports both 100-kHz (Standard-mode)
                                                                          and 400-kHz (Fast-mode) clock frequencies. I/O
•   400-kHz Fast I2C Bus
                                                                          expanders such as the TCA9554 provide a simple
•   Three Hardware Address Pins Allow up to Eight                         solution when additional I/Os are needed for
    Devices on the I2C/SMBus                                              switches, sensors, push-buttons, LEDs, fans, and
•   Input and Output Configuration Register                               other similar devices.
•   Polarity Inversion Register                                           The features of the TCA9554 include an interrupt that
•   Internal Power-On Reset                                               is generated on the INT pin whenever an input port
                                                                          changes state. The A0, A1, and A2 hardware
•   Low Standby Current Consumption
                                                                          selectable address pins allow up to eight TCA9554
•   Power-Up With All Channels Configured as Inputs                       devices on the same I2C bus. The device can also be
•   No Glitch on Power Up                                                 reset to its default sate by cycling the power supply
•   Noise Filter on SCL/SDA Inputs                                        and causing a power-on reset.
•   Latched Outputs With High-Current Drive                                                       Device Information(1)
    Maximum Capability for Directly Driving LEDs                             PART NUMBER              PACKAGE         BODY SIZE (NOM)
•   Latch-Up Performance Exceeds 100 mA Per                                                        TSSOP (16)       5.00 mm × 4.40 mm
    JESD 78, Class II                                                                              SSOP (16)        4.90 mm × 3.90 mm
•   ESD Protection Exceeds JESD 22                                          TCA9554
                                                                                                   SSOP (16)        6.20 mm × 5.30 mm
    – 2000-V Human-Body Model (A114-A)                                                             SOIC (16)        7.50 mm × 10.30 mm
    – 1000-V Charged-Device Model (C101)                                    (1) For all available packages, see the orderable addendum at
                                                                                the end of the datasheet.
2 Applications
•   Servers
•   Routers (Telecom Switching Equipment)
•   Personal Computers
•   Personal Electronics (for example: Gaming
    Consoles)
•   Industrial Automation
•   Products With GPIO-Limited Processors
                                                     Simplified Block Diagram

                                                                    VCC
                                                          SDA                                         Peripheral
                                                          SCL                                          Devices
                               I2C or SMBus                                       P0
                                                          INT
                                  Master                                          P1                 • RESET,
                               (e.g. Processor)                                   P2                   ENABLE, or
                                                                                  P3
                                                                 TCA9554                               control
                                                                                  P4                   inputs
                                                          A0                      P5
                                                                                  P6                 • INT or
                                                          A1                      P7                   status
                                                          A2                                           outputs
                                                          GND                                        • LEDs




1




        An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
        intellectual property matters and other important disclaimers. PRODUCTION DATA.
```
