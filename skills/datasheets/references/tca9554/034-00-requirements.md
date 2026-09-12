---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Requirements"
pdf_pages: 25
retrieved: 2026-09-12
redistribute: true
---

# Requirements

```text
                                                                                                                          TCA9554
www.ti.com                                                                              SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


Typical Application (continued)
9.2.1 Design Requirements

9.2.1.1 Calculating Junction Temperature and Power Dissipation
When designing with this device, it is important that the Recommended Operating Conditions not be violated.
Many of the parameters of this device are rated based on junction temperature. So junction temperature must be
calculated in order to verify that safe operation of the device is met. The basic equation for junction temperature
is shown in Equation 1.
Tj = TA + (qJA ´ Pd )                                                                                            (1)
θJA is the standard junction to ambient thermal resistance measurement of the package, as seen in Thermal
Information table. Pd is the total power dissipation of the device, and the approximation is shown in Equation 2.
      (
Pd » ICC _ STATIC ´ VCC      ) + å Pd _ PORT _ L + å Pd _ PORT _ H                                                                (2)
Equation 2 is the approximation of power dissipation in the device. The equation is the static power plus the
summation of power dissipated by each port (with a different equation based on if the port is outputting high, or
outputting low. If the port is set as an input, then power dissipation is the input leakage of the pin multiplied by
the voltage on the pin). Note that this ignores power dissipation in the INT and SDA pins, assuming these
transients to be small. They can easily be included in the power dissipation calculation by using Equation 3 to
calculate the power dissipation in INT or SDA while they are pulling low, and this gives maximum power
dissipation.
Pd _ PORT _ L = (IOL ´ VOL )                                                                                      (3)
Equation 3 shows the power dissipation for a single port which is set to output low. The power dissipated by the
port is the VOL of the port multiplied by the current it is sinking.
                 (
Pd _ PORT _H = IOH ´ (VCC - VOH )         )                                                                                       (4)
Equation 4 shows the power dissipation for a single port which is set to output high. The power dissipated by the
port is the current sourced by the port multiplied by the voltage drop across the device (difference between VCC
and the output voltage).

9.2.1.2 Minimizing ICC when I/Os Control LEDs
When the I/Os are used to control LEDs, normally they are connected to VCC through a resistor as shown in
Figure 26. For a P-port configured as an input, ICC increases as VI becomes lower than VCC. The LED is a diode,
with threshold voltage VT, and when a P-port is configured as an input the LED is off but VI is a VT drop below
VCC.
For battery-powered applications, it is essential that the voltage of P-ports controlling LEDs is greater than or
equal to VCC when the P-ports are configured as input to minimize current consumption. Figure 27 shows a high-
value resistor in parallel with the LED. Figure 28 shows VCC less than the LED supply voltage by at least VT.
Both of these methods maintain the I/O VI at or above VCC and prevents additional supply current consumption
when the P-port is configured as an input and the LED is off.
The TCA9554 has an integrated 100-kΩ pull-up resistor, so there is no need for an external pull-up.
                                                                                  VCC




                                                                      LED      100 k
                                                         VCC

                                                          LEDx




                                      Figure 27. High-Value Resistor in Parallel With LED

Copyright © 2012–2017, Texas Instruments Incorporated                                          Submit Documentation Feedback      25
                                                        Product Folder Links: TCA9554
```
