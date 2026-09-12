---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Descriptions"
pdf_pages: 20-23
retrieved: 2026-09-12
redistribute: true
---

# Descriptions

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                www.ti.com


Table 3 shows the TCA9554 command byte.

                                                Table 3. Command Byte Table
 CONTROL REGISTER BITS         COMMAND BYTE
                                                               REGISTER                 PROTOCOL              POWER-UP DEFAULT
       B1            B0            (HEX)
       0              0                0×00                     Input Port               Read byte                    XXXX XXXX
       0              1                0×01                    Output Port             Read-write byte                1111 1111
       1              0                0×02                Polarity Inversion          Read-write byte                0000 0000
       1              1                0×03                    Configuration           Read-write byte                1111 1111


8.6.3 Register Descriptions
The Input Port register (register 0) reflects the incoming logic levels of the pins, regardless of whether the pin is
defined as an input or an output by the Configuration register. It only acts on read operation. Writes to these
registers have no effect. The default value, X, is determined by the externally applied logic level.
Before a read operation, a write transmission is sent with the command byte to indicate to the I2C device that the
Input Port register is accessed next. See Table 4.

                                   Table 4. Register 0 (Input Port Register) Table
                       BIT             I7        I6       I5           I4       I3        I2         I1          I0
                    DEFAULT            X         X        X            X        X         X           X          X

The Output Port register (register 1) shows the outgoing logic levels of the pins defined as outputs by the
Configuration register. Bit values in this register have no effect on pins defined as inputs. In turn, reads from this
register reflect the value that is in the flip-flop controlling the output selection, not the actual pin value. See
Table 5.

                                  Table 5. Register 1 (Output Port Register) Table
                       BIT             O7       O6        O5          O4        O3       O2          O1         O0
                    DEFAULT            1         1        1            1        1         1           1          1

The Polarity Inversion register (register 2) allows polarity inversion of pins defined as inputs by the Configuration
register. If a bit in this register is set (written with 1), the corresponding port pin polarity is inverted. If a bit in this
register is cleared (written with a 0), the corresponding port pin original polarity is retained. See Table 6.

                               Table 6. Register 2 (Polarity Inversion Register) Table
                       BIT             N7       N6        N5          N4        N3       N2          N1         N0
                    DEFAULT            0         0        0            0        0         0           0          0

The Configuration register (register 3) configures the directions of the I/O pins. If a bit in this register is set to 1,
the corresponding port pin is enabled as an input with a high-impedance output driver. If a bit in this register is
cleared to 0, the corresponding port pin is enabled as an output. See Table 7.

                                 Table 7. Register 3 (Configuration Register) Table
                       BIT             C7       C6        C5          C4        C3       C2          C1         C0
                    DEFAULT            1         1        1            1        1         1           1          1




20     Submit Documentation Feedback                                                 Copyright © 2012–2017, Texas Instruments Incorporated

                                                  Product Folder Links: TCA9554
                                                                                                                                    TCA9554
www.ti.com                                                                                       SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017


8.6.3.1 Bus Transactions
Data is exchanged between the master and the TCA9554 through write and read commands.

8.6.3.1.1 Writes
To write on the I2C bus, the master sends a START condition on the bus with the address of the slave, as well
as the last bit (the R/W bit) set to 0, which signifies a write. After the slave sends the acknowledge bit, the master
then sends the register address of the register to which it wishes to write. The slave acknowledges again, letting
the master know it is ready. After this, the master starts sending the register data to the slave until the master
has sent all the data necessary (which is sometimes only a single byte), and the master terminates the
transmission with a STOP condition. Note that the command byte/register address does NOT automatically
increment. Writing multiple bytes during a write results in the last byte sent being stored in the register.
See the Register Descriptions section to see list of the TCA9554's internal registers and a description of each
one.
Figure 21 shows an example of writing a single byte to a slave register.

           Master controls SDA line
           Slave controls SDA line

 Write to one register in a device

      Device (Slave) Address (7 bits)                    Register Address N (8 bits)             Data Byte to Register N (8 bits)


  S    0    1    0    0   A2 A1 A0        0    A    B7 B6 B5 B4 B3 B2 B1 B0                 A    D7 D6 D5 D4 D3 D2 D1 D0              A   P


 START                             R/W=0       ACK                                         ACK                                   ACK      STOP
                                                         Figure 21. Write to Register

Figure 22 shows an example of how to write to the polarity inversion register.

           Master controls SDA line
           Slave controls SDA line
      Device (Slave) Address (7 bits)                   Register Address 0x02 (8 bits)          Data Byte to Register 0x02 (8 bits)


  S    0    1    0    0   A2 A1 A0        0    A     0      0   0   0   0   0    1     0    A    D7 D6 D5 D4 D3 D2 D1 D0              A   P


 START                             R/W=0       ACK                                         ACK                                   ACK      STOP
                                       Figure 22. Write to the Polarity Inversion Register




Copyright © 2012–2017, Texas Instruments Incorporated                                                   Submit Documentation Feedback         21
                                                            Product Folder Links: TCA9554
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                                                                     www.ti.com


Figure 23 shows an example of how to write to output port register.
                SCL
                        1    2     3   4        5    6    7    8   9
                                 Slave Address                                   Command Byte


           SDA S         0   1     0       0 A2 A1 A0 0            A    0    0     0       0        0       0       0       1   A              Data 1                   A   P

                    Start Condition                           R/W ACK From Slave                                                ACK From Slave                           ACK From Slave

Write to Port



 Data Out
From Port                                                                                                                                                                        Data 1 Valid
                                                                                                                                                                 tpv

                                                          Figure 23. Write to Output Port Register

8.6.3.1.2 Reads
The bus master first must send the TCA9554 address with the LSB set to a logic 0 (see Figure 19 for device
address). The command byte is sent after the address and determines which register is accessed. After a restart,
the device address is sent again but, this time, the LSB is set to a logic 1. Data from the register defined by the
command byte then is sent by the TCA9554 (see Figure 25). The command byte does not increment
automatically. If multiple bytes are read, data from the specified command byte/register is going to be
continuously read.
See the Register Descriptions section for the list of the TCA9554's internal registers and a description of each
one.
Figure 24 shows an example of reading a single byte from a slave register.

       Master controls SDA line
       Slave controls SDA line
Read from one register in a device
     Device (Slave) Address (7 bits)                 Register Address N (8 bits)                    Device (Slave) Address (7 bits)                Data Byte from Register N (8 bits)


 S     0    1   0   0   A2 A1 A0       0    A       B7 B6 B5 B4 B3 B2 B1 B0            A       Sr       0       1       0   0   A2 A1 A0   1   A    D7 D6 D5 D4 D3 D2 D1 D0 NA           P


 START                           R/W=0      ACK                                    ACK         Repeated START                        R/W=1     ACK                                NACK   STOP

                                                                   Figure 24. Read from Register

After a restart, the value of the register defined by the command byte matches the register being accessed when
the restart occurred. Data is clocked into the register on the rising edge of the ACK clock pulse. After the first
byte, additional bytes may be read, but the same register specified by the command byte is read.
Data is clocked into the register on the rising edge of the ACK clock pulse. There is no limitation on the number
of data bytes received in one read transmission, but when the final byte is received, the bus master must not
acknowledge the data.




22         Submit Documentation Feedback                                                                                            Copyright © 2012–2017, Texas Instruments Incorporated

                                                                        Product Folder Links: TCA9554
                                                                                                                                   TCA9554
www.ti.com                                                                                      SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017



       SCL              1   2        3    4   5   6   7     8   9
                                    Slave Address                          Data From Port                Data From Port


       SDA           S 0        1     0   0 A2 A1 A0 1          A              Data 1           A           Data 4           NA P

                       Start                          R/W           ACK From                    ACK From             NACK From        Stop
                       Condition                                    Slave                       Master                  Master        Condition
Read From
      Port

  Data Into
                                                                      Data 2    Data 3                Data 4                     Data 5
      Port
                                                          tph                            tps



        INT

            tiv                                           tir

       A.     Transfer of data can be stopped at any time by a Stop condition. When this occurs, data present at the latest
              acknowledge phase is valid (output mode). It is assumed that the command byte previously has been set to 00 (Read
              Input Port register).
       B.     This figure eliminates the command byte transfer, a restart, and slave address call between the initial slave address
              call and actual data transfer from the P port (see Figure 24 for these details).

                                                      Figure 25. Read Input Port Register




Copyright © 2012–2017, Texas Instruments Incorporated                                                  Submit Documentation Feedback         23
                                                                Product Folder Links: TCA9554
```
