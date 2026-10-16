/* Cinco cosas: el idioma elegido, el tema, las pestañas de la guía, la demostración del difuminado y la sección actual del menú. Sin dependencias. */
(function () {
  "use strict";

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
    try { localStorage.setItem("kreix-theme", next); } catch (e) { /* sin almacenamiento: se queda en esta visita */ }
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
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav a, .pills a'));
  var sections = links.map(function (a) { return document.querySelector(a.getAttribute("href")); }).filter(Boolean);
  if ("IntersectionObserver" in window && sections.length) {
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          var here = a.getAttribute("href") === "#" + entry.target.id;
          if (here) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
          if (here && a.closest(".pills")) a.scrollIntoView({ block: "nearest", inline: "center" });
        });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    sections.forEach(function (s) { seen.observe(s); });
  }
})();
