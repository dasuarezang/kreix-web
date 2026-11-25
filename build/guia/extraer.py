"""Lista los fragmentos de texto de guia.html (la fuente en castellano) que hay que traducir.

Un fragmento es el contenido (con sus <b>, <i>, <code>, <kbd>) de cada elemento de texto que no contiene otros bloques.
Uso:  python build/guia/extraer.py            -> los imprime numerados
"""
from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup

AQUI = Path(__file__).resolve().parent
FUENTE = AQUI / "guia.html"
EN_LINEA = {"b", "i", "code", "kbd", "br", "img", "svg", "polygon", "em", "strong", "a"}
BLOQUES = ["span", "p", "li", "ul", "ol", "div", "table", "tr", "section", "dl", "figure", "header", "thead", "tbody", "dt", "dd", "td", "th", "h2", "h3", "figcaption"]
CONTENEDORES = {"p", "li", "ul", "ol", "div", "table", "tr", "section", "dl", "figure", "header", "thead", "tbody"}


def hojas(soup: BeautifulSoup):
    """Los elementos de texto: sin bloques dentro y con letras de verdad."""
    for el in soup.body.find_all(True):
        if el.name in EN_LINEA:
            continue
        if el.name in CONTENEDORES and el.find(BLOQUES):
            continue
        interior = el.decode_contents().strip()
        if re.search(r"[A-Za-zÁÉÍÓÚÜáéíóúüñÑ]{2}", re.sub(r"<[^>]+>", "", interior)):
            yield el, interior


def fragmentos() -> list[str]:
    soup = BeautifulSoup(FUENTE.read_text(encoding="utf-8"), "html.parser")
    vistos: dict[str, None] = {}
    for _, interior in hojas(soup):
        vistos.setdefault(interior, None)
    return list(vistos)


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for i, f in enumerate(fragmentos()):
        print(f"[{i}] {f}")
