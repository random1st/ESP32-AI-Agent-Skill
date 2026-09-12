---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.3.2 RTC Functions"
pdf_pages: 23
retrieved: 2026-09-12
redistribute: false
---

# 2.3.2 RTC Functions

```text
2 Pins



2.3.2 RTC Functions
When the chip is in Deep-sleep mode, the IO MUX described in Section 2.3.1 IO MUX Functions will not work.
That is where the RTC IO MUX comes in. It allows multiple input/output signals to be a single input/output pin
in Deep-sleep mode, as the pin is connected to the RTC system and powered by VDD3P3_RTC.

RTC IO pins can be assigned to RTC functions. They can

   • Either work as RTC GPIOs (RTC_GPIO0, RTC_GPIO1, etc.), connected to the ULP coprocessor

   • Or connect to RTC peripheral signals (sar_i2c_scl_0, sar_i2c_sda_0, etc.) - see Table 2-5 RTC
     Peripheral Signals Routed via RTC IO MUX

                             Table 2-5. RTC Peripheral Signals Routed via RTC IO MUX

                                Pin Function      Signal         Description
                                sar_i2c_scl…      Serial clock
                                                                 RTC I2C0/1 interface
                                sar_i2c_sda…      Serial data


Table 2-6 RTC Functions shows the RTC functions of RTC IO pins.

                                               Table 2-6. RTC Functions

                        Pin      RTC                             RTC Function 2
                        No.      IO Name 1          F0             F1   F2     F3
                        5        RTC_GPIO0          RTC_GPIO0                  sar_i2c_scl_0
                        6        RTC_GPIO1          RTC_GPIO1                  sar_i2c_sda_0
                        7        RTC_GPIO2          RTC_GPIO2                  sar_i2c_scl_1
                        8        RTC_GPIO3          RTC_GPIO3                  sar_i2c_sda_1
                        9        RTC_GPIO4          RTC_GPIO4
                        10       RTC_GPIO5          RTC_GPIO5
                        11       RTC_GPIO6          RTC_GPIO6
                        12       RTC_GPIO7          RTC_GPIO7
                        13       RTC_GPIO8          RTC_GPIO8
                        14       RTC_GPIO9          RTC_GPIO9
                        15       RTC_GPIO10         RTC_GPIO10
                        16       RTC_GPIO11         RTC_GPIO11
                        17       RTC_GPIO12         RTC_GPIO12
                        18       RTC_GPIO13         RTC_GPIO13
                        19       RTC_GPIO14         RTC_GPIO14
                        21       RTC_GPIO15         RTC_GPIO15
                        22       RTC_GPIO16         RTC_GPIO16
                        23       RTC_GPIO17         RTC_GPIO17
                        24       RTC_GPIO18         RTC_GPIO18
                        25       RTC_GPIO19         RTC_GPIO19
                        26       RTC_GPIO20         RTC_GPIO20
                        27       RTC_GPIO21         RTC_GPIO21
                        1 This column lists the RTC GPIO names, since RTC functions are con-

                         figured with RTC GPIO registers that use RTC GPIO numbering.
                        2 Regarding highlighted cells, see Section 2.3.4 Restrictions for GPIOs

                             and RTC_GPIOs.



Espressif Systems                                          23                       ESP32-S3 Series Datasheet v2.2
                                             Submit Documentation Feedback
```
