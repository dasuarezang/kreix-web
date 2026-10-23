// Cuentas (ui/views/accounts_view.py): metricas por mes o de todo el historial, graficos, presupuestos, pagos recurrentes
// y la lista de movimientos con buscador, filtro por categoria y menu de cada movimiento.
import { categoryBars, flowChart, pyLines } from "./charts.js";
import { alertSheet, confirmSheet, css, h, plain, promptSheet, py, saveFile, sheet, t, toast } from "./core.js";
import { longPress, section } from "./inicio.js";
import { chartSection, emptyState, offState, pagedList, pageHead, periodBar, statBand } from "./parts.js";

const state = { accounts: null, month: null, category: null, search: "" };

export async function renderCuentas(main, app, params = {}) {
  if (params.category) {                      // desde Inicio (un presupuesto o "Por clasificar"): esa categoria, en el mes actual
    state.category = params.category;
    state.search = "";
    params.category = null;
  }
  const d = await py("cuentas", { accounts: state.accounts, month: state.month });
  if (d.off) return main.replaceChildren(offState(d.off, "accounts", app));
  state.month = d.period.current;

  const picker = d.accounts.length > 1 && h("button.btn.small", { onclick: () => pickAccounts(d, app) }, d.picker.label);
  const manage = h("button.icon-btn", { "aria-label": d.manage.title, onclick: () => manageAccounts(d, app) }, "⋯");
  const parts = [
    pageHead(d.eyebrow, d.title, d.subtitle, manage),
    h("div.toolbar", picker, d.has_movements && periodBar(d.period, (month) => { state.month = month; app.render(); })),
  ];
  if (!d.has_movements) return main.replaceChildren(...parts, emptyState(d.empty, app));

  parts.push(statBand(d.cards, app), statBand(d.minis, app, true));
  const c = d.categories;
  parts.push(chartSection(c.title, c.caption, c.headline, categoryBars(c, (value) => showCategory(value, d, app))));
  parts.push(chartSection(d.balance.title, d.balance.caption, d.balance.headline, pyLines(d.balance)));
  parts.push(chartSection(d.monthly.title, d.monthly.caption, d.monthly.headline, flowChart(d.monthly)));
  parts.push(budgetPanel(d.budgets, app, d));
  parts.push(recurringPanel(d.recurring, app));
  parts.push(movements(d, app));
  main.replaceChildren(...parts);
  if (state.category && params.scrollToMovements !== false) {
    const list = main.querySelector("#movements");
    list && list.scrollIntoView({ block: "start" });
  }
}

function showCategory(value, d, app) {
  state.category = value;
  state.search = "";
  app.render().then(() => {
    const n = d.movements.rows.filter((r) => r[4] === value).length;
    const label = d.categories.items.find((c) => c.value === value)?.label || d.budgets.items.find((b) => b.value === value)?.label || "";
    toast((n === 1 ? d.movements.category_shown_one : d.movements.category_shown).replace("{n}", n).replace("{category}", label));
  });
}

// ----------------------------------------------------------------------------- cuentas (selector y gestion)
function pickAccounts(d, app) {
  const chosen = new Set(d.accounts.filter((a) => a.selected).map((a) => a.id));
  const boxes = d.accounts.map((a) => {
    const box = h("input", { type: "checkbox", checked: chosen.has(a.id) });
    box.addEventListener("change", () => { box.checked ? chosen.add(a.id) : chosen.delete(a.id); });
    return h("label.check-row", box, h("span", a.name));
  });
  const s = sheet(h("h2", d.picker.all), ...boxes,
    h("div.actions",
      h("button.btn", { onclick: () => { state.accounts = null; s.close(); app.render(); } }, d.picker.all),
      h("button.btn.primary", { onclick: () => {
        state.accounts = chosen.size && chosen.size < d.accounts.length ? [...chosen] : null;
        s.close();
        app.render();
      } }, t("Aceptar"))));
}

async function manageAccounts(d, app) {
  const texts = await py("account_texts");
  const m = d.manage;
  app.menu([
    { label: m.add, run: async () => {
      const name = await promptSheet(texts.add_title, texts.add_label);
      if (!name) return;
      const r = await py("add_account", { name });
      if (r.error) return alertSheet(r.error_title, r.error);
      state.accounts = [r.id];
      app.told(r);
    } },
    m.single && { label: m.rename, run: async () => {
      const name = await promptSheet(texts.rename_title, texts.rename_label, m.single_name);
      if (!name) return;
      const r = await py("rename_account", { account_id: m.single_id, name });
      if (r.error) return alertSheet(r.error_title, r.error);
      app.told(r);
    } },
    m.single && { label: m.delete, run: async () => {
      const yes = await confirmSheet(texts.delete_title, texts.delete_text.replace("{currentText}", m.single_name), texts.delete_title, true);
      if (!yes) return;
      state.accounts = null;
      app.told(await py("delete_account", { account_id: m.single_id }));
    } },
  ].filter(Boolean), m.title);
}

// ----------------------------------------------------------------------------- presupuestos y pagos recurrentes
const TONES = { ok: "green", warn: "accent", over: "red" };

function budgetPanel(b, app, d) {
  return section(b.title, b.subtitle,
    b.items.length
      ? b.items.map((line) => h("button.budget-line", { onclick: () => showCategory(line.value, d, app) },
        h("div.top", h("span", line.label), h("span.muted", line.amount)),
        h("div.track", h("i", { style: { width: `${Math.min(line.share, 1) * 100}%`, background: css(TONES[line.state]) } })),
        h(`p${line.state === "over" ? ".state-over" : ".muted"}`, line.note)))
      : h("p.empty", b.empty),
    h("button.btn.small", { style: { marginTop: "14px" }, onclick: () => editBudgets(app) }, b.button));
}

export async function editBudgets(app) {
  const b = await py("budget_texts");
  const inputs = b.items.map((item) => {
    const input = h("input", { type: "number", inputmode: "decimal", min: "0", step: "10", value: item.amount ? String(item.amount) : "", placeholder: "0", "aria-label": item.label });
    return [item.value, input, h("label.budget-row", h("span", item.label), input)];
  });
  const s = sheet(h("h2", b.title), h("p", b.text), ...inputs.map(([, , row]) => row),
    h("div.actions",
      h("button.btn", { onclick: () => s.close() }, b.cancel),
      h("button.btn.primary", { onclick: async () => {
        const budgets = Object.fromEntries(inputs.map(([value, input]) => [value, Number(input.value.replace(",", ".")) || 0]));
        s.close();
        app.told(await py("save_budgets", { budgets }));
      } }, b.save)));
}

function recurringPanel(r, app) {
  return section(r.title, r.subtitle, r.rows.length
    ? h("div.rows",
      h("div.head", h("span", r.columns[0]), h("span.num", r.columns[1]), h("span.num", r.columns[2])),
      r.rows.map((row) => {
        const el = h("div.row", h("span", row.name), h("span.num", row.amount), h("span.num.accent", row.date));
        longPress(el, () => app.menu([{ label: r.remove, run: async () => app.told(await py("set_recurring", { name: row.name, include: false })) }], row.name));
        return el;
      }))
    : h("p.empty", r.empty));
}

// ----------------------------------------------------------------------------- movimientos
function movements(d, app) {
  const m = d.movements;
  const search = h("input", { type: "search", placeholder: m.search, "aria-label": m.search, value: state.search });
  const cats = [...new Map(m.rows.map((r) => [r[4], r[5]])).entries()].sort((a, b) => a[1].localeCompare(b[1]));
  if (state.category && !cats.some(([v]) => v === state.category)) state.category = null;
  const filter = h("select", { "aria-label": m.all },
    h("option", { value: "" }, m.all), cats.map(([value, label]) => h("option", { value, selected: value === state.category }, label)));
  const count = h("span.muted");
  const holder = h("div");
  let visible = [];

  function apply() {
    state.search = search.value.trim();
    state.category = filter.value || null;
    const text = state.search.toLowerCase();
    visible = m.rows.filter((r) => (!state.category || r[4] === state.category) && (!text || r[3].toLowerCase().includes(text)));
    count.textContent = visible.length === m.rows.length ? m.count.replace("{total}", m.rows.length)
      : m.count_filtered.replace("{shown}", visible.length).replace("{total}", m.rows.length);
    holder.replaceChildren(pagedList(visible, (r) => movementRow(r, m, app)));
  }
  let timer = 0;
  search.addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(apply, m.rows.length > 1500 ? 160 : 0); });
  filter.addEventListener("change", apply);
  apply();

  async function exportVisible() {
    if (!visible.length) return;
    const r = await py("export_movements", { hashes: visible.map((row) => row[0]), fmt: "xlsx" });
    if (r.error) return alertSheet(r.error_title, r.error);
    if (await saveFile(r.name, r.bytes)) toast(r.message);
  }

  return h("section.section", { id: "movements" }, h("div.rule"),
    h("div.section-head", h("div", h("h2", m.title), count), h("button.btn.small", { onclick: exportVisible }, m.export)),
    h("p.caption", { style: { margin: "6px 0 12px" } }, m.hint),
    h("div.filters", search, filter),
    holder);
}

function movementRow(r, m, app) {
  const [hash, date, account, description, , category, amount, sign, balance] = r;
  const el = h("div.move",
    h("div.move-main", h("b", description), h("span.muted", [date, m.show_account && account, category].filter(Boolean).join("  ·  "))),
    h("div.move-side", h(`span.amount${sign > 0 ? ".tone-positive" : sign < 0 ? ".tone-negative" : ""}`, amount), h("span.muted", balance)));
  el.setAttribute("aria-label", plain(`${description} ${amount}`));
  const open = () => movementMenu(hash, app);
  longPress(el, open);
  el.addEventListener("click", open);
  return el;
}

async function movementMenu(hash, app) {
  const menu = await py("movement_menu", { tx_hash: hash });
  if (!menu.description) return;
  app.menu([
    { label: menu.change, run: () => pickCategory(menu, app) },
    menu.manual && { label: menu.reset, run: async () => app.told(await py("change_category", { tx_hash: hash, category: null })) },
    { label: menu.rule, run: () => newRule(app, menu.keyword, menu.category) },
    menu.recurring && { label: menu.recurring.label, run: async () => app.told(await py("set_recurring", { name: menu.description, include: menu.recurring.include })) },
    { label: menu.copy, run: () => navigator.clipboard?.writeText(menu.description) },
  ].filter(Boolean), menu.description);

  function pickCategory() {
    const s = sheet(h("h2", menu.change), menu.categories.map((c) => h("button.menu-item", {
      "aria-pressed": String(c.value === menu.category),
      onclick: async () => { s.close(); app.told(await py("change_category", { tx_hash: hash, category: c.value })); },
    }, c.label, c.value === menu.category ? "  ✓" : "")));
  }
}

/** La regla de categoria (RuleDialog): palabra clave y categoria. */
export async function newRule(app, keyword = "", category = null) {
  const r = await py("rule_texts", { keyword, category });
  const word = h("input", { type: "text", value: r.keyword, placeholder: r.placeholder, "aria-label": r.keyword_label });
  const select = h("select", { "aria-label": r.category_label },
    r.categories.map((c) => h("option", { value: c.value, selected: c.value === r.category }, c.label)));
  const s = sheet(h("h2", r.title), h("p", r.text),
    h("span.label", r.keyword_label), word, h("span.label", r.category_label), select,
    h("div.actions",
      h("button.btn", { onclick: () => s.close() }, r.cancel),
      h("button.btn.primary", { onclick: async () => {
        if (!word.value.trim()) return word.focus();
        const res = await py("add_rule", { keyword: word.value.trim(), category: select.value });
        if (res.error) return alertSheet(res.error_title, res.error);
        s.close();
        app.told(res);
      } }, r.save)));
}
