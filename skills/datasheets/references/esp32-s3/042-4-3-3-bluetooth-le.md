---
source: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
document: ESP32-S3 Series Datasheet
vendor: Espressif Systems
section: "4.3.3 Bluetooth LE"
pdf_pages: 62-63
retrieved: 2026-09-12
redistribute: false
---

# 4.3.3 Bluetooth LE

```text
4 Functional Description



4.3.2.1 Wi-Fi Radio and Baseband

The ESP32-S3 Wi-Fi radio and baseband support the following features:

   • 802.11b/g/n

   • 802.11n MCS0-7 that supports 20 MHz and 40 MHz bandwidth

   • 802.11n MCS32

   • 802.11n 0.4 µs guard-interval

   • Data rate up to 150 Mbps

   • RX STBC (single spatial stream)

   • Adjustable transmitting power

   • Antenna diversity:
     ESP32-S3 supports antenna diversity with an external RF switch. This switch is controlled by one or
     more GPIOs, and used to select the best antenna to minimize the effects of channel imperfections.


4.3.2.2     Wi-Fi MAC

ESP32-S3 implements the full 802.11b/g/n Wi-Fi MAC protocol. It supports the Basic Service Set (BSS) STA
and SoftAP operations under the Distributed Control Function (DCF). Power management is handled
automatically with minimal host interaction to minimize the active duty period.

The ESP32-S3 Wi-Fi MAC applies the following low-level protocol functions automatically:

   • Four virtual Wi-Fi interfaces

   • Simultaneous Infrastructure BSS Station mode, SoftAP mode, and Station + SoftAP mode

   • RTS protection, CTS protection, Immediate Block ACK

   • Fragmentation and defragmentation

   • TX/RX A-MPDU, TX/RX A-MSDU

   • TXOP

   • WMM

   • GCMP, CCMP, TKIP, WAPI, WEP, BIP, WPA2-PSK/WPA2-Enterprise, and WPA3-PSK/WPA3-Enterprise

   • Automatic beacon monitoring (hardware TSF)

   • 802.11mc FTM


4.3.2.3 Networking Features

Users are provided with libraries for TCP/IP networking, ESP-WIFI-MESH networking, and other networking
protocols over Wi-Fi. TLS 1.2 support is also provided.


4.3.3 Bluetooth LE
This subsection describes the chip’s Bluetooth capabilities, which facilitate wireless communication for
low-power, short-range applications. ESP32-S3 includes a Bluetooth Low Energy subsystem that integrates a


Espressif Systems                                      62                         ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
4 Functional Description


hardware link layer controller, an RF/modem block and a feature-rich software protocol stack. It supports the
core features of Bluetooth 5 and Bluetooth Mesh.


4.3.3.1 Bluetooth LE PHY

Bluetooth Low Energy radio and PHY in ESP32-S3 support:

   • 1 Mbps PHY

   • 2 Mbps PHY for high transmission speed and high data throughput

   • Coded PHY for high RX sensitivity and long range (125 Kbps and 500 Kbps)

   • Class 1 transmit power without external PA

   • HW Listen Before Talk (LBT)


4.3.3.2 Bluetooth LE Link Controller

Bluetooth Low Energy Link Layer Controller in ESP32-S3 supports:

   • LE Advertising Extensions, to enhance broadcasting capacity and broadcast more intelligent data

   • Multiple Advertising Sets

   • Simultaneous Advertising and Scanning

   • Multiple connections in simultaneous central and peripheral roles

   • Adaptive Frequency Hopping (AFH) and Channel Assessment

   • LE Channel Selection Algorithm #2

   • Connection Parameter Update

   • High Duty Cycle Non-Connectable Advertising

   • LE Privacy v1.2

   • LE Data Packet Length Extension

   • Link Layer Extended Scanner Filter Policies

   • Low Duty Cycle Directed Advertising

   • Link Layer Encryption

   • LE Ping




Espressif Systems                                     63                     ESP32-S3 Series Datasheet v2.2
                                        Submit Documentation Feedback
```
