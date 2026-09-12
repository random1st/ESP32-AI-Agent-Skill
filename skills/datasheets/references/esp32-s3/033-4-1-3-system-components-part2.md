---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "4.1.3 System Components"
pdf_pages: 40-46
retrieved: 2026-09-12
redistribute: false
---

# 4.1.3 System Components

```text
BACKUP32K_CLK

Once the XTAL32K watchdog timer detects the oscillation failure of XTAL32K_CLK, it replaces XTAL32K_CLK
with BACKUP32K_CLK (with a frequency of 32 kHz or so) derived from RTC_CLK as RTC’s SLOW_CLK, so as to
ensure proper functioning of the system.

For details, see ESP32-S3 Technical Reference Manual > Chapter XTAL32K Watchdog Timers.


4.1.3.10 Permission Control

In ESP32-S3, the Permission Control module is used to control access to the slaves (including internal
memory, peripherals, external flash, and RAM). The host can access its slave only if it has the right permission.
In this way, data and instructions are protected from illegitimate read or write.


Espressif Systems                                       45                          ESP32-S3 Series Datasheet v2.2
                                          Submit Documentation Feedback
4 Functional Description


The ESP32-S3 CPU can run in both Secure World and Non-secure World where independent permission
controls are adopted. The Permission Control module is able to identify which World the host is running and
then proceed with its normal operations.

Feature List

   • Manage access to internal memory by:

           – CPU

           – CPU trace module

           – GDMA

   • Manage access to external flash and RAM by:

           – MMU

           – SPI1

           – GDMA

           – CPU through Cache

   • Manage access to peripherals, supporting

           – independent permission control for each peripheral

           – monitoring non-aligned access

           – access control for customized address range

   • Integrate permission lock register

           – All permission registers can be locked with the permission lock register. Once locked, the
             permission register and the lock register cannot be modified, unless the CPU is reset.

   • Integrate permission monitor interrupt

           – In case of illegitimate access, the permission monitor interrupt will be triggered and the CPU will be
             informed to handle the interrupt.

For details, see ESP32-S3 Technical Reference Manual > Chapter Permission Control.


4.1.3.11     World Controller

ESP32-S3 can divide the hardware and software resources into a Secure World and a Non-Secure World to
prevent sabotage or access to device information. Switching between the two worlds is performed by the
World Controller.

Feature List

   • Control of the CPU switching between secure and non-secure worlds

   • Control of 15 DMA peripherals switching between secure and non-secure worlds

   • Record of CPU’s world switching logs

   • Shielding of the CPU’s NMI interrupt



Espressif Systems                                        46                      ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
```
