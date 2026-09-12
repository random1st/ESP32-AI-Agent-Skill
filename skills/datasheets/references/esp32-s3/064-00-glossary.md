---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "Glossary"
pdf_pages: 81
retrieved: 2026-09-12
redistribute: false
---

# Glossary

```text
Glossary



Glossary

module

     A self-contained unit integrated within the chip to extend its capabilities, such as cryptographic modules,
     RF modules 2

peripheral

     A hardware component or subsystem within the chip to interface with the outside world 2

in-package flash

     Flash integrated directly into the chip’s package, and external to the chip die 4, 13

off-package flash

     Flash external to the chip’s package 20

strapping pin

     A type of GPIO pin used to configure certain operational settings during the chip’s power-up, and can be
     reconfigured as normal GPIO after the chip’s reset 32

eFuse parameter

     A parameter stored in an electrically programmable fuse (eFuse) memory within a chip. The parameter
     can be set by programming EFUSE_PGM_DATAn_REG registers, and read by reading a register field
     named after the parameter 32

SPI boot mode

     A boot mode in which users load and execute the existing code from SPI flash 33

joint download boot mode

     A boot mode in which users can download code into flash via the UART or other interfaces (see Table 3-3
     Chip Boot Mode Control > Note), and load and execute the downloaded code from the flash or SRAM 33

eFuse

     A one-time programmable (OTP) memory which stores system and user parameters, such as MAC
     address, chip revision number, flash encryption key, etc. Value 0 indicates the default state, and value 1
     indicates the eFuse has been programmed 39




Espressif Systems                                      81                      ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
```
