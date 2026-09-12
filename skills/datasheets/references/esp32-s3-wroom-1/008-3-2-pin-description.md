---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "3.2 Pin Description"
pdf_pages: 10-12
retrieved: 2026-09-12
redistribute: false
---

# 3.2 Pin Description

```text
3 Pin Definitions



3       Pin Definitions

3.1     Pin Layout
The pin diagram below shows the approximate location of pins on the module. For the actual diagram drawn to
scale, please refer to Figure 10.1 Module Dimensions.




                                                             Keepout Zone




               GND         1                                                                                              40   GND

                3V3        2                                                                                              39   IO1

                 EN        3                                                                                              38   IO2

                 IO4       4                                                                                              37   TXD0

                 IO5       5                                                                                              36   RXD0

                 IO6       6                         GND     GND      GND                                                 35   IO42

                 IO7       7                         GND
                                                              41
                                                             GND
                                                                      GND                                                 34   IO41

               IO15        8                         GND     GND      GND                                                 33   IO40

               IO16        9                                                                                              32   IO39

               IO17       10                                                                                              31   IO38

               IO18        11                                                                                             30   IO37

                 IO8      12                                                                                              29   IO36

               IO19       13                                                                                              28   IO35

               IO20       14    15    16     17     18     19      20          21     22     23      24     25     26     27   IO0



                                IO3   IO46   IO9    IO10   IO11    IO12        IO13   IO14   IO21    IO47   IO48   IO45

                                               Figure 3-1. Pin Layout (Top View)



    Note:
    The pin diagram is applicable to ESP32-S3-WROOM-1 and ESP32-S3-WROOM-1U, but the latter has no antenna keepout
    zone. To learn more about the keepout zone for module’s antenna on the base board, please refer to
    ESP32-S3 Hardware Design Guidelines > Section General Principles of PCB Layout for Modules.




Espressif Systems                                                         10                        ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                                   Submit Documentation Feedback
3 Pin Definitions



3.2     Pin Description
The module has 41 pins. See pin definitions in Table 3-1 Pin Definitions.

For explanations of pin names and function names, as well as configurations of peripheral pins, please refer to
ESP32-S3 Series Datasheet.

                                            Table 3-1. Pin Definitions

      Name      No.    Type a    Function
      GND         1       P      GND
      3V3        2        P      Power supply
                                 High: on, enables the chip.
      EN         3        I      Low: off, the chip powers off.
                                 Note: Do not leave the EN pin floating.
      IO4        4      I/O/T    RTC_GPIO4, GPIO4, TOUCH4, ADC1_CH3
      IO5        5      I/O/T    RTC_GPIO5, GPIO5, TOUCH5, ADC1_CH4
      IO6        6      I/O/T    RTC_GPIO6, GPIO6, TOUCH6, ADC1_CH5
      IO7         7     I/O/T    RTC_GPIO7, GPIO7, TOUCH7, ADC1_CH6
      IO15       8      I/O/T    RTC_GPIO15, GPIO15, U0RTS, ADC2_CH4, XTAL_32K_P
      IO16       9      I/O/T    RTC_GPIO16, GPIO16, U0CTS, ADC2_CH5, XTAL_32K_N
      IO17       10     I/O/T    RTC_GPIO17, GPIO17, U1TXD, ADC2_CH6
      IO18       11     I/O/T    RTC_GPIO18, GPIO18, U1RXD, ADC2_CH7, CLK_OUT3
      IO8        12     I/O/T    RTC_GPIO8, GPIO8, TOUCH8, ADC1_CH7, SUBSPICS1
      IO19       13     I/O/T    RTC_GPIO19, GPIO19, U1RTS, ADC2_CH8, CLK_OUT2, USB_D-
      IO20       14     I/O/T    RTC_GPIO20, GPIO20, U1CTS, ADC2_CH9, CLK_OUT1, USB_D+
      IO3        15     I/O/T    RTC_GPIO3, GPIO3, TOUCH3, ADC1_CH2
      IO46       16     I/O/T    GPIO46
      IO9        17     I/O/T    RTC_GPIO9, GPIO9, TOUCH9, ADC1_CH8, FSPIHD, SUBSPIHD
                                 RTC_GPIO10, GPIO10, TOUCH10, ADC1_CH9, FSPICS0, FSPIIO4,
      IO10       18     I/O/T
                                 SUBSPICS0
      IO11       19     I/O/T    RTC_GPIO11, GPIO11, TOUCH11, ADC2_CH0, FSPID, FSPIIO5, SUBSPID
                                 RTC_GPIO12, GPIO12, TOUCH12, ADC2_CH1, FSPICLK, FSPIIO6,
      IO12       20     I/O/T
                                 SUBSPICLK
      IO13       21     I/O/T    RTC_GPIO13, GPIO13, TOUCH13, ADC2_CH2, FSPIQ, FSPIIO7, SUBSPIQ
                                 RTC_GPIO14, GPIO14, TOUCH14, ADC2_CH3, FSPIWP, FSPIDQS,
      IO14       22     I/O/T
                                 SUBSPIWP
      IO21       23     I/O/T    RTC_GPIO21, GPIO21
      IO47 c     24     I/O/T    SPICLK_P_DIFF,GPIO47, SUBSPICLK_P_DIFF
      IO48 c     25     I/O/T    SPICLK_N_DIFF,GPIO48, SUBSPICLK_N_DIFF
      IO45       26     I/O/T    GPIO45
      IO0        27     I/O/T    RTC_GPIO0, GPIO0
      IO35 b     28     I/O/T    SPIIO6, GPIO35, FSPID, SUBSPID
      IO36 b     29     I/O/T    SPIIO7, GPIO36, FSPICLK, SUBSPICLK
      IO37 b     30     I/O/T    SPIDQS, GPIO37, FSPIQ, SUBSPIQ
      IO38       31     I/O/T    GPIO38, FSPIWP, SUBSPIWP
                                                                                      Cont’d on next page


Espressif Systems                                       11               ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                          Submit Documentation Feedback
3 Pin Definitions


                                   Table 3-1 – cont’d from previous page
      Name     No.     Type a   Function
      IO39      32     I/O/T    MTCK, GPIO39, CLK_OUT3, SUBSPICS1
      IO40      33     I/O/T    MTDO, GPIO40, CLK_OUT2
      IO41      34     I/O/T    MTDI, GPIO41, CLK_OUT1
      IO42      35     I/O/T    MTMS, GPIO42
      RXD0      36     I/O/T    U0RXD, GPIO44, CLK_OUT2
      TXD0      37     I/O/T    U0TXD, GPIO43, CLK_OUT1
      IO2       38     I/O/T    RTC_GPIO2, GPIO2, TOUCH2, ADC1_CH1
      IO1       39     I/O/T    RTC_GPIO1, GPIO1, TOUCH1, ADC1_CH0
      GND       40       P      GND
      EPAD      41       P      GND
      a P: power supply; I: input; O: output; T: high impedance. Pin functions in bold font are the default
       pin functions. For pin 28 ∼ 30, the default function is decided by eFuse bit.
      b For modules with Octal SPI PSRAM, i.e., modules embedded with ESP32-S3R8 or ESP32-S3R16V,
        pins IO35, IO36, and IO37 are connected to the Octal SPI PSRAM and are not available for other
        uses.
      c For modules embedded with ESP32-S3R16V, as the VDD_SPI voltage of the ESP32-S3R16V chip
        is set to 1.8 V, the working voltage for GPIO47 and GPIO48 is also 1.8 V, which is different from
        other GPIOs.




Espressif Systems                                     12              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                        Submit Documentation Feedback
```
