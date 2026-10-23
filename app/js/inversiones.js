// Inversiones (ui/views/investment_view.py): cartera por mes o de todo el historial, distribucion por fondo, aportado
// frente a valor, la evolucion de cada fondo, las posiciones y las operaciones.
import { donut, pyLines } from "./charts.js";
import { h, py } from "./core.js";
import { chartSection, emptyState, offState, pagedList, pageHead, periodBar, statBand } from "./parts.js";

const state = { month: null, fund: null };

export async function renderInversiones(main, app) {
  const d = await py("inversiones", { month: state.month, fund: state.fund });
  if (d.off) return main.replaceChildren(offState(d.off, "investments", app));
  state.month = d.period.current;
  const parts = [pageHead(d.eyebrow, d.title, ""), d.has_data && h("div.toolbar", periodBar(d.period, (month) => { state.month = month; app.render(); }))];
  if (!d.has_data) return main.replaceChildren(...parts.filter(Boolean), emptyState(d.empty, app));

  if (d.banner) parts.push(h("div.banner", { role: "alert" }, h("div", { html: d.banner.html }), h("button.btn.small", { onclick: () => app.go("datos") }, d.banner.button)));
  parts.push(statBand(d.cards, app), statBand(d.minis, app, true));
  const a = d.allocation;
  parts.push(chartSection(a.title, a.caption, a.headline, a.slices.length ? donut(a) : h("p.empty", a.empty)));
  parts.push(chartSection(d.evolution.title, d.evolution.caption, d.evolution.headline, pyLines(d.evolution)));
  if (d.funds) {
    const f = d.funds;
    const select = h("select", { "aria-label": f.aria, onchange: () => { state.fund = select.value || null; app.render(); } },
      h("option", { value: "" }, f.all), f.options.map((o) => h("option", { value: o.value, selected: o.value === f.current }, o.label)));
    parts.push(chartSection(f.title, f.caption, "", h("div", { style: { marginTop: "12px" } }, select), pyLines(f)));
  }
  parts.push(positions(d.positions), operations(d.operations));
  main.replaceChildren(...parts.filter(Boolean));
}

// En el movil cada posicion es una ficha: el nombre arriba y sus cifras debajo (la tabla de 8 columnas no cabe).
function positions(p) {
  const L = p.labels;
  return chartSection(p.title, p.caption, "", p.rows.map((r) => h("div.position",
    h("div.top", h("b", r.name), h(`span.chip${r.tone ? "." + r.tone : ""}`, r.ret)),
    h("dl",
      h("div", h("dt", L.value), h("dd", r.value)),
      h("div", h("dt", L.gain), h(`dd${r.tone ? ".tone-" + r.tone : ""}`, r.gain)),
      h("div", h("dt", L.invested), h("dd", r.invested)),
      h("div", h("dt", L.units), h("dd", r.units)),
      h("div", h("dt", L.avg), h("dd", r.avg)),
      h("div", h("dt", L.price), h("dd", r.price))),
    h("p.muted", r.isin))));
}

function operations(o) {
  return chartSection(o.title, o.count, "", pagedList(o.rows, (r) => h("div.move",
    h("div.move-main", h("b", r.name), h("span.muted", `${r.date}  ·  `, h("span.accent", r.type), `  ·  ${r.units} × ${r.price}`)),
    h("div.move-side", h("span.amount", r.amount))), 20));
}

