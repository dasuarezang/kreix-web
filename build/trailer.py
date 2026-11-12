"""Monta el tráiler de la portada dentro de index.html (entre <!--trailer--> y <!--/trailer-->).

Uso:  python build/trailer.py   y después   python build/build.py   (para llevarlo a ca/ y en/)

El tráiler se escribe en build/trailer.html. Aquí solo se rellenan sus huecos:
  {{dogs_day}}, {{dogs_night}}, {{dog_peek}}   Blitzen y Black: las mismas capas de su ilustración que usa la portada
                                               (assets/perretes, generadas con tools/web_dogs.py en el repositorio de la app)
  {{sun}}, {{moon}}                            el sol y la luna del cielo de Inicio, con su borde de pegatina
  {{qr}}                                       un código de mentira (no se puede leer): solo dibuja la escena del móvil
  {{side:inicio}}                              la barra lateral del programa, con esa pestaña marcada
"""
from __future__ import annotations

import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAV = (("inicio", "home", "Inicio"), ("cuentas", "card", "Cuentas"), ("inversiones", "trend", "Inversiones"), ("datos", "data", "Datos"))
LAYER = '<img{cls} src="assets/perretes/{name}.webp" width="770" height="606" alt="">'


def layer(name: str, cls: str = "") -> str:
    return LAYER.format(name=name, cls=f' class="{cls}"' if cls else "")


def dogs_day() -> str:
    """Los dos despiertos, con las mismas capas y en el mismo orden que la portada de día."""
    return ('<span class="tr-day">' + layer("black-cola", "tail") + layer("blitzen") + layer("blitzen-ojos", "blink") + layer("blitzen-lengua", "tongue")
            + layer("black") + layer("black-ojos", "blink blink-black") + "</span>")


def dogs_night() -> str:
    return ('<span class="tr-nap"><img src="assets/perretes-durmiendo.webp" width="720" height="374" alt="">'
            '<span class="zz zz-blitzen"><i>z</i><i>z</i><i>z</i></span><span class="zz zz-black"><i>z</i><i>z</i><i>z</i></span></span>')


def dog_peek() -> str:
    """Solo Black (su capa y sus ojos), para asomarlo por encima de una tarjeta."""
    return '<span class="tr-peek-in">' + layer("black") + layer("black-ojos", "blink blink-black") + "</span>"


def sun() -> str:
    rays = "".join(f'<rect x="13.6" y="-1.5" width="5.4" height="3" rx="1.5" transform="rotate({i * 45})"/>' for i in range(8))
    return f'<svg viewBox="-22 -22 44 44"><g class="sticker"><g class="spin">{rays}</g><circle r="10.5"/></g></svg>'


def moon() -> str:
    return ('<svg viewBox="0 0 24 24"><path class="sticker" d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>'
            '<circle class="crater" cx="9" cy="13" r="1.3"/><circle class="crater" cx="12.6" cy="17" r=".9"/></svg>')


def qr() -> str:
    """Un dibujo con aspecto de código QR, en dos fotogramas que se alternan (el de verdad también cambia varias veces por segundo)."""
    size, rng = 25, random.Random(7)
    finder = {(x, y) for cx, cy in ((0, 0), (size - 7, 0), (0, size - 7)) for x in range(cx - 1, cx + 8) for y in range(cy - 1, cy + 8)}

    def frame(cls: str) -> str:
        d = "".join(f"M{x} {y}h1v1h-1z" for y in range(size) for x in range(size) if (x, y) not in finder and rng.random() < 0.47)
        return f'<path class="{cls}" d="{d}"/>'

    eyes = "".join(f'<path d="M{x} {y}h7v7h-7zM{x + 1} {y + 1}v5h5v-5z" fill-rule="evenodd"/><rect x="{x + 2}" y="{y + 2}" width="3" height="3"/>'
                   for x, y in ((0, 0), (size - 7, 0), (0, size - 7)))
    return f'<svg viewBox="-2 -2 {size + 4} {size + 4}" shape-rendering="crispEdges">{eyes}{frame("qr-a")}{frame("qr-b")}</svg>'


def side(active: str) -> str:
    """La barra lateral. En la escena de Cuentas, la marca pasa a Inversiones a mitad de escena (clases nav-a y nav-b)."""
    items = []
    for key, icon, label in NAV:
        cls = "tw-nav"
        if key == active:
            cls += " on" + (" nav-a" if active == "cuentas" else "")
        elif active == "cuentas" and key == "inversiones":
            cls += " nav-b"
        if key == "datos":
            cls += " low"
        items.append(f'<span class="{cls}"><svg class="ic"><use href="#ti-{icon}"/></svg><b>{label}</b></span>')
    logo = '<span class="tw-logo"><img src="assets/kreix-icono-oscuro.svg" alt="" width="30" height="30">KREIX</span>'
    return '<div class="tw-side">' + logo + "".join(items) + "</div>"


def main() -> None:
    html = (ROOT / "build" / "trailer.html").read_text(encoding="utf-8")
    for key, make in (("dogs_day", dogs_day), ("dogs_night", dogs_night), ("dog_peek", dog_peek), ("sun", sun), ("moon", moon), ("qr", qr)):
        html = html.replace("{{" + key + "}}", make())
    html = re.sub(r"\{\{side:(\w+)\}\}", lambda m: side(m.group(1)), html)
    left = re.findall(r"\{\{.*?\}\}", html)
    if left:
        raise SystemExit(f"huecos sin rellenar en trailer.html: {left}")
    index = ROOT / "index.html"
    page = index.read_text(encoding="utf-8")
    if "<!--trailer-->" not in page:
        raise SystemExit("index.html no tiene las marcas <!--trailer--> y <!--/trailer-->")
    page = re.sub(r"<!--trailer-->.*?<!--/trailer-->", lambda _: "<!--trailer-->\n" + html.rstrip() + "\n    <!--/trailer-->", page, count=1, flags=re.S)
    index.write_text(page, encoding="utf-8", newline="\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"tráiler montado en index.html ({len(html) // 1024} KB)")


if __name__ == "__main__":
    main()
