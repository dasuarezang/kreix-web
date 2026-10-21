<p align="center">
  <img src="assets/kreix-icono-oscuro.svg" alt="Kreix" width="72">
</p>

<h1 align="center">kreix-web</h1>

<p align="center">
  Web de descarga y guía de uso de <a href="https://github.com/dasuarezang/kreix">Kreix</a>, la app de finanzas personales para Windows que funciona sin conexión y guarda todo cifrado.<br>
  <b><a href="https://dasuarezang.github.io/kreix-web/">dasuarezang.github.io/kreix-web</a></b>
</p>

## Qué hay

- **Una sola página en tres idiomas:** `index.html` es la fuente en castellano; `build/build.py` genera `ca/` y `en/` con los textos de `build/translations.py` y falla si algún texto ya no aparece, para que ninguna página quede a medias.
- **HTML, CSS y JavaScript sin dependencias** (`styles.css`, `script.js`): tema claro u oscuro según el dispositivo, menú para móvil, pestañas de la guía y la demostración del modo privacidad.
- **Descarga según el sistema:** en Windows, el botón baja el instalador; en móvil, Mac o Linux se avisa de que Kreix es para Windows y se ofrece copiar el enlace (con un enlace pequeño para descargarlo igualmente).
- **Blitzen y Black:** de noche (tema oscuro) duermen junto a las barras de la portada; de día (tema claro) están despiertos y animados con CSS; en la llamada a descargar señalan el botón con la pata.
- **Diseño sobrio, el mismo que el del programa:** fondos planos, esquinas de 6 px como mucho, bordes finos y sin sombras.

## Publicación

- La web se sirve con GitHub Pages desde `main`.
- El instalador (`Kreix-Setup-<versión>.exe`) se publica como *release* de este repositorio; los botones de descarga apuntan a esa *release*.
- Las capturas (`assets/shots/`) y los perros (`assets/perretes/`) se generan desde el repositorio de la app con `tools/web_shots.py` y `tools/web_dogs.py`.

Para regenerar las páginas en catalán e inglés tras cambiar `index.html` o `build/translations.py`:

```powershell
python build/build.py
```

## Licencia

© 2026 [Daniel Suárez Angosto](https://dasuarezang.github.io). Todos los derechos reservados. Kreix se distribuye bajo la [PolyForm Strict License 1.0.0](https://github.com/dasuarezang/kreix/blob/main/LICENSE). Las tipografías (DM Sans y Montserrat) son libres; sus licencias están en `assets/fonts/LICENCIAS.txt`.
