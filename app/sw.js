// Service worker de Kreix: guarda la app entera en el movil para que abra sin conexion.
// tools/build_pwa.py rellena la version (cambia con cualquier archivo) y la lista de archivos.
const VERSION = "5f076112a8f0";
const SHELL = `kreix-${VERSION}`;
// Pyodide y sus paquetes (unos 17 MB, en pyodide/) van en una cache aparte que se conserva entre versiones de la app
// mientras no cambie la de Pyodide: una actualizacion de Kreix no vuelve a descargarlos.
const RUNTIME = "pyodide-0.29.5";
const PYODIDE_FILES = [
 "pyodide/cffi-1.17.1-cp313-cp313-pyemscripten_2025_0_wasm32.whl",
 "pyodide/cryptography-46.0.3-cp313-abi3-pyemscripten_2025_0_wasm32.whl",
 "pyodide/pycparser-2.22-py3-none-any.whl",
 "pyodide/pyodide-lock.json",
 "pyodide/pyodide.asm.js",
 "pyodide/pyodide.asm.wasm",
 "pyodide/pyodide.js",
 "pyodide/python_stdlib.zip",
 "pyodide/six-1.17.0-py2.py3-none-any.whl",
 "pyodide/sqlalchemy-2.0.39-cp313-cp313-pyemscripten_2025_0_wasm32.whl",
 "pyodide/sqlite3-1.0.0-cp313-cp313-pyemscripten_2025_0_wasm32.whl",
 "pyodide/typing_extensions-4.15.0-py3-none-any.whl",
 "pyodide/xlrd-2.0.1-py2.py3-none-any.whl"
];
const FILES = [
 "./",
 "app.css",
 "config.json",
 "fonts/DMSans.ttf",
 "fonts/DMSansBold.ttf",
 "fonts/DMSansMedium.ttf",
 "fonts/MontserratBold.ttf",
 "fonts/MontserratExtraBold.ttf",
 "fonts/MontserratSemiBold.ttf",
 "img/apple-touch-icon.png",
 "img/dogs/black-cola.webp",
 "img/dogs/black-ojos.webp",
 "img/dogs/black.webp",
 "img/dogs/blitzen-lengua.webp",
 "img/dogs/blitzen-ojos.webp",
 "img/dogs/blitzen.webp",
 "img/dogs/durmiendo.webp",
 "img/favicon-32.png",
 "img/icon-192.png",
 "img/icon-512.png",
 "img/kreix-icono-oscuro.svg",
 "img/kreix-logotipo-claro.svg",
 "img/kreix-logotipo-oscuro.svg",
 "img/maskable-512.png",
 "index.html",
 "js/ajustes.js",
 "js/app.js",
 "js/charts.js",
 "js/core.js",
 "js/cuentas.js",
 "js/datos.js",
 "js/fountain.js",
 "js/icons.js",
 "js/inicio.js",
 "js/inversiones.js",
 "js/lock.js",
 "js/logo.js",
 "js/parts.js",
 "js/qr.js",
 "js/sky.js",
 "js/worker.js",
 "kreix.zip",
 "manifest.webmanifest",
 "vendor/jsQR.js",
 "wheels/et_xmlfile-2.0.0-py3-none-any.whl",
 "wheels/openpyxl-3.1.5-py2.py3-none-any.whl"
];

self.addEventListener("install", (event) => {
  // la version nueva entra en cuanto se descarga; la app abierta sigue con lo que ya tiene cargado y la proxima vez abre la nueva
  event.waitUntil(Promise.all([
    caches.open(SHELL).then((cache) => cache.addAll(FILES)),
    caches.open(RUNTIME).then(async (cache) => {
      const missing = [];
      for (const file of PYODIDE_FILES) if (!(await cache.match(file))) missing.push(file);
      await cache.addAll(missing);
    }),
  ]).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (event) => {
  // las versiones anteriores de la app (y de Pyodide) se borran
  event.waitUntil(caches.keys().then((keys) => Promise.all(
    keys.filter((k) => k !== SHELL && k !== RUNTIME).map((k) => caches.delete(k)))));
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const url = event.request.url;
  if (event.request.method !== "GET") return;
  if (new URL(url).origin === self.location.origin && new URL(url).pathname.includes("/pyodide/")) {
    event.respondWith(caches.open(RUNTIME).then(async (cache) => {
      const hit = await cache.match(event.request);
      if (hit) return hit;
      const response = await fetch(event.request);
      if (response.ok) cache.put(event.request, response.clone());
      return response;
    }));
    return;
  }
  if (new URL(url).origin !== self.location.origin) return;
  event.respondWith(caches.match(event.request, { ignoreSearch: true }).then((hit) => hit || fetch(event.request)));
});
