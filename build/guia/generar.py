"""Genera Kreix-Guia-es.pdf a partir de guia.html (Edge o Chrome sin cabeza) y rellena los numeros de pagina del indice.

Uso:  python build/guia/generar.py [es] [ca] [en]     (sin argumentos: los tres idiomas)
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
IDIOMAS = ("es", "ca", "en")
NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]


def imprimir(html: Path, destino: Path) -> None:
    navegador = next((n for n in NAVEGADORES if Path(n).exists()), None)
    if not navegador:
        sys.exit("No encuentro Edge ni Chrome.")
    subprocess.run([navegador, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={destino}", html.as_uri()],
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


def optimizar(origen: Path, destino: Path) -> None:
    """Reduce las imagenes a 150 ppp como mucho (los dibujos y capturas salen de Chrome mucho mas grandes de lo que hace falta en una pagina A4)."""
    pymupdf.TOOLS.mupdf_display_errors(False)
    with pymupdf.open(origen) as doc:
        doc.rewrite_images(dpi_threshold=170, dpi_target=150, quality=82)
        doc.save(destino, garbage=3, deflate=True)


def generar(idioma: str) -> None:
    if idioma != "es":
        from traducir import construir
        construir(idioma)
    html_path = AQUI / ("guia.html" if idioma == "es" else f"guia.{idioma}.html")
    salida = AQUI / f"Kreix-Guia-{idioma}.pdf"
    html = html_path.read_text(encoding="utf-8")
    titulos = re.findall(r'<li><b>\d+</b><span>([^<]+)</span><i class="pg">', html)
    if not titulos:
        sys.exit("El indice de guia.html no tiene los <i class=\"pg\"> esperados.")
    with tempfile.TemporaryDirectory() as tmp:
        prueba = Path(tmp) / "prueba.pdf"
        for _ in range(3):
            imprimir(html_path, prueba)
            paginas = paginas_de_capitulos(prueba, titulos)
            nuevo = html
            for titulo, n in zip(titulos, paginas):
                nuevo = re.sub(rf'(<span>{re.escape(titulo)}</span><i class="pg">)[^<]*(</i>)', rf"\g<1>{n}\g<2>", nuevo, count=1)
            if nuevo == html:
                break
            html = nuevo
            html_path.write_text(html, encoding="utf-8")
        else:
            sys.exit("Los numeros de pagina no se estabilizan.")
        optimizar(prueba, salida)
    with pymupdf.open(salida) as doc:
        total = len(doc)
    print(f"{salida.name}: {total} paginas. Capitulos en las paginas {paginas}.")


def main() -> None:
    elegidos = sys.argv[1:] or list(IDIOMAS)
    for idioma in elegidos:
        generar(idioma)


if __name__ == "__main__":
    main()
