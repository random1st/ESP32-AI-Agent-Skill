---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "6 Electrical Characteristics"
pdf_pages: 27
retrieved: 2026-09-12
redistribute: false
---

# 6 Electrical Characteristics

```text
5 Peripherals



6 Electrical Characteristics

6.1     Absolute Maximum Ratings
Stresses above those listed in Table 6-1 Absolute Maximum Ratings may cause permanent damage to the
device. These are stress ratings only and functional operation of the device at these or any other conditions
beyond those indicated under Table 6-2 Recommended Operating Conditions is not implied. Exposure to
absolute-maximum-rated conditions for extended periods may affect device reliability.

                                       Table 6-1. Absolute Maximum Ratings

                              Symbol       Parameter                   Min      Max      Unit
                              VDD33        Power supply voltage       –0.3       3.6      V
                              TST ORE      Storage temperature         –40       105     °C



6.2         Recommended Operating Conditions

                                Table 6-2. Recommended Operating Conditions

              Symbol    Parameter                                                  Min     Typ       Max    Unit
              VDD33     Power supply voltage                                       3.0        3.3    3.6     V
              IV DD     Current delivered by external power supply                 0.5          —     —      A
                                                                65 °C version                         65
              TA        Operating ambient temperature           85 °C version      –40          —     85    °C
                                                                105 °C version                       105


6.3 DC Characteristics (3.3 V, 25 °C)

                                    Table 6-3. DC Characteristics (3.3 V, 25 °C)

 Parameter      Description                                               Min              Typ             Max          Unit
 CIN            Pin capacitance                                                 —                2           —          pF
 VIH            High-level input voltage                              0.75 × VDD 1              —        1
                                                                                                      VDD + 0.3          V
 VIL            Low-level input voltage                                          –0.3           —    0.25 × VDD 1        V
 IIH            High-level input current                                           —            —                  50   nA
 IIL            Low-level input current                                         —               —                  50   nA
 VOH    2       High-level output voltage                              0.8 × VDD 1              —               —        V
 VOL    2       Low-level output voltage                                           —            —      0.1 × VDD 1       V
                High-level source current (VDD 1 = 3.3 V,
 IOH                                                                               —            40                 —    mA
                VOH >= 2.64 V, PAD_DRIVER = 3)
                Low-level sink current (VDD 1 = 3.3 V, V   OL =
 IOL                                                                               —            28                 —    mA
                0.495 V, PAD_DRIVER = 3)
 RP U           Internal weak pull-up resistor                                     —            45                 —    kΩ
 RP D           Internal weak pull-down resistor                                   —            45                 —    kΩ




Espressif Systems                                          27                ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                            Submit Documentation Feedback
```
