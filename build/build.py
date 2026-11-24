"""Genera la web en catalán (ca/) e inglés (en/) a partir de index.html, que es la fuente en castellano.

Uso:  python build/build.py
Cada texto de build/translations.py se busca TAL CUAL en index.html; si alguno ya no aparece (porque se cambió el castellano),
el script falla y dice cuál, para que ninguna página se quede con un texto a medias.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from translations import T  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SOURCE = (ROOT / "index.html").read_text(encoding="utf-8")
LANGS = {"ca": (0, "ca", "ca_ES"), "en": (1, "en", "en_GB")}
ORDER = sorted(T, key=len, reverse=True)                        # primero los textos largos: nunca se pisan
PATTERN = re.compile("|".join(re.escape(k) for k in ORDER))


FLAGS = {          # banderas (24x24) con las esquinas suaves, las mismas que dibuja el programa en Ajustes
    "es": '<rect width="24" height="24" fill="#C60B1E"/><rect y="6" width="24" height="12" fill="#FFC400"/>',
    "ca": '<rect width="24" height="24" fill="#FCDD09"/>' + "".join(f'<rect y="{i * 24 / 9:.3f}" width="24" height="{24 / 9:.3f}" fill="#DA121A"/>' for i in (1, 3, 5, 7)),
    "en": ('<rect width="24" height="24" fill="#012169"/><path d="M0 0L24 24M24 0L0 24" stroke="#fff" stroke-width="4.8"/>'
           '<path d="M0 0L24 24M24 0L0 24" stroke="#C8102E" stroke-width="1.6"/><path d="M12 0V24M0 12H24" stroke="#fff" stroke-width="7"/>'
           '<path d="M12 0V24M0 12H24" stroke="#C8102E" stroke-width="4"/>'),
}


def _flag(code: str, uid: str) -> str:
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><clipPath id="{uid}"><rect width="24" height="24" rx="3.4"/></clipPath><g clip-path="url(#{uid})">{FLAGS[code]}</g></svg>'


def _targets(lang: str) -> dict[str, str]:
    """Enlaces relativos a cada idioma desde la pagina de `lang`."""
    return {
        "es": {"es": "./", "ca": "ca/", "en": "en/"},
        "ca": {"es": "../", "ca": "./", "en": "../en/"},
        "en": {"es": "../", "ca": "../ca/", "en": "./"},
    }[lang]


NAMES = {"es": "Castellano", "ca": "Català", "en": "English"}
LABEL = {"es": "Idioma", "ca": "Idioma", "en": "Language"}
CHEVRON = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'


def switcher(lang: str) -> str:
    """El selector de idioma de la cabecera: un boton con el idioma actual que abre la lista (en el movil, la lista va siempre a la vista)."""
    to = _targets(lang)
    links = "".join(
        f'<a href="{to[code]}" lang="{code}" hreflang="{code}" title="{NAMES[code]}" aria-label="{NAMES[code]}"' + (' aria-current="true"' if code == lang else "") + ">"
        f'{_flag(code, "flag-" + code)}<span>{NAMES[code]}</span></a>'
        for code in ("es", "ca", "en")
    )
    button = (f'<button class="lang-btn" type="button" aria-expanded="false" aria-controls="lang-list" aria-label="{LABEL[lang]}: {NAMES[lang]}">'
              f'{_flag(lang, "flag-btn")}<span>{lang.upper()}</span>{CHEVRON}</button>')
    return f'<!--lang--><nav class="lang" aria-label="{LABEL[lang]}">{button}<div class="lang-list" id="lang-list">{links}</div></nav><!--/lang-->'


def footer_langs(lang: str) -> str:
    """Los tres idiomas como enlaces de texto en el pie."""
    to = _targets(lang)
    links = "".join(
        f'<a href="{to[code]}" lang="{code}" hreflang="{code}"' + (' aria-current="true"' if code == lang else "") + f">{NAMES[code]}</a>"
        for code in ("es", "ca", "en")
    )
    return f'<!--flang--><div class="foot-lang" role="group" aria-label="{LABEL[lang]}">{links}</div><!--/flang-->'


def fill_switchers(html: str, lang: str) -> str:
    html = re.sub(r"<!--lang-->.*?<!--/lang-->", lambda _: switcher(lang), html, count=1, flags=re.S)
    return re.sub(r"<!--flang-->.*?<!--/flang-->", lambda _: footer_langs(lang), html, count=1, flags=re.S)


def build(lang: str) -> str:
    index, html_lang, og_locale = LANGS[lang]
    used: set[str] = set()

    def swap(match: re.Match[str]) -> str:
        used.add(match.group(0))
        return T[match.group(0)][index]

    out = PATTERN.sub(swap, SOURCE)
    missing = [k for k in T if k not in used]
    if missing:
        raise SystemExit(f"[{lang}] estos textos de translations.py ya no estan en index.html:\n  " + "\n  ".join(m[:90] for m in missing))
    out = out.replace('<html lang="es"', f'<html lang="{html_lang}"', 1)
    out = out.replace('content="es_ES"', f'content="{og_locale}"', 1)
    out = fill_switchers(out, lang)
    # rutas: la pagina vive un nivel mas abajo; las capturas son las de la app en ese idioma
    out = out.replace("assets/shots/", f"../assets/shots/{lang}/")
    out = re.sub(r'(href|src|srcset)="assets/', r'\1="../assets/', out)
    out = out.replace('href="styles.css', 'href="../styles.css').replace('src="script.js', 'src="../script.js')
    out = out.replace('href="app/"', f'href="../app/?lang={lang}"')       # la app del movil abre en el idioma de la pagina
    return out


def untranslated(lang: str, html: str) -> list[str]:
    """Textos que han quedado igual que en castellano (nombres propios aparte): para repasarlos a mano."""
    def texts(s: str) -> set[str]:
        found = set(re.findall(r">([^<>]{4,})<", s))
        found |= set(re.findall(r'(?:alt|aria-label|title|content)="([^"]{4,})"', s))
        return {t.strip() for t in found if re.search(r"[a-záéíóúñ]{3}", t.lower())}
    return sorted(texts(SOURCE) & texts(html))


def main() -> None:
    global SOURCE
    es = fill_switchers(SOURCE, "es")
    if es != SOURCE:                                       # el selector del castellano tambien sale de aqui
        (ROOT / "index.html").write_text(es, encoding="utf-8", newline="\n")
        SOURCE = es
    for lang in LANGS:
        html = build(lang)
        target = ROOT / lang
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(html, encoding="utf-8", newline="\n")
        same = untranslated(lang, html)
        print(f"{lang}/index.html escrito ({len(html) // 1024} KB). Iguales que en castellano: {same}")


if __name__ == "__main__":
    main()
