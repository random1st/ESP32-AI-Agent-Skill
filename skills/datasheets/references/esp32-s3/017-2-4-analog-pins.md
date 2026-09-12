---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.4 Analog Pins"
pdf_pages: 28
retrieved: 2026-09-12
redistribute: false
---

# 2.4 Analog Pins

```text
2 Pins



2.4       Analog Pins

                                     Table 2-10. Analog Pins

      Pin    Pin        Pin    Pin
      No.    Name       Type   Function
      1      LNA_IN     I/O    Low Noise Amplifier (RF LNA) input/output signals
                               High: on, enables the chip (powered up).
      4      CHIP_PU    I      Low: off, disables the chip (powered down).
                               Note: Do not leave the CHIP_PU pin floating.
      53     XTAL_N     —      External clock input/output connected to chip’s crystal or oscillator.
      54     XTAL_P     —      P/N means differential clock positive/negative.




Espressif Systems                              28                      ESP32-S3 Series Datasheet v2.2
                                Submit Documentation Feedback
```
