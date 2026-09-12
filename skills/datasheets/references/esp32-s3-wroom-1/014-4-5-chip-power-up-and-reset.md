---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "4.5 Chip Power-up and Reset"
pdf_pages: 16
retrieved: 2026-09-12
redistribute: false
---

# 4.5 Chip Power-up and Reset

```text
4 Boot Configurations


                                             Table 4-5. JTAG Signal Source Control

JTAG Signal Source               EFUSE_DIS_PAD_JTAG EFUSE_DIS_USB_JTAG EFUSE_STRAP_JTAG_SEL GPIO3
                                                0                       0                        0               Ignored
USB Serial/JTAG Controller                      0                       0                         1                 1
                                                1                       0                     Ignored            Ignored
                                                0                       0                         1                 0
JTAG pins 2
                                                0                       1                     Ignored            Ignored
JTAG is disabled                                1                       1                     Ignored            Ignored
 1 Bold marks the default value and configuration.
 2 JTAG pins refer to MTDI, MTCK, MTMS, and MTDO.



4.5 Chip Power-up and Reset
Once the power is supplied to the chip, its power rails need a short time to stabilize. After that, EN – the pin
used for power-up and reset – is pulled high to activate the chip. For information on EN as well as power-up
and reset timing, see Figure 4-2 and Table 4-6.

                                                tST BL                               tRST

                                  2.8 V
             VDDA,
           VDD3P3,
       VDD3P3_RTC,
       VDD3P3_CPU

                                  VIL_nRST
                   EN



                        Figure 4-2. Visualization of Timing Parameters for Power-up and Reset



                        Table 4-6. Description of Timing Parameters for Power-up and Reset

          Parameter         Description                                                               Min (µs)
                            Time reserved for the power rails of VDDA, VDD3P3,
          tST BL            VDD3P3_RTC, and VDD3P3_CPU to stabilize before the EN                          50
                            pin is pulled high to activate the chip
                            Time reserved for EN to stay below VIL_nRST to reset the chip
          tRST                                                                                             50
                            (see Table 6-3)




Espressif Systems                                             16             ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                                 Submit Documentation Feedback
```
