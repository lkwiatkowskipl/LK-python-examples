#!/usr/bin/env python
# coding: utf-8
"""
pdf2txt_hardclean.py
• Ekstrakcja tekstu z PDF-ów (PyMuPDF)
• Bardzo agresywne czyszczenie:
  – URL/DOI/e-mail/tel  (także „http: xyz”, „www xyz”)
  – klauzule prawne (ponad 120 rdzeni haseł)
  – linie referencji (nazwisko + rok)
  – linie z ≥60 % cyfr lub ≥70 % znaków niealfanum.
  – nagłówki/stopy powtarzane na ≥70 % stron
• Grupowanie tak, by wynikowych *.txt* było ≤ 300
Wymagania:  pip install --upgrade pymupdf unidecode
"""
from pathlib import Path
import re, math, logging, fitz
from unidecode import unidecode

SRC_DIR = Path(r"C:\LLM\PDFsToScan\Dieta")
DST_DIR = Path(r"C:\LLM\PDFsToScan\Dieta_txt")
ENC     = "utf-8"

MAX_TXT   = 300          # limit Notebook LM
INIT_CHRS = 1_300_000    # startowy limit znaków w paczce
INIT_PDFS = 25           # startowy limit PDF-ów w paczce
HDR_THR   = .70          # próg nagłówek/stopka
MIN_LEN   = 1_500        # minimalna długość gotowego TXT

# --- słowa-klucze (rdzenie) ---
LEGAL = [
    "copyright", "all rights reserved", "no part of", "reprodu", "redistribu",
    "unauthoriz", "information storage", "retrieval system", "isbn", "issn",
    "library of congress", "publisher", "printed in", "manufactured in",
    "warranty", "disclaimer", "liabil", "responsib", "trademark", "registered",
    "elsevier", "springer", "wiley", "mcgraw", "cengage", "wolters",
]

LEGAL_RE = re.compile("|".join(LEGAL), re.I)
URL_RE   = re.compile(r"(https?\s*:\s*\S+|www\s+\S+\.\w+|www\.\S+|doi\s*[:/]\s*\S+)",
                      re.I)
MAIL_RE  = re.compile(r"[A-Za-z0-9._%+-]+@\S+\.\w+")
REF_RE   = re.compile(r"[A-Z][a-z]{2,}\s+[A-Z]\w+.*\(\d{4}\)")
ALLOWED  = re.compile(r"[^A-Za-z0-9.,;:!?\-()\[\]'\" \r\n]+")

logging.basicConfig(format="%(levelname)s %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

# ---------- funkcje pomocnicze ----------
def strip_headers(pages: list[str]) -> list[str]:
    cnt = {}
    for p in pages:
        for ln in (*p.splitlines()[:1], *p.splitlines()[-1:]):
            cnt[ln.strip()] = cnt.get(ln.strip(), 0) + 1
    killers = {k for k, v in cnt.items() if v >= HDR_THR * len(pages)}
    return ["\n".join(ln for ln in p.splitlines() if ln.strip() not in killers)
            for p in pages]

def kill_line(ln: str) -> bool:
    if (LEGAL_RE.search(ln) or URL_RE.search(ln) or MAIL_RE.search(ln) or
        REF_RE.search(ln)):
        return True
    if ln and sum(ch.isdigit() for ch in ln) / len(ln) > .6:
        return True
    if len(re.sub(r"[A-Za-z0-9]", "", ln)) > .7 * len(ln):
        return True
    return False

def clean(raw: str) -> str:
    txt = unidecode(raw)
    keep = []
    for ln in txt.splitlines():
        ln = re.sub(r"[ ]{2,}", " ", ln)        # kolumny → pojedyncze spacje
        if not kill_line(ln):
            keep.append(ln)
    txt = "\n".join(keep)
    txt = ALLOWED.sub(" ", txt)
    txt = re.sub(r"[ ]{2,}", " ", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()

def pdf_to_txt(pdf: Path) -> str:
    try:
        with fitz.open(pdf) as doc:
            pages = [p.get_text("text") for p in doc]
        return clean("\n".join(strip_headers(pages)))
    except Exception as e:
        log.error("❌ %s – %s", pdf.name, e)
        return ""

def flush(idx: int, buf: list[str], names: list[str]) -> None:
    body = "\n\n".join(buf)
    if len(body) < MIN_LEN:
        log.warning("⚠ group_%04d pominięty – %d znaków", idx, len(body))
        return
    # walidacja końcowa
    if LEGAL_RE.search(body) or URL_RE.search(body) or MAIL_RE.search(body):
        body = "\n".join(l for l in body.splitlines()
                         if not (LEGAL_RE.search(l) or URL_RE.search(l) or MAIL_RE.search(l)))
    out = DST_DIR / f"group_{idx:04d}.txt"
    out.write_text(body, encoding=ENC)
    log.info("group_%04d.txt  %2d PDF | %.1f kB",
             idx, len(names), out.stat().st_size / 1024)

# ---------- MAIN ----------
def main():
    pdfs = sorted(SRC_DIR.rglob("*.pdf"))
    if not pdfs:
        log.error("Brak PDF-ów w %s", SRC_DIR)
        return
    DST_DIR.mkdir(parents=True, exist_ok=True)

    max_chars, max_pdfs = INIT_CHRS, INIT_PDFS
    idx = 1
    buf, names, char_sum = [], [], 0
    total = len(pdfs)

    for n, pdf in enumerate(pdfs, 1):
        txt = pdf_to_txt(pdf)
        if not txt:
            continue
        # Czy trzeba zapisać paczkę?
        if (char_sum + len(txt) > max_chars or len(names)+1 > max_pdfs or
            (idx >= MAX_TXT and buf)):
            flush(idx, buf, names)
            idx, buf, names, char_sum = idx+1, [], [], 0
        buf.append(txt); names.append(pdf.name); char_sum += len(txt)

        # dynamiczne zwiększanie limitów, by zmieścić się w 300
        slots, left = MAX_TXT - idx + 1, total - n
        if slots and left / slots > max_pdfs:
            max_pdfs  = math.ceil(left / slots)
            max_chars = int(max_chars * 1.25)

    if buf:
        flush(idx, buf, names)
    log.info("✅ Gotowe – %d plików TXT (limit %d)", idx, MAX_TXT)

if __name__ == "__main__":
    main()
