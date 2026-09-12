#!/usr/bin/env python3
"""Download, convert and chunk the datasheets declared in sources.yaml.

Vendor PDFs stay out of git (several are marked confidential); this script
materialises them locally and slices each one into small markdown chunks so an
agent can grep one topic instead of loading a 300-page document.

Chunk boundaries come from the PDF's own outline (bookmarks) when it has one —
that is how Espressif and TI documents are structured — and fall back to
detected numbered headings otherwise.

Usage:
    python scripts/fetch_datasheets.py                 # everything in the catalog
    python scripts/fetch_datasheets.py esp32-s3 gt911  # selected slugs
    python scripts/fetch_datasheets.py --list
    python scripts/fetch_datasheets.py --depth 3 esp32-s3-trm
    python scripts/fetch_datasheets.py --max-lines 300 esp32-s3

Text extraction needs `pdftotext` (brew install poppler) or `pip install pypdf`.
Outline-based chunking needs `pypdf`; without it the heading heuristic is used.
Python 3.9+; PyYAML and pypdf are optional.
"""

import argparse
import datetime
import hashlib
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATASHEET_ROOT = SKILL_ROOT / "references" / "datasheets"
CATALOG = DATASHEET_ROOT / "sources.yaml"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

# "4.2 Pin Definitions" / "Chapter 5 LCD_CAM" — used only when the PDF has no outline.
HEADING_RE = re.compile(r"^(?:chapter\s+)?(\d+(?:\.\d+){0,2})\s+([A-Z][^\n]{2,70})$",
                        re.IGNORECASE)
# Table rows and electrical limits masquerade as headings ("2.3 VDDIO", "0.05 MAX").
TABLE_NOISE_RE = re.compile(
    r"\s{3,}|\b(?:V|mV|mA|uA|µA|nA|ns|us|ms|MHz|kHz|GHz|dBm|pF|kΩ|Ω|°C|MAX|MIN|TYP)\b")
PAGE_BREAK = "\f"


# --------------------------------------------------------------------------- #
# Catalog parsing
# --------------------------------------------------------------------------- #

def load_catalog(path: Path) -> List[Dict[str, Any]]:
    """Parse sources.yaml. Uses PyYAML when available, else a minimal reader."""
    text = path.read_text()
    try:
        import yaml  # type: ignore
        return list(yaml.safe_load(text)["datasheets"])
    except ImportError:
        return _parse_catalog_subset(text)


def _parse_catalog_subset(text: str) -> List[Dict[str, Any]]:
    """Read the narrow YAML shape used by sources.yaml without PyYAML.

    Supports a `datasheets:` sequence of mappings whose values are scalars or
    single-/multi-line inline lists. Anything else raises, loudly.
    """
    entries: List[Dict[str, Any]] = []
    current: Optional[Dict[str, Any]] = None
    pending_key: Optional[str] = None
    pending_buf = ""
    in_sequence = False

    for raw in text.splitlines():
        line = "" if raw.strip().startswith("#") else raw.split(" #")[0].rstrip()
        if not line.strip():
            continue
        if line.strip() == "datasheets:":
            in_sequence = True
            continue
        if not in_sequence:
            continue

        if pending_key is not None:              # continuation of an inline list
            pending_buf += " " + line.strip()
            if "]" in pending_buf:
                current[pending_key] = _scalar(pending_buf)  # type: ignore[index]
                pending_key, pending_buf = None, ""
            continue

        stripped = line.strip()
        if stripped.startswith("- "):
            current = {}
            entries.append(current)
            stripped = stripped[2:]
        if ":" not in stripped:
            raise ValueError(f"unsupported catalog line: {raw!r}")
        key, _, value = stripped.partition(":")
        key, value = key.strip(), value.strip()
        if value.startswith("[") and "]" not in value:
            pending_key, pending_buf = key, value
            continue
        current[key] = _scalar(value)            # type: ignore[index]
    return entries


def _scalar(value: str) -> Any:
    if value.startswith("["):
        inner = value.strip().lstrip("[").rstrip("]")
        return [v.strip() for v in inner.split(",") if v.strip()]
    if value in ("true", "false"):
        return value == "true"
    return value.strip("\"'")


# --------------------------------------------------------------------------- #
# Fetch + extract
# --------------------------------------------------------------------------- #

def download(url: str, target: Path) -> Path:
    """Fetch the PDF unless it is already on disk.

    Some mirrors sit behind a WAF that rejects scripted downloads (403). The
    error then names the exact path to drop a manually downloaded copy into,
    because chunking works the same either way.
    """
    if target.exists() and target.stat().st_size > 0:
        print(f"  cached  {target.name} ({target.stat().st_size // 1024} KB)")
        return target
    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"  GET     {url}")
    request = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/pdf,*/*",
        "Referer": f"https://{urllib.parse.urlparse(url).netloc}/",
    })
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = response.read()
    except Exception as error:
        raise RuntimeError(
            f"{error} — mirror refused the download. Fetch it in a browser and "
            f"save it as {target}, then re-run this script."
        ) from error
    if not data.startswith(b"%PDF"):
        raise RuntimeError(
            f"{url} did not return a PDF (got {data[:16]!r}). Save the file "
            f"manually as {target} and re-run."
        )
    target.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()[:16]
    print(f"  saved   {target.name} ({len(data) // 1024} KB, sha256:{digest})")
    return target


def extract_text(pdf: Path, first: Optional[int] = None,
                 last: Optional[int] = None) -> str:
    """Extract text for the whole PDF or one page range, page breaks preserved."""
    if shutil.which("pdftotext"):
        command = ["pdftotext", "-layout"]
        if first:
            command += ["-f", str(first)]
        if last:
            command += ["-l", str(last)]
        command += [str(pdf), "-"]
        return subprocess.run(command, capture_output=True, text=True,
                              check=True).stdout
    reader = _pypdf_reader(pdf)
    if reader is None:
        raise RuntimeError(
            "need `pdftotext` (brew install poppler) or `pip install pypdf`")
    pages = reader.pages[(first - 1 if first else 0):(last if last else None)]
    return PAGE_BREAK.join(page.extract_text() or "" for page in pages)


def _pypdf_reader(pdf: Path):
    try:
        import pypdf  # type: ignore
    except ImportError:
        return None
    return pypdf.PdfReader(str(pdf))


# --------------------------------------------------------------------------- #
# Sectioning
# --------------------------------------------------------------------------- #

def outline_sections(pdf: Path, max_depth: int) -> Optional[List[Dict[str, Any]]]:
    """Sections from the PDF outline, keeping entries up to `max_depth`.

    Depth 0 is the top level (parts/chapters). Page ranges run from one kept
    entry to the next, so a chunk covers its own subsections too.
    """
    reader = _pypdf_reader(pdf)
    if reader is None:
        return None
    try:
        outline = reader.outline
    except Exception:
        return None
    if not outline:
        return None

    flat: List[Dict[str, Any]] = []

    def walk(items, depth: int) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, depth + 1)
                continue
            try:
                page = reader.get_destination_page_number(item) + 1
            except Exception:
                continue
            title = str(getattr(item, "title", "") or "").strip()
            if title:
                flat.append({"depth": depth, "title": title, "page": page})

    walk(outline, 0)
    kept = [e for e in flat if e["depth"] <= max_depth]
    if len(kept) < 3:
        return None

    total_pages = len(reader.pages)
    sections = []
    for index, entry in enumerate(kept):
        end = kept[index + 1]["page"] - 1 if index + 1 < len(kept) else total_pages
        number, _, rest = entry["title"].partition(" ")
        has_number = bool(re.fullmatch(r"[0-9A-Z]+(\.[0-9]+)*", number))
        sections.append({
            "number": number if has_number else None,
            "title": (rest or entry["title"]).strip(),
            "start_page": entry["page"],
            "end_page": max(end, entry["page"]),
        })
    return sections


def heading_sections(text: str, min_lines: int) -> List[Dict[str, Any]]:
    """Fallback sectioning: numbered headings, with small fragments merged.

    Datasheet tables are full of lines that look like headings ("2.3 VDDIO",
    "0.05 MAX"), so a candidate must be a bare line with no columnar spacing
    and no units, and short sections are folded into the previous one.
    """
    sections: List[Dict[str, Any]] = []
    current = {"number": None, "title": "front-matter", "start_page": 1, "lines": []}
    page = 1

    for raw_line in text.splitlines():
        if PAGE_BREAK in raw_line:
            page += raw_line.count(PAGE_BREAK)
            raw_line = raw_line.replace(PAGE_BREAK, "")
        candidate = raw_line.strip()
        match = HEADING_RE.match(candidate)
        is_toc_line = bool(re.search(r"\.{3,}\s*\d+\s*$", candidate))
        is_table_row = bool(TABLE_NOISE_RE.search(raw_line))
        if match and not is_toc_line and not is_table_row:
            current["end_page"] = page
            sections.append(current)
            current = {"number": match.group(1), "title": match.group(2).strip(),
                       "start_page": page, "lines": []}
            continue
        current["lines"].append(raw_line)

    current["end_page"] = page
    sections.append(current)

    merged: List[Dict[str, Any]] = []
    for section in sections:
        body = [line for line in section["lines"] if line.strip()]
        if merged and len(body) < min_lines:
            merged[-1]["lines"].extend(
                [f"### {section['number']} {section['title']}".strip()]
                + section["lines"])
            merged[-1]["end_page"] = section["end_page"]
            continue
        merged.append(section)
    return [s for s in merged if any(line.strip() for line in s["lines"])]


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value[:60] or "section"


def trim(lines: List[str]) -> List[str]:
    body = list(lines)
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return body


def write_chunks(entry: Dict[str, Any], sections: List[Dict[str, Any]],
                 pdf: Path, out_dir: Path, max_lines: int,
                 from_outline: bool) -> List[Dict[str, Any]]:
    for stale in out_dir.glob("*.md"):
        stale.unlink()
    today = datetime.date.today().isoformat()
    written: List[Dict[str, Any]] = []
    index = 0

    for section in sections:
        if from_outline:
            body = trim(extract_text(pdf, section["start_page"],
                                     section["end_page"]).replace(PAGE_BREAK, "")
                        .splitlines())
        else:
            body = trim(section["lines"])
        if not body:
            continue
        parts = [body[i:i + max_lines] for i in range(0, len(body), max_lines)]
        for part_number, part in enumerate(parts, start=1):
            index += 1
            number = section["number"] or "00"
            name_bits = [f"{index:03d}", str(number).replace(".", "-"),
                         slugify(section["title"])]
            if len(parts) > 1:
                name_bits.append(f"part{part_number}")
            path = out_dir / ("-".join(name_bits) + ".md")
            heading = (f"{number} {section['title']}" if section["number"]
                       else section["title"])
            pages = (f"{section['start_page']}" if section["start_page"] == section["end_page"]
                     else f"{section['start_page']}-{section['end_page']}")
            front = [
                "---",
                f"source: {entry['url']}",
                f"document: {entry['title']}",
                f"vendor: {entry['vendor']}",
                f'section: "{heading}"',
                f"pdf_pages: {pages}",
                f"retrieved: {today}",
                f"redistribute: {str(entry.get('redistribute', False)).lower()}",
                "---",
                "",
                f"# {heading}",
                "",
                "```text",
            ]
            path.write_text("\n".join(front + part + ["```", ""]))
            written.append({"path": path, "heading": heading, "pages": pages})
    return written


def write_index(entry: Dict[str, Any], written: List[Dict[str, Any]],
                out_dir: Path, source: str) -> None:
    lines = [
        f"# {entry['title']} — chunk index",
        "",
        f"Source: {entry['url']}  ",
        f"Vendor: {entry['vendor']} — fetched locally, not redistributed.  ",
        f"Sectioning: {source}  ",
        f"Topics: {', '.join(entry.get('topics', [])) or 'n/a'}",
        "",
        "| Chunk | Section | PDF pages |",
        "|---|---|---|",
    ]
    for item in written:
        lines.append(f"| `{item['path'].name}` | {item['heading']} | {item['pages']} |")
    lines.append("")
    (out_dir / "INDEX.md").write_text("\n".join(lines))


def build(entry: Dict[str, Any], max_lines: int, depth: int, min_lines: int) -> None:
    slug = entry["slug"]
    print(f"[{slug}] {entry['title']}")
    out_dir = DATASHEET_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = download(entry["url"], out_dir / f"{slug}.pdf")

    sections = outline_sections(pdf, depth)
    from_outline = sections is not None
    if not from_outline:
        sections = heading_sections(extract_text(pdf), min_lines)
    source = (f"PDF outline, depth <= {depth}" if from_outline
              else "numbered-heading heuristic (no usable PDF outline)")

    written = write_chunks(entry, sections, pdf, out_dir, max_lines, from_outline)
    write_index(entry, written, out_dir, source)
    print(f"  chunks  {len(written)} files via {source}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="catalog slugs (default: all)")
    parser.add_argument("--list", action="store_true", help="list catalog entries")
    parser.add_argument("--max-lines", type=int, default=400,
                        help="max text lines per chunk (default: 400)")
    parser.add_argument("--depth", type=int, default=2,
                        help="deepest PDF outline level to split on (default: 2)")
    parser.add_argument("--min-lines", type=int, default=25,
                        help="fallback mode: merge sections shorter than this")
    args = parser.parse_args()

    catalog = load_catalog(CATALOG)
    if args.list:
        for entry in catalog:
            print(f"{entry['slug']:24s} {entry['title']}")
        return 0

    unknown = set(args.slugs) - {e["slug"] for e in catalog}
    if unknown:
        print(f"unknown slugs: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2
    selected = [e for e in catalog if not args.slugs or e["slug"] in args.slugs]

    failures = []
    for entry in selected:
        try:
            build(entry, args.max_lines, args.depth, args.min_lines)
        except Exception as error:            # one dead mirror must not stop the rest
            failures.append((entry["slug"], error))
            print(f"  FAILED  {entry['slug']}: {error}", file=sys.stderr)
    if failures:
        print(f"\n{len(failures)} of {len(selected)} failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
