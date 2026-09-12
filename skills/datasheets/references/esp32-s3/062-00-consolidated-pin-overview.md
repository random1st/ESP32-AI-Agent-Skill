---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "Consolidated Pin Overview"
pdf_pages: 79
retrieved: 2026-09-12
redistribute: false
---

# Consolidated Pin Overview

```text
                                Espressif Systems




                                                                                                                                                                                                                                                                                                                                                        ESP32-S3 Consolidated Pin Overview
                                                                 ESP32-S3 Consolidated Pin Overview
                                                                                                                                                                                       Table 7-1. Consolidated Pin Overview
                                                                                                                                                Pin Settings                 RTC IO MUX Function                 Analog Function                                                     IO MUX Function
                                                                  Pin No.     Pin Name          Pin Type     Pin Providing Power          At Reset     After Reset      F0             F3                   F0             F1         F0              Type     F1       Type    F2                     Type     F3          Type     F4        Type
                                                                  1           LNA_IN            Analog
                                                                  2           VDD3P3            Power
                                                                  3           VDD3P3            Power
                                                                  4           CHIP_PU           Analog       VDD3P3_RTC
                                                                  5           GPIO0             IO           VDD3P3_RTC                   WPU, IE      WPU, IE          RTC_GPIO0           sar_i2c_scl_0                             GPIO0           I/O/T    GPIO0    I/O/T
                                                                  6           GPIO1             IO           VDD3P3_RTC                   IE           IE               RTC_GPIO1           sar_i2c_sda_0   TOUCH1         ADC1_CH0   GPIO1           I/O/T    GPIO1    I/O/T
                                                                  7           GPIO2             IO           VDD3P3_RTC                   IE           IE               RTC_GPIO2           sar_i2c_scl_1   TOUCH2         ADC1_CH1   GPIO2           I/O/T    GPIO2    I/O/T
                                                                  8           GPIO3             IO           VDD3P3_RTC                   IE           IE               RTC_GPIO3           sar_i2c_sda_1   TOUCH3         ADC1_CH2   GPIO3           I/O/T    GPIO3    I/O/T
                                                                  9           GPIO4             IO           VDD3P3_RTC                                                 RTC_GPIO4                           TOUCH4         ADC1_CH3   GPIO4           I/O/T    GPIO4    I/O/T
                                                                  10          GPIO5             IO           VDD3P3_RTC                                                 RTC_GPIO5                           TOUCH5         ADC1_CH4   GPIO5           I/O/T    GPIO5    I/O/T
                                                                  11          GPIO6             IO           VDD3P3_RTC                                                 RTC_GPIO6                           TOUCH6         ADC1_CH5   GPIO6           I/O/T    GPIO6    I/O/T
                                                                  12          GPIO7             IO           VDD3P3_RTC                                                 RTC_GPIO7                           TOUCH7         ADC1_CH6   GPIO7           I/O/T    GPIO7    I/O/T
                                                                  13          GPIO8             IO           VDD3P3_RTC                                                 RTC_GPIO8                           TOUCH8         ADC1_CH7   GPIO8           I/O/T    GPIO8    I/O/T                                   SUBSPICS1   O/T
                                                                  14          GPIO9             IO           VDD3P3_RTC                                IE               RTC_GPIO9                           TOUCH9         ADC1_CH8   GPIO9           I/O/T    GPIO9    I/O/T                                   SUBSPIHD    I1/O/T   FSPIHD    I1/O/T
                                                                  15          GPIO10            IO           VDD3P3_RTC                                IE               RTC_GPIO10                          TOUCH10        ADC1_CH9   GPIO10          I/O/T    GPIO10   I/O/T   FSPIIO4                I1/O/T   SUBSPICS0   O/T      FSPICS0   I1/O/T
                                                                  16          GPIO11            IO           VDD3P3_RTC                                IE               RTC_GPIO11                          TOUCH11        ADC2_CH0   GPIO11          I/O/T    GPIO11   I/O/T   FSPIIO5                I1/O/T   SUBSPID     I1/O/T   FSPID     I1/O/T
                                                                  17          GPIO12            IO           VDD3P3_RTC                                IE               RTC_GPIO12                          TOUCH12        ADC2_CH1   GPIO12          I/O/T    GPIO12   I/O/T   FSPIIO6                I1/O/T   SUBSPICLK   O/T      FSPICLK   I1/O/T




Submit Documentation Feedback
                                                                  18          GPIO13            IO           VDD3P3_RTC                                IE               RTC_GPIO13                          TOUCH13        ADC2_CH2   GPIO13          I/O/T    GPIO13   I/O/T   FSPIIO7                I1/O/T   SUBSPIQ     I1/O/T   FSPIQ     I1/O/T
                                                                  19          GPIO14            IO           VDD3P3_RTC                                IE               RTC_GPIO14                          TOUCH14        ADC2_CH3   GPIO14          I/O/T    GPIO14   I/O/T   FSPIDQS                O/T      SUBSPIWP    I1/O/T   FSPIWP    I1/O/T
                                                                  20          VDD3P3_RTC        Power
                                                                  21          XTAL_32K_P        IO           VDD3P3_RTC                                                 RTC_GPIO15                          XTAL_32K_P     ADC2_CH4   GPIO15          I/O/T    GPIO15   I/O/T   U0RTS                  O
                                                                  22          XTAL_32K_N        IO           VDD3P3_RTC                                                 RTC_GPIO16                          XTAL_32K_N     ADC2_CH5   GPIO16          I/O/T    GPIO16   I/O/T   U0CTS                  I1
                                                                  23          GPIO17            IO           VDD3P3_RTC                                IE               RTC_GPIO17                                         ADC2_CH6   GPIO17          I/O/T    GPIO17   I/O/T   U1TXD                  O
                                                                  24          GPIO18            IO           VDD3P3_RTC                                IE               RTC_GPIO18                                         ADC2_CH7   GPIO18          I/O/T    GPIO18   I/O/T   U1RXD                  I1       CLK_OUT3    O
                                                                  25          GPIO19            IO           VDD3P3_RTC                                                 RTC_GPIO19                          USB_D-         ADC2_CH8   GPIO19          I/O/T    GPIO19   I/O/T   U1RTS                  O        CLK_OUT2    O
                                79                                26
                                                                  27
                                                                              GPIO20
                                                                              GPIO21
                                                                                                IO
                                                                                                IO
                                                                                                             VDD3P3_RTC
                                                                                                             VDD3P3_RTC
                                                                                                                                          USB_PU       USB_PU           RTC_GPIO20
                                                                                                                                                                        RTC_GPIO21
                                                                                                                                                                                                            USB_D+         ADC2_CH9   GPIO20
                                                                                                                                                                                                                                      GPIO21
                                                                                                                                                                                                                                                      I/O/T
                                                                                                                                                                                                                                                      I/O/T
                                                                                                                                                                                                                                                               GPIO20
                                                                                                                                                                                                                                                               GPIO21
                                                                                                                                                                                                                                                                        I/O/T
                                                                                                                                                                                                                                                                        I/O/T
                                                                                                                                                                                                                                                                                U1CTS                  I1       CLK_OUT1    O

                                                                  28          SPICS1            IO           VDD_SPI                      WPU, IE      WPU, IE                                                                        SPICS1          O/T      GPIO26   I/O/T
                                                                  29          VDD_SPI           Power
                                                                  30          SPIHD             IO           VDD_SPI                      WPU, IE      WPU, IE                                                                        SPIHD           I1/O/T   GPIO27   I/O/T
                                                                  31          SPIWP             IO           VDD_SPI                      WPU, IE      WPU, IE                                                                        SPIWP           I1/O/T   GPIO28   I/O/T
                                                                  32          SPICS0            IO           VDD_SPI                      WPU, IE      WPU, IE                                                                        SPICS0          O/T      GPIO29   I/O/T
                                                                  33          SPICLK            IO           VDD_SPI                      WPU, IE      WPU, IE                                                                        SPICLK          O/T      GPIO30   I/O/T
                                                                  34          SPIQ              IO           VDD_SPI                      WPU, IE      WPU, IE                                                                        SPIQ            I1/O/T   GPIO31   I/O/T
                                                                  35          SPID              IO           VDD_SPI                      WPU, IE      WPU, IE                                                                        SPID            I1/O/T   GPIO32   I/O/T
                                                                  36          SPICLK_N          IO           VDD_SPI/VDD3P3_CPU           IE           IE                                                                             SPICLK_P_DIFF   O/T      GPIO48   I/O/T   SUBSPICLK_P_DIFF       O/T
                                                                  37          SPICLK_P          IO           VDD_SPI/VDD3P3_CPU           IE           IE                                                                             SPICLK_N_DIFF   O/T      GPIO47   I/O/T   SUBSPICLK_N_DIFF       O/T
                                                                  38          GPIO33            IO           VDD_SPI/VDD3P3_CPU                        IE                                                                             GPIO33          I/O/T    GPIO33   I/O/T   FSPIHD                 I1/O/T   SUBSPIHD    I1/O/T   SPIIO4    I1/O/T
                                                                  39          GPIO34            IO           VDD_SPI/VDD3P3_CPU                        IE                                                                             GPIO34          I/O/T    GPIO34   I/O/T   FSPICS0                I1/O/T   SUBSPICS0   O/T      SPIIO5    I1/O/T
                                                                  40          GPIO35            IO           VDD_SPI/VDD3P3_CPU                        IE                                                                             GPIO35          I/O/T    GPIO35   I/O/T   FSPID                  I1/O/T   SUBSPID     I1/O/T   SPIIO6    I1/O/T




                                ESP32-S3 Series Datasheet v2.2
                                                                  41          GPIO36            IO           VDD_SPI/VDD3P3_CPU                        IE                                                                             GPIO36          I/O/T    GPIO36   I/O/T   FSPICLK                I1/O/T   SUBSPICLK   O/T      SPIIO7    I1/O/T
                                                                  42          GPIO37            IO           VDD_SPI/VDD3P3_CPU                        IE                                                                             GPIO37          I/O/T    GPIO37   I/O/T   FSPIQ                  I1/O/T   SUBSPIQ     I1/O/T   SPIDQS    I0/O/T
                                                                  43          GPIO38            IO           VDD3P3_CPU                                IE                                                                             GPIO38          I/O/T    GPIO38   I/O/T   FSPIWP                 I1/O/T   SUBSPIWP    I1/O/T
                                                                  44          MTCK              IO           VDD3P3_CPU                                IE                                                                             MTCK            I1       GPIO39   I/O/T   CLK_OUT3               O        SUBSPICS1   O/T
                                                                  45          MTDO              IO           VDD3P3_CPU                                IE                                                                             MTDO            O/T      GPIO40   I/O/T   CLK_OUT2               O
                                                                  46          VDD3P3_CPU        Power
                                                                  47          MTDI              IO           VDD3P3_CPU                                IE                                                                             MTDI            I1       GPIO41   I/O/T   CLK_OUT1               O
                                                                  48          MTMS              IO           VDD3P3_CPU                                IE                                                                             MTMS            I1       GPIO42   I/O/T
                                                                  49          U0TXD             IO           VDD3P3_CPU                   WPU, IE      WPU, IE                                                                        U0TXD           O        GPIO43   I/O/T   CLK_OUT1               O
                                                                  50          U0RXD             IO           VDD3P3_CPU                   WPU, IE      WPU, IE                                                                        U0RXD           I1       GPIO44   I/O/T   CLK_OUT2               O
                                                                  51          GPIO45            IO           VDD3P3_CPU                   WPD, IE      WPD, IE                                                                        GPIO45          I/O/T    GPIO45   I/O/T
                                                                  52          GPIO46            IO           VDD3P3_CPU                   WPD, IE      WPD, IE                                                                        GPIO46          I/O/T    GPIO46   I/O/T
                                                                  53          XTAL_N            Analog
                                                                  54          XTAL_P            Analog
                                                                  55          VDDA              Power
                                                                  56          VDDA              Power
                                                                  57          GND               Power
                                                                  * For details, see Section 2 Pins. Regarding highlighted cells, see Section 2.3.4 Restrictions for GPIOs and RTC_GPIOs.
```
