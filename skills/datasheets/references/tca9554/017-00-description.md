---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Description"
pdf_pages: 14
retrieved: 2026-09-12
redistribute: true
---

# Description

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                           www.ti.com


8 Detailed Description

8.1 Overview
The TCA9554 is an 8-bit I/O expander for the two-line bidirectional bus (I2C) is designed for 1.65-V to 5.5-V VCC
operation. It provides general-purpose remote I/O expansion for most micro-controller families via the I2C
interface (serial clock, SCL, and serial data, SDA, pins).
The TCA9554 open-drain interrupt (INT) output is activated when any input state differs from its corresponding
Input Port register state and is used to indicate to the system master that an input state has changed. The INT
pin can be connected to the interrupt input of a micro-controller. By sending an interrupt signal on this line, the
remote I/O can inform the micro-controller if there is incoming data on its ports without having to communicate
via the I2C bus. Thus, the TCA9554 can remain a simple slave device. The device outputs (latched) have high-
current drive capability for directly driving LEDs.
Three hardware pins (A0, A1, and A2) are used to program and vary the fixed I2C slave address and allow up to
eight devices to share the same I2C bus or SMBus.
The system master can reset the TCA9554 in the event of a timeout or other improper operation by cycling the
power supply and causing a power-on reset (POR). A reset puts the registers in their default state and initializes
the I2C /SMBus state machine.
The TCA9554 consists of one 8-bit Configuration (input or output selection), Input Port, Output Port, and Polarity
Inversion (active high or active low) registers. At power on, the I/Os are configured as inputs. However, the
system master can enable the I/Os as either inputs or outputs by writing to the I/O configuration bits. The data for
each input or output is kept in the corresponding Input Port or Output Port register. The polarity of the Input Port
register can be inverted with the Polarity Inversion register. All registers can be read by the system master.
The TCA9554 and TCA9554A are identical except for their fixed I2C address. This allows for up to 16 of these
devices (8 of each) on the same I2C/SMBus.
The TCA9554 is identical to the TCA9534 except for the addition of the internal I/O pull-up resistors, which keeps
P-ports from floating when configured as inputs.




14     Submit Documentation Feedback                                            Copyright © 2012–2017, Texas Instruments Incorporated

                                                Product Folder Links: TCA9554
```
