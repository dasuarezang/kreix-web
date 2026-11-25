# Guía de uso en PDF: estado y pendientes

Rama de trabajo: `guia-pdf`. No fusionar con `main` hasta revisar el borrador
(GitHub Pages publica `main`).

## Qué es
Manual de uso completo del programa de Windows y de la app del móvil. Tema claro
para imprimir, mismo diseño que la web, un PDF por idioma. Es una guía de uso,
no de venta.

## Estado (2026-11-25)
Borrador en castellano (26 páginas, 12 capítulos): `Kreix-Guia-es.pdf`.
Pendiente de revisión.

## Pendiente
1. Cambios de contenido y diseño tras la revisión.
2. Traducir a català y English.
3. Botón de descarga en el pie de la web, con el PDF del idioma de cada página.
4. Script en `build/` para regenerar los PDF.

## Cómo se genera
1. En la raíz de `kreix-web`: `python -m http.server 8765`
2. Edge headless con `--print-to-pdf --no-pdf-header-footer` sobre
   `http://localhost:8765/build/guia/guia.html`

Capturas del programa: `capturas.py`, con el Python del venv del repo `kreix`.
Capturas del móvil: `cdp.mjs` y `step*.mjs` contra Edge por CDP (puerto 9333).

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
