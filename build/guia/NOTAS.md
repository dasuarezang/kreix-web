# Guía de uso en PDF: estado y pendientes

Rama de trabajo: `guia-pdf`. No fusionar con `main` hasta revisar el borrador
(GitHub Pages publica `main`).

## Qué es
Manual de uso completo del programa de Windows y de la app del móvil. Tema claro
para imprimir, mismo diseño que la web, un PDF por idioma. Es una guía de uso,
no de venta.

## Estado (2026-11-25)
Diseño cerrado por ahora, en castellano (26 páginas, 12 capítulos): `Kreix-Guia-es.pdf`.
Falta revisar el contenido (verificar afirmaciones contra el código) antes de traducir.

## Pendiente
1. Verificar el contenido contra el código de `kreix` y quitar repeticiones.
2. Traducir a català y English.
3. Botón de descarga en el pie de la web, con el PDF del idioma de cada página
   (la tarjeta de descarga está en la rama `guia-tarjeta`).

## Cómo se genera
`python build/guia/generar.py` (necesita `pymupdf`): imprime `guia.html` con Edge o Chrome
sin cabeza, mira en qué página empieza cada capítulo, escribe esos números en el índice y
vuelve a imprimir hasta que no se muevan. Deja `Kreix-Guia-es.pdf` junto a `guia.html`.
Abrir el PDF siempre en Chrome: el visor de Edge dibuja rayas finas (juntas de teselas) en la portada.

Capturas del programa: `capturas.py`, con el Python del venv del repo `kreix`.
Capturas del móvil: `cdp.mjs` y `step*.mjs` contra Edge por CDP (puerto 9333).

## Dibujos (en `assets/perretes/`)
Portada: `blitzen-leyendo`. Índice: `img/asoma-*.png` (cabezas ya giradas). Cap. 1: `senalando` con el logo.
Cap. 5: `black-calculadora`. Cap. 7: `black-candado`. Cap. 8: `black-qr`. Cap. 11: `blitzen-lupa`.
Cierre: `dudas`. Ninguno lleva texto, para que valgan en todos los idiomas.
Para un dibujo centrado al pie de la página, la sección lleva `fill` (`fill-2` si ocupa dos páginas).

## Al cambiar de ordenador
- `capturas.py` (ruta del repo `kreix`) y `step*.mjs` (carpeta de salida) tienen
  rutas absolutas del ordenador donde se escribieron: hay que ajustarlas.
- Las imágenes ya están en `img/`; solo hace falta repetir capturas si cambia la app.

## Criterios
- No incluir nada sin verificar: el texto sale del README de `kreix` y del código
  de `pwa/`.
- Los degradados o transformaciones que se salen de la portada hacen que Chromium
  reduzca la escala de todo el PDF; por eso las rayas son SVG.
- Commits sin líneas de atribución a Claude.
