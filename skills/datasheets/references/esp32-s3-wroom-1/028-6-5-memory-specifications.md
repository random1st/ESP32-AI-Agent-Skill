---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "6.5 Memory Specifications"
pdf_pages: 30-31
retrieved: 2026-09-12
redistribute: false
---

# 6.5 Memory Specifications

```text
5 Peripherals


                                Table 6-7. Current Consumption in Low-Power Modes

      Work mode         Description                                                                        Typ (µA)
      Light-sleep1      VDD_SPI and Wi-Fi are powered down, and all GPIOs are high-impedance.                   240
                        The ULP co-processor                 ULP-FSM                                             170
                        is powered on2                       ULP-RISC-V                                          190
      Deep-sleep        ULP sensor-monitored pattern3                                                             18
                        RTC memory and RTC peripherals are powered up.                                             8
                        RTC memory is powered up. RTC peripherals are powered down.                                7
      Power off         EN is set to low level. The chip is shut down.                                             1
      1 In Light-sleep mode, all related SPI pins are pulled up. For chips embedded with PSRAM, please add
       corresponding PSRAM consumption values, e.g., 140 µA for 8 MB 8-line PSRAM (3.3 V), 200 µA for
       8 MB 8-line PSRAM (1.8 V) and 40 µA for 2 MB 4-line PSRAM (3.3 V).
      2 During Deep-sleep, when the ULP co-processor is powered on, peripherals such as GPIO and I2C
        are able to operate.
      3 The “ULP sensor-monitored pattern” refers to the mode where the ULP coprocessor or the sensor
       works periodically. When touch sensors work with a duty cycle of 1%, the typical current consumption
       is 18 µA.



6.5       Memory Specifications
The data below is sourced from the memory vendor datasheet. These values are guaranteed through design
and/or characterization but are not fully tested in production. Devices are shipped with the memory
erased.

                                           Table 6-8. Flash Specifications

                   Parameter      Description                        Min           Typ    Max      Unit
                                  Power supply voltage (1.8 V)           1.65     1.80    2.00      V
                   VCC
                                  Power supply voltage (3.3 V)            2.7      3.3     3.6      V
                   FC             Maximum clock frequency                 80         —      —     MHz
                   —              Program/erase cycles            100,000            —      —    cycles
                   TRET           Data retention time                     20         —      —     years
                   TP P           Page program time                        —       0.8       5     ms
                   TSE            Sector erase time (4 KB)                 —        70    500      ms
                   TBE1           Block erase time (32 KB)                 —       0.2       2      s
                   TBE2           Block erase time (64 KB)                 —       0.3       3      s
                                  Chip erase time (16 Mb)                  —         7      20      s
                                  Chip erase time (32 Mb)                  —        20      60      s
                   TCE            Chip erase time (64 Mb)                  —        25     100      s
                                  Chip erase time (128 Mb)                 —        60    200       s
                                  Chip erase time (256 Mb)                 —        70    300       s




Espressif Systems                                           30                  ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                            Submit Documentation Feedback
5 Peripherals


                                     Table 6-9. PSRAM Specifications

                    Parameter   Description                    Min      Typ    Max    Unit
                                Power supply voltage (1.8 V)   1.62    1.80    1.98     V
                    VCC
                                Power supply voltage (3.3 V)   2.7      3.3     3.6     V
                    FC          Maximum clock frequency         80        —      —    MHz




Espressif Systems                                   31                ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                      Submit Documentation Feedback
```
