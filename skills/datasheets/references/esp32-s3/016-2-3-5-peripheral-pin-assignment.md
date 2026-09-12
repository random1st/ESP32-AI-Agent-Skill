---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "2.3.5 Peripheral Pin Assignment"
pdf_pages: 26-27
retrieved: 2026-09-12
redistribute: false
---

# 2.3.5 Peripheral Pin Assignment

```text
2 Pins



2.3.5 Peripheral Pin Assignment
Table 2-9 Peripheral Pin Assignment highlights which pins can be assigned to each peripheral interface
according to the following priorities:

   • Priority 1 (P1) : Fixed pins connected directly to peripheral signals via IO MUX or RTC IO MUX.
      If a peripheral interface does not have priority 1 pins, such as UART2, it can be assigned to any GPIO pins
      from priority 2 to priority 4.

   • Any GPIO pins mapping to peripheral signals via GPIO Matrix, can be priority 2, 3, or 4.

          – Priority 2 (P2) : GPIO pins can be freely used without restrictions.

          – Priority 3 (P3) : GPIO pins should be used with caution, as they may conflict with the following
            important functions described in Section 2.3.4 Restrictions for GPIOs and RTC_GPIOs:

              * GPIO0, GPIO3, GPIO45, GPIO46 : Strapping pins.

              * GPIO19, GPIO20 : USB Serial/JTAG interface.

              * GPIO39, GPIO40, GPIO41, GPIO42 : JTAG interface.

              * GPIO43, GPIO44 : UART0 interface.

              * GPIO33, GPIO34, GPIO35, GPIO36, GPIO37 : The higher 4 bits data line interface and DQS
                 interface for the SPI0/1 interface in 8-line SPI mode, and can be GPIO pins if the chip is not
                 connected to flash or PSRAM in 8-line SPI mode.

          – Priority 4 (P4) : GPIO pins already allocated or not recommended for use, as described in Section
            2.3.4 Restrictions for GPIOs and RTC_GPIOs:

              * GPIO26, GPIO27, GPIO28, GPIO29, GPIO30, GPIO31, GPIO32 : SPI0/1 interface connected to
                 the in-package flash and PSRAM, or recommended for the off-package flash and PSRAM.

      If a peripheral interface does not have priority 2 to 4 pins, such as USB Serial/JTAG, it means it can be
      assigned only to priority 1 pins.

  Note:

      • For details about which peripheral signals are connected to IO MUX or RTC IO MUX pins, please refer to Section
          2.3.1 IO MUX Functions or Section 2.3.2 RTC Functions.

      • For details about which peripheral signals can be assigned to GPIO pins, please refer to
          ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix > Section Peripheral Signal List.




Espressif Systems                                          26                        ESP32-S3 Series Datasheet v2.2
                                            Submit Documentation Feedback
                                                                                                                                                                                                                           Table 2-9. Peripheral Pin Assignment




                                Espressif Systems
                                                                 Pin No. Pin Name
                                                                 1          LNA_IN
                                                                                            USB Serial/JTAG Full-speed USB OTG JTAG           ADC1             ADC2            Touch Sensor UART0           UART1         SPI0/1 (recommended) SPI0/1 (alternative)        SPI2 (recommended) SPI2 (alternative) UART2      I2C          TWAI         LED PWM      I2S          LCD and Camera SPI3         SD/MMC       MCPWM        RMT          PCNT
                                                                                                                                                                                                                                                                                                                                                                                                                                                                2 Pins
                                                                 2          VDD3P3
                                                                 3          VDD3P3
                                                                 4          CHIP_PU
                                                                 5          GPIO0                                                                                                             GPIO0 (P3)    GPIO0 (P3)    GPIO0 (P3)                 GPIO0 (P3)            GPIO0 (P3)          GPIO0 (P3)      GPIO0 (P3)   GPIO0 (P3)   GPIO0 (P3)   GPIO0 (P3)   GPIO0 (P3)   GPIO0 (P3)     GPIO0 (P3)   GPIO0 (P3)   GPIO0 (P3)   GPIO0 (P3)   GPIO0 (P3)
                                                                 6          GPIO1                                                             ADC1_CH0 (P1)                    TOUCH1 (P1)    GPIO1 (P2)    GPIO1 (P2)    GPIO1 (P2)                 GPIO1 (P2)            GPIO1 (P2)          GPIO1 (P2)      GPIO1 (P2)   GPIO1 (P2)   GPIO1 (P2)   GPIO1 (P2)   GPIO1 (P2)   GPIO1 (P2)     GPIO1 (P2)   GPIO1 (P2)   GPIO1 (P2)   GPIO1 (P2)   GPIO1 (P2)
                                                                 7          GPIO2                                                             ADC1_CH1 (P1)                    TOUCH2 (P1) GPIO2 (P2)       GPIO2 (P2)    GPIO2 (P2)                 GPIO2 (P2)            GPIO2 (P2)          GPIO2 (P2)      GPIO2 (P2)   GPIO2 (P2)   GPIO2 (P2)   GPIO2 (P2)   GPIO2 (P2)   GPIO2 (P2)     GPIO2 (P2)   GPIO2 (P2)   GPIO2 (P2)   GPIO2 (P2)   GPIO2 (P2)
                                                                 8          GPIO3                                                             ADC1_CH2 (P1)                    TOUCH3 (P1) GPIO3 (P3)       GPIO3 (P3)    GPIO3 (P3)                 GPIO3 (P3)            GPIO3 (P3)          GPIO3 (P3)      GPIO3 (P3)   GPIO3 (P3)   GPIO3 (P3)   GPIO3 (P3)   GPIO3 (P3)   GPIO3 (P3)     GPIO3 (P3)   GPIO3 (P3)   GPIO3 (P3)   GPIO3 (P3)   GPIO3 (P3)
                                                                 9          GPIO4                                                             ADC1_CH3 (P1)                    TOUCH4 (P1) GPIO4 (P2)       GPIO4 (P2)    GPIO4 (P2)                 GPIO4 (P2)            GPIO4 (P2)          GPIO4 (P2)      GPIO4 (P2)   GPIO4 (P2)   GPIO4 (P2)   GPIO4 (P2)   GPIO4 (P2)   GPIO4 (P2)     GPIO4 (P2)   GPIO4 (P2)   GPIO4 (P2)   GPIO4 (P2)   GPIO4 (P2)
                                                                 10         GPIO5                                                             ADC1_CH4 (P1)                    TOUCH5 (P1) GPIO5 (P2)       GPIO5 (P2)    GPIO5 (P2)                 GPIO5 (P2)            GPIO5 (P2)          GPIO5 (P2)      GPIO5 (P2)   GPIO5 (P2)   GPIO5 (P2)   GPIO5 (P2)   GPIO5 (P2)   GPIO5 (P2)     GPIO5 (P2)   GPIO5 (P2)   GPIO5 (P2)   GPIO5 (P2)   GPIO5 (P2)
                                                                 11         GPIO6                                                             ADC1_CH5 (P1)                    TOUCH6 (P1) GPIO6 (P2)       GPIO6 (P2)    GPIO6 (P2)                 GPIO6 (P2)            GPIO6 (P2)          GPIO6 (P2)      GPIO6 (P2)   GPIO6 (P2)   GPIO6 (P2)   GPIO6 (P2)   GPIO6 (P2)   GPIO6 (P2)     GPIO6 (P2)   GPIO6 (P2)   GPIO6 (P2)   GPIO6 (P2)   GPIO6 (P2)
                                                                 12         GPIO7                                                             ADC1_CH6 (P1)                    TOUCH7 (P1) GPIO7 (P2)       GPIO7 (P2)    GPIO7 (P2)                 GPIO7 (P2)            GPIO7 (P2)          GPIO7 (P2)      GPIO7 (P2)   GPIO7 (P2)   GPIO7 (P2)   GPIO7 (P2)   GPIO7 (P2)   GPIO7 (P2)     GPIO7 (P2)   GPIO7 (P2)   GPIO7 (P2)   GPIO7 (P2)   GPIO7 (P2)
                                                                 13         GPIO8                                                             ADC1_CH7 (P1)                    TOUCH8 (P1) GPIO8 (P2)       GPIO8 (P2)    GPIO8 (P2)                 SUBSPICS1 (P1)        GPIO8 (P2)          GPIO8 (P2)      GPIO8 (P2)   GPIO8 (P2)   GPIO8 (P2)   GPIO8 (P2)   GPIO8 (P2)   GPIO8 (P2)     GPIO8 (P2)   GPIO8 (P2)   GPIO8 (P2)   GPIO8 (P2)   GPIO8 (P2)
                                                                 14         GPIO9                                                             ADC1_CH8 (P1)                    TOUCH9 (P1) GPIO9 (P2)       GPIO9 (P2)    GPIO9 (P2)                 SUBSPIHD (P1)         FSPIHD (P1)         GPIO9 (P2)      GPIO9 (P2)   GPIO9 (P2)   GPIO9 (P2)   GPIO9 (P2)   GPIO9 (P2)   GPIO9 (P2)     GPIO9 (P2)   GPIO9 (P2)   GPIO9 (P2)   GPIO9 (P2)   GPIO9 (P2)
                                                                 15         GPIO10                                                            ADC1_CH9 (P1)                    TOUCH10 (P1) GPIO10 (P2) GPIO10 (P2) GPIO10 (P2)                      SUBSPICS0 (P1)        FSPICS0 (P1)        FSPIIO4 (P1)    GPIO10 (P2) GPIO10 (P2) GPIO10 (P2) GPIO10 (P2) GPIO10 (P2) GPIO10 (P2)         GPIO10 (P2) GPIO10 (P2) GPIO10 (P2) GPIO10 (P2) GPIO10 (P2)
                                                                 16         GPIO11                                                                             ADC2_CH0 (P1) TOUCH11 (P1) GPIO11 (P2) GPIO11 (P2) GPIO11 (P2)                        SUBSPID (P1)          FSPID (P1)          FSPIIO5 (P1)    GPIO11 (P2) GPIO11 (P2) GPIO11 (P2) GPIO11 (P2) GPIO11 (P2) GPIO11 (P2)         GPIO11 (P2) GPIO11 (P2) GPIO11 (P2) GPIO11 (P2) GPIO11 (P2)
                                                                 17         GPIO12                                                                             ADC2_CH1 (P1) TOUCH12 (P1) GPIO12 (P2) GPIO12 (P2) GPIO12 (P2)                        SUBSPICLK (P1)        FSPICLK (P1)        FSPIIO6 (P1)    GPIO12 (P2) GPIO12 (P2) GPIO12 (P2) GPIO12 (P2) GPIO12 (P2) GPIO12 (P2)         GPIO12 (P2) GPIO12 (P2) GPIO12 (P2) GPIO12 (P2) GPIO12 (P2)
                                                                 18         GPIO13                                                                             ADC2_CH2 (P1) TOUCH13 (P1) GPIO13 (P2) GPIO13 (P2) GPIO13 (P2)                        SUBSPIQ (P1)          FSPIQ (P1)          FSPIIO7 (P1)    GPIO13 (P2) GPIO13 (P2) GPIO13 (P2) GPIO13 (P2) GPIO13 (P2) GPIO13 (P2)         GPIO13 (P2) GPIO13 (P2) GPIO13 (P2) GPIO13 (P2) GPIO13 (P2)
                                                                 19         GPIO14                                                                             ADC2_CH3 (P1) TOUCH14 (P1) GPIO14 (P2) GPIO14 (P2) GPIO14 (P2)                        SUBSPIWP (P1)         FSPIWP (P1)         FSPIDQS (P1)    GPIO14 (P2) GPIO14 (P2) GPIO14 (P2) GPIO14 (P2) GPIO14 (P2) GPIO14 (P2)         GPIO14 (P2) GPIO14 (P2) GPIO14 (P2) GPIO14 (P2) GPIO14 (P2)
                                                                 20         VDD3P3_RTC
                                                                 21         XTAL_32K_P                                                                         ADC2_CH4 (P1)                  U0RTS (P1)    GPIO15 (P2) GPIO15 (P2)                  GPIO15 (P2)           GPIO15 (P2)         GPIO15 (P2)     GPIO15 (P2) GPIO15 (P2) GPIO15 (P2) GPIO15 (P2) GPIO15 (P2) GPIO15 (P2)         GPIO15 (P2) GPIO15 (P2) GPIO15 (P2) GPIO15 (P2) GPIO15 (P2)
                                                                 22         XTAL_32K_N                                                                         ADC2_CH5 (P1)                  U0CTS (P1)    GPIO16 (P2) GPIO16 (P2)                  GPIO16 (P2)           GPIO16 (P2)         GPIO16 (P2)     GPIO16 (P2) GPIO16 (P2) GPIO16 (P2) GPIO16 (P2) GPIO16 (P2) GPIO16 (P2)         GPIO16 (P2) GPIO16 (P2) GPIO16 (P2) GPIO16 (P2) GPIO16 (P2)
                                                                 23         GPIO17                                                                             ADC2_CH6 (P1)                  GPIO17 (P2) U1TXD (P1)      GPIO17 (P2)                GPIO17 (P2)           GPIO17 (P2)         GPIO17 (P2)     GPIO17 (P2) GPIO17 (P2) GPIO17 (P2) GPIO17 (P2) GPIO17 (P2) GPIO17 (P2)         GPIO17 (P2) GPIO17 (P2) GPIO17 (P2) GPIO17 (P2) GPIO17 (P2)
                                                                 24         GPIO18                                                                             ADC2_CH7 (P1)                  GPIO18 (P2) U1RXD (P1)      GPIO18 (P2)                GPIO18 (P2)           GPIO18 (P2)         GPIO18 (P2)     GPIO18 (P2) GPIO18 (P2) GPIO18 (P2) GPIO18 (P2) GPIO18 (P2) GPIO18 (P2)         GPIO18 (P2) GPIO18 (P2) GPIO18 (P2) GPIO18 (P2) GPIO18 (P2)




Submit Documentation Feedback
                                                                 25         GPIO19          USB_D- (P1)      USB_D- (P1)                                       ADC2_CH8 (P1)                  GPIO19 (P3) U1RTS (P1)      GPIO19 (P3)                GPIO19 (P3)           GPIO19 (P3)         GPIO19 (P3)     GPIO19 (P3) GPIO19 (P3) GPIO19 (P3) GPIO19 (P3) GPIO19 (P3) GPIO19 (P3)         GPIO19 (P3) GPIO19 (P3) GPIO19 (P3) GPIO19 (P3) GPIO19 (P3)
                                                                 26         GPIO20          USB_D+ (P1)      USB_D+ (P1)                                       ADC2_CH9 (P1)                  GPIO20 (P3) U1CTS (P1)      GPIO20 (P3)                GPIO20 (P3)           GPIO20 (P3)         GPIO20 (P3)     GPIO20 (P3) GPIO20 (P3) GPIO20 (P3) GPIO20 (P3) GPIO20 (P3) GPIO20 (P3)         GPIO20 (P3) GPIO20 (P3) GPIO20 (P3) GPIO20 (P3) GPIO20 (P3)
                                                                 27         GPIO21          GPIO21 (P2)      GPIO21 (P2)                                                                      GPIO21 (P2) GPIO21 (P2) GPIO21 (P2)                    GPIO21 (P2)           GPIO21 (P2)         GPIO21 (P2)     GPIO21 (P2) GPIO21 (P2) GPIO21 (P2) GPIO21 (P2) GPIO21 (P2) GPIO21 (P2)         GPIO21 (P2) GPIO21 (P2) GPIO21 (P2) GPIO21 (P2) GPIO21 (P2)
                                                                 28         SPICS1                                                                                                            GPIO26 (P4) GPIO26 (P4) SPICS1 (P1)                    GPIO26 (P4)           GPIO26 (P4)         GPIO26 (P4)     GPIO26 (P4) GPIO26 (P4) GPIO26 (P4) GPIO26 (P4) GPIO26 (P4) GPIO26 (P4)         GPIO26 (P4) GPIO26 (P4) GPIO26 (P4) GPIO26 (P4) GPIO26 (P4)
                                                                 29         VDD_SPI
                                                                 30         SPIHD                                                                                                             GPIO27 (P4) GPIO27 (P4) SPIHD (P1)                     GPIO27 (P4)           GPIO27 (P4)         GPIO27 (P4)     GPIO27 (P4) GPIO27 (P4) GPIO27 (P4) GPIO27 (P4) GPIO27 (P4) GPIO27 (P4)         GPIO27 (P4) GPIO27 (P4) GPIO27 (P4) GPIO27 (P4) GPIO27 (P4)
                                                                 31         SPIWP                                                                                                             GPIO28 (P4) GPIO28 (P4) SPIWP (P1)                     GPIO28 (P4)           GPIO28 (P4)         GPIO28 (P4)     GPIO28 (P4) GPIO28 (P4) GPIO28 (P4) GPIO28 (P4) GPIO28 (P4) GPIO28 (P4)         GPIO28 (P4) GPIO28 (P4) GPIO28 (P4) GPIO28 (P4) GPIO28 (P4)
                                                                 32         SPICS0                                                                                                            GPIO29 (P4) GPIO29 (P4) SPICS0 (P1)                    GPIO29 (P4)           GPIO29 (P4)         GPIO29 (P4)     GPIO29 (P4) GPIO29 (P4) GPIO29 (P4) GPIO29 (P4) GPIO29 (P4) GPIO29 (P4)         GPIO29 (P4) GPIO29 (P4) GPIO29 (P4) GPIO29 (P4) GPIO29 (P4)
                                                                 33         SPICLK                                                                                                            GPIO30 (P4) GPIO30 (P4) SPICLK (P1)                    GPIO30 (P4)           GPIO30 (P4)         GPIO30 (P4)     GPIO30 (P4) GPIO30 (P4) GPIO30 (P4) GPIO30 (P4) GPIO30 (P4) GPIO30 (P4)         GPIO30 (P4) GPIO30 (P4) GPIO30 (P4) GPIO30 (P4) GPIO30 (P4)
                                                                 34         SPIQ                                                                                                              GPIO31 (P4) GPIO31 (P4) SPIQ (P1)                      GPIO31 (P4)           GPIO31 (P4)         GPIO31 (P4)     GPIO31 (P4) GPIO31 (P4) GPIO31 (P4) GPIO31 (P4) GPIO31 (P4) GPIO31 (P4)         GPIO31 (P4) GPIO31 (P4) GPIO31 (P4) GPIO31 (P4) GPIO31 (P4)

                                27                               35
                                                                 36
                                                                            SPID
                                                                            SPICLK_N
                                                                                                                                                                                              GPIO32 (P4) GPIO32 (P4) SPID (P1)
                                                                                                                                                                                              GPIO48 (P2) GPIO48 (P2) SPICLK_N_DIFF (P1)
                                                                                                                                                                                                                                                     GPIO32 (P4)           GPIO32 (P4)
                                                                                                                                                                                                                                                     SUBSPICLK_N_DIFF (P1) GPIO48 (P2)
                                                                                                                                                                                                                                                                                               GPIO32 (P4)
                                                                                                                                                                                                                                                                                               GPIO48 (P2)
                                                                                                                                                                                                                                                                                                               GPIO32 (P4) GPIO32 (P4) GPIO32 (P4) GPIO32 (P4) GPIO32 (P4) GPIO32 (P4)
                                                                                                                                                                                                                                                                                                               GPIO48 (P2) GPIO48 (P2) GPIO48 (P2) GPIO48 (P2) GPIO48 (P2) GPIO48 (P2)
                                                                                                                                                                                                                                                                                                                                                                                               GPIO32 (P4) GPIO32 (P4) GPIO32 (P4) GPIO32 (P4) GPIO32 (P4)
                                                                                                                                                                                                                                                                                                                                                                                               GPIO48 (P2) GPIO48 (P2) GPIO48 (P2) GPIO48 (P2) GPIO48 (P2)
                                                                 37         SPICLK_P                                                                                                          GPIO47 (P2) GPIO47 (P2) SPICLK_P_DIFF (P1)             SUBSPICLK_P_DIFF (P1) GPIO47 (P2)         GPIO47 (P2)     GPIO47 (P2) GPIO47 (P2) GPIO47 (P2) GPIO47 (P2) GPIO47 (P2) GPIO47 (P2)         GPIO47 (P2) GPIO47 (P2) GPIO47 (P2) GPIO47 (P2) GPIO47 (P2)
                                                                 38         GPIO33                                                                                                            GPIO33 (P3) GPIO33 (P3) SPIIO4 (P1)                    SUBSPIHD (P1)         GPIO33 (P3)         FSPIHD (P1)     GPIO33 (P3) GPIO33 (P3) GPIO33 (P3) GPIO33 (P3) GPIO33 (P3) GPIO33 (P3)         GPIO33 (P3) GPIO33 (P3) GPIO33 (P3) GPIO33 (P3) GPIO33 (P3)
                                                                 39         GPIO34                                                                                                            GPIO34 (P3) GPIO34 (P3) SPIIO5 (P1)                    SUBSPICS0 (P1)        GPIO34 (P3)         FSPICS0 (P1)    GPIO34 (P3) GPIO34 (P3) GPIO34 (P3) GPIO34 (P3) GPIO34 (P3) GPIO34 (P3)         GPIO34 (P3) GPIO34 (P3) GPIO34 (P3) GPIO34 (P3) GPIO34 (P3)
                                                                 40         GPIO35                                                                                                            GPIO35 (P3) GPIO35 (P3) SPIIO6 (P1)                    SUBSPID (P1)          GPIO35 (P3)         FSPID (P1)      GPIO35 (P3) GPIO35 (P3) GPIO35 (P3) GPIO35 (P3) GPIO35 (P3) GPIO35 (P3)         GPIO35 (P3) GPIO35 (P3) GPIO35 (P3) GPIO35 (P3) GPIO35 (P3)
                                                                 41         GPIO36                                                                                                            GPIO36 (P3) GPIO36 (P3) SPIIO7 (P1)                    SUBSPICLK (P1)        GPIO36 (P3)         FSPICLK (P1)    GPIO36 (P3) GPIO36 (P3) GPIO36 (P3) GPIO36 (P3) GPIO36 (P3) GPIO36 (P3)         GPIO36 (P3) GPIO36 (P3) GPIO36 (P3) GPIO36 (P3) GPIO36 (P3)
                                                                 42         GPIO37                                                                                                            GPIO37 (P3) GPIO37 (P3) SPIDQS (P1)                    SUBSPIQ (P1)          GPIO37 (P3)         FSPIQ (P1)      GPIO37 (P3) GPIO37 (P3) GPIO37 (P3) GPIO37 (P3) GPIO37 (P3) GPIO37 (P3)         GPIO37 (P3) GPIO37 (P3) GPIO37 (P3) GPIO37 (P3) GPIO37 (P3)
                                                                 43         GPIO38          GPIO38 (P2)      GPIO38 (P2)                                                                      GPIO38 (P2) GPIO38 (P2) GPIO38 (P2)                    SUBSPIWP (P1)         GPIO38 (P2)         FSPIWP (P1)     GPIO38 (P2) GPIO38 (P2) GPIO38 (P2) GPIO38 (P2) GPIO38 (P2) GPIO38 (P2)         GPIO38 (P2) GPIO38 (P2) GPIO38 (P2) GPIO38 (P2) GPIO38 (P2)
                                                                 44         MTCK            MTCK (P1)        MTCK (P1)            MTCK (P1)                                                   GPIO39 (P3) GPIO39 (P3) GPIO39 (P3)                    SUBSPICS1 (P1)        GPIO39 (P3)         GPIO39 (P3)     GPIO39 (P3) GPIO39 (P3) GPIO39 (P3) GPIO39 (P3) GPIO39 (P3) GPIO39 (P3)         GPIO39 (P3) GPIO39 (P3) GPIO39 (P3) GPIO39 (P3) GPIO39 (P3)
                                                                 45         MTDO            MTDO (P1)        MTDO (P1)            MTDO (P1)                                                   GPIO40 (P3) GPIO40 (P3) GPIO40 (P3)                    GPIO40 (P3)           GPIO40 (P3)         GPIO40 (P3)     GPIO40 (P3) GPIO40 (P3) GPIO40 (P3) GPIO40 (P3) GPIO40 (P3) GPIO40 (P3)         GPIO40 (P3) GPIO40 (P3) GPIO40 (P3) GPIO40 (P3) GPIO40 (P3)
                                                                 46         VDD3P3_CPU
                                                                 47         MTDI            MTDI (P1)        MTDI (P1)            MTDI (P1)                                                   GPIO41 (P3) GPIO41 (P3) GPIO41 (P3)                    GPIO41 (P3)           GPIO41 (P3)         GPIO41 (P3)     GPIO41 (P3) GPIO41 (P3) GPIO41 (P3) GPIO41 (P3) GPIO41 (P3) GPIO41 (P3)         GPIO41 (P3) GPIO41 (P3) GPIO41 (P3) GPIO41 (P3) GPIO41 (P3)
                                                                 48         MTMS            MTMS (P1)        MTMS (P1)            MTMS (P1)                                                   GPIO42 (P3) GPIO42 (P3) GPIO42 (P3)                    GPIO42 (P3)           GPIO42 (P3)         GPIO42 (P3)     GPIO42 (P3) GPIO42 (P3) GPIO42 (P3) GPIO42 (P3) GPIO42 (P3) GPIO42 (P3)         GPIO42 (P3) GPIO42 (P3) GPIO42 (P3) GPIO42 (P3) GPIO42 (P3)
                                                                 49         U0TXD                                                                                                             U0TXD (P1)    GPIO43 (P3) GPIO43 (P3)                  GPIO43 (P3)           GPIO43 (P3)         GPIO43 (P3)     GPIO43 (P3) GPIO43 (P3) GPIO43 (P3) GPIO43 (P3) GPIO43 (P3) GPIO43 (P3)         GPIO43 (P3) GPIO43 (P3) GPIO43 (P3) GPIO43 (P3) GPIO43 (P3)
                                                                 50         U0RXD                                                                                                             U0RXD (P1)    GPIO44 (P3) GPIO44 (P3)                  GPIO44 (P3)           GPIO44 (P3)         GPIO44 (P3)     GPIO44 (P3) GPIO44 (P3) GPIO44 (P3) GPIO44 (P3) GPIO44 (P3) GPIO44 (P3)         GPIO44 (P3) GPIO44 (P3) GPIO44 (P3) GPIO44 (P3) GPIO44 (P3)
                                                                 51         GPIO45                                                                                                            GPIO45 (P3) GPIO45 (P3) GPIO45 (P3)                    GPIO45 (P3)           GPIO45 (P3)         GPIO45 (P3)     GPIO45 (P3) GPIO45 (P3) GPIO45 (P3) GPIO45 (P3) GPIO45 (P3) GPIO45 (P3)         GPIO45 (P3) GPIO45 (P3) GPIO45 (P3) GPIO45 (P3) GPIO45 (P3)




                                ESP32-S3 Series Datasheet v2.2
                                                                 52         GPIO46                                                                                                            GPIO46 (P3) GPIO46 (P3) GPIO46 (P3)                    GPIO46 (P3)           GPIO46 (P3)         GPIO46 (P3)     GPIO46 (P3) GPIO46 (P3) GPIO46 (P3) GPIO46 (P3) GPIO46 (P3) GPIO46 (P3)         GPIO46 (P3) GPIO46 (P3) GPIO46 (P3) GPIO46 (P3) GPIO46 (P3)
                                                                 53         XTAL_N
                                                                 54         XTAL_P
                                                                 55         VDDA
                                                                 56         VDDA
                                                                 57         GND
                                                                     1 For USB Serial/JTAG and USB OTG, use USB_D- and USB_D+ when on internal PHY, and the USB_D- and USB_D+ can be swapped by configuring the USB_SERIAL_JTAG_EXCHG_PINS bit according to ESP32-S3 Technical Reference Manual; use other fixed pins when on external PHY. For how to select PHY, see ESP32-S3 Technical Reference Manual > USB Serial/JTAG Controller > Internal/External

                                                                      PHY Selection.
                                                                     2 Signals of UART0, UART1, SPI0/1, and SPI2 interfaces can be mapped to any GPIO pins through the GPIO Matrix, regardless of whether they are directly routed to   fixed pins   via IO MUX.
```
