---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "4.1.2 Memory Organization"
pdf_pages: 37-39
retrieved: 2026-09-12
redistribute: false
---

# 4.1.2 Memory Organization

```text
4 Functional Description


   • Saturation operation

For details, see ESP32-S3 Technical Reference Manual > Chapter Processor Instruction Extensions.


4.1.1.3 Ultra-Low-Power Coprocessor (ULP)

The ULP coprocessor is designed as a simplified, low-power replacement of CPU in sleep modes. It can be
also used to supplement the functions of the CPU in normal working mode. The ULP coprocessor and RTC
memory remain powered up during the Deep-sleep mode. Hence, the developer can store a program for the
ULP coprocessor in the RTC slow memory to access RTC GPIO, RTC peripheral devices, RTC timers and
internal sensors in Deep-sleep mode.

ESP32-S3 has two ULP coprocessors, one based on RISC-V instruction set architecture (ULP-RISC-V) and the
other on finite state machine (ULP-FSM). The clock of the coprocessors is the internal fast RC oscillator.

Feature List

   • ULP-RISC-V:

          – Support for RV32IMC instruction set

          – Thirty-two 32-bit general-purpose registers

          – 32-bit multiplier and divider

          – Support for interrupts

          – Booted by the CPU, its dedicated timer, or RTC GPIO

   • ULP-FSM:

          – Support for common instructions including arithmetic, jump, and program control instructions

          – Support for on-board sensor measurement instructions

          – Booted by the CPU, its dedicated timer, or RTC GPIO

  Note:
  Note that these two coprocessors cannot work simultaneously.


For details, see ESP32-S3 Technical Reference Manual > Chapter ULP Coprocessor.


4.1.1.4    GDMA Controller (GDMA)

ESP32-S3 has a general-purpose DMA controller (GDMA) with five independent channels for transmitting and
another five independent channels for receiving. These ten channels are shared by peripherals that have DMA
feature, and support dynamic priority.

The GDMA controller controls data transfer using linked lists. It allows peripheral-to-memory and
memory-to-memory data transfer at a high speed. All channels can access internal and external RAM.

The ten peripherals on ESP32-S3 with DMA feature are SPI2, SPI3, UHCI0, I2S0, I2S1, LCD/CAM, AES, SHA,
ADC, and RMT.

For details, see ESP32-S3 Technical Reference Manual > Chapter GDMA Controller.



Espressif Systems                                         37                   ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
4 Functional Description



4.1.2 Memory Organization
This subsection describes the memory arrangement to explain how data is stored, accessed, and managed
for efficient operation.

Figure 4-1 illustrates the address mapping structure of ESP32-S3.

                                                                                CPU

                                                                      0x0000_0000
                                                                                       Reserved
                                                                      0x3BFF_FFFF
                                                        Data bus      0x3C00_0000        32 MB
                                                                      0x3DFF_FFFF   External memory
                                                                      0x3E00_0000
                                                                                       Reserved
                                                                      0x3FC8_7FFF
                                                                                                                     Data bus
                                                                      0x3FC8_8000        480 KB
                                                                      0x3FCF_FFFF   Internal memory
                                                                      0x3FD0_0000
                                                                                       Reserved
                                                                      0x3FEF_FFFF
                                                                      0x3FF0_0000        128 KB        Data bus
                                                                                                                             ROM                 SRAM
                                                                      0x3FF1_FFFF   Internal memory
                                                                      0x3FF2_0000
                                                Cache                                  Reserved
                                                                      0x3FFF_FFFF
                                                                      0x4000_0000        384 KB          Instruction bus
                                                                      0x4005_FFFF   Internal memory
                                                                      0x4006_0000
                                                                                       Reserved
                                                                      0x4036_FFFF
   External Memory                      MMU
                                                                      0x4037_0000        448 KB                   Instruction bus
                                                                      0x403D_FFFF   Internal memory
                                                                      0x403E_0000
                                                                                       Reserved
                                                                      0x41FF_FFFF
                                                    Instruction bus   0x4200_0000        32 MB
                                                                                                                                                    GDMA
                                                                      0x43FF_FFFF   External memory
                                                                      0x4400_0000
                                                                                       Reserved
                                                                      0x4FFF_FFFF
                                                                      0x5000_0000         8 KB      Data/Instruction bus                 ★
                                                                                                                                   RTC
                                                                      0x5000_1FFF   Internal memory                            Slow Memory
                                                                      0x5000_2000
                                                                                       Reserved
                                                                      0x5FFF_FFFF
                                                                      0x6000_0000      836 KB         Data/Instruction bus    RTC Peripherals★
                                                                      0x600D_0FFF     Peripherals                            Other Peripherals
                                                                      0x600D_1000
                                                                                       Reserved
                                                                      0x600F_DFFF
                                                                      0x600F_E000         8 KB                                     RTC
                                                                      0x600F_FFFF   Internal memory                            Fast Memory
       Not available for use
                                                                      0x6010_0000
                                                                                       Reserved
       Available for use                                              0xFFFF_FFFF

   ★   Accessible by ULP co-processor




                                              Figure 4-1. Address Mapping Structure



4.1.2.1 Internal Memory

The internal memory of ESP32-S3 refers to the memory integrated on the chip die or in the chip package,
including ROM, SRAM, eFuse, and flash.

Feature List

   • 384 KB ROM: for booting and core functions

   • 512 KB on-chip SRAM: for data and instructions, running at a configurable frequency of up to 240 MHz

   • RTC FAST memory: 8 KB SRAM that supports read/write/instruction fetch by the main CPU (LX7
       dual-core processor). It can retain data in Deep-sleep mode



Espressif Systems                                                     38                                   ESP32-S3 Series Datasheet v2.2
                                                  Submit Documentation Feedback
4 Functional Description


   • RTC SLOW Memory: 8 KB SRAM that supports read/write/instruction fetch by the main CPU (LX7
     dual-core processor) or coprocessors. It can retain data in Deep-sleep mode

   • 4096-bit eFuse memory: 1792 bits are available for users, such as encryption key and device ID. See
     also Section 4.1.2.4 eFuse Controller

   • In-package flash and PSRAM:

          – See flash and PSRAM size in Chapter 1 ESP32-S3 Series Comparison

          – For specifications, refer to Section 5.7 Memory Specifications.

For details, see ESP32-S3 Technical Reference Manual > Chapter System and Memory.


4.1.2.2     External Flash and RAM

ESP32-S3 supports SPI, Dual SPI, Quad SPI, Octal SPI, QPI, and OPI interfaces that allow connection to
multiple external flash and RAM.

The external flash and RAM can be mapped into the CPU instruction memory space and read-only data
memory space. The external RAM can also be mapped into the CPU data memory space. ESP32-S3 supports
up to 1 GB of external flash and RAM, and hardware encryption/decryption based on XTS-AES to protect users’
programs and data in flash and external RAM.

Through high-speed caches, ESP32-S3 can support at a time up to:

   • External flash or RAM mapped into 32 MB instruction space as individual blocks of 64 KB

   • External RAM mapped into 32 MB data space as individual blocks of 64 KB. 8-bit, 16-bit, 32-bit, and
     128-bit reads and writes are supported. External flash can also be mapped into 32 MB data space as
     individual blocks of 64 KB, but only supporting 8-bit, 16-bit, 32-bit and 128-bit reads.

  Note:
  After ESP32-S3 is initialized, firmware can customize the mapping of external RAM or flash into the CPU address space.


For details, see ESP32-S3 Technical Reference Manual > Chapter System and Memory.


4.1.2.3 Cache

ESP32-S3 has an instruction cache and a data cache shared by the two CPU cores. Each cache can be
partitioned into multiple banks.

Feature List

   • Instruction cache: 16 KB (one bank) or 32 KB (two banks)
     Data cache: 32 KB (one bank) or 64 KB (two banks)

   • Instruction cache: four-way or eight-way set associative
     Data cache: four-way set associative

   • Block size of 16 bytes or 32 bytes for both instruction cache and data cache

   • Pre-load function

   • Lock function


Espressif Systems                                          39                        ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
```
