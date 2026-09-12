---
name: lvgl
description: LVGL embedded GUI library — version-accurate APIs, widgets and styles for v8.2 through v9.5, the v8 to v9 migration, lv_conf.h and CONFIG_LV_* configuration, draw-buffer and memory sizing, display/input driver registration, performance tuning. Use when the user mentions LVGL, lv_obj, lv_display, lv_timer, a widget API, screen refresh/FPS tuning, or upgrading an LVGL version.
---

# LVGL

LVGL's API broke between v8 and v9, so the first job is always to establish the
version in use and answer from that version's reference. Panel and bus concerns
(RGB timing, tearing, bounce buffers) belong to the `display-panels` skill; the
MCU side to `esp32`.

## 1. Establish the version before answering

Read it, don't assume:

* ESP-IDF component registry: `idf_component.yml` / `dependencies.lock`
  (e.g. `lvgl/lvgl: 8.3.11`);
* PlatformIO: `lib_deps` in `platformio.ini`;
* vendored copy: `lvgl/lv_version.h` or the `lv_conf.h` header comment;
* config source: `CONFIG_LV_*` in `sdkconfig` (IDF component) **or** `lv_conf.h`
  (everything else) — mixing both silently loses settings.

## 2. Reference loading

| File | Load when |
|---|---|
| `references/lvgl/README.md` | LVGL mentioned, version not yet known |
| `references/lvgl/migration/version-matrix.md` | choosing a version, or checking what a toolchain/board supports |
| `references/lvgl/migration/v8-to-v9.md` | planning or reviewing a v8→v9 upgrade |
| `references/lvgl/v9.0/migration-from-v8.md` | symbol-by-symbol v8→v9 replacements |
| `references/lvgl/v8.2/`, `v8.3/`, `v8.4/` | project pinned to LVGL 8.x |
| `references/lvgl/v8.3/widgets.md` | widget APIs on 8.3 (the common ESP-IDF pin) |
| `references/lvgl/v9.0/` … `v9.5/` | project on LVGL 9.x |
| `references/lvgl/v9.5/widgets.md` | widget APIs on 9.5 |
| `references/lvgl/v9.5/esp32-integration.md` | wiring LVGL 9.5 to esp_lcd / esp_lcd_touch |

Quote the version's own doc. A symbol that exists in 9.x but not in 8.x is the
single most common reason AI-written LVGL code does not compile.

## 3. The v8 → v9 break, in one place

* Display renames: `lv_disp_*` → `lv_display_*`; `lv_disp_drv_t` is gone, a
  display is created and configured directly.
* Draw buffers: `lv_disp_draw_buf_t` → `lv_display_set_buffers()`.
* Input: `lv_indev_drv_t` → `lv_indev_create()` plus setters.
* Colour and image descriptors changed layout, as did many style setters.
* Tick/timer plumbing (`lv_tick_inc`, `lv_timer_handler`) kept its shape — ports
  usually die on display/input registration, not on the main loop.

When a project must stay on 8.3 (for example because an IDF component pins it),
say so and answer in 8.3 terms instead of turning the question into an upgrade.

## 4. Memory and performance

* `CONFIG_LV_MEM_CUSTOM=y` (8.x) / LVGL's stdlib hooks (9.x) hand allocation to
  the platform heap, which is what lets widget trees live in PSRAM.
* Draw buffers are **not** frame buffers. Partial draw buffers of ~1/10 screen
  are the usual starting point; full-screen double buffering is a panel-level
  decision (see `display-panels`).
* `CONFIG_LV_USE_PERF_MONITOR` prints FPS and CPU load per refresh — measure
  before optimising and report the numbers, not an impression.
* Common wins, in order: shrink the redraw area (avoid full-screen
  invalidation), drop unnecessary opacity/shadow styles, keep images in the
  native colour depth, cache rendered text, and only then raise the pixel clock.
* Optional modules (snapshot, QR code, animations, file system) cost flash and
  RAM — enable deliberately.

## 5. Review checklist for LVGL code

1. Every symbol matches the project's LVGL version.
2. All LVGL calls happen on one task, or are guarded by a mutex — LVGL is not
   thread-safe.
3. `lv_tick_inc()` is driven by a real tick source and `lv_timer_handler()` runs
   on a predictable period.
4. Input device read callbacks neither block nor run in an ISR.
5. Objects and styles created in a loop are freed (`lv_obj_del`) or reused —
   leaks here look like slow death, not a crash.
