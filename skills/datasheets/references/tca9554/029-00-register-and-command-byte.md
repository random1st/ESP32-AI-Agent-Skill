---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Register and Command Byte"
pdf_pages: 19
retrieved: 2026-09-12
redistribute: true
---

# Register and Command Byte

```text
                                                                                                                                        TCA9554
www.ti.com                                                                                            SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


8.6 Register Maps
8.6.1 Device Address
Figure 19 shows the address byte of the TCA9554.
                                                                      Slave Address



                                                         0       1        0   0   A2    A1   A0 R/W



                                                                 Fixed              Hardware
                                                                                    Selectable

                                                        Figure 19. TCA9554 Address

Table 2 shows the TCA9554 address reference.

                                                        Table 2. Address Reference
                                                INPUTS
                                                                                   I2C BUS SLAVE ADDRESS
                                       A2          A1            A0
                                        L          L             L                32 (decimal), 20 (hexadecimal)
                                        L          L             H                33 (decimal), 21 (hexadecimal)
                                        L          H             L                34 (decimal), 22 (hexadecimal)
                                        L          H             H                35 (decimal), 23 (hexadecimal)
                                        H          L             L                36 (decimal), 24 (hexadecimal)
                                        H          L             H                37 (decimal), 25 (hexadecimal)
                                        H          H             L                38 (decimal), 26 (hexadecimal)
                                        H          H             H                39 (decimal), 27 (hexadecimal)

The last bit of the slave address defines the operation (read or write) to be performed. When it is high (1), a read
is selected, while a low (0) selects a write operation.

8.6.2 Control Register and Command Byte
Following the successful Acknowledgment of the address byte, the bus master sends a command byte that is
stored in the control register in the TCA9554 (see Figure 20). Two bits of this command byte state the operation
(read or write) and the internal register (input, output, polarity inversion or configuration) that is affected. This
register can be written or read through the I2C bus. The command byte is sent only during a write transmission.
Once a command byte has been sent, the register that was addressed continues to be accessed by reads until a
new command byte has been sent.

                                                    0        0        0       0     0    B2      B1   B0

                                                    Figure 20. Control Register Bits




Copyright © 2012–2017, Texas Instruments Incorporated                                                        Submit Documentation Feedback      19
                                                             Product Folder Links: TCA9554
```
