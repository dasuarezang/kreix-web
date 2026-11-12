"""Graba el tráiler de la portada en un archivo de vídeo (MP4), fotograma a fotograma.

Uso:  python build/trailer_video.py [salida.mp4] [--vertical] [--lang es|ca|en] [--theme dark|light]

Abre la página en Chrome sin ventana, sustituye el reloj del navegador por uno propio y avanza el tráiler 1/30 de segundo
cada vez (el reproductor y todas las animaciones CSS), sacando una captura por fotograma. Así el vídeo sale fluido y siempre
igual, tarde lo que tarde cada captura. Horizontal: 1920x1080. Vertical (--vertical): 1080x1920, con el lienzo de móvil.

Necesita:  pip install playwright imageio-ffmpeg   (usa el Chrome ya instalado; no descarga otro navegador)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
FPS = 30
TAIL = 2.0          # segundos que se queda el último plano

CLOCK = """
window.__q = []; window.__now = 0; window.__times = new WeakMap();
performance.now = function () { return window.__now; };
window.requestAnimationFrame = function (cb) { window.__q.push(cb); return window.__q.length; };
window.cancelAnimationFrame = function () { window.__q = []; };
window.__step = function (dt) {
  window.__now += dt;
  var q = window.__q; window.__q = [];
  q.forEach(function (cb) { cb(window.__now); });
  document.getAnimations().forEach(function (a) {
    var t = window.__times.get(a);
    if (t === undefined) { t = 0; a.pause(); } else t += dt;
    window.__times.set(a, t);
    try { a.currentTime = t; } catch (e) {}
  });
  return document.getElementById("trailer").getAttribute("data-state");
};
"""

STYLE = """
header.top, .hero > :not(.trailer), main > :not(.hero), footer, .to-top, .tr-start, .tr-segs, .tr-toggle { display: none !important; }
html, body { overflow: hidden; }
.hero { width: auto !important; margin: 0 !important; padding: 0 !important; }
.trailer { margin: 0 !important; padding: %(pad)s; }
.tr-row { justify-content: center; margin-top: %(gap)s !important; }
.tr-caps { flex: none !important; width: 100%%; min-height: 0 !important; text-align: center; justify-items: center; font-size: %(font)s !important; color: var(--text) !important; }
.tr-caps li.on { max-width: 30em; }
"""


def main() -> None:
    args = argparse.ArgumentParser()
    args.add_argument("out", nargs="?", default="kreix-trailer.mp4")
    args.add_argument("--vertical", action="store_true")
    args.add_argument("--lang", default="es", choices=("es", "ca", "en"))
    args.add_argument("--theme", default="dark", choices=("dark", "light"))
    opt = args.parse_args()

    if opt.vertical:      # 540 px de ancho CSS (el lienzo de móvil entra por debajo de 640) al doble de densidad: 1080x1920
        view, scale, style = {"width": 540, "height": 960}, 2, STYLE % {"pad": "96px 20px 0", "gap": "34px", "font": "23px"}
    else:
        view, scale, style = {"width": 1920, "height": 1080}, 1, STYLE % {"pad": "36px 160px 0", "gap": "30px", "font": "32px"}
    page_file = ROOT / ("index.html" if opt.lang == "es" else f"{opt.lang}/index.html")
    width, height = view["width"] * scale, view["height"] * scale

    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(viewport=view, device_scale_factor=scale, color_scheme=opt.theme)
        page = context.new_page()
        page.add_init_script(CLOCK)
        page.goto(page_file.as_uri())
        page.add_style_tag(content=style)
        page.evaluate("theme => document.documentElement.setAttribute('data-theme', theme)", opt.theme)
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(600)
        total = page.evaluate("Array.from(document.querySelectorAll('.tr-scene')).reduce((s, e) => s + +e.dataset.d, 0)") / 1000
        frames = round((total + TAIL) * FPS)

        ffmpeg = subprocess.Popen(
            [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
             "-vf", f"scale={width}:{height}", "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", opt.out],
            stdin=subprocess.PIPE)
        page.evaluate("document.getElementById('tr-toggle').click()")
        for i in range(frames):
            page.evaluate("dt => window.__step(dt)", 1000 / FPS)
            ffmpeg.stdin.write(page.screenshot(type="jpeg", quality=95))
            if i % 150 == 0:
                print(f"{i}/{frames}", flush=True)
        ffmpeg.stdin.close()
        ffmpeg.wait()
        browser.close()
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"{opt.out}: {total + TAIL:.1f} s, {width}x{height}, {Path(opt.out).stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
