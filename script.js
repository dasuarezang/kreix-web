/* Cinco cosas: el idioma elegido, el tema, las pestañas de la guía, la demostración del difuminado y la sección actual del menú. Sin dependencias. */
(function () {
  "use strict";

  /* Menú del móvil: un panel bajo la cabecera; se cierra con Esc, al elegir una sección, al tocar fuera o al ensanchar la ventana */
  var toggle = document.getElementById("menu-toggle");
  var menu = document.getElementById("menu");
  function setMenu(open) {
    menu.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }
  toggle.addEventListener("click", function () { setMenu(!menu.classList.contains("open")); });
  Array.prototype.forEach.call(menu.querySelectorAll(".nav a"), function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && menu.classList.contains("open")) { setMenu(false); toggle.focus(); }
  });
  document.addEventListener("click", function (e) {
    if (menu.classList.contains("open") && !menu.contains(e.target) && !toggle.contains(e.target)) setMenu(false);
  });
  matchMedia("(min-width: 1021px)").addEventListener("change", function (e) { if (e.matches) setMenu(false); });

  /* Botón de volver arriba: solo aparece cuando ya se ha bajado un buen trozo */
  var toTop = document.querySelector(".to-top");
  var waiting = false;
  function showToTop() { waiting = false; toTop.classList.toggle("show", window.scrollY > 900); }
  window.addEventListener("scroll", function () { if (!waiting) { waiting = true; requestAnimationFrame(showToTop); } }, { passive: true });
  showToTop();

  /* El idioma que se elige con el selector se recuerda (la primera visita sigue el idioma del navegador) */
  Array.prototype.forEach.call(document.querySelectorAll(".lang a"), function (a) {
    a.addEventListener("click", function () { try { localStorage.setItem("kreix-lang", a.getAttribute("lang")); } catch (e) { /* sin almacenamiento */ } });
  });

  /* Tema claro / oscuro */
  var root = document.documentElement;
  var themeButton = document.getElementById("theme");
  var meta = document.querySelector('meta[name="theme-color"]');
  function syncMeta() { if (meta) meta.setAttribute("content", root.getAttribute("data-theme") === "light" ? "#f6f2ea" : "#101418"); }
  syncMeta();
  themeButton.addEventListener("click", function () {
    var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", next);
    try { sessionStorage.setItem("kreix-theme", next); } catch (e) { /* sin almacenamiento: igual, dura esta visita */ }
    syncMeta();
  });
  /* Si el dispositivo cambia de modo (por ejemplo, al anochecer) y no se ha elegido otro en esta visita, la web lo sigue */
  var systemLight = matchMedia("(prefers-color-scheme: light)");
  systemLight.addEventListener("change", function (e) {
    try { if (sessionStorage.getItem("kreix-theme")) return; } catch (err) { /* sin almacenamiento */ }
    root.setAttribute("data-theme", e.matches ? "light" : "dark");
    syncMeta();
  });

  /* Pestañas de la guía (con flechas, Inicio y Fin) */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  function select(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", on ? "true" : "false");
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
    });
    if (focus) tab.focus();
    if (tab.scrollIntoView) tab.scrollIntoView({ block: "nearest", inline: "nearest" });   /* en móvil la fila de pestañas se desliza */
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () { select(tab, false); });
    tab.addEventListener("keydown", function (e) {
      var go = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
      if (go === undefined) return;
      e.preventDefault();
      select(tabs[(go + tabs.length) % tabs.length], true);
    });
  });

  /* El ojo: difumina la cifra de ejemplo, igual que el programa. Oculta, el número tampoco llega al lector de pantalla */
  var eye = document.getElementById("eye");
  var figure = document.getElementById("figure");
  var figureNote = document.getElementById("figure-sr");
  var label = document.getElementById("eye-text");
  eye.addEventListener("click", function () {
    var hide = figure.getAttribute("data-hidden") !== "true";
    figure.setAttribute("data-hidden", hide ? "true" : "false");
    figure.setAttribute("aria-hidden", hide ? "true" : "false");
    figureNote.hidden = !hide;
    eye.setAttribute("aria-pressed", hide ? "true" : "false");
    label.textContent = hide ? eye.dataset.show : eye.dataset.hide;
  });

  /* La sección que se está leyendo, marcada en el menú (y en la barra de secciones del móvil) */
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav a'));
  var sections = links.map(function (a) { return document.querySelector(a.getAttribute("href")); }).filter(Boolean);
  if ("IntersectionObserver" in window && sections.length) {
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          var here = a.getAttribute("href") === "#" + entry.target.id;
          if (here) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    sections.forEach(function (s) { seen.observe(s); });
  }
})();
