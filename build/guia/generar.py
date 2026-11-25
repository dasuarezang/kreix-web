"""Genera Kreix-Guia-es.pdf a partir de guia.html (Edge o Chrome sin cabeza) y rellena los numeros de pagina del indice.

Uso:  python build/guia/generar.py [es] [ca] [en]     (sin argumentos: los tres idiomas)
Primero imprime el PDF, mira en que pagina empieza cada capitulo, escribe esos numeros en el indice de guia.html y vuelve a
imprimir para comprobar que no se ha movido nada. Necesita pymupdf (pip install pymupdf).
"""
from __future__ import annotations

import re
import shutil
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


def preparar_copia(html_path: Path, tmp: Path) -> Path:
    """Copia la guia a una carpeta temporal con las imagenes ya reducidas (Chrome las incrusta tal cual: las capturas, a JPEG de 1000 px
    como mucho, y los dibujos con transparencia, a 640 px). Optimizar el PDF despues con MuPDF rompia los degradados del logo."""
    from PIL import Image

    raiz = AQUI.parent.parent
    (tmp / "build" / "guia").mkdir(parents=True)
    shutil.copytree(raiz / "assets" / "fonts", tmp / "assets" / "fonts")
    shutil.copy(raiz / "assets" / "kreix-icono-oscuro.svg", tmp / "assets" / "kreix-icono-oscuro.svg")
    (tmp / "assets" / "perretes").mkdir(parents=True)
    texto = html_path.read_text(encoding="utf-8")

    def reducir(origen: Path, destino: Path, ancho: int) -> Path:
        im = Image.open(origen)
        if im.width > ancho:
            im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
        destino.parent.mkdir(parents=True, exist_ok=True)
        if im.mode in ("RGBA", "LA", "P"):
            im.convert("RGBA").save(destino.with_suffix(".png"), optimize=True)
            return destino.with_suffix(".png")
        im.convert("RGB").save(destino.with_suffix(".jpg"), quality=85, optimize=True)
        return destino.with_suffix(".jpg")

    for ref in sorted(set(re.findall(r'src="((?:\.\./\.\./assets/perretes/|img/)[^"]+)"', texto))):
        origen = (AQUI / ref).resolve()
        destino = (tmp / "build" / "guia" / ref).resolve()
        ancho = 1000 if ref.startswith("img/") and origen.suffix == ".png" and ("/pc-" in ref or "/mv-" in ref or ref.startswith(("img/pc-", "img/mv-"))) else 640
        nuevo = reducir(origen, destino, ancho)
        if nuevo.suffix != origen.suffix:
            texto = texto.replace(f'src="{ref}"', f'src="{ref[: -len(origen.suffix)]}{nuevo.suffix}"')
    shutil.copy(AQUI / "guia.css", tmp / "build" / "guia" / "guia.css")
    copia = tmp / "build" / "guia" / html_path.name
    copia.write_text(texto, encoding="utf-8")
    return copia


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
            copia_dir = Path(tmp) / "copia"
            shutil.rmtree(copia_dir, ignore_errors=True)
            imprimir(preparar_copia(html_path, copia_dir), prueba)
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
        salida.write_bytes(prueba.read_bytes())
    with pymupdf.open(salida) as doc:
        total = len(doc)
    print(f"{salida.name}: {total} paginas. Capitulos en las paginas {paginas}.")


def main() -> None:
    elegidos = sys.argv[1:] or list(IDIOMAS)
    for idioma in elegidos:
        generar(idioma)


if __name__ == "__main__":
    main()
