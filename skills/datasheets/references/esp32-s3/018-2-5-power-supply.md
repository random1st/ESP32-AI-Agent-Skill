---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.5 Power Supply"
pdf_pages: 29
retrieved: 2026-09-12
redistribute: false
---

# 2.5 Power Supply

```text
2 Pins



2.5      Power Supply
2.5.1 Power Pins
The chip is powered via the power pins described in Table 2-11 Power Pins.

                                              Table 2-11. Power Pins

                                                                       Power Supply 1, 2
         Pin No.    Pin Name        Direction        Power Domain/Other                         IO Pins 5
         2          VDD3P3          Input            Analog power domain
         3          VDD3P3          Input            Analog power domain
         20         VDD3P3_RTC      Input            RTC and part of Digital power domains      RTC IO
                                    Input            In-package memory (backup power line)
         29         VDD_SPI 3,4
                                    Output           In-package and off-package flash/PSRAM     SPI IO
         46         VDD3P3_CPU      Input            Digital power domain                       Digital IO
         55         VDDA            Input            Analog power domain
         56         VDDA            Input            Analog power domain
         57         GND             –                External ground connection
         1 See in conjunction with Section 2.5.2 Power Scheme.
         2 For recommended and maximum voltage and current, see Section 5.1 Absolute Maximum
           Ratings and Section 5.2 Recommended Operating Conditions.
         3 To configure VDD_SPI as input or output, see ESP32-S3 Technical Reference Manual > Chap-
           ter Low-power Management.
         4 To configure output voltage, see Section 3.2 VDD_SPI Voltage Control and Section 5.3
           VDD_SPI Output Characteristics.
         5 RTC IO pins are those powered by VDD3P3_RTC and so on, as shown in Figure 2-2 ESP32-S3
             Power Scheme. See also Table 2-1 Pin Overview > Column Pin Providing Power.


2.5.2    Power Scheme
The power scheme is shown in Figure 2-2 ESP32-S3 Power Scheme.

The components on the chip are powered via voltage regulators.

                                          Table 2-12. Voltage Regulators

                      Voltage Regulator     Output      Power Supply
                      Digital                1.1 V      Digital power domain
                      Low-power              1.1 V      RTC power domain
                                                        Can be configured to power
                      Flash                  1.8 V      in-package flash/PSRAM or
                                                        off-package memory




Espressif Systems                                         29                      ESP32-S3 Series Datasheet v2.2
                                          Submit Documentation Feedback
```
