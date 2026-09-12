---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.5.3 Chip Power-up and Reset"
pdf_pages: 30
retrieved: 2026-09-12
redistribute: false
---

# 2.5.3 Chip Power-up and Reset

```text
2 Pins




                                          Figure 2-2. ESP32-S3 Power Scheme



2.5.3 Chip Power-up and Reset
Once the power is supplied to the chip, its power rails need a short time to stabilize. After that, CHIP_PU – the
pin used for power-up and reset – is pulled high to activate the chip. For information on CHIP_PU as well as
power-up and reset timing, see Figure 2-3 and Table 2-13.

                                             tST BL                           tRST

                               2.8 V
             VDDA,
           VDD3P3,
       VDD3P3_RTC,
       VDD3P3_CPU

                               VIL_nRST
           CHIP_PU



                     Figure 2-3. Visualization of Timing Parameters for Power-up and Reset



                     Table 2-13. Description of Timing Parameters for Power-up and Reset

          Parameter      Description                                                         Min (µs)
                         Time reserved for the power rails of VDDA, VDD3P3,
          tST BL         VDD3P3_RTC, and VDD3P3_CPU to stabilize before the CHIP_PU                50
                         pin is pulled high to activate the chip
                         Time reserved for CHIP_PU to stay below VIL_nRST to reset the
          tRST                                                                                     50
                         chip (see Table 5-4)




Espressif Systems                                         30                   ESP32-S3 Series Datasheet v2.2
                                             Submit Documentation Feedback
```
