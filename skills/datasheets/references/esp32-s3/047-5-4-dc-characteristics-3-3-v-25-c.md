---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "5.4 DC Characteristics (3.3 V, 25 °C)"
pdf_pages: 65
retrieved: 2026-09-12
redistribute: false
---

# 5.4 DC Characteristics (3.3 V, 25 °C)

```text
5 Electrical Characteristics



5.3         VDD_SPI Output Characteristics

                              Table 5-3. VDD_SPI Internal and Output Characteristics

                   Parameter      Description 1                                      Typ       Unit
                                  VDD_SPI powered by VDD3P3_RTC via RSP I
                   RSP I                                                               14       Ω
                                  for 3.3 V flash/PSRAM 2
                                  Output current when VDD_SPI is powered by
                   ISP I                                                               40      mA
                                  Flash Voltage Regulator for 1.8 V flash/PSRAM
                    1 See in conjunction with Section 2.5.2 Power Scheme.
                    2 VDD3P3_RTC must be more than VDD_flash_min + I_flash_max * R
                                                                                               SP I ;

                     where
                           • VDD_flash_min – minimum operating voltage of flash/PSRAM
                           • I_flash_max – maximum operating current of flash/PSRAM



5.4         DC Characteristics (3.3 V, 25 °C)

                                    Table 5-4. DC Characteristics (3.3 V, 25 °C)

 Parameter      Description                                           Min            Typ                Max        Unit
 CIN            Pin capacitance                                             —              2                  —    pF
 VIH            High-level input voltage                          0.75 × VDD 1          —       VDD 1 + 0.3         V
 VIL            Low-level input voltage                                     –0.3        —      0.25 × VDD 1         V
 IIH            High-level input current                                      —         —                     50   nA
 IIL            Low-level input current                                     —           —                     50   nA
 VOH    2       High-level output voltage                          0.8 × VDD 1          —                  —        V
 VOL    2       Low-level output voltage                                      —         —         0.1 × VDD 1       V
                High-level source current (VDD 1 = 3.3 V,
 IOH                                                                          —        40                     —    mA
                VOH >= 2.64 V, PAD_DRIVER = 3)
                Low-level sink current (VDD 1 = 3.3 V, V   OL =
 IOL                                                                          —        28                     —    mA
                0.495 V, PAD_DRIVER = 3)
 RP U           Internal weak pull-up resistor                                —        45                     —    kΩ
 RP D           Internal weak pull-down resistor                              —        45                     —    kΩ
                Chip reset release voltage (CHIP_PU voltage
 VIH_nRST                                                         0.75 × VDD 1          —        VDD 1 + 0.3        V
                is within the specified range)
                Chip reset voltage (CHIP_PU voltage is within
 VIL_nRST                                                                   –0.3        —      0.25 × VDD 1         V
                the specified range)
 1 VDD – voltage from a power pin of a respective power domain.
 2V
       OH and VOL are measured using high-impedance load.




Espressif Systems                                        65                        ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
```
