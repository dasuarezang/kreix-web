"""Capturas en tema claro de la app del movil para la guia en PDF (datos de demostracion), en castellano, catalan o ingles.

Uso:  python build/guia/capturas_movil.py <es|ca|en> [salida]
Necesita la web servida en local:  python -m http.server 8765   (desde la raiz de kreix-web, con app/ al dia)
Salida: build/guia/img/<idioma>/mv-*.png (castellano: build/guia/img/mv-*.png). Mismo recorrido que los step*.mjs, pero con
los textos de los botones de cada idioma. Necesita playwright y Chrome.
"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

LANG = sys.argv[1] if len(sys.argv) > 1 else "es"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent / "img" / ("" if LANG == "es" else LANG)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = "http://localhost:8765/app/"
LANG_BUTTON = {"es": "Castellano", "ca": "Català", "en": "English"}
SAMPLE = {"es": "Probar con datos de ejemplo", "ca": "Provar amb dades d'exemple", "en": "Try with sample data"}
NO_SCROLLBAR = "<style>::-webkit-scrollbar{display:none}html{scrollbar-width:none}</style>"
PASSWORD = "correcto caballo bateria grapa"


def to_light(page) -> None:
    """La app arranca en oscuro tras la bienvenida: se pasa al claro con el boton del tema."""
    if page.evaluate("document.documentElement.getAttribute('data-theme')") != "light":
        page.evaluate("document.querySelector('header button:last-child, .topbar button:last-child')?.click()")
        page.wait_for_timeout(700)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        ctx = browser.new_context(viewport={"width": 496, "height": 751}, device_scale_factor=1, is_mobile=True, has_touch=True,
                                  color_scheme="light")
        page = ctx.new_page()
        page.clock.install(time=datetime.now().replace(hour=11, minute=30, second=0, microsecond=0))   # la app elige tema y saludo por la hora: de dia
        page.clock.resume()
        page.add_init_script("try { localStorage.setItem('kreix.theme', 'light'); } catch (e) {}")   # tema claro tambien en la contrasena y la bienvenida
        page.goto(f"{BASE}?lang={LANG}")
        page.wait_for_timeout(11000)
        page.evaluate(f"document.head.insertAdjacentHTML('beforeend', {NO_SCROLLBAR!r})")
        page.evaluate("""(pw) => { const [p, q] = document.querySelectorAll('input[type=password]');
            const set = (el, v) => { el.value = v; el.dispatchEvent(new Event('input', {bubbles: true})); }; set(p, pw); set(q, pw); }""", PASSWORD)
        page.wait_for_timeout(1200)
        page.screenshot(path=str(OUT / "mv-bloqueo.png"))
        page.evaluate("document.querySelector('form.panel button[type=submit]').click()")
        page.wait_for_timeout(7000)
        page.evaluate(f"document.head.insertAdjacentHTML('beforeend', {NO_SCROLLBAR!r})")
        page.evaluate("(t) => [...document.querySelectorAll('button')].find(b => b.innerText.trim() === t).click()", LANG_BUTTON[LANG])
        page.wait_for_timeout(1500)
        page.evaluate("""() => { const i = document.querySelector('input[type=text]'); i.value = 'Blitzen'; i.dispatchEvent(new Event('input', {bubbles: true})); }""")
        page.wait_for_timeout(600)
        page.screenshot(path=str(OUT / "mv-bienvenida.png"))
        page.evaluate("document.querySelector('button.btn.primary').click()")
        page.wait_for_timeout(4000)
        to_light(page)
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(600)
        page.screenshot(path=str(OUT / "mv-vacio.png"))
        page.evaluate("(t) => [...document.querySelectorAll('button,a')].find(b => b.innerText.trim() === t).click()", SAMPLE[LANG])
        page.wait_for_timeout(6000)
        to_light(page)
        for pid in ("inicio", "cuentas", "inversiones", "datos", "ajustes"):
            page.evaluate(f"document.querySelector('.tabbar button[data-page=\"{pid}\"]').click()")
            page.wait_for_timeout(2500)
            height = page.evaluate("document.documentElement.scrollHeight")
            for i, y in enumerate((0, 800, 1600, 2400)):
                if y > height - 400:
                    break
                page.evaluate(f"window.scrollTo(0, {y})")
                page.wait_for_timeout(900)
                page.screenshot(path=str(OUT / f"mv-{pid}-{i}.png"))
        browser.close()
    print("Capturas del movil en", OUT)


if __name__ == "__main__":
    main()
