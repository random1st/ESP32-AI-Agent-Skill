---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "8.5 Programming"
pdf_pages: 17
retrieved: 2026-09-12
redistribute: true
---

# 8.5 Programming

```text
                                                                                                                          TCA9554
www.ti.com                                                                              SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


8.4 Device Functional Modes
8.4.1 Power-On Reset
When power (from 0 V) is applied to VCC, an internal power-on reset holds the TCA9554 in a reset condition
until VCC has reached VPORR. At that point, the reset condition is released and the TCA9554 registers and
SMBus/I2C state machine initializes to their default states. After that, VCC must be lowered to below VPORF and
then back up to the operating voltage for a power-on reset cycle.

8.5 Programming
8.5.1 I2C Interface
The bidirectional I2C bus consists of the serial clock (SCL) and serial data (SDA) lines. Both lines must be
connected to a positive supply through a pull-up resistor when connected to the output stages of a device. Data
transfer may be initiated only when the bus is not busy.
I2C communication with this device is initiated by a master sending a Start condition, a high-to-low transition on
the SDA input-output while the SCL input is high (see Figure 16). After the Start condition, the device address
byte is sent, most significant bit (MSB) first, including the data direction bit (R/W).
After receiving the valid address byte, this device responds with an acknowledge (ACK), a low on the SDA
input/output during the high of the ACK-related clock pulse. The address inputs (A0–A2) of the slave device must
not be changed between the Start and the Stop conditions.
On the I2C bus, only one data bit is transferred during each clock pulse. The data on the SDA line must remain
stable during the high pulse of the clock period, as changes in the data line at this time are interpreted as control
commands (Start or Stop) (see Figure 17).
A Stop condition, a low-to-high transition on the SDA input/output while the SCL input is high, is sent by the
master (see Figure 16).
Any number of data bytes can be transferred from the transmitter to receiver between the Start and the Stop
conditions. Each byte of eight bits is followed by one ACK bit. The transmitter must release the SDA line before
the receiver can send an ACK bit. The device that acknowledges must pull down the SDA line during the ACK
clock pulse so that the SDA line is stable low during the high pulse of the ACK-related clock period (see
Figure 18). When a slave receiver is addressed, it must generate an ACK after each byte is received. Similarly,
the master must generate an ACK after each byte that it receives from the slave transmitter. Setup and hold
times must be met to ensure proper operation.
A master receiver signals an end of data to the slave transmitter by not generating an acknowledge (NACK) after
the last byte has been clocked out of the slave. This is done by the master receiver by holding the SDA line high.
In this event, the transmitter must release the data line to enable the master to generate a Stop condition.


                       SDA




                       SCL
                                           S                                                       P

                                    Start Condition                                          Stop Condition

                                       Figure 16. Definition of Start and Stop Conditions




Copyright © 2012–2017, Texas Instruments Incorporated                                          Submit Documentation Feedback      17
                                                        Product Folder Links: TCA9554
```
