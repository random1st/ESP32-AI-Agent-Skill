---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "6.4.1 Current Consumption in Active Mode"
pdf_pages: 28
retrieved: 2026-09-12
redistribute: false
---

# 6.4.1 Current Consumption in Active Mode

```text
5 Peripherals



                Chip reset release voltage (EN voltage is
 VIH_nRST                                                         0.75 × VDD 1       —      VDD 1 + 0.3      V
                within the specified range)
                Chip reset voltage (EN voltage is within the
 VIL_nRST                                                                –0.3        —    0.25 × VDD 1       V
                specified range)
 1 VDD – voltage from a power pin of a respective power domain.
 2V
      OH and VOL are measured using high-impedance load.




6.4     Current Consumption Characteristics
6.4.1 Current Consumption in Active Mode
With the use of advanced power-management technologies, the module can switch between different power
modes. For details on different power modes, please refer to ESP32-S3 Series Datasheet > Section Power
Management Unit.

The current consumption measurements are taken with a 3.3 V supply at 25 °C ambient temperature.

TX current consumption is rated at a 100% duty cycle.

RX current consumption is rated when the peripherals are disabled and the CPU idle.

                      Table 6-4. Current Consumption for Wi-Fi (2.4 GHz) in Active Mode

       Work Mode               RF Condition       Description                                 Peak (mA)
                                                  802.11b, 1 Mbps, @20.5 dBm                          355
                                                  802.11g, 54 Mbps, @18 dBm                           297
                               TX
                                                  802.11n, HT20, MCS 7, @17.5 dBm                     286
       Active (RF working)
                                                  802.11n, HT40, MCS 7, @17 dBm                       285
                                                  802.11b/g/n, HT20                                    95
                               RX
                                                  802.11n, HT40                                         97


                       Table 6-5. Current Consumption for Bluetooth LE in Active Mode

       Work Mode               RF Condition       Description                                 Peak (mA)
                                                  Bluetooth LE @ 20.0 dBm                             344
                               TX                 Bluetooth LE @ 9.0 dBm                              202
       Active (RF working)                        Bluetooth LE @ 0 dBm                                 187
                                                  Bluetooth LE @ –15.0 dBm                             119
                               RX                 Bluetooth LE                                         93




Espressif Systems                                       28              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                         Submit Documentation Feedback
```
