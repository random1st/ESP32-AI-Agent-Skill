---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "4.1 Chip Boot Mode Control"
pdf_pages: 14
retrieved: 2026-09-12
redistribute: false
---

# 4.1 Chip Boot Mode Control

```text
4 Boot Configurations


any other way. It makes the strapping pin values available during the entire chip operation, and the pins are
freed up to be used as regular IO pins after reset.

The timing of signals connected to the strapping pins should adhere to the setup time and hold time
specifications in Table 4-2 and Figure 4-1.

                       Table 4-2. Description of Timing Parameters for the Strapping Pins

           Parameter     Description                                                               Min (ms)
                         Setup time is the time reserved for the power rails to stabilize be-
           tSU                                                                                            0
                         fore the EN pin is pulled high to activate the chip.
                         Hold time is the time reserved for the chip to read the strapping
           tH            pin values after EN is already high and before these pins start op-               3
                         erating as regular IO pins.


                                                       tSU          tH




                                     VIL_nRST
                              EN




                                        VIH



                     Strapping pin


                       Figure 4-1. Visualization of Timing Parameters for the Strapping Pins



4.1    Chip Boot Mode Control
GPIO0 and GPIO46 control the boot mode after the reset is released. See Table 4-3 Chip Boot Mode
Control.

                                              Table 4-3. Chip Boot Mode Control

                                     Boot Mode                     GPIO0    GPIO46
                                     SPI Boot                          1   Any value
                                     Joint Download Boot 2             0         0
                                     1 Bold marks the default value and configura-
                                      tion.
                                     2 Joint Download Boot mode supports the fol-
                                        lowing download methods:
                                                • USB Download Boot:
                                                   – USB-Serial-JTAG Download Boot
                                                   – USB-OTG Download Boot
                                                • UART Download Boot


Espressif Systems                                             14             ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                                 Submit Documentation Feedback
```
