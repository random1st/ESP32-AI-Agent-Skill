---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "Applications"
pdf_pages: 5-12
retrieved: 2026-09-12
redistribute: false
---

# Applications

```text
       – RMT (TX/RX)

       – Pulse count controller

   • Analog signal processing:

       – Two 12-bit SAR ADCs, up to 20 channels

       – Temperature sensor

       – 14 capacitive touch sensing IOs

   • Timers:

       – Four 54-bit general-purpose timers

       – 52-bit system timer

       – Three watchdog timers


Power Management

   • Fine-resolution power control, including clock frequency, duty cycle, Wi-Fi operating modes, and
     individual internal component control

   • Four power modes designed for typical scenarios: Active, Modem-sleep, Light-sleep, Deep-sleep

   • Power consumption in Deep-sleep mode is 7 µA

   • RTC memory remains powered on in Deep-sleep mode


Security

   • Secure boot - permission control on accessing internal and external memory

   • Flash encryption - memory encryption and decryption

   • Cryptographic hardware acceleration:

       – SHA Accelerator (FIPS PUB 180-4)

       – AES Accelerator (FIPS PUB 197)

       – RSA Accelerator

       – HMAC Accelerator

       – RSA Digital Signature Peripheral (RSA_DS)

       – Random Number Generator (RNG)


RF Module

   • Antenna switches, RF balun, power amplifier, low-noise receive amplifier

   • Up to +21 dBm of power for an 802.11b transmission

   • Up to +19.5 dBm of power for an 802.11n transmission

   • Up to -104.5 dBm of sensitivity for Bluetooth LE receiver (125 Kbps)




Espressif Systems                                     5                     ESP32-S3 Series Datasheet v2.2
                                       Submit Documentation Feedback
Applications
With low power consumption, ESP32-S3 is an ideal choice for IoT devices in the following areas:

   • Smart Home                                           • Generic Low-power IoT Sensor Hubs

   • Industrial Automation                                • Generic Low-power IoT Data Loggers

   • Health Care                                          • Cameras for Video Streaming

   • Consumer Electronics                                 • USB Devices

   • Smart Agriculture                                    • Speech Recognition

   • POS Machines                                         • Image Recognition

   • Service Robot                                        • Wi-Fi + Bluetooth Networking Card

   • Audio Devices                                        • Touch and Proximity Sensing




Espressif Systems                                    6                     ESP32-S3 Series Datasheet v2.2
                                       Submit Documentation Feedback
Contents



      Note:

       Check the link or the QR code to make sure that you use the latest version of this document:
       https://www.espressif.com/documentation/esp32-s3_datasheet_en.pdf




Contents

Product Overview                                                                                                   2
Features                                                                                                           3
Applications                                                                                                       6

1         ESP32-S3 Series Comparison                                                                               13
1.1       Nomenclature                                                                                             13
1.2       Comparison                                                                                               13
1.3       Chip Revision                                                                                            14

2         Pins                                                                                                     15
2.1       Pin Layout                                                                                               15
2.2       Pin Overview                                                                                             16
2.3       IO Pins                                                                                                 20
          2.3.1     IO MUX Functions                                                                              20
          2.3.2     RTC Functions                                                                                 23
          2.3.3     Analog Functions                                                                              24
          2.3.4     Restrictions for GPIOs and RTC_GPIOs                                                          25
          2.3.5     Peripheral Pin Assignment                                                                     26
2.4       Analog Pins                                                                                             28
2.5       Power Supply                                                                                            29
          2.5.1     Power Pins                                                                                    29
          2.5.2     Power Scheme                                                                                  29
          2.5.3     Chip Power-up and Reset                                                                       30
2.6       Pin Mapping Between Chip and Flash/PSRAM                                                                 31

3         Boot Configurations                                                                                     32
3.1       Chip Boot Mode Control                                                                                  33
3.2       VDD_SPI Voltage Control                                                                                 34
3.3       ROM Messages Printing Control                                                                           34
3.4       JTAG Signal Source Control                                                                              34

4         Functional Description                                                                                  36
4.1       System                                                                                                  36
          4.1.1     Microprocessor and Master                                                                     36
                    4.1.1.1   CPU                                                                                 36
                    4.1.1.2   Processor Instruction Extensions (PIE)                                              36



Espressif Systems                                             7                        ESP32-S3 Series Datasheet v2.2
                                              Submit Documentation Feedback
Contents


              4.1.1.3    Ultra-Low-Power Coprocessor (ULP)                                             37
              4.1.1.4    GDMA Controller (GDMA)                                                        37
      4.1.2   Memory Organization                                                                      38
              4.1.2.1    Internal Memory                                                               38
              4.1.2.2    External Flash and RAM                                                        39
              4.1.2.3    Cache                                                                         39
              4.1.2.4    eFuse Controller                                                              40
      4.1.3   System Components                                                                        40
              4.1.3.1    IO MUX and GPIO Matrix                                                        40
              4.1.3.2    Reset                                                                          41
              4.1.3.3    Clock                                                                          41
              4.1.3.4    Interrupt Matrix                                                              42
              4.1.3.5    Power Management Unit (PMU)                                                   42
              4.1.3.6    System Timer                                                                  44
              4.1.3.7    General Purpose Timers                                                        44
              4.1.3.8    Watchdog Timers                                                               45
              4.1.3.9    XTAL32K Watchdog Timers                                                       45
              4.1.3.10   Permission Control                                                            45
              4.1.3.11   World Controller                                                              46
              4.1.3.12   System Registers                                                              47
      4.1.4   Cryptography and Security Component                                                      47
              4.1.4.1    SHA Accelerator                                                               47
              4.1.4.2    AES Accelerator                                                               48
              4.1.4.3    RSA Accelerator                                                               48
              4.1.4.4    Secure Boot                                                                   48
              4.1.4.5    HMAC Accelerator                                                              49
              4.1.4.6    RSA Digital Signature Peripheral (RSA_DS)                                     49
              4.1.4.7    External Memory Encryption and Decryption                                     49
              4.1.4.8    Clock Glitch Detection                                                        50
              4.1.4.9    Random Number Generator                                                       50
4.2   Peripherals                                                                                       51
      4.2.1   Connectivity Interface                                                                    51
              4.2.1.1    UART Controller                                                                51
              4.2.1.2    I2C Interface                                                                  51
              4.2.1.3    I2S Interface                                                                 52
              4.2.1.4    LCD and Camera Controller                                                     52
              4.2.1.5    Serial Peripheral Interface (SPI)                                             53
                                                                 ®
              4.2.1.6    Two-Wire Automotive Interface (TWAI )                                         54
              4.2.1.7    USB 2.0 OTG Full-Speed Interface                                              55
              4.2.1.8    USB Serial/JTAG Controller                                                    56
              4.2.1.9    SD/MMC Host Controller                                                        56
              4.2.1.10   Motor Control PWM (MCPWM)                                                     57
              4.2.1.11   Remote Control Peripheral (RMT)                                               58
              4.2.1.12   Pulse Count Controller (PCNT)                                                 58
      4.2.2   Analog Signal Processing                                                                 59
              4.2.2.1    SAR ADC                                                                       59


Espressif Systems                                        8                  ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
Contents


               4.2.2.2   Temperature Sensor                                                          59
               4.2.2.3   Touch Sensor                                                                59
4.3   Wireless Communication                                                                          61
      4.3.1    Radio                                                                                  61
               4.3.1.1   2.4 GHz Receiver                                                             61
               4.3.1.2   2.4 GHz Transmitter                                                          61
               4.3.1.3   Clock Generator                                                              61
      4.3.2    Wi-Fi                                                                                  61
               4.3.2.1   Wi-Fi Radio and Baseband                                                    62
               4.3.2.2   Wi-Fi MAC                                                                   62
               4.3.2.3   Networking Features                                                         62
      4.3.3    Bluetooth LE                                                                          62
               4.3.3.1   Bluetooth LE PHY                                                            63
               4.3.3.2   Bluetooth LE Link Controller                                                63

5     Electrical Characteristics                                                                     64
5.1   Absolute Maximum Ratings                                                                       64
5.2   Recommended Operating Conditions                                                               64
5.3   VDD_SPI Output Characteristics                                                                 65
5.4   DC Characteristics (3.3 V, 25 °C)                                                              65
5.5   ADC Characteristics                                                                            66
5.6   Current Consumption                                                                            66
      5.6.1    Current Consumption in Active Mode                                                    66
      5.6.2    Current Consumption in Other Modes                                                    67
5.7   Memory Specifications                                                                          68
5.8   Reliability                                                                                    69

6     RF Characteristics                                                                             70
6.1   Wi-Fi Radio                                                                                    70
      6.1.1    Wi-Fi RF Transmitter (TX) Characteristics                                             70
      6.1.2    Wi-Fi RF Receiver (RX) Characteristics                                                 71
6.2   Bluetooth LE Radio                                                                             72
      6.2.1    Bluetooth LE RF Transmitter (TX) Characteristics                                      73
      6.2.2    Bluetooth LE RF Receiver (RX) Characteristics                                          74

7     Packaging                                                                                      77


ESP32-S3 Consolidated Pin Overview                                                                   79

Datasheet Versioning                                                                                 80


Glossary                                                                                              81


Related Documentation and Resources                                                                  82

Revision History                                                                                     83



Espressif Systems                                       9                 ESP32-S3 Series Datasheet v2.2
                                          Submit Documentation Feedback
List of Tables



List of Tables
   1-1   ESP32-S3 Series Comparison                                                                 13
   2-1   Pin Overview                                                                               16
   2-2 Power-Up Glitches on Pins                                                                    18
   2-3 Peripheral Signals Routed via IO MUX                                                        20
   2-4 IO MUX Functions                                                                             21
   2-5 RTC Peripheral Signals Routed via RTC IO MUX                                                23
   2-6 RTC Functions                                                                               23
   2-7 Analog Signals Routed to Analog Functions                                                   24
   2-8 Analog Functions                                                                            24
   2-9 Peripheral Pin Assignment                                                                   27
   2-10 Analog Pins                                                                                28
   2-11 Power Pins                                                                                 29
   2-12 Voltage Regulators                                                                         29
   2-13 Description of Timing Parameters for Power-up and Reset                                    30
   2-14 Pin Mapping Between Chip and Flash or PSRAM                                                 31
   3-1   Default Configuration of Strapping Pins                                                   32
   3-2 Description of Timing Parameters for the Strapping Pins                                     33
   3-3 Chip Boot Mode Control                                                                      33
   3-4 VDD_SPI Voltage Control                                                                     34
   3-5 JTAG Signal Source Control                                                                  35
   4-1   Components and Power Domains                                                              44
   5-1   Absolute Maximum Ratings                                                                  64
   5-2 Recommended Operating Conditions                                                            64
   5-3 VDD_SPI Internal and Output Characteristics                                                 65
   5-4 DC Characteristics (3.3 V, 25 °C)                                                           65
   5-5 ADC Characteristics                                                                         66
   5-6 ADC Calibration Results                                                                     66
   5-7 Current Consumption for Wi-Fi (2.4 GHz) in Active Mode                                      66
   5-8 Current Consumption for Bluetooth LE in Active Mode                                         67
   5-9 Current Consumption in Modem-sleep Mode                                                     67
   5-10 Current Consumption in Low-Power Modes                                                     68
   5-11 Flash Specifications                                                                       68
   5-12 PSRAM Specifications                                                                       69
   5-13 Reliability Qualifications                                                                 69
   6-1 Wi-Fi RF Characteristics                                                                    70
   6-2 TX Power with Spectral Mask and EVM Meeting 802.11 Standards                                70
   6-3 TX EVM Test1                                                                                70
   6-4 RX Sensitivity                                                                               71
   6-5 Maximum RX Level                                                                            72
   6-6 RX Adjacent Channel Rejection                                                               72
   6-7 Bluetooth LE Frequency                                                                      72
   6-8 Transmitter Characteristics - Bluetooth LE 1 Mbps                                           73
   6-9 Transmitter Characteristics - Bluetooth LE 2 Mbps                                           73



Espressif Systems                                    10                 ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
List of Tables


   6-10 Transmitter Characteristics - Bluetooth LE 125 Kbps                                       73
   6-11 Transmitter Characteristics - Bluetooth LE 500 Kbps                                        74
   6-12 Receiver Characteristics - Bluetooth LE 1 Mbps                                             74
   6-13 Receiver Characteristics - Bluetooth LE 2 Mbps                                            75
   6-14 Receiver Characteristics - Bluetooth LE 125 Kbps                                          75
   6-15 Receiver Characteristics - Bluetooth LE 500 Kbps                                          76
   7-1   Consolidated Pin Overview                                                                79




Espressif Systems                                     11               ESP32-S3 Series Datasheet v2.2
                                       Submit Documentation Feedback
List of Figures



List of Figures
   1-1   ESP32-S3 Series Nomenclature                                                               13
   2-1   ESP32-S3 Pin Layout (Top View)                                                             15
   2-2 ESP32-S3 Power Scheme                                                                       30
   2-3 Visualization of Timing Parameters for Power-up and Reset                                   30
   3-1   Visualization of Timing Parameters for the Strapping Pins                                 33
   4-1   Address Mapping Structure                                                                 38
   4-2 Components and Power Domains                                                                43
   7-1   QFN56 (7×7 mm) Package                                                                    77
   7-2 QFN56 (7×7 mm) Package (Only for ESP32-S3FH4R2)                                             78




Espressif Systems                                      12               ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
```
