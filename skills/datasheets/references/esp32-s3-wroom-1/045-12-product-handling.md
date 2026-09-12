---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "12 Product Handling"
pdf_pages: 47
retrieved: 2026-09-12
redistribute: false
---

# 12 Product Handling

```text
12 Product Handling



12 Product Handling

12.1 Storage Conditions
The products sealed in moisture barrier bags (MBB) should be stored in a non-condensing atmospheric
environment of < 40 °C and 90%RH. The module is rated at the moisture sensitivity level (MSL) of 3.

After unpacking, the module must be soldered within 168 hours with the factory conditions 25±5 °C and
60%RH. If the above conditions are not met, the module needs to be baked.


12.2 Electrostatic Discharge (ESD)
   • Human body model (HBM): ±2000 V
   • Charged-device model (CDM): ±500 V


12.3 Reflow Profile
Solder the module in a single reflow.


                                                 Peak temperature: 235 – 250 °C
                                                 Peak time: 30 – 70 s
              Temperature (°C)
                                                 Soldering time: ＞ 30 s
                                                 Solder: Sn-Ag-Cu (SAC305) lead-free solder
     250

     230
     217
     200
      180


      150




      100




      50       Ramp-up            Preheating                    Soldering                 Cooling
               25 – 150 °C        150 – 200 °C                   ＞ 217 °C                 ＜ 180 °C
      25        60 – 90 s          60 – 120 s                    60 – 90 s               –5 ~ –1 °C/s
                1 – 3 °C/s
                                                                                                        Time (s)
         0             50               100           150           200             250

                                              Figure 12-1. Reflow Profile




Espressif Systems                                         47                ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                          Submit Documentation Feedback
```
