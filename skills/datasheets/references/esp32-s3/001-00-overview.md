---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "Overview"
pdf_pages: 2
retrieved: 2026-09-12
redistribute: false
---

# Overview

```text
Product Overview

ESP32-S3 is a low-power MCU-based system on a chip (SoC) with integrated 2.4 GHz Wi-Fi and Bluetooth®
Low Energy (Bluetooth LE). It consists of high-performance dual-core microprocessor (Xtensa® 32-bit LX7), a
ULP coprocessor, a Wi-Fi baseband, a Bluetooth LE baseband, RF module, and numerous peripherals.

The functional block diagram of the SoC is shown below.


                                   Espressif ESP32-S3 Wi-Fi + Bluetooth® Low Energy SoC

                  CPU and Memory                                                       RF                      Wireless Digital Circuits
                    ®                                       2.4 GHz Balun +                       External                          Wi-Fi
            Xtensa Dual-core 32-bit LX7                                                                        Wi-Fi MAC
                  Microprocessor                                 Switch                          Main Clock                       Baseband

                                                                                                  Fast RC
          Cache         SRAM
                                                                      2.4 GHz
                                                                                                               Bluetooth LE Link Controller
                                        Interrupt         2.4 GHz                      RF         Oscillator
                                          Matrix          Receiver   Transmitter   Synthesizer   Phase Lock
           JTAG          ROM                                                                                     Bluetooth LE Baseband
                                                                                                    Loop


                                             Peripherals                                                                Security

                            System                                        GPIO                   RTC GPIO      SHA     RSA     AES      RNG
           GDMA                                General-
                             Timer             purpose
                                                Timers
                                                                      DIG ADC                     RTC ADC        HMAC
                                                                                                                                  RSA_DS
          SD/MMC             Pulse
            Host            Counter            World                 USB Serial/                   eFuse
                                                                                                               Secure Boot
                                              Controller               JTAG                       Controller
                                                                                                                                    Flash
                                                                                                               Permission         Encryption
           SPI0/1            SPI2/3                 I2S
                                                                     Main System                   RTC          Control
                                                                      Watchdog                   Watchdog
                                                                       Timers                     Timer
          USB OTG            TWAI®                  I2C
                                                                                                                            RTC

                                                                       Super                       Touch         RTC
            UART           LED PWM             MCPWM                                                                                PMU
                                                                      Watchdog                     Sensor       Memory

                              LCD               Camera                                           Temperature
            RMT                                                        RTC I2C                                       ULP Coprocessor
                            Interface          Interface                                           Sensor




        Power consumption
                    Normal
                    Low power consumption components capable of working in Deep-sleep mode


                                              ESP32-S3 Functional Block Diagram


For more information on power consumption, see Section 4.1.3.5 Power Management Unit (PMU).




Espressif Systems                                                                  2                           ESP32-S3 Series Datasheet v2.2
                                                    Submit Documentation Feedback
```
