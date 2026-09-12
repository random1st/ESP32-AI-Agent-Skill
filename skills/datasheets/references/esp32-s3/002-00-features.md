---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "Features"
pdf_pages: 3-4
retrieved: 2026-09-12
redistribute: false
---

# Features

```text
Features
Wi-Fi

   • Complies with IEEE 802.11b/g/n

   • Supports 20 MHz and 40 MHz bandwidth in 2.4 GHz band

   • 1T1R mode with data rate up to 150 Mbps

   • Wi-Fi Multimedia (WMM)

   • TX/RX A-MPDU, TX/RX A-MSDU

   • Immediate Block ACK

   • Fragmentation and defragmentation

   • Automatic Beacon monitoring (hardware TSF)

   • Four virtual Wi-Fi interfaces

   • Simultaneous support for Infrastructure BSS in Station, SoftAP, or Station + SoftAP modes
     Note that when ESP32-S3 scans in Station mode, the SoftAP channel will change along with the Station
     channel

   • Antenna diversity

   • 802.11mc FTM


Bluetooth®

   • Bluetooth LE: Bluetooth 5, Bluetooth Mesh

   • High-power mode with up to 20 dBm transmission power

   • Speed: 125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps

   • LE Advertising Extensions

   • Multiple Advertising Sets

   • LE Channel Selection Algorithm #2

   • Internal co-existence mechanism between Wi-Fi and Bluetooth to share the same antenna


CPU and Memory

   • Xtensa® dual-core 32-bit LX7 microprocessor

   • Clock speed: up to 240 MHz

   • CoreMark® score:

        – Two cores at 240 MHz: 1329.92 CoreMark; 5.54 CoreMark/MHz

   • Five-stage pipeline

   • 128-bit data bus and dedicated SIMD instructions

   • Single precision floating point unit (FPU)


Espressif Systems                                    3                      ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
   • Ultra-Low-Power (ULP) coprocessors:

       – ULP-RISC-V coprocessor

       – ULP-FSM coprocessor

   • General DMA controller, with 5 transmit channels and 5 receive channels

   • L1 cache

   • ROM: 384 KB

   • SRAM: 512 KB

   • SRAM in RTC: 16 KB

   • 4096-bit eFuse memory, up to 1792 bits for users

   • Supported SPI protocols: SPI, Dual SPI, Quad SPI, Octal SPI, QPI and OPI interfaces that allow
     connection to flash, external RAM, and other SPI devices

   • Flash controller with cache is supported

   • Flash in-Circuit Programming (ICP) is supported


Peripherals

   • 45 programmable GPIOs

       – 4 strapping GPIOs

       – GPIOs allocated for in-package memory:

            * 6 GPIOs for either in-package flash or PSRAM

            * 7 GPIOs when both in-package flash and PSRAM are integrated

   • Connectivity interfaces:

       – Three UART interfaces

       – Two I2C interfaces

       – Two I2S interfaces

       – LCD interface

       – 8-bit ~ 16-bit DVP camera interface

       – Two SPI ports for communication with flash and RAM

       – Two general-purpose SPI ports

       – TWAI® controller, compatible with ISO 11898-1 (CAN Specification 2.0)

       – Full-speed USB OTG

       – USB Serial/JTAG controller

       – SD/MMC host controller with 2 slots

       – LED PWM controller, up to 8 channels

       – Two Motor Control PWM (MCPWM)


Espressif Systems                                      4                     ESP32-S3 Series Datasheet v2.2
                                       Submit Documentation Feedback
```
