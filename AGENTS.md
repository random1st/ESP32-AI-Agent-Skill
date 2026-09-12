# Repository guide

This repo is a set of six agent skills for ESP32 and surrounding hardware. It
targets two hosts from one tree:

* **Claude Code** — `skills/<name>/` (plugin manifest in `.claude-plugin/plugin.json`);
* **Codex** — `.agents/skills/<name>` symlinks pointing at the same directories.

Skills: `esp32`, `lvgl`, `display-panels`, `hardware-boards`, `electronics`,
`datasheets`. See `README.md` for what each one covers and how to install them.

## Working rules

* **A skill directory is self-contained.** `SKILL.md` plus its own `references/`,
  `scripts/`, `tests/`. Never reference a path outside the skill — that is what
  keeps one tree working in both hosts.
* **Front matter is `name` + `description` only.** Extra keys (`version`,
  `allowed-tools`, …) are not portable to Codex.
* **Hardware claims need a primary source.** ESP-IDF `soc_caps.h` for silicon
  facts, then the chip datasheet, then the module datasheet. Cite the file or
  section in a comment or in the test that asserts it; the existing code does.
* **Add a regression test with every pin-model change.**
  `skills/esp32/tests/` runs with `python -m pytest -q` from the repo root or
  from `skills/esp32`.
* **Vendor PDFs are never committed.** `skills/datasheets/references/.gitignore`
  keeps PDFs and non-redistributable chunk sets out; `INDEX.md` files are always
  committed so the corpus stays navigable.

## Checks before a commit

```bash
python -m pytest -q                                   # 69 tests
cd skills/esp32 && python scripts/validate_pinmap.py --format text \
  tests/fixtures/board_pregmate_main_a1.json          # real board stays valid
```

Both hosts should still enumerate all six skills:

```bash
claude -p "List only the names of project-level skills you can invoke."
codex exec "List only the names of the project skills available to you."
```
