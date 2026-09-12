---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "4.2.2 Analog Signal Processing"
pdf_pages: 59-60
retrieved: 2026-09-12
redistribute: false
---

# 4.2.2 Analog Signal Processing

```text
4 Functional Description


   • Each channel has the following parameters:

          1. Selection between counting on positive or negative edges of the input pulse signal

          2. Configuration to Increment, Decrement, or Disable counter mode for control signal’s high and low
             states

For details, see ESP32-S3 Technical Reference Manual > Chapter Pulse Count Controller.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.


4.2.2      Analog Signal Processing
This subsection describes components on the chip that sense and process real-world data.


4.2.2.1 SAR ADC

ESP32-S3 integrates two 12-bit SAR ADCs and supports measurements on 20 channels (analog-enabled pins).
For power-saving purpose, the ULP coprocessors in ESP32-S3 can also be used to measure voltage in sleep
modes. By using threshold settings or other methods, we can awaken the CPU from sleep modes.

  Note:
  Please note that the ADC2_CH… analog functions (see Table 2-8 Analog Functions) cannot be used with Wi-Fi simul-
  taneously.


For details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal
Processing.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.


4.2.2.2        Temperature Sensor

The temperature sensor generates a voltage that varies with temperature. The voltage is internally converted
via an ADC into a digital value.

The temperature sensor has a range of –40 °C to 125 °C. It is designed primarily to sense the temperature
changes inside the chip. The temperature value depends on factors such as microcontroller clock frequency
or I/O load. Generally, the chip’s internal temperature is higher than the ambient temperature.

For details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal
Processing.


4.2.2.3 Touch Sensor

ESP32-S3 has 14 capacitive-sensing GPIOs, which detect variations induced by touching or approaching the
GPIOs with a finger or other objects. The low-noise nature of the design and the high sensitivity of the circuit
allow relatively small pads to be used. Arrays of pads can also be used, so that a larger area or more points



Espressif Systems                                       59                       ESP32-S3 Series Datasheet v2.2
                                          Submit Documentation Feedback
4 Functional Description


can be detected. The touch sensing performance can be further enhanced by the waterproof design and
digital filtering feature.

  Note:
  ESP32-S3 touch sensor has not passed the Conducted Susceptibility (CS) test for now, and thus has limited application
  scenarios.



For details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal
Processing.

Pin Assignment

For details, see Section 2.3.5 Peripheral Pin Assignment.




Espressif Systems                                         60                         ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
```
