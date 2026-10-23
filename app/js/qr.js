// Recibir los datos del ordenador por QR animado (ver core/qr_transfer.py, que es quien los emite en el escritorio).
// La camara lee fotogramas con jsQR; cada uno lleva un bloque o la suma XOR de varios, y el decodificador "pela" los que
// faltan. El reparto de bloques y el generador aleatorio son los mismos que en Python, bit a bit.
import { h, t } from "./core.js";
import { Decoder } from "./fountain.js";

// ----------------------------------------------------------------------------- camara
let jsQRLoaded = null;

function loadJsQR() {
  jsQRLoaded ||= new Promise((resolve, reject) => {
    const script = h("script", { src: "vendor/jsQR.js" });
    script.onload = () => resolve(window.jsQR);
    script.onerror = reject;
    document.head.append(script);
  });
  return jsQRLoaded;
}

/** Pantalla de escaneo. Resuelve con los bytes recibidos, o null si se cancela. */
export function scanTransfer(texts) {
  return new Promise(async (resolve) => {
    const video = h("video", { playsinline: true, muted: true, autoplay: true });
    const bar = h("i");
    const status = h("p.scan-status", texts.aim);
    const overlay = h("div.scanner", { role: "dialog", "aria-modal": "true", "aria-label": texts.title },
      h("div.scan-view", video, h("div.scan-frame")),
      h("div.scan-panel",
        h("h2", texts.title), status, h("div.progress.wide", bar),
        h("button.btn.block", { onclick: () => finish(null) }, t("Cancelar"))));
    document.body.append(overlay);

    let stream = null, running = true;
    function finish(value) {
      running = false;
      stream?.getTracks().forEach((track) => track.stop());
      overlay.remove();
      resolve(value);
    }

    let jsQR;
    try {
      jsQR = await loadJsQR();
      stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment", width: { ideal: 1280 }, height: { ideal: 720 } }, audio: false });
    } catch (e) {
      status.textContent = texts.no_camera;
      return;
    }
    video.srcObject = stream;
    await video.play().catch(() => {});

    const decoder = new Decoder();
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d", { willReadFrequently: true });
    function tick() {
      if (!running) return;
      if (video.readyState >= 2 && video.videoWidth) {
        // se lee el centro de la imagen a una resolucion moderada: mas rapido y suficiente para un QR que llena el visor
        const side = Math.min(video.videoWidth, video.videoHeight);
        const size = Math.min(720, side);
        canvas.width = canvas.height = size;
        ctx.drawImage(video, (video.videoWidth - side) / 2, (video.videoHeight - side) / 2, side, side, 0, 0, size, size);
        const code = jsQR(ctx.getImageData(0, 0, size, size).data, size, size, { inversionAttempts: "dontInvert" });
        if (code && code.binaryData && decoder.add(new Uint8Array(code.binaryData))) {
          bar.style.width = `${Math.round(decoder.progress * 100)}%`;
          status.textContent = texts.reading.replace("{pct}", Math.round(decoder.progress * 100));
          if (decoder.done) {
            navigator.vibrate?.(60);
            return finish(decoder.result());
          }
        }
      }
      requestAnimationFrame(tick);
    }
    tick();
  });
}
