// Inicio (ui/views/dashboard_view.py): el saludo, la cifra principal y lo que pide atencion. Los textos llegan ya hechos
// de pwa/py/kreix_web.py:inicio, que replica DashboardView._render.
import { donut, flowChart, lineChart, sparkline } from "./charts.js";
import { skyWidget } from "./sky.js";
import { confirmSheet, css, h, icon, py, sheet, t, toast } from "./core.js";

export function section(title, caption, ...content) {
  return h("section.section", h("div.rule"), h("div.section-head", h("div", h("h2", title), caption && h("p.caption", caption))), ...content);
}

function stat(data, app, extraClass = "") {
  return h(`div.${extraClass || "section"}`,
    !extraClass && h("div.rule"),
    h("div.stat-title", h("span", data.title), data.help && infoButton(data.help, app)),
    h(`div.stat-value${data.tone ? ".tone-" + data.tone : ""}`, data.value),
    data.sub && h("p.stat-sub", data.sub));
}

export function infoButton(term, app) {
  return h("button.info", { "aria-label": t("Ayuda"), onclick: () => app.help(term) }, "?");
}

export async function renderInicio(main, app) {
  const today = new Date();
  const d = await py("inicio", { today: isoDate(today) });
  if (!d.has_data) return renderOnboarding(main, d.onboarding, app);

  const header = h("header.page-head",
    sky(app),
    h("p.eyebrow", t("Inicio")),
    h("h1", { id: "greeting" }, app.clock.greeting),
    h("p.date", { id: "date-line" }, app.clock.date),
    d.subtitle && h("p.sub", d.subtitle));

  const net = d.net;
  const hero = h("div.card.hero",
    h("div.stat-title", h("span", net.title), infoButton(net.help, app)),
    h("div.stat-value", net.value),
    h("div.chips", net.chips.map((c) => h(`span.chip${c.tone ? "." + c.tone : ""}`, c.text))),
    h("p.stat-sub", net.caption),
    sparkline(net.trend),
    net.split.length && h("div.split",
      h("div.bar", net.split.map((p) => h("i", { style: { flex: `${Math.max(p.share, 0.02)}`, background: css(p.tone) } }))),
      h("div.legend", net.split.map((p) => h("span", h("i.dot", { style: { background: css(p.tone) } }), p.label, " ", h("b", p.value))))));

  const parts = [header];
  if (d.banner) parts.push(h("div.banner", { role: "alert" }, h("div", { html: d.banner.html }), h("button.btn.small", { onclick: () => app.go("datos") }, d.banner.button)));
  parts.push(hero);
  if (d.return.visible) parts.push(stat(d.return, app));
  if (d.savings.visible) parts.push(stat(d.savings, app));
  if (d.forecast) parts.push(stat(d.forecast, app));

  if (d.setup) {
    const s = d.setup;
    parts.push(h("div.card.raised",
      h("div.section-head", h("div", h("h2", { style: { fontFamily: "var(--medium)", fontWeight: "normal", fontSize: "16px", margin: 0 } }, s.title), h("p.caption", s.subtitle)),
        h("button.btn.small", { onclick: async () => { const r = await py("hide_setup"); toast(r.message); app.refresh(); } }, s.hide)),
      h("p.caption", { style: { margin: "6px 0 12px" } }, s.caption),
      s.steps.map((step) => h(`div.step${step.done ? ".done" : ""}`,
        h("span.check", step.done && checkMark()), h("span", step.text),
        !step.done && h("button.btn.small", { onclick: () => app.go(step.target === "accounts" ? "cuentas" : "datos") }, s.go)))));
  }

  if (d.review) {
    const r = d.review;
    parts.push(section(r.title, r.subtitle,
      r.hint && h("p.empty", r.hint),
      r.suggestions.map((sg) => h("div.suggestion", h("b", sg.title), h("p", sg.text),
        h("button.btn.small", { onclick: () => app.newRule(sg.keyword) }, sg.button))),
      h("button.btn.small", { style: { marginTop: "14px" }, onclick: () => app.go("cuentas", { category: "uncategorized" }) }, r.button)));
  }

  if (d.upcoming.visible) parts.push(upcoming(d.upcoming, app));
  if (d.budgets.visible) parts.push(budgetCarousel(d.budgets, app));
  if (d.goals.visible) parts.push(goalsPanel(d.goals, app));

  if (d.allocation.visible) parts.push(section(d.allocation.title, d.allocation.caption, headline(d.allocation.headline), donut(d.allocation)));
  if (d.flow.visible) parts.push(section(d.flow.title, d.flow.caption, headline(d.flow.headline), flowChart(d.flow)));
  const w = d.wealth;
  const series = [{ label: w.legend[0], color: css("accent"), values: w.net, texts: w.net_text, width: 1.9, fill: true }];
  if (w.value_line) series.push({ label: w.legend[1], color: css("text"), values: w.value, texts: w.value_text, width: 1.3 });
  if (w.contributions) series.push({ label: w.legend[2], color: css("neutral"), values: w.contrib, texts: w.contrib_text, width: 1.2, dashed: true });
  parts.push(section(w.title, w.caption, headline(w.headline), lineChart({ labels: w.dates, tips: w.dates_long, series })));

  main.replaceChildren(...parts);
}

function checkMark() {
  const span = h("span", { style: { display: "contents" }, html: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.2 4.2L19 7"/></svg>' });
  return span.firstChild;
}

/** El cielo animado sobre el saludo (en el movil va encima: al lado del saludo no cabe). */
function sky(app) {
  const now = () => { const d = new Date(); return d.getHours() + d.getMinutes() / 60 + d.getSeconds() / 3600; };
  return skyWidget(now, app.state.settings.ambient, app.clock.sky);
}

function headline(text) { return text ? h("p.headline", text) : null; }

function upcoming(u, app) {
  const rows = u.rows.length
    ? h("div.rows",
      h("div.head", h("span", u.columns[0]), h("span.num", u.columns[1]), h("span.num", u.columns[2])),
      u.rows.map((r) => {
        const row = h("div.row", h("span", r.name), h("span.num", r.amount), h("span.num.accent", r.date));
        longPress(row, () => app.menu([{ label: u.remove, run: async () => { const res = await py("set_recurring", { name: r.name, include: false }); app.told(res); } }], r.name));
        return row;
      }))
    : h("p.empty", u.empty);
  return section(u.title, u.subtitle, rows);
}

/** Mantener pulsado (o clic derecho) abre el menu de una fila, como el clic derecho del escritorio. */
export function longPress(el, open) {
  let timer = 0;
  el.addEventListener("contextmenu", (e) => { e.preventDefault(); open(); });
  el.addEventListener("touchstart", () => { timer = setTimeout(open, 520); }, { passive: true });
  for (const ev of ["touchend", "touchmove", "touchcancel"]) el.addEventListener(ev, () => clearTimeout(timer), { passive: true });
}

function budgetCarousel(b, app) {
  const card = h("div.card.raised");
  let index = 0;
  let timer = 0;
  const tones = { ok: "green", warn: "accent", over: "red" };

  function draw() {
    const head = h("div.section-head", h("div", h("h2", { style: { fontFamily: "var(--medium)", fontWeight: "normal", fontSize: "16px", margin: 0 } }, b.title), h("p.caption", b.subtitle)));
    if (!b.items.length) return card.replaceChildren(head, h("p.empty", b.empty));
    const line = b.items[index];
    const controls = h("div.carousel-top",
      h("span.count", b.counter.replace("{n}", index + 1).replace("{total}", b.items.length)),
      h("button.icon-btn", { "aria-label": b.prev, onclick: () => move(-1) }, h("span", { style: { transform: "scaleX(-1)", display: "flex" } }, icon("chevron", 2))),
      h("button.icon-btn", { "aria-label": b.next, onclick: () => move(1) }, icon("chevron", 2)));
    const body = h("div.budget", { onclick: () => app.go("cuentas", { category: line.category }) },
      h("div.name", h("span", line.label), h(`span.state.state-${line.state}`, line.state_text)),
      h("div.amount", h("b", line.spent), h("span", line.of), h("em", line.pct)),
      h("div.track", h("i", { style: { width: `${Math.min(line.share, 1) * 100}%`, background: css(tones[line.state]) } })),
      h(`p.note${line.state === "over" ? ".state-over" : ""}`, line.note));
    const dots = h("div.pager", b.items.map((_, i) => h(`i${i === index ? ".on" : ""}`)));
    card.replaceChildren(head, controls, body, dots);
  }

  function move(step) {
    index = (index + step + b.items.length) % b.items.length;
    draw();
    restart();
  }

  // pasa solo cada pocos segundos (como en el escritorio), salvo si se ha pedido quitar el movimiento
  function restart() {
    clearInterval(timer);
    if (b.items.length > 1 && app.state.settings.ambient)
      timer = setInterval(() => { if (!document.body.contains(card)) return clearInterval(timer); index = (index + 1) % b.items.length; draw(); }, 6000);
  }

  let startX = null;
  card.addEventListener("touchstart", (e) => { startX = e.touches[0].clientX; }, { passive: true });
  card.addEventListener("touchend", (e) => {
    if (startX === null) return;
    const dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50 && b.items.length > 1) move(dx < 0 ? 1 : -1);
    startX = null;
  });
  draw();
  restart();
  return card;
}

function goalsPanel(g, app) {
  return section(g.title, g.subtitle,
    g.items.length
      ? g.items.map((goal) => h("div.goal",
        h("div.top", h("b", { style: { fontWeight: "normal" } }, goal.name), h("span", goal.amount)),
        h("div.track", h("i", { style: { width: `${Math.min(goal.progress, 1) * 100}%`, background: css(goal.reached ? "green" : "accent") } })),
        h("p", goal.note)))
      : h("p.empty", g.empty),
    h("button.btn.small", { style: { marginTop: "14px" }, onclick: () => app.goals() }, g.button));
}

function renderOnboarding(main, o, app) {
  main.replaceChildren(h("div.onboarding",
    h("header.page-head", sky(app), h("h1", { id: "greeting" }, app.clock.greeting), h("p.date", { id: "date-line" }, app.clock.date)),
    h("p", { style: { color: "var(--muted)", margin: 0 } }, o.intro),
    h("div.steps", o.steps.map((s, i) => h("div.step-card", h("span.badge", String(i + 1)), h("div", h("b", s.title), h("p", s.text))))),
    h("div.stack",
      h("button.btn.primary.block", { onclick: () => app.go("datos") }, o.import),
      h("button.btn.block", { title: o.demo_tip, onclick: () => app.startDemo() }, o.demo)),
    h("p.privacy", o.privacy)));
}

export function isoDate(d) {
  const p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
}

export function isoLocal(d) {
  const p = (n) => String(n).padStart(2, "0");
  return `${isoDate(d)}T${p(d.getHours())}:${p(d.getMinutes())}:${p(d.getSeconds())}`;
}

// ----------------------------------------------------------------------------- metas de ahorro (ui/goals_dialog.py)
export async function goalsSheet(app) {
  let g = await py("goals_open");
  let changed = false;
  const list = h("div");
  const s = sheet(h("h2", g.title), h("p", g.text), list,
    h("div.actions",
      h("button.btn", { onclick: () => edit(null) }, g.add),
      h("button.btn.primary", { onclick: close }, g.done)));
  s.panel.parentElement.addEventListener("click", (e) => { if (e.target === s.panel.parentElement) close(); });

  async function close() {
    s.close();
    app.told(await py("goals_close", { changed }));
  }
  function update(next) { g = next; changed = true; draw(); }

  function draw() {
    list.replaceChildren(...(g.items.length ? g.items.map((goal) => h("div.goal",
      h("div.top", h("b", { style: { fontWeight: "normal" } }, goal.name), h("span", goal.amount)),
      h("div.track", h("i", { style: { width: `${Math.min(goal.progress, 1) * 100}%`, background: css(goal.reached ? "green" : "accent") } })),
      h("div.inline", { style: { marginTop: "10px" } },
        h("button.btn.small", { onclick: () => contribute(goal) }, g.contribute),
        h("button.btn.small", { onclick: () => edit(goal) }, g.edit),
        h("button.btn.small.danger", { onclick: () => remove(goal) }, g.delete)))) : [h("p.empty", g.empty)]));
  }

  function edit(goal) {
    const f = g.form;
    const name = h("input", { type: "text", value: goal?.name || "", placeholder: f.placeholder, maxlength: 60 });
    const target = h("input", { type: "number", inputmode: "decimal", min: "0", step: "10", value: goal ? String(goal.target) : "" });
    const saved = h("input", { type: "number", inputmode: "decimal", min: "0", step: "10", value: goal ? String(goal.saved) : "0" });
    const hasDate = h("input", { type: "checkbox", checked: !!goal?.deadline });
    const deadline = h("input", { type: "date", value: goal?.deadline || "", hidden: !goal?.deadline });
    hasDate.addEventListener("change", () => { deadline.hidden = !hasDate.checked; });
    const error = h("p.field-error");
    const form = sheet(h("h2", goal ? f.edit : f.new), h("p", f.text),
      h("span.label", f.name), name, h("span.label", f.target), target, h("span.label", f.saved), saved,
      h("label.check-row", hasDate, h("span", f.deadline)), deadline, error,
      h("div.actions", h("button.btn", { onclick: () => form.close() }, f.cancel),
        h("button.btn.primary", { onclick: async () => {
          if (!name.value.trim()) return (error.textContent = f.no_name);
          if (!(Number(target.value) > 0)) return (error.textContent = f.no_target);
          const r = await py("goal_save", { name: name.value, target: Number(target.value), saved: Number(saved.value) || 0,
            deadline: hasDate.checked && deadline.value ? deadline.value : null, goal_id: goal?.id ?? null });
          if (r.error) return (error.textContent = r.error);
          form.close();
          update(r);
        } }, f.save)));
  }

  function contribute(goal) {
    const amount = h("input", { type: "number", inputmode: "decimal", step: "10", value: "" });
    const form = sheet(h("h2", g.contribute), h("p", g.contribute_text.replace("{name}", goal.name)), amount,
      h("div.actions", h("button.btn", { onclick: () => form.close() }, g.form.cancel),
        h("button.btn.primary", { onclick: async () => {
          const value = Number(String(amount.value).replace(",", "."));
          form.close();
          if (value) update(await py("goal_contribute", { goal_id: goal.id, amount: value }));
        } }, g.form.save)));
    setTimeout(() => amount.focus(), 50);
  }

  async function remove(goal) {
    if (await confirmSheet(g.delete_title, g.delete_text.replace("{name}", goal.name), g.delete, true))
      update(await py("goal_delete", { goal_id: goal.id }));
  }
  draw();
}
