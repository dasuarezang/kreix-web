// Piezas de pagina que comparten Cuentas e Inversiones (en el escritorio: PeriodBar, StatBand, EmptyState...).
import { h, icon, py, t } from "./core.js";
import { infoButton } from "./inicio.js";

/** Selector de periodo: todo el historial o un mes, con flechas para ir al mes anterior o siguiente. */
export function periodBar(p, onchange) {
  const values = [null, ...p.months.map((m) => m.value)];
  const index = values.indexOf(p.current);
  const select = h("select", { "aria-label": p.aria, onchange: () => onchange(select.value || null) },
    h("option", { value: "" }, p.label),
    p.months.map((m) => h("option", { value: m.value, selected: m.value === p.current }, m.label)));
  // los meses van del mas reciente al mas antiguo: "anterior" es bajar en la lista
  const older = h("button.icon-btn", { "aria-label": p.older, disabled: index >= values.length - 1, onclick: () => onchange(values[Math.max(1, index + 1)]) },
    h("span", { style: { transform: "scaleX(-1)", display: "flex" } }, icon("chevron", 2)));
  const newer = h("button.icon-btn", { "aria-label": p.newer, disabled: index <= 1, onclick: () => onchange(values[index - 1]) }, icon("chevron", 2));
  return h("div.period", older, select, newer);
}

/** Cuatro cifras en rejilla de 2x2 bajo el filo de marca (StatBand). */
export function statBand(cards, app, compact = false) {
  return h("section.section", h("div.rule"), h(`div.band${compact ? ".compact" : ""}`, cards.map((c) => h("div.cell",
    h("div.stat-title", h("span", c.title), c.help && infoButton(c.help, app)),
    h(`div.stat-value${c.tone ? ".tone-" + c.tone : ""}`, c.value),
    c.sub && h("p.stat-sub", c.sub)))));
}

/** Pagina vacia con sentido: que verias aqui, que hace falta y un boton para empezar. */
export function emptyState(e, app) {
  return h("div.empty-state",
    h("h1", e.title), h("p", e.text),
    h("section.section", h("div.rule"), h("div.stat-title", h("span", e.needs_title)), h("p", e.needs)),
    h("button.btn.primary.block", { onclick: () => app.go("datos") }, e.button));
}

/** Pestana desactivada en "Lo que te interesa": solo ofrece activarla. */
export function offState(o, target, app) {
  return h("div.empty-state",
    h("h1", o.title), h("p", o.text),
    h("button.btn.primary.block", { onclick: async () => { await py("set_interest", { [target]: true }); await app.reload(); } }, o.button),
    h("p.note", o.note));
}

export function pageHead(eyebrow, title, subtitle, ...right) {
  return h("header.page-head", h("div.head-row",
    h("div", h("p.eyebrow", eyebrow), h("h1", title), subtitle && h("p.sub", subtitle)), ...right));
}

export function chartSection(title, caption, headline, ...content) {
  return h("section.section", h("div.rule"), h("div.section-head", h("div", h("h2", title), caption && h("p.caption", caption))),
    headline && h("p.headline", headline), ...content);
}

/** Lista que se va mostrando por tandas (miles de movimientos no caben de golpe en un movil). */
export function pagedList(rows, render, step = 60) {
  const box = h("div.list");
  const more = h("button.btn.small.block", { style: { marginTop: "12px" } }, t("Ver más"));
  let shown = 0;
  function add() {
    const next = rows.slice(shown, shown + step);
    box.append(...next.map(render));
    shown += next.length;
    more.hidden = shown >= rows.length;
  }
  more.addEventListener("click", add);
  add();
  return h("div", box, more);
}
