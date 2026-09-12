---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "3.1 Chip Boot Mode Control"
pdf_pages: 33
retrieved: 2026-09-12
redistribute: false
---

# 3.1 Chip Boot Mode Control

```text
3 Boot Configurations


The timing of signals connected to the strapping pins should adhere to the setup time and hold time
specifications in Table 3-2 and Figure 3-1.

                       Table 3-2. Description of Timing Parameters for the Strapping Pins

           Parameter     Description                                                                 Min (ms)
                         Setup time is the time reserved for the power rails to stabilize be-
           tSU                                                                                              0
                         fore the CHIP_PU pin is pulled high to activate the chip.
                         Hold time is the time reserved for the chip to read the strapping
           tH            pin values after CHIP_PU is already high and before these pins                     3
                         start operating as regular IO pins.


                                                        tSU      tH




                                     VIH_nRST


                        CHIP_PU




                                        VIH



                    Strapping pin



                     Figure 3-1. Visualization of Timing Parameters for the Strapping Pins



3.1    Chip Boot Mode Control
GPIO0 and GPIO46 control the boot mode after the reset is released. See Table 3-3 Chip Boot Mode
Control.

                                                Table 3-3. Chip Boot Mode Control

                                Boot Mode                             GPIO0       GPIO46
                                SPI boot mode                            1        Any value
                                Joint download boot mode 2               0           0
                                    1 Bold marks the default value and configuration.
                                    2 Joint Download Boot mode supports the following
                                     download methods:
                                         • USB Download Boot:
                                                 – USB-Serial-JTAG Download Boot
                                                 – USB-OTG Download Boot
                                         • UART Download Boot


In addition to SPI Boot and Joint Download Boot modes, ESP32-S3 also supports SPI Download Boot mode.


Espressif Systems                                              33                        ESP32-S3 Series Datasheet v2.2
                                                  Submit Documentation Feedback
```
