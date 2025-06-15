#!/usr/bin/env python3
"""
merge_txts.py: przechodzi przez wszystkie pliki .txt w katalogu i łączy ich zawartość
z zachowaniem prostego czyszczenia tekstu, aby uniknąć błędów podczas chunkingu.
Użycie:
    python merge_txts.py /sciezka/do/katalogu output.txt
"""
import os
import sys
import argparse
import re
from tqdm import tqdm

def clean_text(text):
    """Usuń niechciane znaki kontrolne, ujednolić odstępy i zakończenia wierszy."""
    # Znormalizuj zakończenia wierszy
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Usuń wszystkie znaki kontrolne poza \n i \t
    text = re.sub(r"[\x00-\x08\x0B-\x0C\x0E-\x1F]", "", text)
    # Skondensuj wiele spacji/tabów do jednego odstępu
    text = re.sub(r"[ \t]+", " ", text)
    # Usuń spacje na końcu linii
    text = re.sub(r"[ \t]+(?=\n)", "", text)
    return text

def gather_txt_files(root_dir):
    """Zwraca listę ścieżek do plików .txt pod root_dir."""
    txt_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.lower().endswith('.txt'):
                txt_files.append(os.path.join(dirpath, fname))
    return txt_files

def merge_files(input_dir, output_file):
    files = gather_txt_files(input_dir)
    total = len(files)
    if total == 0:
        print("Brak plików .txt w podanym katalogu.")
        return

    print(f"Znaleziono {total} plików .txt. Rozpoczynam scalanie i czyszczenie...")
    with open(output_file, 'w', encoding='utf-8') as out:
        for idx, path in enumerate(tqdm(files, desc="Scalanie", unit="plik"), start=1):
            try:
                # Użyj utf-8, fallback na cp1250
                try:
                    raw = open(path, 'r', encoding='utf-8').read()
                except UnicodeDecodeError:
                    raw = open(path, 'r', encoding='cp1250', errors='ignore').read()
                cleaned = clean_text(raw)
                out.write(cleaned)
                out.write("\n\n")  # oddziel pliki podwójną linią
            except Exception as e:
                print(f"Błąd przy pliku {path}: {e}")
    print(f"Scalanie zakończone. Wynik zapisano w {output_file}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Scal wszystkie .txt i oczyść tekst.")
    parser.add_argument('input_dir', help='Katalog z plikami .txt')
    parser.add_argument('output_file', help='Plik wyjściowy .txt')
    args = parser.parse_args()
    merge_files(args.input_dir, args.output_file)
