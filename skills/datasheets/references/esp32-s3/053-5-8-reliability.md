---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "5.8 Reliability"
pdf_pages: 69
retrieved: 2026-09-12
redistribute: false
---

# 5.8 Reliability

```text
5 Electrical Characteristics


                                    Table 5-11 – cont’d from previous page
                   Parameter   Description                       Min        Typ        Max         Unit
                   TBE1        Block erase time (32 KB)                —    0.2              2        s
                   TBE2        Block erase time (64 KB)                —    0.3              3        s
                               Chip erase time (16 Mb)                 —         7      20            s
                               Chip erase time (32 Mb)                 —     20         60            s
                   TCE         Chip erase time (64 Mb)                 —     25         100           s
                               Chip erase time (128 Mb)                —     60        200            s
                               Chip erase time (256 Mb)                —     70        300            s



                                      Table 5-12. PSRAM Specifications

                     Parameter    Description                     Min      Typ        Max        Unit
                                  Power supply voltage (1.8 V)    1.62     1.80       1.98        V
                     VCC
                                  Power supply voltage (3.3 V)     2.7     3.3         3.6        V
                     FC           Maximum clock frequency           80       —          —        MHz



5.8 Reliability

                                       Table 5-13. Reliability Qualifications

 Test Item                     Test Conditions                                                    Test Standard
 HTOL (High Temperature
                               125 °C, 1000 hours                                                 JESD22-A108
 Operating Life)
 ESD (Electro-Static           HBM (Human Body Mode) 1 ± 2000 V                                   JS-001
 Discharge Sensitivity)        CDM (Charge Device Mode) 2 ± 1000 V                                JS-002
                               Current trigger ± 200 mA
 Latch up                                                                                         JESD78
                               Voltage trigger 1.5 × VDDmax
                               Bake 24 hours @125 °C
                                                                                                  J-STD-020, JESD47,
 Preconditioning               Moisture soak (level 3: 192 hours @30 °C, 60% RH)
                                                                                                  JESD22-A113
                               IR reflow solder: 260 + 0 °C, 20 seconds, three times
 TCT (Temperature Cycling
                               –65 °C / 150 °C, 500 cycles                                        JESD22-A104
 Test)
 uHAST (Highly
 Accelerated Stress Test,      130 °C, 85% RH, 96 hours                                           JESD22-A118
 unbiased)
 HTSL (High Temperature
                               150 °C, 1000 hours                                                 JESD22-A103
 Storage Life)
 LTSL (Low Temperature
                               –40 °C, 1000 hours                                                 JESD22-A119
 Storage Life)
 1 JEDEC document JEP155 states that 500 V HBM allows safe manufacturing with a standard ESD control process.
 2 JEDEC document JEP157 states that 250 V CDM allows safe manufacturing with a standard ESD control process.




Espressif Systems                                        69                          ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
```
