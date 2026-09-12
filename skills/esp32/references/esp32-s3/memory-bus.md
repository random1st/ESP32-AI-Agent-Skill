# ESP32-S3 flash / PSRAM bus, modules and XIP

Sources: ESP32-S3 Series Datasheet §2.3.5, §2.5 (Power Supply), §4.1.2 (Memory
Organization); ESP32-S3-WROOM-1/1U Datasheet §1.2 (Series Comparison), §3.2
(Pin Description), §6.5 (Memory Specifications); ESP-IDF v5.5.1 ESP32-S3 GPIO
reference and `esp_psram` Kconfig. Full text: `datasheets` skill.

## 1. Which pins the memory bus takes

| Interface | Pins | When |
|---|---|---|
| SPI0/1 (flash + quad PSRAM) | GPIO26-32 | always on a module with in-package flash |
| SPIIO4 / SPIIO5 | GPIO33, GPIO34 | only when the **flash** is octal |
| SPIIO6 / SPIIO7 / SPIDQS | GPIO35, GPIO36, GPIO37 | whenever **octal PSRAM** is present |

The chip-level statement — "When using Octal flash or Octal PSRAM or both,
GPIO33 ~ GPIO37 are connected to SPIIO4 ~ SPIIO7 and SPIDQS" — covers both rows.
The module datasheet is narrower and more useful in practice: on
ESP32-S3-WROOM-1/1U, "for modules with Octal SPI PSRAM, i.e. modules embedded
with ESP32-S3R8 or ESP32-S3R16V, pins IO35, IO36, and IO37 are connected to the
Octal SPI PSRAM and are not available for other use". GPIO33/34 are not brought
out on that module at all, because its flash is quad SPI.

Practical rule for an octal-PSRAM module (N16R8, N8R8, N4R8, N16R16V):
**35/36/37 are gone, 33/34 do not exist on the pad, 26-32 are flash.** What is
left for the application is GPIO0-21 and GPIO38-48.

## 2. Module part numbers

Decode `N<flash MB>R<psram MB>[V]` — "V" means the VDD_SPI rail is 1.8 V:

| Module | Flash | PSRAM | Ambient max |
|---|---|---|---|
| ESP32-S3-WROOM-1-N8R2 | 8 MB quad | 2 MB **quad** | 85 °C |
| ESP32-S3-WROOM-1-N4R8 | 4 MB quad | 8 MB **octal** | 65 °C |
| ESP32-S3-WROOM-1-N8R8 | 8 MB quad | 8 MB **octal** | 65 °C |
| ESP32-S3-WROOM-1-N16R8 | 16 MB quad | 8 MB **octal** | 65 °C |
| ESP32-S3-WROOM-1-N16R16VA7 | 16 MB quad | 16 MB **octal**, 1.8 V | 65 °C |

Two consequences that get missed:

* **Octal PSRAM costs you ambient temperature** — 65 °C instead of 85 °C. With
  PSRAM ECC enabled the module datasheet allows 85 °C again at the cost of 1/16
  of the PSRAM capacity.
* **"V" parts run VDD_SPI at 1.8 V**, which also drops GPIO47/48 (SPICLK_N/P) to
  1.8 V logic levels. Light-sleep PSRAM current differs too: ~140 µA for 8 MB
  8-line at 3.3 V vs ~200 µA at 1.8 V (vs 40 µA for 2 MB 4-line).

A board cannot tell R8 from R8V from `sdkconfig`. Read the module marking or
`esptool.py flash_id` / eFuse, and say so rather than guessing.

## 3. Bus contention — the rule that explains most display and OTA bugs

Flash and PSRAM share one SPI bus and one cache. At any moment there is a single
consumer of that bus, and bandwidth is split between the CPU and EDMA. Therefore:

* A high-bandwidth DMA consumer (RGB LCD, camera, I2S) plus heavy flash access
  (SPIFFS, OTA write, NVS commit) produces starvation, not just slowdown.
* Anything that **disables the external-memory cache** — erasing/writing the
  main flash — stalls every PSRAM reader. Code that must keep running has to be
  in IRAM, and data it touches in internal RAM.
* `CONFIG_SPIRAM_XIP_FROM_PSRAM` (equivalently
  `CONFIG_SPIRAM_FETCH_INSTRUCTIONS` + `CONFIG_SPIRAM_RODATA`) moves
  instructions and read-only data into PSRAM so the cache survives flash
  writes — that is what keeps a display alive during an OTA.

## 4. Allocation

```c
// Frame buffers, big caches, anything DMA reads linearly:
void *fb = heap_caps_malloc(w * h * 2, MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT);
// DMA descriptors, ISR state, ring buffers touched with cache off:
void *dma = heap_caps_malloc(len, MALLOC_CAP_DMA | MALLOC_CAP_INTERNAL);
```

`MALLOC_CAP_DMA` is not automatically PSRAM-safe: on S3 only the AHB GDMA can
reach PSRAM (`SOC_AHB_GDMA_SUPPORT_PSRAM`), and the descriptors themselves must
stay in internal RAM. `CONFIG_SPIRAM_USE_MALLOC` lets plain `malloc()` fall back
to PSRAM above a threshold — convenient, and a good way to accidentally put a
DMA buffer in the wrong place, so allocate explicitly in driver code.

Check the split with `idf.py size-components` and, at runtime,
`heap_caps_get_free_size(MALLOC_CAP_INTERNAL)` versus `MALLOC_CAP_SPIRAM`.
