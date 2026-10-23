// Datos: importar extractos (ui/views/import_view.py), recibir del ordenador por QR y exportar (ui/views/export_view.py).
import { alertSheet, confirmSheet, h, py, saveFile, sheet, t, toast } from "./core.js";
import { isoDate } from "./inicio.js";
import { pageHead } from "./parts.js";
import { scanTransfer } from "./qr.js";

const state = { account: null, asOf: isoDate(new Date()), fund: null, last: [], preview: null, results: null };

export async function renderDatos(main, app) {
  const d = await py("datos");
  const im = d.import;
  if (state.account === null || !im.accounts.some((a) => a.id === state.account)) state.account = im.accounts[0].id;

  const picker = h("input", { type: "file", multiple: true, hidden: true, accept: ".csv,.xls,.xlsx,.txt,.kreix,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
  picker.addEventListener("change", async () => {
    const files = [...picker.files];
    picker.value = "";
    if (!files.length) return;
    const payload = await Promise.all(files.map(async (f) => ({ name: f.name, bytes: new Uint8Array(await f.arrayBuffer()) })));
    state.last = await py("put_files", { files: payload });
    await preview(app, true);
  });

  const account = h("select", { "aria-label": im.account_label, onchange: () => { state.account = account.value ? Number(account.value) : null; refreshPreview(app); } },
    im.accounts.map((a) => h("option", { value: a.id ?? "", selected: a.id === state.account }, a.name)));
  const asOf = h("input", { type: "date", value: state.asOf, "aria-label": im.as_of_label, onchange: () => { state.asOf = asOf.value || isoDate(new Date()); refreshPreview(app); } });
  const fund = im.funds.length && h("select", { "aria-label": im.fund_label, onchange: () => { state.fund = fund.value || null; refreshPreview(app); } },
    im.funds.map((f) => h("option", { value: f.isin ?? "", selected: f.isin === state.fund }, f.name)));

  const setting = (label, hint, control) => h("div.setting-col", h("b", label), h("small", hint), control);
  const parts = [
    pageHead(im.eyebrow, im.title, im.subtitle),
    h("div.dropzone", picker,
      h("button.btn.primary.block", { onclick: () => picker.click() }, im.choose),
      h("p", im.choose_hint)),
    h("div.card.settings",
      setting(im.account_label, im.account_hint, account),
      setting(im.as_of_label, im.as_of_hint, asOf),
      fund && setting(im.fund_label, im.fund_hint, fund)),
    h("div", { id: "import-preview" }),
    h("div", { id: "import-results" }),
  ];
  if (d.formats.items.length) parts.push(formats(d.formats, app));

  const r = d.receive;
  parts.push(h("section.section", h("div.rule"), h("h2", r.title), h("p.caption", r.text),
    h("button.btn.block", { style: { marginTop: "14px" }, onclick: () => receive(app, r) }, r.button),
    h("p.caption", { style: { marginTop: "8px" } }, r.replace)));

  parts.push(exportSection(d.export));
  main.replaceChildren(...parts);
  drawPreview(app);
  drawResults();
}

// ----------------------------------------------------------------------------- vista previa e importacion
async function preview(app, askColumns = false) {
  const p = await py("import_preview", { paths: state.last, as_of: state.asOf, account_id: state.account, fund: state.fund });
  if (p.backup) await restore(app, p.backup);
  state.preview = p.rows.length ? p : null;
  state.results = null;
  drawPreview(app);
  drawResults();
  const unknown = p.rows.find((row) => row.map);
  if (askColumns && unknown) openMapping(app, unknown.path);       // como en el escritorio: se pregunta ya mismo
}

function refreshPreview(app) { if (state.preview) preview(app); }

function pill(row) { return h(`span.pill.state-${row.state}`, row.label); }

function drawPreview(app) {
  const box = document.getElementById("import-preview");
  if (!box) return;
  const p = state.preview;
  if (!p) return box.replaceChildren();
  box.replaceChildren(h("section.section", h("div.rule"),
    h("h2", t("Revisa antes de importar")), h("p.caption", t("Esto es lo que Kreix ha leído. Todavía no se ha guardado nada.")),
    p.rows.map((row) => h("div.file-row",
      h("div.top", h("b", row.name), pill(row)),
      row.lines.map((line) => h("p", line)),
      row.warnings.map((w) => h("p.small", `• ${w}`)),
      row.map && h("button.btn.primary.small", { onclick: () => openMapping(app, row.path) }, row.map))),
    h("div.actions",
      h("button.btn", { onclick: () => { state.preview = null; drawPreview(app); } }, t("Cancelar")),
      h("button.btn.primary", { disabled: !p.ready, onclick: () => confirmImport(app) }, p.confirm))));
}

async function confirmImport(app) {
  const pending = state.preview.pending;
  state.preview = null;
  drawPreview(app);
  const r = await py("import_confirm", { paths: pending, as_of: state.asOf, account_id: state.account, fund: state.fund });
  state.results = r;
  state.last = [];
  app.told(r);
}

function drawResults() {
  const box = document.getElementById("import-results");
  if (!box) return;
  const r = state.results;
  if (!r) return box.replaceChildren();
  box.replaceChildren(h("section.section", h("div.rule"), h("h2", t("Resultado")),
    r.rows.map((row) => h("div.file-row", h("div.top", h("b", row.name), pill(row)), h("p", row.detail), row.warnings.map((w) => h("p.small", `• ${w}`)))),
    r.reconcile && h("div.banner", h("div", { html: r.reconcile.title }), r.reconcile.items.map((w) => h("p", `• ${w}`)), h("p.small", r.reconcile.tip))));
}

function formats(f, app) {
  return h("section.section", h("div.rule"), h("h2", f.title), h("p.caption", f.hint),
    f.items.map((item) => h("div.file-row", h("div.top", h("b", item.name),
      h("button.btn.small", { onclick: async () => app.told(await py("forget_format", { name: item.name })) }, f.forget)), h("p", item.detail))));
}

// ----------------------------------------------------------------------------- asistente para otro banco (MappingDialog)
async function openMapping(app, path, headerIndex = null, keep = null) {
  const m = await py("mapping_open", { path, header_index: headerIndex, name: keep?.name || "" });
  if (m.error) return alertSheet(m.error_title, m.error);
  const g = keep ? { ...m.guess, ...keep } : m.guess;
  const L = m.labels;
  const columns = (optional, value) => h("select", {},
    h("option", { value: "" }, optional ? m.unused : m.choose),
    m.headers.map((header, i) => h("option", { value: m.keys[i], selected: m.keys[i] === value }, header)));
  const fields = {
    date: columns(false, g.date), description: columns(false, g.description), amount: columns(false, g.amount),
    income: columns(false, g.income), expense: columns(false, g.expense), balance: columns(true, g.balance),
  };
  const mode = h("select", {}, m.modes.map((o) => h("option", { value: o.value, selected: o.value === g.mode }, o.label)));
  const decimals = h("select", {}, m.decimal_options.map((o) => h("option", { value: String(o.value), selected: o.value === g.decimal_comma }, o.label)));
  const order = h("select", {}, m.order_options.map((o) => h("option", { value: String(o.value), selected: o.value === g.day_first }, o.label)));
  const invert = h("input", { type: "checkbox", checked: !!g.invert_sign });
  const name = h("input", { type: "text", value: g.name, placeholder: m.placeholder });
  const header = h("select", { "aria-label": m.header_label }, m.header_rows.map((n) => h("option", { value: n - 1, selected: n - 1 === m.header_index }, String(n))));
  const result = h("p.headline"), lines = h("pre.sample-lines"), error = h("p.field-error");
  const save = h("button.btn.primary", {}, m.save);

  const table = h("div.sample-scroll", h("table.sample",
    h("thead", h("tr", m.headers.map((x) => h("th", x)))),
    h("tbody", m.rows.map((row) => h("tr", m.headers.map((_, i) => h("td", row[i] ?? "")))))));

  function values() {
    return { name: name.value, date: fields.date.value, description: fields.description.value, amount: fields.amount.value,
      income: fields.income.value, expense: fields.expense.value, balance: fields.balance.value, mode: mode.value,
      decimal_comma: decimals.value === "true", day_first: order.value === "true", invert_sign: invert.checked };
  }
  const two = h("div"), one = h("div");
  async function refresh() {
    const v = values();
    one.hidden = v.mode === "two";
    two.hidden = v.mode !== "two";
    const r = await py("mapping_try", { path, header_index: Number(header.value), fields: v });
    result.textContent = r.result;
    lines.textContent = r.lines.join("\n");
    error.textContent = r.ok ? "" : r.error;
    save.disabled = !r.ok;
  }
  const row = (label, control) => h("label.map-row", h("span", label), control);
  one.append(row(L.amount, fields.amount));
  two.append(row(L.income, fields.income), row(L.expense, fields.expense));
  const s = sheet(h("h2", m.title), h("p", m.text),
    row(m.header_label, header), h("span.label", L.table), table,
    row(L.date, fields.date), row(L.description, fields.description), row(L.mode, mode), one, two,
    h("label.check-row", invert, h("span", m.invert)),
    row(L.balance, fields.balance), row(L.decimals, decimals), row(L.order, order), row(L.name, name),
    result, lines, error,
    h("div.actions", h("button.btn", { onclick: () => s.close() }, m.cancel), save));
  for (const el of [...Object.values(fields), mode, decimals, order, invert]) el.addEventListener("change", refresh);
  name.addEventListener("input", refresh);
  header.addEventListener("change", () => { s.close(); openMapping(app, path, Number(header.value), { name: name.value }); });
  save.addEventListener("click", async () => {
    const r = await py("mapping_save", { fields: values() });
    if (r.error) { error.textContent = r.error; return; }
    s.close();
    toast(r.message);
    if (state.last.length) await preview(app);                    // se vuelve a leer lo pendiente, ya con el formato
    app.render();
  });
  refresh();
}

// ----------------------------------------------------------------------------- restaurar un .kreix y recibir por QR
async function restore(app, path) {
  let password = null;
  for (;;) {
    const check = await py("restore_check", { path, password });
    if (check.error) return alertSheet(check.error_title, check.error);
    if (check.password) {
      if (check.wrong) toast(check.wrong);
      password = await passwordSheet(check.title, check.label);
      if (password === null) return;
      continue;
    }
    if (check.confirm && !(await confirmSheet(check.confirm.title, check.confirm.text, t("Aceptar"), true))) return;
    const r = await py("restore_apply", { path, password });
    if (r.error) return alertSheet(r.error_title, r.error);
    app.page = "inicio";
    return app.told(r);
  }
}

function passwordSheet(title, label) {
  return new Promise((resolve) => {
    const input = h("input", { type: "password", "aria-label": label, autocomplete: "current-password" });
    const s = sheet(h("h2", title), h("p", label), input,
      h("div.actions",
        h("button.btn", { onclick: () => { s.close(); resolve(null); } }, t("Cancelar")),
        h("button.btn.primary", { onclick: () => { s.close(); resolve(input.value); } }, t("Aceptar"))));
    setTimeout(() => input.focus(), 50);
  });
}

async function receive(app, texts) {
  const bytes = await scanTransfer({
    title: texts.title, aim: t("Apunta la cámara al código QR de la pantalla del ordenador."),
    reading: t("Recibiendo… {pct} %"), no_camera: t("No se puede usar la cámara. Revisa el permiso de la cámara para Kreix en los ajustes del móvil."),
  });
  if (!bytes) return;
  const [path] = await py("put_files", { files: [{ name: "qr.bin", bytes }] });
  const r = await py("receive_transfer", { path });
  if (r.error) return alertSheet(r.error_title, r.error);
  await restore(app, r.path);
}

// ----------------------------------------------------------------------------- exportar
function exportSection(e) {
  const encrypt = h("input", { type: "checkbox", checked: true });
  const warn = h("div.banner", { hidden: true }, h("div", { html: e.warn_title }), h("p", e.warn_text));
  encrypt.addEventListener("change", () => { warn.hidden = encrypt.checked; });
  return h("section.section", h("div.rule"),
    h("p.eyebrow", { style: { color: "var(--accent-text)", fontSize: "12px", margin: "0 0 4px" } }, e.eyebrow),
    h("h2", e.title), h("p.caption", e.subtitle),
    h("label.check-row", { style: { borderTop: 0 } }, encrypt, h("span", e.encrypt)),
    h("p.caption", e.encrypt_note), warn,
    h("p.caption", { style: { marginTop: "12px" } }, h("b", { style: { color: "var(--text)", fontFamily: "var(--medium)", fontWeight: "normal" } }, e.what), " — ", e.what_text),
    h("p.caption", e.contents),
    h("button.btn.block", { style: { marginTop: "14px" }, onclick: async () => {
      const r = await py("export_kreix", { encrypt: encrypt.checked });
      if (await saveFile(r.name, r.bytes)) toast(r.message);
    } }, e.button));
}
