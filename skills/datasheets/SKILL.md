---
name: datasheets
description: Primary-source lookup for ESP32 and peripheral hardware — downloads vendor PDFs (ESP32-S3 datasheet and TRM, WROOM-1 module, ST7701S, GT911, TCA9554) and splits each into small per-section markdown chunks with an index, so a register, timing figure or pin table can be grepped instead of guessed. Use when a hardware claim needs a citation, when a register/bit field or electrical limit is in question, or when the answer is "check the datasheet".
---

# ESP32 Datasheet Corpus

Turns 300- and 1500-page vendor PDFs into chunks an agent can actually search.
Use it whenever a hardware answer needs to be *sourced* rather than recalled.

## 1. What is in the repo vs fetched on demand

`references/sources.yaml` is the catalog: slug, title, URL, vendor and topic
hints for every document. Per document, `references/<slug>/` holds:

* `INDEX.md` — the section map (chunk file → section title → PDF pages).
  **Always committed**, for every document, even when the chunks are not.
* `NNN-<section>.md` — one chunk per outline section, with YAML front matter
  naming the source URL, document, vendor, section and PDF page range.
* `<slug>.pdf` — the original, never committed.

Committed chunks: `esp32-s3` (chip datasheet), `esp32-s3-wroom-1` (module),
`tca9554` (TI I/O expander). Fetched on demand: `esp32-s3-trm` (~6 MB of text —
index only in git), `st7701s` and `gt911*` (the Sitronix document is marked
confidential and the Goodix mirrors are third-party re-hosts).

## 2. Building or refreshing the corpus

```bash
python scripts/fetch_datasheets.py --list          # catalog
python scripts/fetch_datasheets.py                 # everything
python scripts/fetch_datasheets.py esp32-s3-trm    # one document
python scripts/fetch_datasheets.py --depth 3 esp32-s3-trm   # finer sections
python scripts/fetch_datasheets.py --max-lines 250 esp32-s3 # smaller chunks
```

Sectioning uses the PDF's own outline (bookmarks) when it has one, falling back
to a numbered-heading heuristic otherwise — `INDEX.md` states which was used.
`--depth 2` (default) gives chapters plus second-level sections: ~66 chunks for
the S3 datasheet, ~463 for the TRM.

Needs `pdftotext` (`brew install poppler`) or `pypdf`; outline-based sectioning
needs `pypdf`. Some mirrors sit behind a WAF and return 403 — the error then
prints the exact path to drop a browser-downloaded PDF into, after which the
chunking step works identically.

## 3. Lookup workflow

1. Pick the document from `references/sources.yaml` (match the `topics` hints).
2. Grep that document's `INDEX.md` for the section, e.g. `grep -i "io mux"
   references/esp32-s3/INDEX.md`.
3. Read the named chunk. If the directory has only `INDEX.md`, fetch the
   document first (§2).
4. **Quote with the citation** from the chunk's front matter — document, section
   and PDF pages — so the claim is checkable.

Useful entry points:

| Question | Document → section |
|---|---|
| Which pins does the octal PSRAM take? | `esp32-s3-wroom-1` → 3.2 Pin Description (footnote b) |
| Pin's alternate functions, reset state, power rail | `esp32-s3` → 2.2 Pin Overview, 2.3.1 IO MUX Functions |
| Drive strength, VIH/VIL, absolute maxima | `esp32-s3` → 5.x Electrical Characteristics |
| GPIO matrix signal numbers | `esp32-s3-trm` → 6 IO MUX and GPIO Matrix |
| RGB/LCD peripheral registers and timing | `esp32-s3-trm` → 29 LCD and Camera Controller |
| Module variants, temperature limits, PSRAM current | `esp32-s3-wroom-1` → 1.2 Series Comparison, 6.5 Memory Specifications |
| I/O expander register semantics | `tca9554` → Register and Command Byte |
| Touch controller I2C addressing and registers | `gt911`, `gt911-programming` (fetch first) |

## 4. Rules

- A chunk is raw vendor text inside a fenced block. Quote it; do not paraphrase a
  number.
- Front matter carries `retrieved:`. If a document is months old and the question
  is about current silicon revisions, re-fetch before answering.
- Do not commit the PDFs, and do not commit chunks whose `redistribute:` flag is
  `false` — `references/.gitignore` enforces both.
