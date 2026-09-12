---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "5.3 VDD_SPI Output Characteristics"
pdf_pages: 64
retrieved: 2026-09-12
redistribute: false
---

# 5.3 VDD_SPI Output Characteristics

```text
5 Electrical Characteristics



5 Electrical Characteristics

5.1    Absolute Maximum Ratings
Stresses above those listed in Table 5-1 Absolute Maximum Ratings may cause permanent damage to the
device. These are stress ratings only and normal operation of the device at these or any other conditions
beyond those indicated in Section 5.2 Recommended Operating Conditions is not implied. Exposure to
absolute-maximum-rated conditions for extended periods may affect device reliability.

                                     Table 5-1. Absolute Maximum Ratings

                Parameter                Description                     Min         Max         Unit
                Input power pins1        Allowed input voltage             –0.3          3.6         V
                Ioutput   2              Cumulative IO output current          —     1500            mA
                TST ORE                  Storage temperature               –40           150         °C
                1 For more information on input power pins, see Section 2.5.1 Power Pins.
                2 The product proved to be fully functional after all its IO pins were pulled high
                    while being connected to ground for 24 consecutive hours at ambient tem-
                    perature of 25 °C.



5.2     Recommended Operating Conditions
For recommended ambient temperature, see Section 1 ESP32-S3 Series Comparison.

                                Table 5-2. Recommended Operating Conditions

             Parameter 1             Description                        Min        Typ     Max            Unit
             VDDA, VDD3P3            Recommended input voltage          3.0        3.3         3.6         V
             VDD3P3_RTC 2            Recommended input voltage          3.0        3.3         3.6         V
             VDD_SPI (as input)      —                                   1.8       3.3         3.6         V
             VDD3P3_CPU 3            Recommended input voltage          3.0        3.3         3.6         V
             IV DD   4               Cumulative input current           0.5          —          —          A
              1 See in conjunction with Section 2.5 Power Supply.
              2 If VDD3P3_RTC is used to power VDD_SPI (see Section 2.5.2 Power Scheme),
               the voltage drop on RSP I should be accounted for. See also Section 5.3 VDD_SPI
                Output Characteristics.
              3 If writing to eFuses, the voltage on VDD3P3_CPU should not exceed 3.3 V as the
                circuits responsible for burning eFuses are sensitive to higher voltages.
              4 If you use a single power supply, the recommended output current is 500 mA or
               more.




Espressif Systems                                        64                        ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
```
