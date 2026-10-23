// Kreix movil: arranque, estructura (barra superior y pestanas) y lo que en el escritorio hace ui/main_window.py.
import { brand, h, hideToast, icon, py, setCatalog, sheet, stripes, t, toast, watchProgress } from "./core.js";
import { goalsSheet, isoLocal, renderInicio } from "./inicio.js";
import { lockScreen, welcomeScreen } from "./lock.js";
import { newRule, renderCuentas } from "./cuentas.js";
import { renderInversiones } from "./inversiones.js";
import { renderDatos } from "./datos.js";
import { renderAjustes, renderAyuda } from "./ajustes.js";
import { applyAmbient } from "./sky.js";

const root = document.getElementById("app");
const PAGES = [
  { id: "inicio", label: "Inicio", icon: "home" },
  { id: "cuentas", label: "Cuentas", icon: "card" },
  { id: "inversiones", label: "Inversiones", icon: "trend" },
  { id: "datos", label: "Datos", icon: "database" },
  { id: "ajustes", label: "Ajustes", icon: "gear" },
];

// Pistas sin cifrar para las pantallas que salen antes de abrir los datos (como idioma.txt y texto.txt del escritorio).
const hint = {
  get(key, fallback) { try { return localStorage.getItem(`kreix.${key}`) || fallback; } catch { return fallback; } },
  set(key, value) { try { localStorage.setItem(`kreix.${key}`, value); } catch { /* sin almacenamiento: no pasa nada */ } },
};

const app = {
  state: null,
  page: "inicio",
  params: {},
  clock: { greeting: "", date: "" },
  lockInfo: null,
  locked: false,

  async go(page, params = {}) {
    this.page = page;
    this.params = params;
    window.scrollTo(0, 0);
    await this.render();
  },

  async refresh() { await this.render(); },

  async render() {
    if (this.locked) return;
    const main = document.querySelector("main");
    if (!main) return;
    const tab = this.page === "ayuda" ? "ajustes" : this.page;
    document.querySelectorAll(".tabbar button").forEach((b) => b.setAttribute("aria-current", b.dataset.page === tab ? "page" : "false"));
    try {
      const view = VIEWS[this.page] || placeholder;
      await view(main, this, this.params);
    } catch (e) {
      main.replaceChildren(h("div.banner", { role: "alert" }, e.message));
    }
  },

  /** Resultado de una accion con aviso: {message, undoable}. */
  told(result) {
    if (!result) return;
    toast(result.message, result.undoable ? async () => { const r = await py("undo"); await this.reload(); toast(r.message); } : null);
    this.reload();
  },

  async reload() {
    this.state = await py("app_state");
    applySettings(this.state.settings);
    renderShell();
    await this.render();
  },

  async startDemo() {
    const r = await py("start_demo");
    this.page = "inicio";
    this.told(r);
  },

  async endDemo() {
    const r = await py("end_demo");
    this.page = "inicio";
    this.told(r);
  },

  async help(term) {
    const e = await py("help_entry", { term });
    if (!e) return;
    sheet(h("p.eyebrow", { style: { color: "var(--accent-text)", fontSize: "12px", margin: "0 0 4px" } }, e.section),
      h("h2", e.term), h("p", { style: { color: "var(--text)" } }, e.plain),
      e.parts.map((p) => h("div", { style: { marginTop: "14px" } },
        h("b", { style: { fontFamily: "var(--medium)", fontWeight: "normal", fontSize: "13px", color: p.tone === "alert" ? "var(--red)" : p.tone === "tip" ? "var(--accent-text)" : "var(--muted)" } }, p.label),
        h("p", { style: { color: "var(--text)", margin: "4px 0 0" } }, p.text))));
  },

  menu(items, title) {
    const s = sheet(title && h("h2", title), items.map((item) => h("button.menu-item", { onclick: () => { s.close(); item.run(); } }, item.label)));
  },

  newRule(keyword) { newRule(this, keyword); },
  goals() { goalsSheet(this); },

  async lock() {
    if (this.locked) return;
    this.locked = true;
    hideToast();
    await py("flush");
    await lockScreen(root, { ...this.lockInfo, exists: true });
    this.locked = false;
    renderShell();
    await this.render();
  },
};

const VIEWS = { inicio: renderInicio, cuentas: renderCuentas, inversiones: renderInversiones, datos: renderDatos, ajustes: renderAjustes, ayuda: renderAyuda };

async function placeholder(main) {
  main.replaceChildren(h("header.page-head", h("h1", t(PAGES.find((p) => p.id === app.page).label))),
    h("p.empty", "…"));
}

export function registerView(id, render) { VIEWS[id] = render; }

// ----------------------------------------------------------------------------- tema, tamano del texto y privacidad
function applySettings(s) {
  applyAmbient(app.clock.hour || 12, s.ambient);
  document.documentElement.dataset.theme = s.theme === "light" ? "light" : "dark";
  document.documentElement.style.setProperty("--scale", String((s.text_scale || 100) / 100));
  document.documentElement.lang = s.language;
  document.querySelector('meta[name="theme-color"]').content = s.theme === "light" ? "#F6F2EA" : "#101418";
  hint.set("theme", s.theme);
  hint.set("lang", s.language);
  hint.set("scale", String(s.text_scale || 100));
}

async function saveSettings(changes) {
  app.state = await py("save_settings", changes);
  applySettings(app.state.settings);
}

// ----------------------------------------------------------------------------- estructura
function renderShell() {
  const s = app.state.settings;
  const privacy = h("button.icon-btn", {
    "aria-pressed": String(s.privacy_mode), "aria-label": t("Ocultar las cantidades"),
    onclick: async () => {
      await saveSettings({ privacy_mode: !app.state.settings.privacy_mode });
      toast(app.state.settings.privacy_mode ? t("Cantidades ocultas. Pulsa el ojo o Ctrl+H para verlas.").replace(" o Ctrl+H", "") : t("Cantidades visibles."));
      renderShell();
      app.render();
    },
  }, icon(s.privacy_mode ? "eye_off" : "eye"));
  const theme = h("button.icon-btn", {
    "aria-label": t("Modo claro y oscuro"),
    onclick: async () => { await saveSettings({ theme: app.state.settings.theme === "light" ? "dark" : "light" }); renderShell(); app.render(); },
  }, icon(s.theme === "light" ? "moon" : "sun"));
  const helpButton = h("button.icon-btn", { "aria-label": t("Ayuda"), onclick: () => app.go("ayuda") }, icon("help"));
  const top = h("header.topbar", brand(), helpButton, privacy, theme);
  const banner = app.state.demo && h("div.demo-banner", h("span", t("Estás viendo datos de ejemplo inventados. Nada de esto es tuyo.")),
    h("button.btn.small.primary", { onclick: () => app.endDemo() }, t("Empezar con mis datos")));
  const tabs = h("nav.tabbar", { "aria-label": "Kreix" }, PAGES.map((p) => h("button", {
    "data-page": p.id, "aria-current": p.id === app.page ? "page" : "false", onclick: () => app.go(p.id),
  }, icon(p.icon, 1.7), h("span", t(p.label)))));
  root.replaceChildren(h("div", top, banner, h("main"), tabs));
}

window.addEventListener("scroll", () => document.querySelector(".topbar")?.classList.toggle("scrolled", window.scrollY > 4), { passive: true });

// ----------------------------------------------------------------------------- reloj de Inicio (cada minuto)
async function tick() {
  if (!app.state || app.locked) return;
  app.clock = await py("clock", { now: isoLocal(new Date()) });
  const g = document.getElementById("greeting"), d = document.getElementById("date-line");
  if (g) g.textContent = app.clock.greeting;
  if (d) d.textContent = app.clock.date;
  applyAmbient(app.clock.hour, app.state.settings.ambient);      // la pantalla baja muy poco su brillo con la hora
}

// ----------------------------------------------------------------------------- bloqueo automatico (ui/autolock.py)
// En el movil, "minimizar" es salir de la app: si esta activado, al volver se pide la contrasena. Si no, se pide cuando
// la app ha estado mas de los minutos elegidos sin usarse (en segundo plano o sin tocarla).
let hiddenAt = 0;
let lastTouch = Date.now();
for (const ev of ["pointerdown", "keydown"]) addEventListener(ev, () => { lastTouch = Date.now(); }, { passive: true });

document.addEventListener("visibilitychange", () => {
  if (!app.state || app.locked) return;
  if (document.hidden) {
    hiddenAt = Date.now();
    py("flush");
    return;
  }
  const s = app.state.settings;
  const away = (Date.now() - hiddenAt) / 60000;
  if (s.lock_on_minimize || (s.auto_lock_minutes && away >= s.auto_lock_minutes)) app.lock();
  else tick().then(() => app.page === "inicio" && app.render());
});

setInterval(() => {
  if (!app.state || app.locked || document.hidden) return;
  const minutes = app.state.settings.auto_lock_minutes;
  if (minutes && (Date.now() - lastTouch) / 60000 >= minutes) app.lock();
}, 15000);
addEventListener("pagehide", () => py("flush"));

// ----------------------------------------------------------------------------- arranque
async function start() {
  document.documentElement.dataset.theme = hint.get("theme", "dark") === "light" ? "light" : "dark";
  document.documentElement.style.setProperty("--scale", String(Number(hint.get("scale", "100")) / 100));
  const bar = document.querySelector("#splash .progress i");
  watchProgress(({ step, total }) => { bar.style.width = `${(step / total) * 100}%`; });
  if (navigator.storage?.persist) navigator.storage.persist().catch(() => {});

  // el idioma de la pantalla de bloqueo: el que se eligio en la app, el de la pagina de la web desde la que se llega
  // (?lang=ca) o el del navegador
  const browser = (navigator.language || "es").slice(0, 2);
  const fromWeb = new URLSearchParams(location.search).get("lang");
  const known = (code) => ["es", "ca", "en"].includes(code);
  const language = hint.get("lang", known(fromWeb) ? fromWeb : known(browser) ? browser : "es");
  let info;
  try {
    info = await py("boot", { language });
  } catch (e) {
    document.querySelector("#splash p").textContent = e.message;
    return;
  }
  app.lockInfo = { ...info, exists: true };
  document.getElementById("splash").remove();
  app.locked = true;
  await lockScreen(root, info);
  app.locked = false;
  app.state = await py("app_state");
  if (app.state.needs_welcome) app.state = await welcomeScreen(root, app.state);
  setCatalog(await py("catalog"));
  app.lockInfo = { ...info, texts: await py("lock_texts"), exists: true };     // ya en el idioma elegido
  applySettings(app.state.settings);
  await tick();
  setInterval(tick, 30000);
  renderShell();
  await app.render();
}

if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
start();

export { app, saveSettings };
