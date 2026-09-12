---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.3.4 Restrictions for GPIOs and RTC_GPIOs"
pdf_pages: 25
retrieved: 2026-09-12
redistribute: false
---

# 2.3.4 Restrictions for GPIOs and RTC_GPIOs

```text
2 Pins



2.3.4      Restrictions for GPIOs and RTC_GPIOs
All IO pins of ESP32-S3 have GPIO and some have RTC_GPIO pin functions. However, the IO pins are
multiplexed and can be configured for different purposes based on the requirements. Some IOs have
restrictions for usage. It is essential to consider the multiplexed nature and the limitations when using these IO
pins.

In tables of this chapter, some pin functions are in red or yellow . These functions indicate pins that require
extra caution when used as GPIO / GPIO :

   • IO Pins – allocated for communication with in-package flash/PSRAM and NOT recommended for other
        uses. For details, see Section 2.6 Pin Mapping Between Chip and Flash/PSRAM.

   • IO Pins – have one of the following important functions:

          – Strapping pins – need to be at certain logic levels at startup. See Section 3 Boot Configurations.

              Note:
              Strapping pins are highlighted by Pin Name or configurations At Reset, instead of the pin functions.

          – USB_D+/- – by default, connected to the USB Serial/JTAG Controller. To function as GPIOs, these
            pins need to be reconfigured via the IO_MUX_MCU_SEL bit (see
            ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix for details).

          – JTAG interface – often used for debugging. See Table 2-4 IO MUX Functions. To free these pins
            up, the pin functions USB_D+/- of the USB Serial/JTAG Controller can be used instead. See also
            Section 3.4 JTAG Signal Source Control.

          – UART0 interface – often used for debugging. See Table 2-4 IO MUX Functions.

          – 8-line SPI interface – no restrictions, unless the chip is connected to flash/PSRAM using 8-line SPI
            mode.

For more information about assigning pins, please see Section 2.3.5 Peripheral Pin Assignment and ESP32-S3
Consolidated Pin Overview.




Espressif Systems                                          25                         ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
```
