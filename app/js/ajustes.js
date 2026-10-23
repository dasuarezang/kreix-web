// Ajustes (ui/views/settings_view.py) y Ayuda (ui/views/help_view.py).
import { confirmSheet, h, icon, py, sheet, switchButton, toast } from "./core.js";
import { newRule } from "./cuentas.js";
import { interestsRows, languagePicker } from "./lock.js";
import { pageHead } from "./parts.js";

function group(title, ...rows) {
  return h("section.section", h("div.rule"), h("h2.group-title", title), h("div.card.group", ...rows));
}

function field(title, hint, ...control) {
  return h("div.setting-col", h("b", title), hint && h("small", hint), ...control);
}

export async function renderAjustes(main, app) {
  const a = await py("ajustes");
  const s = a.settings;
  const save = async (changes, rerender = false) => {
    app.state = await py("save_settings", changes);
    if (rerender) await app.reload();
  };

  const name = h("input", { type: "text", value: s.user_name, placeholder: a.name.placeholder, maxlength: 40, "aria-label": a.name.title });
  const saveName = h("button.btn", { disabled: true }, a.name.save);
  name.addEventListener("input", () => { saveName.disabled = name.value.trim() === s.user_name; });
  saveName.addEventListener("click", async () => {
    const r = await py("save_name", { name: name.value });
    toast(r.message);
    await app.reload();
  });

  const textSize = h("select", { "aria-label": a.text.title, onchange: () => save({ text_scale: Number(textSize.value) }, true) },
    a.text.options.map((o) => h("option", { value: o.value, selected: o.value === s.text_scale }, o.label)));
  const lockAfter = h("select", { "aria-label": a.security.auto_title, onchange: () => save({ auto_lock_minutes: Number(lockAfter.value) }) },
    a.security.auto_options.map((o) => h("option", { value: o.value, selected: o.value === s.auto_lock_minutes }, o.label)));

  const switchRow = (key, title, text, after) => h("div.setting-row",
    h("div.txt", h("b", title), h("small", text)),
    switchButton(s[key], (on) => { save({ [key]: on }, after); }, title));

  const rules = a.rules.items.length
    ? a.rules.items.map((r) => h("div.rule-row", h("b", r.keyword), h("span.muted", `→  ${r.category}`),
      h("button.btn.small", { onclick: async () => app.told(await py("delete_rule", { rule_id: r.id })) }, a.rules.remove)))
    : [h("p.empty", { style: { marginTop: 0 } }, a.rules.empty)];

  main.replaceChildren(
    pageHead(a.eyebrow, a.title, ""),
    group(a.groups.you,
      field(a.name.title, a.name.hint, h("div.inline", name, saveName)),
      field(a.language.title, a.language.hint, languagePicker(a.language.options, s.language, async (code) => {
        await save({ language: code });
        await app.reload();
      })),
      field(a.interests.title, a.interests.hint, interestsRows(a.interests, { accounts: s.interest_accounts, investments: s.interest_investments },
        (st) => save({ interest_accounts: st.accounts, interest_investments: st.investments }, true)))),
    group(a.groups.look,
      field(a.text.title, a.text.hint, textSize),
      ...a.switches.map((sw) => switchRow(sw.key, sw.title, sw.text, sw.key !== "ambient")),
      field(a.rules.title, a.rules.intro, ...rules, h("button.btn.small", { style: { marginTop: "10px", alignSelf: "flex-start" }, onclick: () => newRule(app) }, a.rules.add))),
    group(a.groups.security,
      field(a.security.title, a.security.hint, h("div.inline",
        h("button.btn", { onclick: () => changePassword(app) }, a.security.change),
        h("button.btn", { onclick: () => app.lock() }, a.security.lock))),
      field(a.security.auto_title, a.security.auto_hint, lockAfter),
      switchRow("lock_on_minimize", a.security.leave_title, a.security.leave_text, false)),
    group(a.groups.backups, field(a.groups.backups, a.backups.text, h("button.btn", { style: { alignSelf: "flex-start" }, onclick: () => app.go("datos") }, a.backups.button))),
    group(a.groups.app,
      field(a.data.title, a.data.hint, h("button.btn.danger", { style: { alignSelf: "flex-start" }, onclick: async () => {
        if (await confirmSheet(a.data.reset_title, a.data.reset_text, a.data.reset, true)) app.told(await py("reset_data"));
      } }, a.data.reset)),
      field(a.about.title, a.about.version, h("div.inline",
        h("button.btn", { onclick: () => whatsNew() }, a.about.whats_new),
        h("button.btn", { onclick: () => app.go("ayuda") }, a.about.help)))));
}

async function changePassword(app) {
  const p = await py("password_texts");
  const field = (label, autocomplete) => h("input", { type: "password", placeholder: label, "aria-label": label, autocomplete });
  const current = field(p.current, "current-password"), next = field(p.new, "new-password"), again = field(p.again, "new-password");
  const error = h("p.field-error");
  const ok = h("button.btn.primary", {}, p.ok);
  const s = sheet(h("h2", p.title), h("p", p.text), h("div.stack", current, next, again), error,
    h("div.actions", h("button.btn", { onclick: () => s.close() }, p.cancel), ok));
  ok.addEventListener("click", async () => {
    if (!current.value) return (error.textContent = p.empty);
    if (next.value.length < p.min) return (error.textContent = p.short);
    if (next.value !== again.value) return (error.textContent = p.mismatch);
    ok.disabled = true;
    const r = await py("change_password", { old: current.value, new: next.value });
    ok.disabled = false;
    if (r.error) return (error.textContent = r.error);
    s.close();
    toast(r.message);
  });
  setTimeout(() => current.focus(), 50);
}

async function whatsNew() {
  const w = await py("whats_new");
  sheet(h("h2", w.title), w.items.map((i) => h("div", { style: { marginTop: "14px" } }, h("b", { style: { fontFamily: "var(--medium)", fontWeight: "normal" } }, i.title), h("p", i.text))));
}

// ----------------------------------------------------------------------------- Ayuda
const help = { query: "", section: null };

export async function renderAyuda(main, app, params = {}) {
  if (params.section !== undefined) { help.section = params.section; help.query = ""; params.section = undefined; }
  const d = await py("ayuda", { query: help.query, section: help.section });
  const search = h("input", { type: "search", placeholder: d.search, "aria-label": d.search_label, value: help.query });
  let timer = 0;
  search.addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(async () => {
      help.query = search.value;
      await app.render();
      const again = main.querySelector('input[type="search"]');
      again?.focus();
      again?.setSelectionRange(again.value.length, again.value.length);
    }, 200);
  });
  const parts = [pageHead(d.eyebrow, d.title, d.subtitle), search];
  if (d.entries && (help.query.trim() || help.section)) {
    if (help.section && !help.query.trim())
      parts.push(h("button.btn.small", { style: { marginTop: "16px" }, onclick: () => { help.section = null; app.render(); } }, `‹  ${d.back}`),
        h("header.page-head", h("h1", d.section_title), h("p.sub", d.section_text)));
    if (d.summary) parts.push(h("p.caption", { style: { marginTop: "14px" } }, d.summary));
    if (d.empty) parts.push(h("p.empty", d.empty));
    parts.push(...d.entries.map(entryCard));
  } else {
    parts.push(h("div.hub", d.sections.map((s) => h("button.hub-card", { onclick: () => { help.section = s.key; app.render(); window.scrollTo(0, 0); } },
      h("span.hub-icon", icon(s.icon)), h("span", h("b", s.title), h("small", s.text))))));
  }
  main.replaceChildren(...parts);
}

function entryCard(e) {
  return h("article.entry", h("h3", e.term), h("p", e.plain),
    e.parts.map((p) => h(`div.entry-part${p.tone ? "." + p.tone : ""}`, h("b", p.label), h("p", p.text))));
}

