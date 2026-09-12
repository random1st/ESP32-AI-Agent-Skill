---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.2 Pin Overview"
pdf_pages: 16-19
retrieved: 2026-09-12
redistribute: false
---

# 2.2 Pin Overview

```text
2 Pins



2.2 Pin Overview
The ESP32-S3 chip integrates multiple peripherals that require communication with the outside world. To keep
the chip package size reasonably small, the number of available pins has to be limited. So the only way to
route all the incoming and outgoing signals is through pin multiplexing. Pin muxing is controlled via software
programmable registers (see ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO
Matrix).

All in all, the ESP32-S3 chip has the following types of pins:

      • IO pins with the following predefined sets of functions to choose from:

           – Each IO pin has predefined IO MUX functions – see Table 2-4 IO MUX Functions

           – Some IO pins have predefined RTC functions – see Table 2-6 RTC Functions

           – Some IO pins have predefined analog functions – see Table 2-8 Analog Functions

        Predefined functions means that each IO pin has a set of direct connections to certain on-chip
        peripherals. During run-time, the user can configure which peripheral from a predefined set to connect
        to a certain pin at a certain time via memory mapped registers (see
        ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO pins).

      • Analog pins that have exclusively-dedicated analog functions – see Table 2-10 Analog Pins

      • Power pins that supply power to the chip components and non-power pins – see Table 2-11 Power Pins


Table 2-1 Pin Overview gives an overview of all the pins. For more information, see the respective sections for
each pin type below, or ESP32-S3 Consolidated Pin Overview.

                                                 Table 2-1. Pin Overview

                                                                      Pin Settings 6             Pin Function Sets 1
 Pin No.     Pin Name       Pin Type   Pin Providing Power 2-5   At Reset     After Reset   IO MUX   RTC IO MUX    Analog
 1           LNA_IN         Analog
 2           VDD3P3         Power
 3           VDD3P3         Power
 4           CHIP_PU        Analog     VDD3P3_RTC
 5           GPIO0          IO         VDD3P3_RTC                WPU, IE      WPU, IE       IO MUX   RTC IO MUX
 6           GPIO1          IO         VDD3P3_RTC                IE           IE            IO MUX   RTC IO MUX    Analog
 7           GPIO2          IO         VDD3P3_RTC                IE           IE            IO MUX   RTC IO MUX    Analog
 8           GPIO3          IO         VDD3P3_RTC                IE           IE            IO MUX   RTC IO MUX    Analog
 9           GPIO4          IO         VDD3P3_RTC                                           IO MUX   RTC IO MUX    Analog
 10          GPIO5          IO         VDD3P3_RTC                                           IO MUX   RTC IO MUX    Analog
 11          GPIO6          IO         VDD3P3_RTC                                           IO MUX   RTC IO MUX    Analog
 12          GPIO7          IO         VDD3P3_RTC                                           IO MUX   RTC IO MUX    Analog
 13          GPIO8          IO         VDD3P3_RTC                                           IO MUX   RTC IO MUX    Analog
 14          GPIO9          IO         VDD3P3_RTC                             IE            IO MUX   RTC IO MUX    Analog
 15          GPIO10         IO         VDD3P3_RTC                             IE            IO MUX   RTC IO MUX    Analog
 16          GPIO11         IO         VDD3P3_RTC                             IE            IO MUX   RTC IO MUX    Analog
 17          GPIO12         IO         VDD3P3_RTC                             IE            IO MUX   RTC IO MUX    Analog
 18          GPIO13         IO         VDD3P3_RTC                             IE            IO MUX   RTC IO MUX    Analog
                                                                                                      Cont’d on next page



Espressif Systems                                       16                         ESP32-S3 Series Datasheet v2.2
                                          Submit Documentation Feedback
2 Pins


                                                            Cont’d from previous page
                                                                                     Pin Settings 6                   Pin Function Sets 1
 Pin No.       Pin Name           Pin Type      Pin Providing Power 2-5         At Reset     After Reset      IO MUX      RTC IO MUX        Analog
 19            GPIO14             IO            VDD3P3_RTC                                   IE               IO MUX      RTC IO MUX        Analog
 20            VDD3P3_RTC         Power
 21            XTAL_32K_P         IO            VDD3P3_RTC                                                    IO MUX      RTC IO MUX        Analog
 22            XTAL_32K_N         IO            VDD3P3_RTC                                                    IO MUX      RTC IO MUX        Analog
 23            GPIO17             IO            VDD3P3_RTC                                   IE               IO MUX      RTC IO MUX        Analog
 24            GPIO18             IO            VDD3P3_RTC                                   IE               IO MUX      RTC IO MUX        Analog
 25            GPIO19             IO            VDD3P3_RTC                                                    IO MUX      RTC IO MUX        Analog
 26            GPIO20             IO            VDD3P3_RTC                      USB_PU       USB_PU           IO MUX      RTC IO MUX        Analog
 27            GPIO21             IO            VDD3P3_RTC                                                    IO MUX      RTC IO MUX
 28            SPICS1             IO            VDD_SPI                         WPU, IE      WPU, IE          IO MUX
 29            VDD_SPI            Power
 30            SPIHD              IO            VDD_SPI                         WPU, IE      WPU, IE          IO MUX
 31            SPIWP              IO            VDD_SPI                         WPU, IE      WPU, IE          IO MUX
 32            SPICS0             IO            VDD_SPI                         WPU, IE      WPU, IE          IO MUX
 33            SPICLK             IO            VDD_SPI                         WPU, IE      WPU, IE          IO MUX
 34            SPIQ               IO            VDD_SPI                         WPU, IE      WPU, IE          IO MUX
 35            SPID               IO            VDD_SPI                         WPU, IE      WPU, IE          IO MUX
 36            SPICLK_N           IO            VDD_SPI/VDD3P3_CPU              IE           IE               IO MUX
 37            SPICLK_P           IO            VDD_SPI/VDD3P3_CPU              IE           IE               IO MUX
 38            GPIO33             IO            VDD_SPI/VDD3P3_CPU                           IE               IO MUX
 39            GPIO34             IO            VDD_SPI/VDD3P3_CPU                           IE               IO MUX
 40            GPIO35             IO            VDD_SPI/VDD3P3_CPU                           IE               IO MUX
 41            GPIO36             IO            VDD_SPI/VDD3P3_CPU                           IE               IO MUX
 42            GPIO37             IO            VDD_SPI/VDD3P3_CPU                           IE               IO MUX
 43            GPIO38             IO            VDD3P3_CPU                                   IE               IO MUX
 44            MTCK               IO            VDD3P3_CPU                                   IE 7             IO MUX
 45            MTDO               IO            VDD3P3_CPU                                   IE               IO MUX
 46            VDD3P3_CPU         Power
 47            MTDI               IO            VDD3P3_CPU                                   IE               IO MUX
 48            MTMS               IO            VDD3P3_CPU                                   IE               IO MUX
 49            U0TXD              IO            VDD3P3_CPU                      WPU, IE      WPU, IE          IO MUX
 50            U0RXD              IO            VDD3P3_CPU                      WPU, IE      WPU, IE          IO MUX
 51            GPIO45             IO            VDD3P3_CPU                      WPD, IE      WPD, IE          IO MUX
 52            GPIO46             IO            VDD3P3_CPU                      WPD, IE      WPD, IE          IO MUX
 53            XTAL_N             Analog
 54            XTAL_P             Analog
 55            VDDA               Power
 56            VDDA               Power
 57            GND                Power

      1. Bold marks the pin function set in which a pin has its default function in the default boot mode. For more information about the
        boot mode，see Section 3.1 Chip Boot Mode Control.

  2. In column Pin Providing Power, regarding pins powered by VDD_SPI:
            • Power actually comes from the internal power rail supplying power to VDD_SPI. For details, see Section 2.5.2 Power
               Scheme.

  3. In column Pin Providing Power, regarding pins powered by VDD3P3_CPU / VDD_SPI:




Espressif Systems                                                    17                             ESP32-S3 Series Datasheet v2.2
                                                    Submit Documentation Feedback
2 Pins


         • Pin Providing Power (either VDD3P3_CPU or VDD_SPI) is decided by eFuse bit EFUSE_PIN_POWER_SELECTION (see
           ESP32-S3 Technical Reference Manual > Chapter eFuse Controller) and can be configured via the
           IO_MUX_PAD_POWER_CTRL bit (see ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO pins).

  4. For ESP32-S3R8V and ESP32-S3R16V chip, as the VDD_SPI voltage has been set to 1.8 V, the working voltage for pins SPICLK_N
     and SPICLK_P (GPIO47 and GPIO48) would also be 1.8 V, which is different from other GPIOs.

  5. The default drive strengths for each pin are as follows:
         • GPIO17 and GPIO18: 10 mA
         • GPIO19 and GPIO20: 40 mA
         • All other pins: 20 mA

  6. Column Pin Settings shows predefined settings at reset and after reset with the following abbreviations:
         • IE – input enabled
         • WPU – internal weak pull-up resistor enabled
         • WPD – internal weak pull-down resistor enabled
         • USB_PU – USB pull-up resistor enabled
              – By default, the USB function is enabled for USB pins (i.e., GPIO19 and GPIO20), and the pin pull-up is decided by the
                 USB pull-up. The USB pull-up is controlled by USB_SERIAL_JTAG_DP/DM_PULLUP and the pull-up resistor value is
                 controlled by USB_SERIAL_JTAG_PULLUP_VALUE. For details, see ESP32-S3 Technical Reference Manual > Chapter
                 USB Serial/JTAG Controller).
              – When the USB function is disabled, USB pins are used as regular GPIOs and the pin’s internal weak pull-up and
                 pull-down resistors are disabled by default (configurable by IO_MUX_FUN_
                 WPU/WPD). For details, see ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

   7. Depends on the value of EFUSE_DIS_PAD_JTAG
         • 0 - WPU is enabled
         • 1 - pin floating


Some pins have glitches during power-up. See details in Table 2-2.

                                           Table 2-2. Power-Up Glitches on Pins

           Pin                                  Glitch1                                     Typical Time Period (µs)
           GPIO1                                Low-level glitch                                                      60
           GPIO2                                Low-level glitch                                                      60
           GPIO3                                Low-level glitch                                                      60
           GPIO4                                Low-level glitch                                                      60
           GPIO5                                Low-level glitch                                                      60
           GPIO6                                Low-level glitch                                                      60
           GPIO7                                Low-level glitch                                                      60
           GPIO8                                Low-level glitch                                                      60
           GPIO9                                Low-level glitch                                                      60
           GPIO10                               Low-level glitch                                                      60
           GPIO11                               Low-level glitch                                                      60
           GPIO12                               Low-level glitch                                                      60
           GPIO13                               Low-level glitch                                                      60
           GPIO14                               Low-level glitch                                                      60
           XTAL_32K_P                           Low-level glitch                                                      60
           XTAL_32K_N                           Low-level glitch                                                      60
           GPIO17                               Low-level glitch                                                      60
                                                                                                Cont’d on next page



Espressif Systems                                                18                           ESP32-S3 Series Datasheet v2.2
                                                 Submit Documentation Feedback
2 Pins


                                    Table 2-2 – cont’d from previous page
          Pin                           Glitch1                           Typical Time Period (µs)
                                        Low-level glitch                                              60
          GPIO18
                                        High-level glitch                                             60
                                        Low-level glitch                                              60
          GPIO19
                                        High-level glitch2                                            60
                                        Pull-down glitch                                              60
          GPIO20
                                        High-level glitch2                                            60
          1 Low-level glitch: the pin is at a low level output status during the time period;
            High-level glitch: the pin is at a high level output status during the time period;
            Pull-down glitch: the pin is at an internal weak pulled-down status during the time period;
            Pull-up glitch: the pin is at an internal weak pulled-up status during the time period.
            Please refer to Table 5-4 DC Characteristics (3.3 V, 25 °C) for detailed parameters about
           low/high-level and pull-down/up.
          2 GPIO19 and GPIO20 pins both have two high-level glitches during chip power-up, each
            lasting for about 60 µs. The total duration for the glitches and the delay are 3.2 ms and
            2 ms respectively for GPIO19 and GPIO20.




Espressif Systems                                      19                       ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
```
