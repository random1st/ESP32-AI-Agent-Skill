---
source: https://www.ti.com/lit/ds/symlink/tca9554.pdf
document: TCA9554 8-bit I2C I/O Expander Datasheet
vendor: Texas Instruments
section: "Characteristics"
pdf_pages: 8
retrieved: 2026-09-12
redistribute: true
---

# Characteristics

```text
TCA9554
SCPS233E – MARCH 2012 – REVISED FEBRUARY 2017                                                                                                   www.ti.com


6.6 I2C Interface Timing Requirements
over operating free-air temperature range (unless otherwise noted) (see Figure 11)
                                                                                                                          MIN           MAX        UNIT
STANDARD MODE
fscl           I2C clock frequency                                                                                          0            100       kHz
tsch           2                                                                                                            4                       µs
               I C clock high time
tscl           2                                                                                                           4.7                      µs
               I C clock low time
tsp            I2C spike time                                                                                                             50        ns
tsds           2                                                                                                          250                       ns
               I C serial-data setup time
tsdh           2                                                                                                            0                       ns
               I C serial-data hold time
ticr           I2C input rise time                                                                                                      1000        ns
ticf           I2C input fall time                                                                                                       300        ns
tocf           2                                               10-pF to 400-pF bus                                                       300        ns
               I C output fall time
tbuf           I2C bus free time between Stop and Start                                                                    4.7                      µs
tsts           I2C Start or repeated Start condition setup                                                                 4.7                      µs
tsth           2                                                                                                            4                       µs
               I C Start or repeated Start condition hold
tsps           2                                                                                                            4                       µs
               I C Stop condition setup
tvd(data)      Valid data time                                 SCL low to SDA output valid                                               3.45       µs
                                                               ACK signal from SCL low to
tvd(ack)       Valid data time of ACK condition                                                                                          3.45       µs
                                                               SDA (out) low
Cb             I2C bus capacitive load                                                                                                   400        pF
FAST MODE
fscl           I2C clock frequency                                                                                          0            400       kHz
tsch           I2C clock high time                                                                                         0.6                      µs
tscl           I2C clock low time                                                                                          1.3                      µs
tsp            2                                                                                                                          50        ns
               I C spike time
tsds           2                                                                                                          100                       ns
               I C serial-data setup time
tsdh           I2C serial-data hold time                                                                                    0                       ns
ticr           I2C input rise time                                                                                         20            300        ns
                                                                                                                   20 × (VDD /
ticf           I2C input fall time                                                                                                       300        ns
                                                                                                                        5.5 V)
                                                                                                                   20 × (VDD /
tocf           I2C output fall time                            10-pF to 400-pF bus                                                       300        ns
                                                                                                                        5.5 V)
tbuf           2                                                                                                           1.3                      µs
               I C bus free time between Stop and Start
tsts           I2C Start or repeated Start condition setup                                                                 0.6                      µs
tsth           I2C Start or repeated Start condition hold                                                                  0.6                      µs
tsps           2                                                                                                           0.6                      µs
               I C Stop condition setup
tvd(data)      Valid data time                                                                                                            0.9       µs
tvd(ack)       Valid data time of ACK condition                                                                                           0.9       µs
Cb             I2C bus capacitive load                                                                                                   400        pF


6.7 Switching Characteristics
over operating free-air temperature range (unless otherwise noted) (see Figure 12 and Figure 13)
                                                                FROM                            TO
                      PARAMETER                                                                                           MIN          MAX         UNIT
                                                               (INPUT)                       (OUTPUT)
STANDARD MODE and FAST MODE
tiv         Interrupt valid time                                P port                         INT                                         4        µs
tir         Interrupt reset delay time                           SCL                           INT                                         4        µs
tpv         Output data valid                                    SCL                          P7–P0                                     350         ns
tps         Input data setup time                               P port                         SCL                         100                      ns
tph         Input data hold time                                P port                         SCL                           1                      µs


8           Submit Documentation Feedback                                                            Copyright © 2012–2017, Texas Instruments Incorporated

                                                             Product Folder Links: TCA9554
```
