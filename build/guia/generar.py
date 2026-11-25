"""Genera Kreix-Guia-es.pdf a partir de guia.html (Edge o Chrome sin cabeza) y rellena los numeros de pagina del indice.

Uso:  python build/guia/generar.py
Primero imprime el PDF, mira en que pagina empieza cada capitulo, escribe esos numeros en el indice de guia.html y vuelve a
imprimir para comprobar que no se ha movido nada. Necesita pymupdf (pip install pymupdf).
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf

AQUI = Path(__file__).resolve().parent
HTML = AQUI / "guia.html"
SALIDA = AQUI / "Kreix-Guia-es.pdf"
NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]


def imprimir(destino: Path) -> None:
    navegador = next((n for n in NAVEGADORES if Path(n).exists()), None)
    if not navegador:
        sys.exit("No encuentro Edge ni Chrome.")
    subprocess.run([navegador, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={destino}", HTML.as_uri()],
                   check=True, capture_output=True, timeout=180)


def paginas_de_capitulos(pdf: Path, titulos: list[str]) -> list[int]:
    """Pagina en la que empieza cada capitulo: la del encabezado «N Titulo» (el titulo puede ocupar dos lineas; el indice, pagina 2, no cuenta)."""
    with pymupdf.open(pdf) as doc:
        textos = [" ".join(doc[i].get_text().split()) for i in range(len(doc))]
    encontradas: list[int] = []
    for n, titulo in enumerate(titulos, start=1):
        pagina = next((i + 1 for i in range(2, len(textos)) if f"{n} {titulo}" in textos[i]), None)
        if pagina is None:
            sys.exit(f"No encuentro el capitulo «{n} {titulo}» en el PDF.")
        encontradas.append(pagina)
    return encontradas


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    titulos = re.findall(r'<li><b>\d+</b><span>([^<]+)</span><i class="pg">', html)
    if not titulos:
        sys.exit("El indice de guia.html no tiene los <i class=\"pg\"> esperados.")
    with tempfile.TemporaryDirectory() as tmp:
        prueba = Path(tmp) / "prueba.pdf"
        for intento in range(3):
            imprimir(prueba)
            paginas = paginas_de_capitulos(prueba, titulos)
            nuevo = html
            for titulo, n in zip(titulos, paginas):
                nuevo = re.sub(rf'(<span>{re.escape(titulo)}</span><i class="pg">)[^<]*(</i>)', rf"\g<1>{n}\g<2>", nuevo, count=1)
            if nuevo == html:
                break
            html = nuevo
            HTML.write_text(html, encoding="utf-8")
        else:
            sys.exit("Los numeros de pagina no se estabilizan.")
        SALIDA.write_bytes(prueba.read_bytes())
    with pymupdf.open(SALIDA) as doc:
        total = len(doc)
    print(f"{SALIDA.name}: {total} paginas. Capitulos en las paginas {paginas}.")


if __name__ == "__main__":
    main()
