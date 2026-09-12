---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Application"
pdf_pages: 24
retrieved: 2026-09-12
redistribute: true
---

# Application

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                               www.ti.com


9 Application and Implementation

                                                           NOTE
               Information in the following applications sections is not part of the TI component
               specification, and TI does not warrant its accuracy or completeness. TI’s customers are
               responsible for determining suitability of components for their purposes. Customers should
               validate and test their design implementation to confirm system functionality.


9.1 Application Information
Applications of the TCA9554 has this device connected as a slave to an I2C master (processor), and the I2C bus
may contain any number of other slave devices. The TCA9554 is typically in a remote location from the master,
placed close to the GPIOs to which the master must monitor or control.
IO Expanders such as the TCA9554 are typically used for controlling LEDs (for feedback or status lights),
controlling enable or reset signals of other devices, and even reading the outputs of other devices or buttons.

9.2 Typical Application
Figure 26 shows an application in which the TCA9554 can be used.

VCC
                                   (1)       (1)                                 16            2 kΩ
                  VCC          10 kΩ     10 kΩ     10 kΩ
                                                                                 VCC
                                                                      15
                         SDA                                               SDA                 4                                   Subsystem 1
                                                                                          P0                               (e.g., temperature sensor)
            Master                                                    14
                         SCL                                               SCL                 5
            Controller                                                                    P1                               INT
                                                                      13
                         INT                                               INT
                                                                                          P2 6
                                                                                               7
                                                                                                                              RESET
                                                                                          P3
                 GND                                                                                                            Subsystem 2
                                                                                TCA9554
                                                                                               9                               (e.g., counter)
                                                                                          P4
                                                                                               10
                                                                                          P5                                 A

                                                                       3
                                                                           A2             P6   11                                  Controlled Device
                                                                       2                                                           (e.g., CBT device)
                                                                                                                  ENABLE
                                                                           A1
                                                                                          P7 12
                                                                       1
                                                                           A0                                                B


                                                                                 GND                                          ALARM
                                                                                  8

                                                                                                                                  Subsystem 3
                                                                                                                              (e.g., alarm system)


                                                                                                                                         VCC
      (1)    The SCL and SDA pins must be tied directly to VCC because if SCL and SDA are tied to an auxiliary power supply
             that can be powered on while VCC is powered off, then the supply current, ICC, will increase as a result.
      (2)    Device address is configured as 0100000 for this example.
      (3)    P0, P2, and P3 are configured as outputs.
      (4)    P1, P4, and P5 are configured as inputs.
      (5)    P6 and P7 are not used and have internal 100-kΩ pullup resistors to protect them from floating.

                                                   Figure 26. Application Schematic



24     Submit Documentation Feedback                                                                Copyright © 2012–2017, Texas Instruments Incorporated

                                                           Product Folder Links: TCA9554
```
