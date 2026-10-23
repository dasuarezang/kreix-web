// Piezas comunes de la interfaz: hablar con la logica (worker), construir el DOM, traducir y avisar.
import { SHAPES } from "./icons.js";
import { WORDMARK } from "./logo.js";

// ----------------------------------------------------------------------------- logica (Pyodide en un worker)
const worker = new Worker("js/worker.js");
const pending = new Map();
let nextId = 1;
let onProgress = () => {};

worker.onmessage = (event) => {
  const { id, ok, error, trace, progress } = event.data;
  if (progress) return onProgress(progress);
  const waiter = pending.get(id);
  if (!waiter) return;
  pending.delete(id);
  if (error !== undefined) {
    console.error(trace || error);
    waiter.reject(new Error(error));
  } else waiter.resolve(ok);
};

/** Llama a una funcion de pwa/py/kreix_web.py y devuelve su resultado. */
export function py(fn, args = {}) {
  return new Promise((resolve, reject) => {
    const id = nextId++;
    pending.set(id, { resolve, reject });
    worker.postMessage({ id, fn, args });
  });
}

export function watchProgress(callback) { onProgress = callback; }

// ----------------------------------------------------------------------------- textos fijos
let catalog = {};

/** Como `tr` del escritorio: el texto original (castellano) es la clave. */
export function t(text) { return catalog[text] || text; }
export function setCatalog(entries) { catalog = entries || {}; }

// ----------------------------------------------------------------------------- DOM
/** h("div.card", {onclick}, hijos...) -> elemento. Las cadenas se insertan como texto (con las cantidades ocultas). */
export function h(tag, props, ...children) {
  const [name, ...classes] = tag.split(".");
  const el = document.createElement(name || "div");
  if (classes.length) el.className = classes.join(" ");
  if (props && (typeof props !== "object" || props instanceof Node || Array.isArray(props))) {
    children.unshift(props);
    props = null;
  }
  for (const [key, value] of Object.entries(props || {})) {
    if (value === undefined || value === null || value === false) continue;
    if (key.startsWith("on")) el.addEventListener(key.slice(2), value);
    else if (key === "html") el.innerHTML = value;
    else if (key === "class") el.className += (el.className ? " " : "") + value;
    else if (key === "style" && typeof value === "object") Object.assign(el.style, value);
    else el.setAttribute(key, value === true ? "" : value);
  }
  append(el, children);
  return el;
}

function append(el, children) {
  for (const child of children.flat(Infinity)) {
    if (child === null || child === undefined || child === false) continue;
    el.append(child instanceof Node ? child : rich(String(child)));
  }
}

// Modo privacidad: `ui.format.fmt_eur` ya no devuelve el importe sino una cifra de relleno entre dos marcas invisibles
// (ui/blur.py). Aqui ese relleno se difumina; la cifra real nunca llega a la pantalla.
const START = "⁠";
const END = "⁣";

export function rich(text) {
  if (!text.includes(START)) return document.createTextNode(text);
  const frag = document.createDocumentFragment();
  const parts = text.split(START);
  frag.append(parts[0]);
  for (const part of parts.slice(1)) {
    const [hidden, rest = ""] = part.split(END);
    frag.append(h("span.priv", { "aria-hidden": "true" }, document.createTextNode(hidden)), rest);
  }
  return frag;
}

/** Texto plano (sin marcas) para atributos como aria-label. */
export function plain(text) { return String(text).replaceAll(START, "").replaceAll(END, ""); }

export function icon(name, stroke = 1.6) {
  const span = document.createElement("span");
  span.style.display = "contents";
  span.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${stroke}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${SHAPES[name] || ""}</svg>`;
  return span.firstChild;
}

export function css(name) { return getComputedStyle(document.documentElement).getPropertyValue(`--${name}`).trim(); }

/** Las cuatro franjas inclinadas de la K (StripeMark de ui/widgets/cards.py), del amarillo al rojo y cada vez mas tenues. */
export function stripes(width = 64, height = 34) {
  const yellow = hex(css("accent")), red = hex(css("red"));
  const slant = height * 0.5, bar = height * 0.185, gap = height * 0.165;
  const left = width - (slant + 4 * bar + 3 * gap);
  const bars = [1, 0.745, 0.47, 0.235].map((alpha, i) => {
    const k = i / 3, c = yellow.map((v, j) => Math.round(v + (red[j] - v) * k));
    const x = left + i * (bar + gap);
    return `<path d="M${x + slant} 2L${x + slant + bar} 2L${x + bar} ${height - 2}L${x} ${height - 2}Z" fill="rgba(${c},${alpha})"/>`;
  }).join("");
  const span = document.createElement("span");
  span.innerHTML = `<svg class="stripes" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" aria-hidden="true">${bars}</svg>`;
  return span.firstChild;
}

function hex(color) {
  const c = color.replace("#", "");
  return [0, 2, 4].map((i) => parseInt(c.slice(i, i + 2), 16));
}

export function brand() {
  return h("div.brand", { html: WORDMARK });
}

// ----------------------------------------------------------------------------- avisos con Deshacer (ui/feedback.py)
let toastTimer = 0;
let undoHandler = null;

export function toast(message, onUndo = null) {
  if (!message) return;
  let el = document.querySelector(".toast");
  if (!el) {
    el = h("div.toast", { role: "status" },
      h("span"), h("button.undo", { onclick: () => { hideToast(); undoHandler && undoHandler(); } }),
      h("button.close", { "aria-label": t("Cerrar"), onclick: hideToast }, "×"));
    document.body.append(el);
  }
  el.querySelector("span").replaceChildren(rich(message));
  const undo = el.querySelector(".undo");
  undo.textContent = t("Deshacer");
  undo.hidden = !onUndo;
  undoHandler = onUndo;
  el.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(hideToast, onUndo ? 8000 : 4000);
}

export function hideToast() {
  document.querySelector(".toast")?.classList.remove("show");
  undoHandler = null;
}

// ----------------------------------------------------------------------------- hojas (cuadros de dialogo del escritorio)
export function sheet(...content) {
  const panel = h("div.sheet", { role: "dialog", "aria-modal": "true" }, ...content);
  const backdrop = h("div.sheet-backdrop", panel);
  backdrop.addEventListener("click", (e) => { if (e.target === backdrop) close(); });
  function close() { backdrop.remove(); }
  document.body.append(backdrop);
  return { panel, close };
}

/** Pregunta con dos botones; devuelve true si se confirma. */
export function confirmSheet(title, text, ok, danger = false) {
  return new Promise((resolve) => {
    const s = sheet(
      h("h2", title), h("p", text),
      h("div.actions",
        h("button.btn", { onclick: () => { s.close(); resolve(false); } }, t("Cancelar")),
        h(`button.btn.${danger ? "danger" : "primary"}`, { onclick: () => { s.close(); resolve(true); } }, ok)));
  });
}

export function switchButton(checked, onchange, label) {
  const button = h("button.switch", { role: "switch", "aria-checked": String(!!checked), "aria-label": label });
  button.addEventListener("click", () => {
    const next = button.getAttribute("aria-checked") !== "true";
    if (onchange(next) !== false) button.setAttribute("aria-checked", String(next));
  });
  return button;
}

// ----------------------------------------------------------------------------- archivos para el usuario
const TYPES = { xlsx: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", csv: "text/csv", kreix: "application/octet-stream" };

/** Entrega un archivo: con la hoja de compartir del movil (guardar en Archivos, Drive, enviarlo...) o como descarga. */
export async function saveFile(name, bytes) {
  const type = TYPES[name.split(".").pop()] || "application/octet-stream";
  const file = new File([bytes], name, { type });
  if (navigator.canShare && navigator.canShare({ files: [file] })) {
    try { await navigator.share({ files: [file], title: name }); return true; } catch (e) { if (e.name === "AbortError") return false; }
  }
  const url = URL.createObjectURL(file);
  const a = h("a", { href: url, download: name });
  document.body.append(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 4000);
  return true;
}

/** Pide un texto (como QInputDialog.getText). Resuelve con el texto o null. */
export function promptSheet(title, label, value = "", ok = t("Aceptar")) {
  return new Promise((resolve) => {
    const input = h("input", { type: "text", value, "aria-label": label });
    const s = sheet(h("h2", title), h("p", label), input,
      h("div.actions",
        h("button.btn", { onclick: () => { s.close(); resolve(null); } }, t("Cancelar")),
        h("button.btn.primary", { onclick: () => { s.close(); resolve(input.value.trim() || null); } }, ok)));
    setTimeout(() => input.focus(), 50);
  });
}

/** Aviso con un solo boton (como QMessageBox.information/warning). */
export function alertSheet(title, text) {
  const s = sheet(h("h2", title), h("p", text), h("div.actions", h("button.btn.primary", { onclick: () => s.close() }, t("Aceptar"))));
}
