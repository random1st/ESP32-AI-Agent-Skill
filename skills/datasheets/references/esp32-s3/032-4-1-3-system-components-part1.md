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
4 Functional Description


   • Critical word first and early restart

For details, see ESP32-S3 Technical Reference Manual > Chapter System and Memory.


4.1.2.4       eFuse Controller

ESP32-S3 contains a 4-Kbit eFuse to store parameters, which are burned and read by an eFuse
controller.

Feature List

   • 4 Kbits in total, with 1792 bits reserved for users, e.g., encryption key and device ID

   • One-time programmable storage

   • Configurable write protection

   • Configurable read protection

   • Various hardware encoding schemes to protect against data corruption

For details, see ESP32-S3 Technical Reference Manual > Chapter eFuse Controller.


4.1.3 System Components
This subsection describes the essential components that contribute to the overall functionality and control of
the system.


4.1.3.1 IO MUX and GPIO Matrix

The IO MUX and GPIO Matrix in the ESP32-S3 chip provide flexible routing of peripheral input and output
signals to the GPIO pins. These peripherals enhance the functionality and performance of the chip by allowing
the configuration of I/O, support for multiplexing, and signal synchronization for peripheral inputs.

Feature List

   • GPIO Matrix:

          – A full-switching matrix between the peripheral input/output signals and the GPIO pins

          – 175 digital peripheral input signals can be sourced from the input of any GPIO pins

          – The output of any GPIO pins can be from any of the 184 digital peripheral output signals

          – Supports signal synchronization for peripheral inputs based on APB clock bus

          – Provides input signal filter

          – Supports sigma delta modulated output

          – Supports GPIO simple input and output

   • IO MUX:

          – Provides one configuration register IO_MUX_GPIOn_REG for each GPIO pin. The pin can be
              configured to

               * perform GPIO function routed by GPIO matrix


Espressif Systems                                         40                    ESP32-S3 Series Datasheet v2.2
                                             Submit Documentation Feedback
4 Functional Description


               * or perform direct connection bypassing GPIO matrix

        – Supports some high-speed digital signals (SPI, JTAG, UART) bypassing GPIO matrix for better
          high-frequency digital performance (IO MUX is used to connect these pins directly to peripherals)

   • RTC IO MUX:

        – Controls low power feature of 22 RTC GPIO pins

        – Controls analog functions of 22 RTC GPIO pins

        – Redirects 22 RTC input/output signals to RTC system

For details, see ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.


4.1.3.2 Reset

ESP32-S3 provides four reset levels, namely CPU Reset, Core Reset, System Reset, and Chip Reset.

Feature List

   • Support four reset levels:

        – CPU Reset: only resets CPUx core. CPUx can be CPU0 or CPU1 here. Once such reset is released,
          programs will be executed from CPUx reset vector. Each CPU core has its own reset logic. If CPU
          Reset is from CPU0, the sensitive registers will be reset, too.

        – Core Reset: resets the whole digital system except RTC, including CPU0, CPU1, peripherals, Wi-Fi,
          Bluetooth® LE (BLE), and digital GPIOs.

        – System Reset: resets the whole digital system, including RTC.

        – Chip Reset: resets the whole chip.

   • Support software reset and hardware reset:

        – Software reset is triggered by CPUx configuring its corresponding registers. Refer to
          ESP32-S3 Technical Reference Manual > Chapter Low-power Management for more details.

        – Hardware reset is directly triggered by the circuit.

For details, see ESP32-S3 Technical Reference Manual > Chapter Reset and Clock.


4.1.3.3 Clock

CPU Clock

The CPU clock has three possible sources:

   • External main crystal clock

   • Internal fast RC oscillator (typically about 17.5 MHz, adjustable)

   • PLL clock

The application can select the clock source from the three clocks above. The selected clock source drives
the CPU clock directly, or after division, depending on the application. Once the CPU is reset, the default
clock source would be the external main crystal clock divided by 2.



Espressif Systems                                       41                    ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
4 Functional Description



  Note:
  ESP32-S3 is unable to operate without an external main crystal clock.



RTC Clock

The RTC slow clock is used for RTC counter, RTC watchdog and low-power controller. It has three possible
sources:

   • External low-speed (32 kHz) crystal clock

   • Internal slow RC oscillator (typically about 136 kHz, adjustable)

   • Internal fast RC oscillator divided clock (derived from the internal fast RC oscillator divided by 256)

The RTC fast clock is used for RTC peripherals and sensor controllers. It has two possible sources:

   • External main crystal clock divided by 2

   • Internal fast RC oscillator (typically about 17.5 MHz, adjustable)

For details, see ESP32-S3 Technical Reference Manual > Chapter Reset and Clock.


4.1.3.4    Interrupt Matrix

The interrupt matrix embedded in ESP32-S3 independently allocates peripheral interrupt sources to the two
CPUs’ peripheral interrupts, to timely inform CPU0 or CPU1 to process the interrupts once the interrupt signals
are generated.

Feature List

   • 99 peripheral interrupt sources as input

   • Generate 26 peripheral interrupts to CPU0 and 26 peripheral interrupts to CPU1 as output.

     Note that the remaining six CPU0 interrupts and six CPU1 interrupts are internal interrupts.

   • Disable CPU non-maskable interrupt (NMI) sources

   • Query current interrupt status of peripheral interrupt sources

For details, see ESP32-S3 Technical Reference Manual > Chapter Interrupt Matrix.


4.1.3.5 Power Management Unit (PMU)

ESP32-S3 has an advanced Power Management Unit (PMU). It can be flexibly configured to power up
different power domains of the chip to achieve the best balance between chip performance, power
consumption, and wakeup latency.

The integrated Ultra-Low-Power (ULP) coprocessors allow ESP32-S3 to operate in Deep-sleep mode with
most of the power domains turned off, thus achieving extremely low-power consumption.

Configuring the PMU is a complex procedure. To simplify power management for typical scenarios, there are
the following predefined power modes that power up different combinations of power domains:

   • Active mode – The CPU, RF circuits, and all peripherals are on. The chip can process data, receive,
     transmit, and listen.


Espressif Systems                                         42                    ESP32-S3 Series Datasheet v2.2
                                           Submit Documentation Feedback
4 Functional Description


   • Modem-sleep mode – The CPU is on, but the clock frequency can be reduced. The wireless
     connections can be configured to remain active as RF circuits are periodically switched on when
     required.

   • Light-sleep mode – The CPU stops running, and can be optionally powered on. The RTC peripherals, as
     well as the ULP coprocessor can be woken up periodically by the timer. The chip can be woken up via
     all wake up mechanisms: MAC, RTC timer, or external interrupts. Wireless connections can remain active.
     Some groups of digital peripherals can be optionally powered off.

   • Deep-sleep mode – Only RTC is powered on. Wireless connection data is stored in RTC memory.

For power consumption in different power modes, see Section 5.6 Current Consumption.

Figure 4-2 Components and Power Domains and the following Table 4-1 show the distribution of chip
components between power domains and power subdomains .


                                  Espressif’s ESP32-S3 Wi-Fi + Bluetooth® Low Energy SoC

                                                   Digital Power Domain

                         CPU                                                                                      System
                                               SPI0/1        I2C              GPIO              TWAI®              Timer
           Xtensa® Dual-          JTAG
           core 32-bit LX7                     Camera                                         USB Serial/         General-
                                                             I2S              UART
           Microprocessor        Cache        Interface                                         JTAG              purpose
                                                                                                                   Timers
             World             Interrupt       Pulse         LCD              Flash
                                                                                                 RMT
            Controller           Matrix       Counter      Interface        Encryption
                                                                                                                Main System
                                                                                                                 Watchdog
              ROM               SRAM          DIG ADC        RNG            MCPWM             LED PWM             Timers


            Wireless Digital Circuits                           Optional Digital Peripherals
          Bluetooth LE Link                                                                                     SD/MMC
                                Wi-Fi MAC        SHA         RSA             HMAC             RSA_DS
              Controller                                                                                          Host
            Bluetooth LE          Wi-Fi
                                                 AES        SPI2/3         Secure Boot         GDMA            USB OTG
             Baseband           Baseband


                         RTC Power Domain                                     Analog Power Domain
                                eFuse                                                RF Circuits
              PMU                            RTC Memory
                               Controller
                                                                             2.4 GHz             2.4 GHz
           Optional RTC Peripherals                                          Receiver           Transmitter
                                               Super
                                 ULP          Watchdog                          RF            2.4 GHz Balun
           RTC GPIO
                              Coprocessor                                   Synthesizer          + Switch

            RTC I2C            RTC ADC
                                                RTC                  PLL          RC_FAST_CLK                 XTAL_CLK
                                              Watchdog
          Temperature           Touch                           Phase Lock               Fast RC              External Main
                                               Timer
            Sensor              Sensor                             Loop                  Oscillator               Clock



        Power distribution
                   Power domain
                   Power subdomain


                                      Figure 4-2. Components and Power Domains




Espressif Systems                                          43                               ESP32-S3 Series Datasheet v2.2
                                             Submit Documentation Feedback
4 Functional Description


                                       Table 4-1. Components and Power Domains

           Power     RTC                 Digital                                 Analog
           Domain           Optional                      Optional   Wireless             RC_
                                                                                                 XTAL_               RF
  Power                       RTC                  CPU     Digital    Digital           FAST_               PLL
                                                                                                   CLK             Circuits
  Mode                       Periph                       Periph     Circuits             CLK
  Active             ON       ON          ON       ON       ON         ON        ON       ON       ON       ON       ON
  Modem-sleep        ON       ON          ON        ON      ON         ON1       ON       ON       ON       ON      OFF2
  Light-sleep        ON       ON          ON       OFF1     ON1       OFF1       ON       OFF      OFF     OFF      OFF2
  Deep-sleep         ON       ON1        OFF       OFF      OFF        OFF       ON       OFF      OFF     OFF       OFF
  1 Configurable. See ESP32-S3 Technical Reference Manual > Chapter Low-power Management for more details.
  2 If Wireless Digital Circuits are on, RF circuits are periodically switched on when required by internal operation to keep

   active wireless connections running.


For details, see ESP32-S3 Technical Reference Manual > Chapter Low Power Management.


4.1.3.6 System Timer

ESP32-S3 integrates a 52-bit system timer, which has two 52-bit counters and three comparators.

Feature List

   • Counters with a clock frequency of 16 MHz

   • Three types of independent interrupts generated according to alarm value

   • Two alarm modes: target mode and period mode

   • 52-bit target alarm value and 26-bit periodic alarm value

   • Read sleep time from RTC timer when the chip is awaken from Deep-sleep or Light-sleep mode

   • Counters can be stalled if the CPU is stalled or in OCD mode

For details, see ESP32-S3 Technical Reference Manual > Chapter System Timer.


4.1.3.7 General Purpose Timers

ESP32-S3 is embedded with four 54-bit general-purpose timers, which are based on 16-bit prescalers and
54-bit auto-reload-capable up/down-timers.

Feature List

   • 16-bit clock prescaler, from 2 to 65536

   • 54-bit time-base counter programmable to be incrementing or decrementing

   • Able to read real-time value of the time-base counter

   • Halting and resuming the time-base counter

   • Programmable alarm generation

   • Timer value reload (Auto-reload at alarm or software-controlled instant reload)



Espressif Systems                                             44                        ESP32-S3 Series Datasheet v2.2
                                               Submit Documentation Feedback
4 Functional Description


   • Level interrupt generation

For details, see ESP32-S3 Technical Reference Manual > Chapter Timer Group.


4.1.3.8     Watchdog Timers

ESP32-S3 contains three watchdog timers: one in each of the two timer groups (called Main System
Watchdog Timers, or MWDT) and one in the RTC Module (called the RTC Watchdog Timer, or RWDT).

During the flash boot process, RWDT and the first MWDT are enabled automatically in order to detect and
recover from booting errors.

Feature List

   • Four stages:

          – Each with a programmable timeout value

          – Each stage can be configured, enabled and disabled separately

   • Upon expiry of each stage:

          – Interrupt, CPU reset, or core reset occurs for MWDT

          – Interrupt, CPU reset, core reset, or system reset occurs for RWDT

   • 32-bit expiry counter

   • Write protection, to prevent RWDT and MWDT configuration from being altered inadvertently

   • Flash boot protection: If the boot process from an SPI flash does not complete within a predetermined
      period of time, the watchdog will reboot the entire main system

For details, see ESP32-S3 Technical Reference Manual > Chapter Watchdog Timers.


4.1.3.9     XTAL32K Watchdog Timers

Interrupt and Wake-Up

When the XTAL32K watchdog timer detects the oscillation failure of XTAL32K_CLK, an oscillation failure
interrupt RTC_XTAL32K_DEAD_INT (for interrupt description, please refer to
ESP32-S3 Technical Reference Manual > Chapter Low-power Management) is generated. At this point, the
CPU will be woken up if in Light-sleep mode or Deep-sleep mode.

```
