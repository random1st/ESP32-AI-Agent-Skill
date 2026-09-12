---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "History"
pdf_pages: 82-87
retrieved: 2026-09-12
redistribute: false
---

# History

```text
Related Documentation and Resources



Related Documentation and Resources
Related Documentation
   • ESP32-S3 Technical Reference Manual – Detailed information on how to use the ESP32-S3 memory and periph-
     erals.
   • ESP32-S3 Hardware Design Guidelines – Guidelines on how to integrate the ESP32-S3 into your hardware prod-
     uct.
   • ESP32-S3 Series SoC Errata – Descriptions of known errors in ESP32-S3 series of SoCs.
   • Certificates
     https://espressif.com/en/support/documents/certificates
   • ESP32-S3 Product/Process Change Notifications (PCN)
     https://espressif.com/en/support/documents/pcns?keys=ESP32-S3
   • ESP32-S3 Advisories – Information on security, bugs, compatibility, component reliability.
     https://espressif.com/en/support/documents/advisories?keys=ESP32-S3
   • Documentation Updates and Update Notification Subscription
     https://espressif.com/en/support/download/documents

Developer Zone
   • ESP-IDF Programming Guide for ESP32-S3 – Extensive documentation for the ESP-IDF development framework.
   • ESP-IDF and other development frameworks on GitHub.
     https://github.com/espressif
   • ESP32 BBS Forum – Engineer-to-Engineer (E2E) Community for Espressif products where you can post questions,
     share knowledge, explore ideas, and help solve problems with fellow engineers.
     https://esp32.com/
   • ESP-FAQ – A summary document of frequently asked questions released by Espressif.
     https://espressif.com/projects/esp-faq/en/latest/index.html
   • The ESP Journal – Best Practices, Articles, and Notes from Espressif folks.
     https://blog.espressif.com/
   • See the tabs SDKs and Demos, Apps, Tools, AT Firmware.
     https://espressif.com/en/support/download/sdks-demos

Products
   • ESP32-S3 Series SoCs – Browse through all ESP32-S3 SoCs.
     https://espressif.com/en/products/socs?id=ESP32-S3
   • ESP32-S3 Series Modules – Browse through all ESP32-S3-based modules.
     https://espressif.com/en/products/modules?id=ESP32-S3
   • ESP32-S3 Series DevKits – Browse through all ESP32-S3-based devkits.
     https://espressif.com/en/products/devkits?id=ESP32-S3
   • ESP Product Selector – Find an Espressif hardware product suitable for your needs by comparing or applying filters.
     https://products.espressif.com/#/product-selector?language=en

Contact Us
   • See the tabs Sales Questions, Technical Enquiries, Circuit Schematic & PCB Design Review, Get Samples
     (Online stores), Become Our Supplier, Comments & Suggestions.
     https://espressif.com/en/contact-us/sales-questions


Espressif Systems                                         82                       ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
Revision History



Revision History

 Date              Version   Release notes
                                • Renamed the Digital Signature module to “RSA Digital Signature Peripheral
                                  (RSA_DS)”
                                • Updated Figure 4-1 Address Mapping Structure
 2026-03-05        v2.2
                                • Added a note in Section 4.2.1.9 SD/MMC Host Controller
                                • Updated table 5-10 Current Consumption in Low-Power Modes


                                • Updated the status of ESP32-S3R2 to End of Life and added chip variant
                                  ESP32-S3RH2
                                • Updated “Ordering Code” to “Part Number” in Table 1-1 ESP32-S3 Series
                                  Comparison
                                • Added Section 1.3 Chip Revision and chip version information in Table 1-1
                                  ESP32-S3 Series Comparison
                                • Added Section 2.3.5 Peripheral Pin Assignment and updated the Pin As-
                                  signment part for each subsection in Section 4.2 Peripherals
 2025-11-28        v2.1
                                • Updated Figure 3-1 Visualization of Timing Parameters for the Strapping
                                  Pins
                                • Added Section 5.7 Memory Specifications
                                • Added Table 5-8 Current Consumption for Bluetooth LE in Active Mode
                                  in Section 5.6 Current Consumption
                                • Added Appendix Datasheet Status Definitions and Glossary
                                • Other structural, formatting, and content improvements


                                • Updated the status of ESP32-S3R8V to End of Life
                                • Updated the CoreMark® score in Section CPU and Memory
                                • Updated Figure 4.1.2 Memory Organization in Section 4-1 Address Map-
                                  ping Structure
                                • Updated the temperature sensor’s measurement range in Section 4.2.2.2
 2025-04-24        v2.0
                                  Temperature Sensor
                                • Added some notes in Chapter 6 RF Characteristics
                                • Updated the source file link for the recommended land pattern in Chapter
                                  7 Packaging


                                                                                      Cont’d on next page




Espressif Systems                                     83                    ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
Revision History


                                       Cont’d from previous page
 Date              Version   Release notes
                                • Updated descriptions on the title page
                                • Updated feature descriptions in Section Features and adjusted the format
                                • Updated the pin introduction in Section 2.2 Pin Overview and adjusted
                                  the format
                                • Updated descriptions in Section 2.3 IO Pins, and divided Section RTC and
                                  Analog Pin Functions into Section 2.3.3 Analog Functions and Section
 2024-09-11        v1.9
                                  2.3.2 RTC Functions
                                • Updated Section Strapping Pins to Section 3 Boot Configurations
                                • Adjusted the structure and section order in Section 4 Functional Descrip-
                                  tion, deleted Section Peripheral Pin Configurations, and added the Pin
                                  Assignment part in each subsection in Section 4.2 Peripherals


                                • Added chip variant ESP32-S3R16V and updated related information
                                • Added the second and third table notes in Table 1-1 ESP32-S3 Series
                                  Comparison
 2023-11-24        v1.8         • Updated Section 3.1 Chip Boot Mode Control
                                • Updated Section 5.5 ADC Characteristics
                                • Other minor updates


                                • Removed the sample status for ESP32-S3FH4R2
                                • Updated Figure ESP32-S3 Functional Block Diagram and Figure 4-2 Com-
                                  ponents and Power Domains
                                • Added the predefined settings at reset and after reset for GPIO20 in Table
                                  2-1 Pin Overview
                                • Updated notes for Table 2-4 IO MUX Functions
 2023-06           v1.7
                                • Updated the clock name “FOSC_CLK” to “RC_FAST_CLK” in Section
                                  4.1.3.5 Power Management Unit (PMU)
                                • Updated descriptions in Section 4.2.1.5 Serial Peripheral Interface (SPI)
                                  and Section 4.1.4.3 RSA Accelerator
                                • Other minor updates


                                                                                       Cont’d on next page




Espressif Systems                                    84                      ESP32-S3 Series Datasheet v2.2
                                      Submit Documentation Feedback
Revision History


                                         Cont’d from previous page
 Date              Version   Release notes
                                • Improved the content in the following sections:
                                    – Section Product Overview
                                    – Section 2 Pins
                                    – Section 4.1.3.5 Power Management Unit (PMU)
                                    – Section 4.2.1.5 Serial Peripheral Interface (SPI)
                                    – Section 5.1 Absolute Maximum Ratings
                                    – Section 5.2 Recommended Operating Conditions
                                    – Section 5.3 VDD_SPI Output Characteristics
 2023-02           v1.6             – Section 5.5 ADC Characteristics
                                • Added ESP32-S3 Consolidated Pin Overview
                                • Updated the notes in Section 1 ESP32-S3 Series Comparison and Section
                                  7 Packaging
                                • Updated the effective measurement range in Table 5-5 ADC Characteris-
                                  tics
                                • Updated the Bluetooth maximum transmit power
                                • Other minor updates


                                • Removed the “External PA is supported” feature from Section Features
                                • Updated the ambient temperature for ESP32-S3FH4R2 from –40 ∼ 105
 2022-12           v1.5           °C to –40 ∼ 85 °C
                                • Added two notes in Section 7


                                • Added the package information for ESP32-S3FH4R2 in Section 7
                                • Added ESP32-S3 Series SoC Errata in Section
 2022-11           v1.4
                                • Other minor updates


                                • Added a note about the maximum ambient temperature of R8 series chips
                                  to Table 1-1 and Table 5-2
                                • Added information about power-up glitches for some pins in Section 2.2
                                • Added the information about VDD3P3 power pins to Table 2.2 and Sec-
                                  tion 2.5.2
 2022-09           v1.3         • Updated section 4.3.3.1
                                • Added the fourth note in Table 2-1
                                • Updated the minimum and maximum values of Bluetooth LE RF transmit
                                  power in Section 6.2.1
                                • Other minor updates


                                • Updated description of ROM code printing in Section 3
                                • Updated Figure ESP32-S3 Functional Block Diagram
 2022-07           v1.2         • Update Section 5.6
                                • Deleted the hyperlinks in Application


                                                                                      Cont’d on next page



Espressif Systems                                     85                    ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
Revision History


                                        Cont’d from previous page
 Date              Version   Release notes
                                • Synchronized eFuse size throughout
                                • Updated pin description in Table 2-1
 2022-04           v1.1         • Updated SPI resistance in Table 5-3
                                • Added information about chip ESP32-S3FH4R2


                                • Added wake-up sources for Deep-sleep mode
                                • Added Table 3-4 for default configurations of VDD_SPI
                                • Added ADC calibration results in Table 5-5
                                • Added typical values when all peripherals and peripheral clocks are en-
                                  abled to Table 5-9
                                • Added more descriptions of modules/peripherals in Section 4
 2022-01           v1.0         • Updated Figure ESP32-S3 Functional Block Diagram
                                • Updated JEDEC specification
                                • Updated Wi-Fi RF data in Section 5.6
                                • Updated temperature for ESP32-S3R8 and ESP32-S3R8V
                                • Updated description of Deep-sleep mode in Table 5-10
                                • Updated wording throughout


 2021-10-12        v0.6.1    Updated text description
                                • Updated to chip revision 1 by swapping pin 53 and pin 54 (XTAL_P and
                                  XTAL_N)
                                • Updated Figure ESP32-S3 Functional Block Diagram
                                • Added CoreMark score in section Features
                                • Updated Section 3
 2021-09-30        v0.6
                                • Added data for cumulative IO output current in Table 5-1
                                • Added data for Modem-sleep current consumption in Table 5-9
                                • Updated data in section 5.6, 6.1, and 6.2
                                • Updated wording throughout


                                • Added “for chip revision 0” on cover, in footer and watermark to indicate
                                  that the current and previous versions of this datasheet are for chip ver-
 2021-07-19        v0.5.1         sion 0
                                • Corrected a few typos


 2021-07-09        v0.5      Preliminary version




Espressif Systems                                      86                      ESP32-S3 Series Datasheet v2.2
                                       Submit Documentation Feedback
Disclaimer and Copyright Notice
Information in this document, including URL references, is subject to change without notice.
ALL THIRD PARTY’S INFORMATION IN THIS DOCUMENT IS PROVIDED AS IS WITH NO WARRANTIES TO ITS AUTHENTICITY AND
ACCURACY.
NO WARRANTY IS PROVIDED TO THIS DOCUMENT FOR ITS MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR
PURPOSE, NOR DOES ANY WARRANTY OTHERWISE ARISING OUT OF ANY PROPOSAL, SPECIFICATION OR SAMPLE.
All liability, including liability for infringement of any proprietary rights, relating to use of information in this document is disclaimed. No
licenses express or implied, by estoppel or otherwise, to any intellectual property rights are granted herein.
The Wi-Fi Alliance Member logo is a trademark of the Wi-Fi Alliance. The Bluetooth logo is a registered trademark of Bluetooth SIG.
All trade names, trademarks and registered trademarks mentioned in this document are property of their respective owners, and are
hereby acknowledged.
Copyright © 2026 Espressif Systems (Shanghai) Co., Ltd. All rights reserved.
www.espressif.com
```
