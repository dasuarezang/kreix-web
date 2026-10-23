// Graficos de Kreix en SVG, con el estilo de ui/widgets/charts.py: planos (sin degradados), extremos rectos, cuadricula
// tenue y los colores de la paleta. Tocar (o arrastrar el dedo) ensena los valores de ese punto, como el raton en el PC.
import { css, h, rich } from "./core.js";

const NS = "http://www.w3.org/2000/svg";

function svg(tag, attrs = {}, ...children) {
  const el = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) if (v !== undefined && v !== null) el.setAttribute(k, v);
  el.append(...children);
  return el;
}

function niceMax(value) {
  if (value <= 0) return 1;
  const exp = Math.pow(10, Math.floor(Math.log10(value)));
  for (const step of [1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10]) if (step * exp >= value) return step * exp;
  return 10 * exp;
}

function compact(value) {
  const abs = Math.abs(value);
  if (abs >= 1e6) return `${(value / 1e6).toLocaleString(undefined, { maximumFractionDigits: 1 })}M`;
  if (abs >= 1e3) return `${(value / 1e3).toLocaleString(undefined, { maximumFractionDigits: 1 })}k`;
  return Math.round(value).toLocaleString();
}

/** Ancho real del contenedor (los graficos se dibujan a su medida, no se estiran). */
function widthOf(el) { return Math.max(260, Math.round(el.getBoundingClientRect().width || 320)); }

// ----------------------------------------------------------------------------- tooltip tactil
function attachTip(wrap, plot, count, x0, step, render) {
  const tip = h("div.tip", { hidden: true });
  const guide = svg("line", { stroke: css("field-edge"), "stroke-width": 1, visibility: "hidden" });
  plot.append(guide);
  wrap.append(tip);
  function show(clientX) {
    const box = plot.getBoundingClientRect();
    const scale = box.width / plot.viewBox.baseVal.width;
    const x = (clientX - box.left) / scale;
    const i = Math.max(0, Math.min(count - 1, Math.round((x - x0) / step)));
    const gx = x0 + i * step;
    guide.setAttribute("x1", gx); guide.setAttribute("x2", gx);
    guide.setAttribute("y1", 0); guide.setAttribute("y2", plot.viewBox.baseVal.height - 18);
    guide.setAttribute("visibility", "visible");
    tip.replaceChildren(...render(i));
    tip.hidden = false;
    const wbox = wrap.getBoundingClientRect();
    const left = box.left - wbox.left + gx * scale;
    tip.style.top = "0px";
    tip.style.left = `${Math.max(0, Math.min(wbox.width - tip.offsetWidth, left - tip.offsetWidth / 2))}px`;
  }
  function hide() { tip.hidden = true; guide.setAttribute("visibility", "hidden"); }
  plot.addEventListener("pointerdown", (e) => { show(e.clientX); plot.setPointerCapture(e.pointerId); });
  plot.addEventListener("pointermove", (e) => { if (e.buttons || e.pointerType === "mouse") show(e.clientX); });
  plot.addEventListener("pointerup", () => setTimeout(hide, 1600));
  plot.addEventListener("pointerleave", (e) => { if (e.pointerType === "mouse") hide(); });
  plot.style.touchAction = "pan-y";
}

function tipLine(color, label, value) {
  return h("div", { style: { display: "flex", gap: "8px", alignItems: "center" } },
    color && h("i.dot", { style: { background: color } }), h("span", { style: { color: css("muted") } }, label), rich(value));
}

// ----------------------------------------------------------------------------- curva pequena de la tarjeta principal
export function sparkline(values, height = 90) {
  const wrap = h("div", { style: { position: "relative", marginTop: "12px" } });
  requestAnimationFrame(() => {
    if (values.length < 2) return;
    const w = widthOf(wrap), pad = 6;
    const lo = Math.min(...values), hi = Math.max(...values), span = hi - lo || 1;
    const pts = values.map((v, i) => [pad + (w - 2 * pad) * i / (values.length - 1), height - pad - (height - 2 * pad) * (v - lo) / span]);
    const line = pts.map(([x, y], i) => `${i ? "L" : "M"}${x.toFixed(1)} ${y.toFixed(1)}`).join("");
    const accent = css("accent");
    const plot = svg("svg", { viewBox: `0 0 ${w} ${height}`, width: "100%", height, class: "chart", style: "margin-top:0" },
      svg("path", { d: `${line}L${pts.at(-1)[0]} ${height}L${pts[0][0]} ${height}Z`, fill: accent, "fill-opacity": 0.086 }),
      svg("path", { d: line, fill: "none", stroke: accent, "stroke-width": 1.7, "stroke-linecap": "round", "stroke-linejoin": "round" }),
      svg("circle", { cx: pts.at(-1)[0], cy: pts.at(-1)[1], r: 3.4, fill: accent, stroke: css("surface"), "stroke-width": 2 }));
    wrap.append(plot);
  });
  return wrap;
}

// ----------------------------------------------------------------------------- donut (distribucion)
const FIXED = { "Inversión": "accent", "Liquidez": "neutral" };
const SERIES = ["accent", "red", "neutral", "#C48F00", "#F59A9C", "#A5B0BC"];

export function seriesColor(key, i) {
  const name = FIXED[key] || SERIES[i % SERIES.length];
  return name.startsWith("#") ? name : css(name);
}

export function donut(data) {
  const size = 132, thick = size * 0.105, r = size / 2 - thick / 2 - 4, c = size / 2;
  const total = data.slices.reduce((a, s) => a + s.value, 0) || 1;
  const gap = data.slices.length > 1 ? 2.4 : 0;
  const plot = svg("svg", { viewBox: `0 0 ${size} ${size}`, role: "img" });
  let start = 0;
  data.slices.forEach((s, i) => {
    const span = 360 * s.value / total, visible = Math.max(span - gap, 0.8), from = start + (span - visible) / 2;
    plot.append(svg("path", { d: arc(c, c, r, from, from + Math.min(visible, 359.99)), fill: "none", stroke: seriesColor(s.key, i), "stroke-width": thick }));
    start += span;
  });
  plot.append(
    svg("text", { x: c, y: c - 8, "text-anchor": "middle", style: `font-family:var(--label);font-size:9px;letter-spacing:1.2px;fill:${css("muted")}` }, "TOTAL"),
    svg("text", { x: c, y: c + 12, "text-anchor": "middle", style: `font-family:var(--display);font-size:${data.total.length > 9 ? 13 : 16}px;fill:${css("text")}`, class: data.total.includes("⁠") ? "priv" : "" },
      data.total.replace(/[⁠⁣]/g, "")));
  return h("div.donut-wrap", plot,
    h("ul", data.slices.map((s, i) => h("li", h("i.dot", { style: { background: seriesColor(s.key, i) } }), h("span", s.label), h("b", { style: { fontFamily: "var(--medium)", fontWeight: "normal" } }, s.text, "  ·  ", s.pct)))));
}

function arc(cx, cy, r, a0, a1) {
  const p = (a) => [cx + r * Math.sin(a * Math.PI / 180), cy - r * Math.cos(a * Math.PI / 180)];
  const [x0, y0] = p(a0), [x1, y1] = p(a1);
  return `M${x0.toFixed(2)} ${y0.toFixed(2)}A${r} ${r} 0 ${a1 - a0 > 180 ? 1 : 0} 1 ${x1.toFixed(2)} ${y1.toFixed(2)}`;
}

// ----------------------------------------------------------------------------- barras apiladas (flujo de caja)
export function flowChart(data) {
  const wrap = h("div", { style: { position: "relative" } });
  const series = [
    { label: data.legend[0], color: css("accent"), values: data.income, texts: data.income_text },
    { label: data.legend[1], color: css("red"), values: data.expenses, texts: data.expenses_text },
  ];
  if (data.contributions) series.push({ label: data.legend[2], color: css("neutral"), values: data.contrib, texts: data.contrib_text });
  requestAnimationFrame(() => {
    const w = widthOf(wrap), height = 220, left = 36, bottom = 22, top = 8;
    const n = data.months.length;
    if (!n) return;
    const totals = data.months.map((_, i) => data.grouped ? Math.max(...series.map((s) => s.values[i]))
      : series.reduce((a, s) => a + Math.max(0, s.values[i]), 0));
    const max = niceMax(Math.max(...totals));
    const plotH = height - bottom - top, step = (w - left) / n, barW = Math.min(22, step * 0.56);
    const plot = svg("svg", { viewBox: `0 0 ${w} ${height}`, width: "100%", height, class: "chart" });
    for (let k = 0; k <= 4; k++) {
      const y = top + plotH * (1 - k / 4);
      plot.append(svg("line", { x1: left, x2: w, y1: y, y2: y, stroke: css("grid"), "stroke-width": 1 }),
        svg("text", { x: left - 6, y: y + 4, "text-anchor": "end" }, compact(max * k / 4)));
    }
    data.months.forEach((label, i) => {
      const x = left + step * i + (step - barW) / 2;
      let y = top + plotH;
      series.forEach((s, k) => {
        const hgt = plotH * Math.max(0, s.values[i]) / max;
        if (data.grouped) {
          const w = barW / series.length - 1;
          if (hgt > 0) plot.append(svg("rect", { x: x + k * (w + 2), y: top + plotH - hgt, width: w, height: hgt, fill: s.color }));
          return;
        }
        if (hgt > 0) plot.append(svg("rect", { x, y: y - hgt, width: barW, height: Math.max(hgt - 1, 0.5), fill: s.color }));
        y -= hgt;
      });
      if (n <= 8 || i % Math.ceil(n / 8) === 0 || i === n - 1)
        plot.append(svg("text", { x: x + barW / 2, y: height - 6, "text-anchor": "middle" }, label));
    });
    wrap.prepend(plot);
    attachTip(wrap, plot, n, left + step / 2, step, (i) => [
      h("div", { style: { marginBottom: "4px" } }, data.months_long[i]),
      ...series.map((s) => tipLine(s.color, s.label, s.texts[i]))]);
  });
  wrap.append(legend(series));
  return wrap;
}

// ----------------------------------------------------------------------------- lineas (evolucion patrimonial)
export function lineChart({ labels, tips, series, height = 220 }) {
  const wrap = h("div", { style: { position: "relative" } });
  requestAnimationFrame(() => {
    const n = labels.length;
    if (n < 2) return;
    const w = widthOf(wrap), left = 40, bottom = 22, top = 8, plotH = height - bottom - top;
    const all = series.flatMap((s) => s.values);
    const lo = Math.min(0, ...all), max = niceMax(Math.max(...all));
    const x = (i) => left + (w - left - 6) * i / (n - 1);
    const y = (v) => top + plotH * (1 - (v - lo) / (max - lo || 1));
    const plot = svg("svg", { viewBox: `0 0 ${w} ${height}`, width: "100%", height, class: "chart" });
    for (let k = 0; k <= 4; k++) {
      const v = lo + (max - lo) * k / 4, gy = y(v);
      plot.append(svg("line", { x1: left, x2: w, y1: gy, y2: gy, stroke: css("grid"), "stroke-width": 1 }),
        svg("text", { x: left - 6, y: gy + 4, "text-anchor": "end" }, compact(v)));
    }
    for (const s of series) {
      const d = s.values.map((v, i) => `${i ? "L" : "M"}${x(i).toFixed(1)} ${y(v).toFixed(1)}`).join("");
      if (s.fill) plot.append(svg("path", { d: `${d}L${x(n - 1)} ${y(lo)}L${x(0)} ${y(lo)}Z`, fill: s.color, "fill-opacity": 0.086 }));
      plot.append(svg("path", { d, fill: "none", stroke: s.color, "stroke-width": s.width || 1.5, "stroke-dasharray": s.dashed ? "5 4" : null, "stroke-linejoin": "round", "stroke-linecap": "round" }));
    }
    const every = Math.ceil(n / 5);
    labels.forEach((label, i) => {
      if (i % every === 0 || i === n - 1) plot.append(svg("text", { x: x(i), y: height - 6, "text-anchor": i === n - 1 ? "end" : i === 0 ? "start" : "middle" }, label));
    });
    wrap.prepend(plot);
    attachTip(wrap, plot, n, x(0), x(1) - x(0), (i) => [
      h("div", { style: { marginBottom: "4px" } }, tips[i]),
      ...series.map((s) => tipLine(s.color, s.label, s.texts[i]))]);
  });
  wrap.append(legend(series));
  return wrap;
}

function legend(series) {
  return h("div.chart-legend", series.map((s) => h("span", h("i.dot", { style: { background: s.color } }), s.label)));
}

/** Colores de una serie que llegan por nombre desde Python ("accent", "neutral", "series2"...). */
export function colorOf(name) {
  if (name.startsWith("series")) return SERIES_COLORS()[Number(name.slice(6)) % 6];
  return name.startsWith("#") ? name : css(name);
}

function SERIES_COLORS() {
  return document.documentElement.dataset.theme === "light"
    ? ["#EDB00C", "#DC2F36", "#9098A3", "#B07F00", "#E8703F", "#BCC2CB"]
    : ["#F5BE1E", "#F2464A", "#6B7885", "#C48F00", "#F59A9C", "#A5B0BC"];
}

/** lineChart con las series tal como llegan de Python. */
export function pyLines(data, height = 220) {
  return lineChart({ labels: data.labels, tips: data.tips, height,
    series: data.series.map((s) => ({ ...s, color: colorOf(s.color) })) });
}

// ----------------------------------------------------------------------------- gastos por categoria (barras horizontales)
export function categoryBars(data, onpick) {
  if (!data.items.length) return h("p.empty", data.empty);
  const top = Math.max(...data.items.map((c) => c.share)) || 1;
  return h("div.cat-bars", data.items.map((c, i) => h("button.cat-bar", { onclick: () => onpick(c.value) },
    h("div.cat-top", h("span", c.label), h("b", c.amount), h("em", c.pct)),
    h("div.track", h("i", { style: { width: `${(c.share / top) * 100}%`, background: css("red"), opacity: String(Math.max(150, 255 - i * 14) / 255) } })))));
}
