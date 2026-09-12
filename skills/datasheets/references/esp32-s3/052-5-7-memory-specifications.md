---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "5.7 Memory Specifications"
pdf_pages: 68
retrieved: 2026-09-12
redistribute: false
---

# 5.7 Memory Specifications

```text
5 Electrical Characteristics


                                         Table 5-9 – cont’d from previous page
                        Frequency                                                                        Typ1          Typ2
 Work mode                (MHz)       Description                                                        (mA)          (mA)
                                      Dual core running 128-bit data access instructions                  91.7         107.9
 1 Current consumption when all peripheral clocks are disabled.
 2 Current consumption when all peripheral clocks are enabled. In practice, the current consumption might be
   different depending on which peripherals are enabled.
 3 In Modem-sleep mode, Wi-Fi is clock gated, and the current consumption might be higher when accessing
   flash. For a flash rated at 80 Mbit/s, in SPI 2-line mode the consumption is 10 mA.

                               Table 5-10. Current Consumption in Low-Power Modes

      Work mode         Description                                                                      Typ (µA)
      Light-sleep1      VDD_SPI and Wi-Fi are powered down, and all GPIOs are high-impedance.                   240
                        The ULP co-processor                 ULP-FSM                                             170
                        is powered on2                       ULP-RISC-V                                         190
      Deep-sleep        ULP sensor-monitored pattern3                                                             18
                        RTC memory and RTC peripherals are powered up.                                            8
                        RTC memory is powered up. RTC peripherals are powered down.                               7
      Power off         CHIP_PU is set to low level. The chip is shut down.                                        1
      1 In Light-sleep mode, all related SPI pins are pulled up. For chips embedded with PSRAM, please add
       corresponding PSRAM consumption values, e.g., 140 µA for 8 MB 8-line PSRAM (3.3 V), 200 µA for
       8 MB 8-line PSRAM (1.8 V) and 40 µA for 2 MB 4-line PSRAM (3.3 V).
      2 During Deep-sleep, when the ULP co-processor is powered on, peripherals such as GPIO and I2C
        are able to operate.
      3 The “ULP sensor-monitored pattern” refers to the mode where the ULP coprocessor or the sensor
       works periodically. When touch sensors work with a duty cycle of 1%, the typical current consumption
       is 18 µA.



5.7       Memory Specifications
The data below is sourced from the memory vendor datasheet. These values are guaranteed through design
and/or characterization but are not fully tested in production. Devices are shipped with the memory
erased.

                                           Table 5-11. Flash Specifications

                   Parameter      Description                       Min         Typ      Max     Unit
                                  Power supply voltage (1.8 V)         1.65     1.80     2.00     V
                   VCC
                                  Power supply voltage (3.3 V)            2.7   3.3       3.6     V
                   FC             Maximum clock frequency                 80      —        —    MHz
                   —              Program/erase cycles            100,000         —        —    cycles
                   TRET           Data retention time                     20      —        —    years
                   TP P           Page program time                        —    0.8         5    ms
                   TSE            Sector erase time (4 KB)                 —     70      500     ms
                                                                                Cont’d on next page


Espressif Systems                                        68                            ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
```
