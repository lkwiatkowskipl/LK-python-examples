import re
from pathlib import Path
import os

def clean_and_split_streaming(input_path, output_dir, max_part_size_mb=90):
    allowed_pattern = re.compile(r"[^a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ.,:;!?()\[\]{}\"'\-\s\n]")
    max_bytes = max_part_size_mb * 1024 * 1024  # np. 90 MB

    os.makedirs(output_dir, exist_ok=True)

    part_num = 1
    current_chunk = ''
    current_chunk_bytes = 0

    with open(input_path, 'r', encoding='utf-8', errors='ignore') as infile:
        for line in infile:
            # Oczyszczamy linijkę
            cleaned_line = allowed_pattern.sub('', line)
            cleaned_line = re.sub(r'\s+', ' ', cleaned_line)

            encoded_line = cleaned_line.encode('utf-8')
            line_size = len(encoded_line)

            if current_chunk_bytes + line_size >= max_bytes:
                # Zapisz aktualny chunk
                output_file = Path(output_dir) / f'czyszczenie_part{part_num:03}.txt'
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(current_chunk)
                print(f"✔ Zapisano: {output_file}")
                part_num += 1
                current_chunk = ''
                current_chunk_bytes = 0

            current_chunk += cleaned_line + '\n'
            current_chunk_bytes += line_size

    # Zapisz końcówkę
    if current_chunk.strip():
        output_file = Path(output_dir) / f'czyszczenie_part{part_num:03}.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(current_chunk)
        print(f"✔ Zapisano: {output_file}")

# ⬇️ ZMIENIONE: użycie r"" dla ścieżek
if __name__ == "__main__":
    clean_and_split_streaming(
        input_path=r"C:\Moje programy\mergedAllDieta.txt",
        output_dir=r"C:\Moje programy\wynik_oczyszczony",
        max_part_size_mb=90
    )
