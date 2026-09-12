---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
document: ESP32-S3-WROOM-1 / 1U Module Datasheet
vendor: Espressif Systems
section: "5.2.2 Analog Signal Processing"
pdf_pages: 25-26
retrieved: 2026-09-12
redistribute: false
---

# 5.2.2 Analog Signal Processing

```text
5 Peripherals



5.2.1.12 Pulse Count Controller (PCNT)

The pulse count controller (PCNT) captures pulse and counts pulse edges through multiple modes.

Feature List

   • Four independent pulse counters (units) that count from 1 to 65535

   • Each unit consists of two independent channels sharing one pulse counter

   • All channels have input pulse signals (e.g. sig_ch0_un) with their corresponding control signals (e.g.
      ctrl_ch0_un)

   • Independently filter glitches of input pulse signals (sig_ch0_un and sig_ch1_un) and control signals
      (ctrl_ch0_un and ctrl_ch1_un) on each unit

   • Each channel has the following parameters:

        1. Selection between counting on positive or negative edges of the input pulse signal

        2. Configuration to Increment, Decrement, or Disable counter mode for control signal’s high and low
           states

For details, see ESP32-S3 Technical Reference Manual > Chapter Pulse Count Controller.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.2 Analog Signal Processing
This subsection describes components on the chip that sense and process real-world data.


5.2.2.1 SAR ADC

ESP32-S3 integrates two 12-bit SAR ADCs and supports measurements on 20 channels (analog-enabled pins).
For power-saving purpose, the ULP coprocessors in ESP32-S3 can also be used to measure voltage in sleep
modes. By using threshold settings or other methods, we can awaken the CPU from sleep modes.

For details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal
Processing.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.


5.2.2.2 Temperature Sensor

The temperature sensor generates a voltage that varies with temperature. The voltage is internally converted
via an ADC into a digital value.

The temperature sensor has a range of –40 °C to 125 °C. It is designed primarily to sense the temperature
changes inside the chip. The temperature value depends on factors such as microcontroller clock frequency
or I/O load. Generally, the chip’s internal temperature is higher than the ambient temperature.


Espressif Systems                                      25              ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                         Submit Documentation Feedback
5 Peripherals


For details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal
Processing.


5.2.2.3 Touch Sensor

ESP32-S3 has 14 capacitive-sensing GPIOs, which detect variations induced by touching or approaching the
GPIOs with a finger or other objects. The low-noise nature of the design and the high sensitivity of the circuit
allow relatively small pads to be used. Arrays of pads can also be used, so that a larger area or more points
can be detected. The touch sensing performance can be further enhanced by the waterproof design and
digital filtering feature.

  Note:
  ESP32-S3 touch sensor has not passed the Conducted Susceptibility (CS) test for now, and thus has limited application
  scenarios.



For details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal
Processing.

Pin Assignment

For details, see ESP32-S3 Series Datasheet > Section Peripheral Pin Assignment.




Espressif Systems                                          26               ESP32-S3-WROOM-1 & WROOM-1U Datasheet v1.8
                                           Submit Documentation Feedback
```
