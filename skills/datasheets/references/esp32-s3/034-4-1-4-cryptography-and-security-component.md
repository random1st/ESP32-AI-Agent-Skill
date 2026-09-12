---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "4.1.4 Cryptography and Security Component"
pdf_pages: 47-50
retrieved: 2026-09-12
redistribute: false
---

# 4.1.4 Cryptography and Security Component

```text
4 Functional Description


For details, see ESP32-S3 Technical Reference Manual > Chapter World Controller.


4.1.3.12 System Registers

ESP32-S3 system registers can be used to control the following peripheral blocks and core modules:

   • System and memory

   • Clock

   • Software Interrupt

   • Low-power management

   • Peripheral clock gating and reset

   • CPU Control

For details, see ESP32-S3 Technical Reference Manual > Chapter System Registers.


4.1.4    Cryptography and Security Component
This subsection describes the security features incorporated into the chip, which safeguard data and
operations.


4.1.4.1 SHA Accelerator

ESP32-S3 integrates an SHA accelerator, which is a hardware device that speeds up SHA algorithm
significantly.

Feature List

   • All the hash algorithms introduced in FIPS PUB 180-4 Spec.

         – SHA-1

         – SHA-224

         – SHA-256

         – SHA-384

         – SHA-512

         – SHA-512/224

         – SHA-512/256

         – SHA-512/t

   • Two working modes

         – Typical SHA

         – DMA-SHA

   • interleaved function when working in Typical SHA working mode

   • Interrupt function when working in DMA-SHA working mode

For details, see ESP32-S3 Technical Reference Manual > Chapter SHA Accelerator.


Espressif Systems                                     47                    ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
4 Functional Description



4.1.4.2     AES Accelerator

ESP32-S3 integrates an Advanced Encryption Standard (AES) Accelerator, which is a hardware device that
speeds up AES algorithm significantly.

Feature List

   • Typical AES working mode

          – AES-128/AES-256 encryption and decryption

   • DMA-AES working mode

          – AES-128/AES-256 encryption and decryption

          – Block cipher mode

               * ECB (Electronic Codebook)

               * CBC (Cipher Block Chaining)

               * OFB (Output Feedback)

               * CTR (Counter)

               * CFB8 (8-bit Cipher Feedback)

               * CFB128 (128-bit Cipher Feedback)

          – Interrupt on completion of computation

For details, see ESP32-S3 Technical Reference Manual > Chapter AES Accelerator.


4.1.4.3 RSA Accelerator

The RSA Accelerator provides hardware support for high precision computation used in various RSA
asymmetric cipher algorithms.

Feature List

   • Large-number modular exponentiation with two optional acceleration options

   • Large-number modular multiplication, up to 4096 bits

   • Large-number multiplication, with operands up to 2048 bits

   • Operands of different lengths

   • Interrupt on completion of computation

For details, see ESP32-S3 Technical Reference Manual > Chapter RSA Accelerator.


4.1.4.4     Secure Boot

Secure Boot feature uses a hardware root of trust to ensure only signed firmware (with RSA-PSS signature) can
be booted.




Espressif Systems                                     48                    ESP32-S3 Series Datasheet v2.2
                                         Submit Documentation Feedback
4 Functional Description



4.1.4.5 HMAC Accelerator

The Hash-based Message Authentication Code (HMAC) module computes Message Authentication Codes
(MACs) using Hash algorithm and keys as described in RFC 2104.

Feature List

   • Standard HMAC-SHA-256 algorithm

   • Hash result only accessible by configurable hardware peripheral (in downstream mode)

   • Compatible to challenge-response authentication algorithm

   • Generates required keys for the RSA Digital Signature Peripheral (RSA_DS) (in downstream mode)

   • Re-enables soft-disabled JTAG (in downstream mode)

For details, see ESP32-S3 Technical Reference Manual > Chapter HMAC Accelerator.


4.1.4.6 RSA Digital Signature Peripheral (RSA_DS)

An RSA Digital Signature Peripheral (RSA_DS) is used to verify the authenticity and integrity of a message
using a cryptographic algorithm.

Feature List

   • RSA_DS with key length up to 4096 bits

   • Encrypted private key data, only decryptable by RSA_DS

   • SHA-256 digest to protect private key data against tampering by an attacker

For details, see ESP32-S3 Technical Reference Manual > Chapter RSA Digital Signature Peripheral (RSA_DS).



4.1.4.7 External Memory Encryption and Decryption

ESP32-S3 integrates an External Memory Encryption and Decryption module that complies with the XTS-AES
standard.

Feature List

   • General XTS-AES algorithm, compliant with IEEE Std 1619-2007

   • Software-based manual encryption

   • High-speed auto encryption, without software’s participation

   • High-speed auto decryption, without software’s participation

   • Encryption and decryption functions jointly determined by registers configuration, eFuse parameters,
     and boot mode

For details, see ESP32-S3 Technical Reference Manual > Chapter External Memory Encryption and
Decryption.




Espressif Systems                                     49                      ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
4 Functional Description



4.1.4.8   Clock Glitch Detection

The Clock Glitch Detection module on ESP32-S3 monitors input clock signals from XTAL_CLK. If it detects a
glitch with a width shorter than 3 ns, input clock signals from XTAL_CLK are blocked.

For details, see ESP32-S3 Technical Reference Manual > Chapter Clock Glitch Detection.


4.1.4.9   Random Number Generator

The random number generator (RNG) in ESP32-S3 generates true random numbers, which means random
number generated from a physical process, rather than by means of an algorithm. No number generated
within the specified range is more or less likely to appear than any other number.

For details, see ESP32-S3 Technical Reference Manual > Chapter Random Number Generator.




Espressif Systems                                     50                      ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
```
