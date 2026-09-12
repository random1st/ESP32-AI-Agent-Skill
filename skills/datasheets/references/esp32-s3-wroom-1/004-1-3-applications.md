---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "1.3 Applications"
pdf_pages: 4-8
retrieved: 2026-09-12
redistribute: false
---

# 1.3 Applications

```text
1 Module Overview



   2 For customization of ESP32-S3-WROOM-1-H4, ESP32-S3-WROOM-1U-H4, and ESP32-S3-WROOM-1U-
     N16R16VA, please contact us.
   3 By default, the SPI flash on the module operates at a maximum clock frequency of 80 MHz and does
     not support the auto suspend feature. If you have a requirement for a higher flash clock frequency of
     120 MHz or if you need the flash auto suspend feature, please contact us.
   4 The modules use PSRAM integrated in the chip’s package. For specifications, refer to Section 6.5
     Memory Specifications.
   5 Ambient temperature specifies the recommended temperature range of the environment immediately
    outside the Espressif module.
   6 For details, refer to Section 10.1 Module Dimensions.
   7 Please note that the VDD_SPI voltage is 1.8 V for ESP32-S3-WROOM-1-N16R16VA and ESP32-S3-
     WROOM-1U-N16R16VA only.


At the core of the modules is an ESP32-S3 series of SoC, an Xtensa® 32-bit LX7 CPU that operates at up to
240 MHz. You can power off the CPU and make use of the low-power co-processor to constantly monitor the
peripherals for changes or crossing of thresholds.

  Note:
  For more information on ESP32-S3, please refer to ESP32-S3 Series Datasheet.
  For chip revision identification, ESP-IDF release that supports a specific chip revision, and other information on chip
  revisions, please refer to ESP32-S3 Series SoC Errata > Section Chip Revision Identification.




1.3 Applications
   • Smart Home                                                   • Generic Low-power IoT Sensor Hubs

   • Industrial Automation                                        • Generic Low-power IoT Data Loggers

   • Health Care                                                  • Cameras for Video Streaming

   • Consumer Electronics                                         • USB Devices

   • Smart Agriculture                                            • Speech Recognition

   • POS Machines                                                 • Image Recognition

   • Service Robot                                                • Wi-Fi + Bluetooth Networking Card

   • Audio Devices                                                • Touch and Proximity Sensing




Espressif Systems                                           4                 ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                            Submit Documentation Feedback
Contents



Contents

1     Module Overview                                                                                         2
1.1   Features                                                                                                2
1.2   Series Comparison                                                                                       3
1.3   Applications                                                                                            4

2     Block Diagram                                                                                           9


3     Pin Definitions                                                                                        10
3.1   Pin Layout                                                                                             10
3.2   Pin Description                                                                                         11

4     Boot Configurations                                                                                    13
4.1   Chip Boot Mode Control                                                                                 14
4.2   VDD_SPI Voltage Control                                                                                15
4.3   ROM Messages Printing Control                                                                          15
4.4   JTAG Signal Source Control                                                                             15
4.5   Chip Power-up and Reset                                                                                16

5     Peripherals                                                                                            17
5.1   Peripheral Overview                                                                                    17
5.2   Peripheral Description                                                                                 17
      5.2.1   Connectivity Interface                                                                         17
              5.2.1.1    UART Controller                                                                     17
              5.2.1.2    I2C Interface                                                                       18
              5.2.1.3    I2S Interface                                                                       18
              5.2.1.4    LCD and Camera Controller                                                           19
              5.2.1.5    Serial Peripheral Interface (SPI)                                                   19
                                                               ®
              5.2.1.6    Two-Wire Automotive Interface (TWAI )                                               21
              5.2.1.7    USB 2.0 OTG Full-Speed Interface                                                    21
              5.2.1.8    USB Serial/JTAG Controller                                                          22
              5.2.1.9    SD/MMC Host Controller                                                              23
              5.2.1.10   Motor Control PWM (MCPWM)                                                           24
              5.2.1.11   Remote Control Peripheral (RMT)                                                     24
              5.2.1.12   Pulse Count Controller (PCNT)                                                       25
      5.2.2   Analog Signal Processing                                                                       25
              5.2.2.1    SAR ADC                                                                             25
              5.2.2.2    Temperature Sensor                                                                  25
              5.2.2.3    Touch Sensor                                                                        26

6     Electrical Characteristics                                                                             27
6.1   Absolute Maximum Ratings                                                                               27
6.2   Recommended Operating Conditions                                                                       27
6.3   DC Characteristics (3.3 V, 25 °C)                                                                      27


Espressif Systems                                       5             ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                          Submit Documentation Feedback
Contents


6.4    Current Consumption Characteristics                                                                  28
       6.4.1   Current Consumption in Active Mode                                                           28
       6.4.2   Current Consumption in Other Modes                                                           29
6.5    Memory Specifications                                                                                30

7      RF Characteristics                                                                                   32
7.1    Wi-Fi Radio                                                                                          32
       7.1.1   Wi-Fi RF Transmitter (TX) Characteristics                                                    32
       7.1.2   Wi-Fi RF Receiver (RX) Characteristics                                                       33
7.2    Bluetooth LE Radio                                                                                   34
       7.2.1   Bluetooth LE RF Transmitter (TX) Characteristics                                             35
       7.2.2   Bluetooth LE RF Receiver (RX) Characteristics                                                36

8      Module Schematics                                                                                    39

9      Peripheral Schematics                                                                                41


10 Physical Dimensions                                                                                      42
10.1   Module Dimensions                                                                                    42
10.2   Dimensions of External Antenna Connector                                                             43

11 PCB Layout Recommendations                                                                               45
11.1   PCB Land Pattern                                                                                     45
11.2   Module Placement for PCB Design                                                                      46

12 Product Handling                                                                                         47
12.1   Storage Conditions                                                                                   47
12.2   Electrostatic Discharge (ESD)                                                                        47
12.3   Reflow Profile                                                                                       47
12.4   Ultrasonic Vibration                                                                                 48

Datasheet Versioning                                                                                        49


Related Documentation and Resources                                                                         50

Revision History                                                                                            51




Espressif Systems                                       6            ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                         Submit Documentation Feedback
List of Tables



List of Tables
   1-1   ESP32-S3-WROOM-1 Series Comparison1                                                                   3
   1-2   ESP32-S3-WROOM-1U Series Comparison                                                                   3
   3-1   Pin Definitions                                                                                       11
   4-1   Default Configuration of Strapping Pins                                                              13
   4-2 Description of Timing Parameters for the Strapping Pins                                                14
   4-3 Chip Boot Mode Control                                                                                 14
   4-4 VDD_SPI Voltage Control                                                                                15
   4-5 JTAG Signal Source Control                                                                             16
   4-6 Description of Timing Parameters for Power-up and Reset                                                16
   6-1 Absolute Maximum Ratings                                                                               27
   6-2 Recommended Operating Conditions                                                                       27
   6-3 DC Characteristics (3.3 V, 25 °C)                                                                      27
   6-4 Current Consumption for Wi-Fi (2.4 GHz) in Active Mode                                                 28
   6-5 Current Consumption for Bluetooth LE in Active Mode                                                    28
   6-6 Current Consumption in Modem-sleep Mode                                                                29
   6-7 Current Consumption in Low-Power Modes                                                                 30
   6-8 Flash Specifications                                                                                   30
   6-9 PSRAM Specifications                                                                                   31
   7-1   Wi-Fi RF Characteristics                                                                             32
   7-2 TX Power with Spectral Mask and EVM Meeting 802.11 Standards                                           32
   7-3 TX EVM Test1                                                                                           32
   7-4 RX Sensitivity                                                                                         33
   7-5 Maximum RX Level                                                                                       34
   7-6 RX Adjacent Channel Rejection                                                                          34
   7-7   Bluetooth LE RF Characteristics                                                                      34
   7-8 Bluetooth LE - Transmitter Characteristics - 1 Mbps                                                    35
   7-9 Bluetooth LE - Transmitter Characteristics - 2 Mbps                                                    35
   7-10 Bluetooth LE - Transmitter Characteristics - 125 Kbps                                                 35
   7-11 Bluetooth LE - Transmitter Characteristics - 500 Kbps                                                 36
   7-12 Bluetooth LE - Receiver Characteristics - 1 Mbps                                                      36
   7-13 Bluetooth LE - Receiver Characteristics - 2 Mbps                                                      36
   7-14 Bluetooth LE - Receiver Characteristics - 125 Kbps                                                    37
   7-15 Bluetooth LE - Receiver Characteristics - 500 Kbps                                                    37




Espressif Systems                                       7              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
List of Figures



List of Figures
   2-1   ESP32-S3-WROOM-1 Block Diagram                                                                      9
   2-2 ESP32-S3-WROOM-1U Block Diagram                                                                       9
   3-1   Pin Layout (Top View)                                                                              10
   4-1   Visualization of Timing Parameters for the Strapping Pins                                          14
   4-2 Visualization of Timing Parameters for Power-up and Reset                                            16
   8-1   ESP32-S3-WROOM-1 Schematics                                                                        39
   8-2 ESP32-S3-WROOM-1U Schematics                                                                         40
   9-1   Peripheral Schematics                                                                              41
   10-1 ESP32-S3-WROOM-1 Physical Dimensions                                                                42
   10-2 ESP32-S3-WROOM-1U Physical Dimensions                                                               42
   10-3 Dimensions of External Antenna Connector                                                            43
   11-1 ESP32-S3-WROOM-1 Recommended PCB Land Pattern                                                       45
   11-2 ESP32-S3-WROOM-1U Recommended PCB Land Pattern                                                      46
   12-1 Reflow Profile                                                                                      47




Espressif Systems                                      8             ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                        Submit Documentation Feedback
```
