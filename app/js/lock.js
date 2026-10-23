// Pantalla de la contrasena maestra (ui/lock_screen.py): crearla la primera vez o desbloquear. Y la bienvenida de la
// primera vez (WelcomeDialog de ui/dialogs.py): idioma, nombre y lo que se quiere gestionar.
import { brand, confirmSheet, h, py, stripes, switchButton } from "./core.js";

/** Muestra la pantalla de bloqueo en `root` y resuelve cuando la contrasena abre los datos. */
export function lockScreen(root, { exists, texts, min_password: minLength }) {
  return new Promise((resolve) => {
    let creating = !exists;
    render();

    function render() {
      const password = h("input", { type: "password", placeholder: texts.password, "aria-label": texts.password, autocomplete: creating ? "new-password" : "current-password" });
      const confirm = h("input", { type: "password", placeholder: texts.confirm, "aria-label": texts.confirm, autocomplete: "new-password" });
      const error = h("p.field-error", { role: "alert" });
      const meter = h("div.meter", { "data-level": "0" }, h("div.bars", [0, 1, 2, 3].map(() => h("i"))), h("span"));
      const hint = h("p.meter-hint", { hidden: true });
      const ok = h("button.btn.primary", { type: "submit" }, creating ? texts.create : texts.unlock);

      let strengthCall = 0;
      async function updateMeter() {
        const ticket = ++strengthCall;
        const s = await py("password_strength", { password: password.value });
        if (ticket !== strengthCall) return;
        meter.dataset.level = s.level;
        meter.querySelectorAll(".bars i").forEach((bar, i) => bar.classList.toggle("on", i < s.filled));
        meter.querySelector("span").textContent = s.word;
        hint.textContent = s.hint;
        hint.hidden = !s.hint;
      }
      if (creating) {
        password.addEventListener("input", updateMeter);
        updateMeter();
      }

      async function submit(event) {
        event.preventDefault();
        error.textContent = "";
        if (!password.value) return fail(texts.empty);
        if (creating) {
          if (password.value.length < minLength) return fail(texts.too_short);
          if (password.value !== confirm.value) return fail(texts.mismatch);
        }
        ok.disabled = true;
        ok.textContent = texts.opening;
        try {
          const result = await py(creating ? "create" : "unlock", { password: password.value });
          if (result.error) {
            ok.disabled = false;
            ok.textContent = creating ? texts.create : texts.unlock;
            return fail(result.error);
          }
          password.value = confirm.value = "";
          resolve();
        } catch (e) {
          ok.disabled = false;
          ok.textContent = creating ? texts.create : texts.unlock;
          fail(e.message);
        }
      }

      function fail(message) {
        error.textContent = message;
        password.focus();
        password.select();
      }

      async function forgot() {
        const yes = await confirmSheet(texts.reset_title, texts.reset_body, texts.reset_title, true);
        if (!yes) return;
        await py("reset");
        creating = true;
        render();
      }

      root.replaceChildren(h("div.screen",
        h("div.screen-head", brand(), stripes()),
        h("form.panel", { onsubmit: submit },
          h("h1", creating ? texts.create_title : texts.unlock_title),
          h("p.intro", creating ? texts.create_body : texts.unlock_body),
          h("div.stack",
            password,
            creating && meter,
            creating && hint,
            creating && confirm),
          error,
          h("div.actions", !creating && h("button.link", { type: "button", onclick: forgot, style: { marginRight: "auto" } }, texts.forgot), ok)),
        h("p.screen-foot", texts.footer)));
      setTimeout(() => password.focus(), 50);
    }
  });
}

// ----------------------------------------------------------------------------- banderas (ui/flags.py)
const FLAGS = {
  es: '<rect width="24" height="24" fill="#AA151B"/><rect y="6" width="24" height="12" fill="#F1BF00"/>',
  ca: '<rect width="24" height="24" fill="#FCDD09"/>' + [1, 3, 5, 7].map((i) => `<rect y="${i * 24 / 9}" width="24" height="${24 / 9}" fill="#DA121A"/>`).join(""),
  en: '<rect width="24" height="24" fill="#012169"/>' +
      '<path d="M-24-24L48 48M48-24L-24 48" stroke="#FFF" stroke-width="4.8"/><path d="M-24-24L48 48M48-24L-24 48" stroke="#C8102E" stroke-width="1.92"/>' +
      '<rect x="7.92" width="8.16" height="24" fill="#FFF"/><rect y="7.92" width="24" height="8.16" fill="#FFF"/>' +
      '<rect x="9.6" width="4.8" height="24" fill="#C8102E"/><rect y="9.6" width="24" height="4.8" fill="#C8102E"/>',
};

export function flag(code) {
  const span = document.createElement("span");
  span.innerHTML = `<svg class="flag" viewBox="0 0 24 24" aria-hidden="true"><clipPath id="f-${code}"><circle cx="12" cy="12" r="12"/></clipPath><g clip-path="url(#f-${code})">${FLAGS[code]}</g></svg>`;
  return span.firstChild;
}

export function languagePicker(languages, current, onpick) {
  const row = h("div.choice", { role: "group" });
  for (const lang of languages) {
    row.append(h("button", {
      type: "button", "aria-pressed": String(lang.code === current),
      onclick: () => {
        row.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", "false"));
        row.querySelector(`[data-code="${lang.code}"]`).setAttribute("aria-pressed", "true");
        onpick(lang.code);
      },
      "data-code": lang.code,
    }, flag(lang.code), lang.name));
  }
  return row;
}

/** Cuentas e inversiones (ui/widgets/interests.py): siempre queda al menos una activada. */
export function interestsRows(texts, state, onchange) {
  const hint = h("p.meter-hint", { hidden: true, role: "status" }, texts.at_least_one);
  const row = (key, title, text) => h("div.setting-row",
    h("div.txt", h("b", title), h("small", text)),
    switchButton(state[key], (on) => {
      const other = key === "accounts" ? "investments" : "accounts";
      if (!on && !state[other]) { hint.hidden = false; return false; }
      hint.hidden = true;
      state[key] = on;
      onchange && onchange({ ...state });
    }, title));
  return h("div",
    row("accounts", texts.accounts_title, texts.accounts_text),
    row("investments", texts.investments_title, texts.investments_text),
    hint);
}

/** La bienvenida de la primera vez. Resuelve con el estado de la app ya guardado. */
export function welcomeScreen(root, state) {
  return new Promise((resolve) => {
    const s = state.settings;
    const choice = { name: s.user_name, language: s.language, accounts: s.interest_accounts, investments: s.interest_investments };

    async function render() {
      const texts = await py("welcome_texts", { language: choice.language });
      const name = h("input", { type: "text", value: choice.name, placeholder: texts.name_placeholder, "aria-label": texts.name_placeholder, maxlength: 40, autocomplete: "given-name" });
      name.addEventListener("input", () => { choice.name = name.value; });
      async function finish(accepted) {
        const next = await py("finish_welcome", { accepted, name: choice.name, language: choice.language, accounts: choice.accounts, investments: choice.investments });
        resolve(next);
      }
      root.replaceChildren(h("div.screen",
        h("div.screen-head", brand(), stripes()),
        h("div.panel",
          h("h1", texts.title),
          h("p.intro", texts.intro),
          h("span.label", texts.ask_language),
          languagePicker(state.languages, choice.language, (code) => { choice.language = code; render(); }),
          h("span.label", texts.ask_name),
          name,
          h("span.label", texts.ask_interest),
          interestsRows(texts, choice),
          h("div.actions",
            h("button.btn", { onclick: () => finish(false) }, texts.cancel),
            h("button.btn.primary", { onclick: () => finish(true) }, texts.ok)))));
    }
    render();
  });
}
