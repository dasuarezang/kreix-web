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

  /* El selector de navegador (Android) queda centrado bajo el selector de sistema: se mide el ancho de este y se pasa al CSS */
  var osTabs = document.getElementById("os-tabs");
  if (osTabs) {
    var setOsW = function () { document.documentElement.style.setProperty("--os-w", osTabs.offsetWidth + "px"); };
    setOsW();
    if (window.ResizeObserver) new ResizeObserver(setOsW).observe(osTabs); else window.addEventListener("resize", setOsW);
    window.addEventListener("load", setOsW);
  }

  /* Botón de volver arriba: solo aparece cuando ya se ha bajado un buen trozo */
  var toTop = document.querySelector(".to-top");
  var waiting = false;
  var lastY = window.scrollY, goingUp = false, narrow = matchMedia("(max-width: 1020px)");
  /* en el móvil solo aparece al subir (así no tapa el texto mientras se lee hacia abajo) */
  function showToTop() {
    waiting = false;
    var y = window.scrollY;
    if (Math.abs(y - lastY) > 6) { goingUp = y < lastY; lastY = y; }
    toTop.classList.toggle("show", y > 900 && (!narrow.matches || goingUp));
  }
  window.addEventListener("scroll", function () { if (!waiting) { waiting = true; requestAnimationFrame(showToTop); } }, { passive: true });
  showToTop();

  /* Cabecera: al bajar estrena una línea con las barras de la marca */
  var header = document.querySelector(".top");
  function markScrolled() { header.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", markScrolled, { passive: true });
  markScrolled();

  /* Selectores de idioma (el de la cabecera y el del pie): un botón con el idioma actual que abre la lista (se cierra con Esc o al tocar fuera) */
  Array.prototype.forEach.call(document.querySelectorAll(".lang, .foot-lang"), function (langBox) {
    var langBtn = langBox.querySelector(".lang-btn, .foot-btn");
    if (!langBtn) return;
    function setLang(open) { langBox.classList.toggle("open", open); langBtn.setAttribute("aria-expanded", open ? "true" : "false"); }
    langBtn.addEventListener("click", function () { setLang(!langBox.classList.contains("open")); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && langBox.classList.contains("open")) { setLang(false); langBtn.focus(); } });
    document.addEventListener("click", function (e) { if (langBox.classList.contains("open") && !langBox.contains(e.target)) setLang(false); });
  });

  /* El idioma que se elige con el selector se recuerda (la primera visita sigue el idioma del navegador) */
  Array.prototype.forEach.call(document.querySelectorAll(".lang a, .foot-lang a"), function (a) {
    a.addEventListener("click", function () { try { localStorage.setItem("kreix-lang", a.getAttribute("lang")); } catch (e) { /* sin almacenamiento */ } });
  });

  /* Tema claro / oscuro */
  var root = document.documentElement;
  var themeButtons = document.querySelectorAll(".theme, .foot-theme");   /* el de la cabecera y el del pie */
  var meta = document.querySelector('meta[name="theme-color"]');
  function syncMeta() { if (meta) meta.setAttribute("content", root.getAttribute("data-theme") === "light" ? "#d0c4a6" : "#030405"); }
  syncMeta();
  function toggleTheme() {
    var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", next);
    try { sessionStorage.setItem("kreix-theme", next); } catch (e) { /* sin almacenamiento: igual, dura esta visita */ }
    syncMeta();
  }
  Array.prototype.forEach.call(themeButtons, function (b) { b.addEventListener("click", toggleTheme); });
  /* Si el dispositivo cambia de modo (por ejemplo, al anochecer) y no se ha elegido otro en esta visita, la web lo sigue */
  var systemLight = matchMedia("(prefers-color-scheme: light)");
  systemLight.addEventListener("change", function (e) {
    try { if (sessionStorage.getItem("kreix-theme")) return; } catch (err) { /* sin almacenamiento */ }
    root.setAttribute("data-theme", e.matches ? "light" : "dark");
    syncMeta();
  });

  /* Pestañas (con flechas, Inicio y Fin): las pantallas de la guía y, en «Kreix en el móvil», el tipo de teléfono */
  Array.prototype.forEach.call(document.querySelectorAll('[role="tablist"]'), function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    function select(tab, focus, byUser) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
      });
      if (focus) tab.focus();
      if (byUser && tab.scrollIntoView) tab.scrollIntoView({ block: "nearest", inline: "nearest" });   /* en móvil la fila de pestañas se desliza */
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab, false, true); });
      tab.addEventListener("keydown", function (e) {
        var go = { ArrowRight: i + 1, ArrowLeft: i - 1, ArrowDown: i + 1, ArrowUp: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
        if (go === undefined) return;
        e.preventDefault();
        select(tabs[(go + tabs.length) % tabs.length], true, true);
      });
    });
    /* La guía de instalación se abre por el teléfono desde el que se lee (un iPad moderno dice ser un Mac, pero es táctil) */
    if (list.id === "os-tabs") {
      var ua = navigator.userAgent || "";
      if (/iPhone|iPad|iPod/i.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1)) select(document.getElementById("t-iphone"), false, false);
    }
    /* y en un Samsung, el navegador que trae es Samsung Internet */
    if (list.id === "br-tabs" && /SamsungBrowser/i.test(navigator.userAgent || "")) select(document.getElementById("t-samsung"), false, false);
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

/* El tráiler de la portada: un reloj propio recorre las escenas (cada una se anima sola con CSS al recibir la clase "on"),
   escala el lienzo al ancho disponible, cuenta las cifras y atiende los mandos. Sin dependencias. */
(function () {
  "use strict";
  var root = document.getElementById("trailer");
  if (!root || !window.requestAnimationFrame) return;
  var stage = document.getElementById("tr-stage");
  var canvas = document.getElementById("tr-canvas");
  var start = document.getElementById("tr-start");
  var startText = start.querySelector("span");
  var toggle = document.getElementById("tr-toggle");
  var segBox = document.getElementById("tr-segs");
  var scenes = Array.prototype.slice.call(canvas.querySelectorAll(".tr-scene"));
  var caps = Array.prototype.slice.call(document.querySelectorAll("#tr-caps li"));
  var calm = matchMedia("(prefers-reduced-motion: reduce)");
  var narrow = matchMedia("(max-width: 640px)");
  var english = (document.documentElement.lang || "es").slice(0, 2) === "en";

  /* Cifras con el formato de cada idioma, igual que el programa: 8.586,64 € o €8,586.64 */
  function format(value, kind) {
    var signed = kind.charAt(kind.length - 1) === "+";
    var base = signed ? kind.slice(0, -1) : kind;
    var sign = value < 0 ? "-" : (signed ? "+" : "");
    var parts = Math.abs(value).toFixed(base === "pct0" ? 0 : 2).split(".");
    var number = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, english ? "," : ".") + (parts[1] ? (english ? "." : ",") + parts[1] : "");
    if (base === "eur") return english ? sign + "€" + number : sign + number + " €";
    return sign + number + (english ? "%" : " %");
  }
  var counters = scenes.map(function () { return []; });
  Array.prototype.forEach.call(canvas.querySelectorAll("[data-n]"), function (el) {
    var value = parseFloat(el.getAttribute("data-n")), kind = el.getAttribute("data-f");
    el.textContent = format(value, kind);
    var count = el.getAttribute("data-count");
    if (!count) return;
    var at = count.split(",");
    counters[scenes.indexOf(el.closest(".tr-scene"))].push({ el: el, value: value, kind: kind, from: +at[0], span: +at[1], shown: "" });
  });

  /* El lienzo tiene tamaño fijo y se escala entero: así el móvil y el ordenador ven lo mismo */
  function fit() {
    var tall = narrow.matches;
    root.setAttribute("data-layout", tall ? "tall" : "wide");
    canvas.style.setProperty("--s", (stage.clientWidth / (tall ? 400 : 960)).toFixed(4));
    root.classList.add("ready");
  }
  fit();
  if (window.ResizeObserver) new ResizeObserver(fit).observe(stage); else window.addEventListener("resize", fit);

  /* La línea de tiempo */
  var lengths = scenes.map(function (s) { return +s.getAttribute("data-d"); });
  var starts = [], total = 0;
  lengths.forEach(function (d) { starts.push(total); total += d; });
  var segs = scenes.map(function (s, i) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "tr-seg";
    b.style.setProperty("--grow", lengths[i]);
    b.setAttribute("aria-label", (i + 1) + ". " + caps[i].textContent);
    b.innerHTML = "<span><i></i></span>";
    b.addEventListener("click", function () { seek(i); });
    segBox.appendChild(b);
    return b.querySelector("i");
  });

  var time = 0, current = 0, last = 0, frameId = 0, state = "idle";
  function clamp(x) { return x < 0 ? 0 : (x > 1 ? 1 : x); }
  function setState(next) {
    state = next;
    root.setAttribute("data-state", next);
    toggle.setAttribute("aria-label", root.getAttribute(next === "playing" ? "data-pause" : "data-play"));
    if (next === "ended") startText.textContent = start.getAttribute("data-again");
  }
  function show(index, restart) {
    if (index === current && !restart) return;
    scenes.forEach(function (s) { s.classList.remove("on"); });
    caps.forEach(function (c, k) { c.classList.toggle("on", k === index); });
    void canvas.offsetWidth;                       /* para que las animaciones de la escena empiecen de cero */
    scenes[index].classList.add("on");
    current = index;
  }
  function paint() {
    var local = time - starts[current];
    segs.forEach(function (fill, k) { fill.style.setProperty("--p", clamp((time - starts[k]) / lengths[k]).toFixed(3)); });
    counters[current].forEach(function (c) {
      var p = calm.matches ? 1 : clamp((local - c.from) / c.span);
      var text = format(c.value * (1 - Math.pow(1 - p, 3)), c.kind);
      if (text !== c.shown) { c.el.textContent = text; c.shown = text; }
    });
  }
  function frame(now) {
    if (state !== "playing") return;
    time += Math.min(now - last, 100);
    last = now;
    if (time >= total) { time = total; paint(); setState("ended"); return; }
    var index = 0;
    while (index < scenes.length - 1 && time >= starts[index + 1]) index++;
    show(index, false);
    paint();
    frameId = requestAnimationFrame(frame);
  }
  function play() {
    if (state === "playing") return;
    if (state === "idle" || state === "ended") { time = 0; show(0, true); }
    setState("playing");
    last = performance.now();
    frameId = requestAnimationFrame(frame);
  }
  function pause() {
    if (state !== "playing") return;
    cancelAnimationFrame(frameId);
    setState("paused");
  }
  function seek(index) {
    cancelAnimationFrame(frameId);
    time = starts[index];
    state = "paused";
    show(index, true);
    paint();
    play();
  }
  function flip() { if (state === "playing") pause(); else play(); }

  stage.addEventListener("click", function () {
    var fromStart = document.activeElement === start;
    flip();
    if (fromStart && state === "playing") toggle.focus();      /* el botón grande se esconde al empezar: el foco pasa a la pausa */
  });
  toggle.addEventListener("click", flip);
  document.addEventListener("visibilitychange", function () { if (document.hidden) pause(); });
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) { if (!entries[0].isIntersecting) pause(); }, { threshold: 0.15 }).observe(stage);
  }
  setState("idle");
  paint();
})();
