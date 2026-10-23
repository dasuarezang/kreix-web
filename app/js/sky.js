// El cielo de Inicio (ui/widgets/sky.py) con Blitzen y Black (ui/widgets/dogs.py), y la luz ambiente (ui/widgets/ambient.py).
// Mismas coordenadas, colores y tiempos que el escritorio: el sol sale a las 6 y se pone a las 21 por la parte izquierda, y
// de noche hay luna con estrellas. Los perros son las capas recortadas de su ilustracion (las mismas de la web), animados con CSS.
import { css, h } from "./core.js";

const NS = "http://www.w3.org/2000/svg";
const DAWN = 6, DUSK = 21;
const W = 92, H = 50, BASE = 46, PAD_X = 17, PAD_TOP = 12, RADIUS = 8.5;
const ARC_X0 = 14, ARC_X1 = 33, GROUND = BASE + 1.2, CENTER_X = 77;
const CREAM = "rgb(232,216,192)", LINE = 0.62;
const VIEW_W = W + 2 * PAD_X, VIEW_H = H + PAD_TOP;

// Los perros sobre el lienzo de la ilustracion (pixeles de basePerretes.jpg): UNIT unidades del cielo por pixel, apoyados en el
// horizonte por la base de las patas y centrados en CENTER_X. Ver dogs.py (UNIT, GROUND_Y, PAIR_CENTER_X) y tools/web_dogs.py.
const DAY = { x0: 130, y0: 60, x1: 2330, y1: 1790, unit: 0.025, ground: 1759, center: 1221 };
const NIGHT = { x0: 47, y0: 105, w: 934 / 0.35, h: 485 / 0.35, unit: 0.0205, ground: 1492, center: 1382 };
const SLEEP_ZS = [[1690, 300, 1.0, 0.0], [2170, 780, 0.8, 1.7]];

function el(tag, attrs = {}) {
  const node = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, v);
  return node;
}

const hex = (c) => c.match(/\w\w/g).map((x) => parseInt(x, 16));
const rgb = (c) => `rgb(${c.join(",")})`;

/** Mezcla dos colores ([r, g, b]) como `_mix` del escritorio. */
function mix(a, b, t) {
  t = Math.max(0, Math.min(1, t));
  return a.map((v, i) => Math.round(v + (b[i] - v) * t));
}

export function skyState(hour) {
  hour = ((hour % 24) + 24) % 24;
  if (hour >= DAWN && hour < DUSK) return { kind: "sun", progress: (hour - DAWN) / (DUSK - DAWN) };
  return { kind: "moon", progress: ((hour - DUSK + 24) % 24) / (24 - DUSK + DAWN) };
}

function arcPoint(progress) {
  const edge = BASE + 1, high = 18, inside = Math.max(0, Math.min(1, progress));
  return [ARC_X0 + inside * (ARC_X1 - ARC_X0), edge - Math.pow(Math.sin(Math.PI * inside), 0.85) * (edge - high)];
}

/** Pegatina: la forma con su contorno crema por fuera (se pinta primero el contorno de todas las piezas y luego el relleno). */
function sticker(parts, fill, alpha = 1) {
  const g = el("g", { opacity: alpha });
  const edge = el("g", { fill: CREAM, stroke: CREAM, "stroke-width": LINE * 2, "stroke-linejoin": "round" });
  const body = el("g", { fill });
  for (const p of parts) { edge.append(p.cloneNode()); body.append(p); }
  g.append(edge, body);
  return g;
}

function sun(progress, t, light) {
  const inside = Math.max(0, Math.min(1, progress));
  const low = 1 - Math.pow(Math.sin(Math.PI * inside), 0.55);
  const color = mix(hex(light ? "F2A100" : "FFD23F"), hex("FF8A3D"), low * 1.15);
  const [x, y0] = arcPoint(progress);
  const y = y0 + Math.sin(t * 1.3) * 1.3;
  const vis = Math.max(0, Math.min(1, (BASE + RADIUS + 4 - y) / (RADIUS * 2.4)));
  const parts = [el("circle", { cx: x, cy: y, r: RADIUS })];
  const angle = t * 0.35;
  for (let i = 0; i < 8; i++) {
    const reach = (4.2 + 1.1 * Math.sin(t * 2.2 + i * 0.9)) * vis;
    if (reach < 0.4) continue;
    const a = (angle + (i * Math.PI * 2) / 8) * 180 / Math.PI;
    parts.push(el("rect", { x: RADIUS + 1.6, y: -1.25, width: reach, height: 2.5, rx: 1.25, transform: `translate(${x} ${y}) rotate(${a})` }));
  }
  const g = el("g");
  g.append(sticker(parts, rgb(color)), el("ellipse", { cx: x - 2.6, cy: y - 2.8, rx: RADIUS * 0.42, ry: RADIUS * 0.3, fill: rgb(mix(color, [255, 255, 255], 0.5)) }));
  g.append(cloud(t));
  return g;
}

function cloud(t) {
  const span = W + 44, x = ((t * 3.2) % span) - 28;
  const fade = Math.max(0, Math.min(1, (x + 6) / 18, (W - x - 20) / 18));
  if (fade <= 0) return el("g");
  const parts = [[4, 0, 4], [10, -3, 5], [17, -1, 4.4], [23, 0, 3.4]].map(([dx, dy, r]) => el("circle", { cx: x + dx, cy: 15 + dy, r }));
  parts.push(el("rect", { x, y: 15, width: 26, height: 4.4, rx: 2.2 }));
  return sticker(parts, "#FFFFFF", fade);
}

let moonId = 0;

function moon(progress, t, light) {
  const color = light ? "#7580C4" : "#F6E7B0";
  const [x, y0] = arcPoint(progress);
  const y = y0 + Math.sin(t) * 1.2;
  const inside = Math.max(0, Math.min(1, progress));
  const nightFade = Math.max(0.25, Math.min(1, Math.sin(Math.PI * inside) * 2.4));
  const g = el("g");
  for (const [sx, sy, shift] of [[6, 10, 0], [38, 10, 1.7], [52, 6, 3.1], [45, 22, 4.4], [38, 32, 5.2]]) {
    const twinkle = 0.5 + 0.5 * Math.sin(t * 1.8 + shift), size = 1.7 + 1.1 * twinkle;
    const d = `M${sx} ${sy - size}Q${sx} ${sy} ${sx + size} ${sy}Q${sx} ${sy} ${sx} ${sy + size}Q${sx} ${sy} ${sx - size} ${sy}Q${sx} ${sy} ${sx} ${sy - size}Z`;
    g.append(sticker([el("path", { d })], color, (0.45 + 0.55 * twinkle) * nightFade));
  }
  // el creciente: el disco menos otro disco desplazado (con una mascara)
  const id = `bite-${++moonId}`;
  const mask = el("mask", { id });
  mask.append(el("rect", { x: -50, y: -50, width: 300, height: 300, fill: "#fff" }),
    el("circle", { cx: x + 4.2, cy: y - 2.6, r: RADIUS * 0.86, fill: "#000" }));
  const crescent = sticker([el("circle", { cx: x, cy: y, r: RADIUS })], color);
  crescent.setAttribute("mask", `url(#${id})`);
  g.append(mask, crescent);
  for (const [dx, dy, r] of [[-5, 1.8, 1.2], [-2.2, 5.2, 0.9]])
    g.append(el("circle", { cx: x + dx, cy: y + dy, r, fill: light ? "#6771AD" : "#D8CB9B" }));
  return g;
}

function zs(t, light) {
  const g = el("g", { fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round", stroke: light ? "#17191D" : CREAM });
  for (const [ix, iy, size, offset] of SLEEP_ZS) {
    for (let k = 0; k < 3; k++) {
      const u = (((t + offset + k * 1.1) % 3.3) + 3.3) % 3.3 / 3.3;
      const side = (40 + 90 * u) * size;
      const cx = ix + u * 260 * size, cy = iy - u * 330 * size;
      // a coordenadas del cielo
      const X = (v) => CENTER_X + (v - NIGHT.center) * NIGHT.unit, Y = (v) => GROUND + (v - NIGHT.ground) * NIGHT.unit;
      const s = side / 2;
      g.append(el("path", {
        d: `M${X(cx - s)} ${Y(cy - s)}L${X(cx + s)} ${Y(cy - s)}L${X(cx - s)} ${Y(cy + s)}L${X(cx + s)} ${Y(cy + s)}`,
        "stroke-width": side * 0.2 * NIGHT.unit, opacity: 0.9 * Math.pow(Math.sin(Math.PI * u), 1.2),
      }));
    }
  }
  return g;
}

function placed(box, unit, ground, center, x0, y0, w, h) {
  const x = CENTER_X + (x0 - center) * unit + PAD_X, y = GROUND + (y0 - ground) * unit + PAD_TOP;
  return { left: `${(x / VIEW_W) * 100}%`, top: `${(y / VIEW_H) * 100}%`, width: `${((w * unit) / VIEW_W) * 100}%`, height: `${((h * unit) / VIEW_H) * 100}%` };
}

/** El cielo para la cabecera de Inicio. `hour()` da la hora decimal actual; `animated` es el ajuste "Cielo animado". */
export function skyWidget(hour, animated, label) {
  const svg = el("svg", { viewBox: `${-PAD_X} ${-PAD_TOP} ${VIEW_W} ${VIEW_H}`, class: "sky-svg" });
  const box = h("div.sky", { role: "img", "aria-label": label }, svg);
  const day = h("div.dogs.day", { style: placed(null, DAY.unit, DAY.ground, DAY.center, DAY.x0, DAY.y0, DAY.x1 - DAY.x0, DAY.y1 - DAY.y0) },
    h("img.tail", { src: "img/dogs/black-cola.webp", alt: "" }), h("img", { src: "img/dogs/blitzen.webp", alt: "" }),
    h("img.blink", { src: "img/dogs/blitzen-ojos.webp", alt: "" }), h("img.tongue", { src: "img/dogs/blitzen-lengua.webp", alt: "" }),
    h("img", { src: "img/dogs/black.webp", alt: "" }), h("img.blink.blink-black", { src: "img/dogs/black-ojos.webp", alt: "" }));
  const night = h("div.dogs.night", { style: placed(null, NIGHT.unit, NIGHT.ground, NIGHT.center, NIGHT.x0, NIGHT.y0, NIGHT.w, NIGHT.h) },
    h("img", { src: "img/dogs/durmiendo.webp", alt: "" }));
  if (animated) box.append(day, night);

  const start = performance.now();
  function frame() {
    if (!box.isConnected) return;
    const t = animated ? (performance.now() - start) / 1000 : 0;
    const light = document.documentElement.dataset.theme === "light";
    const state = skyState(hour());
    svg.replaceChildren();
    svg.append(el("line", { x1: 6, y1: BASE + 2, x2: W + 12, y2: BASE + 2, stroke: css("muted"), "stroke-opacity": 0.35, "stroke-width": 1.6, "stroke-linecap": "round" }));
    if (animated) svg.append(el("ellipse", { cx: CENTER_X, cy: GROUND + 0.4, rx: 29, ry: 1.9, fill: light ? "rgba(0,0,0,.08)" : "rgba(255,255,255,.086)" }));
    const clip = el("clipPath", { id: "sky-clip" });
    clip.append(el("rect", { x: -PAD_X, y: -PAD_TOP, width: VIEW_W, height: BASE + 2 + PAD_TOP }));
    const bodies = el("g", { "clip-path": "url(#sky-clip)" });
    bodies.append(state.kind === "sun" ? sun(state.progress, t, light) : moon(state.progress, t, light));
    svg.append(clip, bodies);
    if (animated && state.kind === "moon") svg.append(zs(t, light));
    day.hidden = state.kind !== "sun";
    night.hidden = state.kind === "sun";
    if (animated && !matchMedia("(prefers-reduced-motion: reduce)").matches) setTimeout(() => requestAnimationFrame(frame), 40);
  }
  requestAnimationFrame(frame);
  return box;
}

// ----------------------------------------------------------------------------- luz ambiente
const KEYFRAMES = [[0, [8, 14, 40, 18]], [5, [8, 14, 40, 15]], [7.5, [0, 0, 0, 0]], [13, [0, 0, 0, 0]], [16, [0, 0, 0, 4]],
  [19, [255, 120, 40, 9]], [21, [10, 16, 48, 14]], [24, [8, 14, 40, 18]]];

export function ambientTint(hour) {
  hour = ((hour % 24) + 24) % 24;
  for (let i = 0; i < KEYFRAMES.length - 1; i++) {
    const [h0, c0] = KEYFRAMES[i], [h1, c1] = KEYFRAMES[i + 1];
    if (hour >= h0 && hour <= h1) {
      const f = h1 > h0 ? (hour - h0) / (h1 - h0) : 0;
      const rgb = c0[3] === 0 ? c1.slice(0, 3) : c1[3] === 0 ? c0.slice(0, 3) : c0.slice(0, 3).map((a, j) => Math.round(a + (c1[j] - a) * f));
      return [...rgb, Math.round(c0[3] + (c1[3] - c0[3]) * f)];
    }
  }
  return KEYFRAMES[0][1];
}

export function applyAmbient(hour, on) {
  let layer = document.getElementById("ambient");
  if (!layer) { layer = h("div", { id: "ambient", "aria-hidden": "true" }); document.body.append(layer); }
  const [r, g, b, a] = on ? ambientTint(hour) : [0, 0, 0, 0];
  layer.style.background = `rgba(${r},${g},${b},${a / 255})`;
}
