"""Genera guia.ca.html y guia.en.html a partir de guia.html (la fuente en castellano) y de las traducciones trad_<idioma>_*.txt.

Cada traduccion es una linea «[n] texto», donde n es el numero de fragmento que lista extraer.py. fragmentos_es.txt guarda el
castellano con el que se tradujo: si se cambia guia.html, este script dice que fragmentos hay que volver a traducir.
Las capturas de cada idioma estan en img/ca y img/en (capturas.py y capturas_movil.py).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

from extraer import FUENTE, fragmentos, hojas

AQUI = Path(__file__).resolve().parent
IDIOMAS = {
    "ca": {"title": "Kreix · Guia d'ús", "pie": "Kreix · Guia d'ús"},
    "en": {"title": "Kreix · User guide", "pie": "Kreix · User guide"},
}


def leer_traduccion(idioma: str) -> dict[int, str]:
    textos: dict[int, str] = {}
    for archivo in sorted(AQUI.glob(f"trad_{idioma}_*.txt")):
        for linea in archivo.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\[(\d+)\] (.*)$", linea)
            if m:
                textos[int(m.group(1))] = m.group(2)
    return textos


def comprobar(frags: list[str], textos: dict[int, str], idioma: str) -> None:
    referencia = re.findall(r"^\[(\d+)\] (.*)$", (AQUI / "fragmentos_es.txt").read_text(encoding="utf-8"), re.M)
    cambiados = [int(n) for n, t in referencia if int(n) >= len(frags) or frags[int(n)] != t] + list(range(len(referencia), len(frags)))
    if len(referencia) != len(frags) or cambiados:
        sys.exit(f"[{idioma}] guia.html ha cambiado desde la traduccion. Fragmentos por revisar: {cambiados[:20]}")
    faltan = [i for i in range(len(frags)) if i not in textos]
    if faltan:
        sys.exit(f"[{idioma}] faltan traducciones de los fragmentos {faltan[:20]}")


def construir(idioma: str) -> Path:
    frags = fragmentos()
    textos = leer_traduccion(idioma)
    comprobar(frags, textos, idioma)
    por_fuente = {f: textos[i] for i, f in enumerate(frags)}
    soup = BeautifulSoup(FUENTE.read_text(encoding="utf-8"), "html.parser")
    for el, interior in list(hojas(soup)):
        el.clear()
        el.append(BeautifulSoup(por_fuente[interior], "html.parser"))
    soup.html["lang"] = idioma
    soup.title.string = IDIOMAS[idioma]["title"]
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src.startswith("img/pc-") or src.startswith("img/mv-"):
            img["src"] = f"img/{idioma}/{src[4:]}"
            if not (AQUI / img["src"]).exists():
                sys.exit(f"[{idioma}] falta la captura {img['src']}")
    estilo = soup.new_tag("style")
    estilo.string = f'@page {{ @bottom-left {{ content: "{IDIOMAS[idioma]["pie"]}"; }} }}'
    soup.head.append(estilo)
    destino = AQUI / f"guia.{idioma}.html"
    destino.write_text(str(soup), encoding="utf-8")
    return destino


if __name__ == "__main__":
    for idioma in IDIOMAS:
        print(construir(idioma).name)
