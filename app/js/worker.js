// Worker de Kreix: aqui corre Pyodide con la logica del escritorio, lejos del hilo de la interfaz (derivar la clave de la
// contrasena maestra tarda unos segundos en un movil y la pantalla no debe congelarse).
//
// Protocolo: la interfaz manda {id, fn, args} y recibe {id, ok} o {id, error}. `fn` es una funcion de pwa/py/kreix_web.py,
// salvo las de este archivo (boot). El archivo cifrado .krx vive en /data dentro de Pyodide; cada vez que Python guarda,
// se copia tal cual (cifrado) a IndexedDB, que es lo que sobrevive al cerrar la app.

const DB_NAME = "kreix";
const STORE = "files";
const VAULT_FILES = ["kreix.krx", "kreix.krx.bak"];

let py = null;
let bridge = null;

function idb() {
  return new Promise((resolve, reject) => {
    const open = indexedDB.open(DB_NAME, 1);
    open.onupgradeneeded = () => open.result.createObjectStore(STORE);
    open.onsuccess = () => resolve(open.result);
    open.onerror = () => reject(open.error);
  });
}

async function idbDo(mode, work) {
  const db = await idb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORE, mode);
    const result = work(tx.objectStore(STORE));
    tx.oncomplete = () => { db.close(); resolve(result && result.result); };
    tx.onerror = () => { db.close(); reject(tx.error); };
  });
}

// IndexedDB -> /data (al arrancar)
async function restoreFiles() {
  py.FS.mkdirTree("/data");
  for (const name of VAULT_FILES) {
    const data = await idbDo("readonly", (s) => s.get(name));
    if (data) py.FS.writeFile(`/data/${name}`, new Uint8Array(data));
  }
}

// /data -> IndexedDB (tras cada guardado). Se escribe todo en una sola transaccion: o se guarda entero o nada.
async function persistFiles() {
  const present = VAULT_FILES.filter((n) => py.FS.analyzePath(`/data/${n}`).exists);
  const blobs = present.map((n) => [n, py.FS.readFile(`/data/${n}`)]);
  await idbDo("readwrite", (s) => {
    for (const name of VAULT_FILES) {
      const found = blobs.find(([n]) => n === name);
      if (found) s.put(found[1].buffer.slice(0), name); else s.delete(name);
    }
  });
}

function progress(step, total, text) {
  postMessage({ progress: { step, total, text } });
}

async function boot({ language }) {
  const config = await (await fetch("../config.json")).json();
  progress(1, 4, "python");
  const base = new URL("../" + config.pyodide, self.location.href).href;      // Pyodide va junto a la app (pyodide/)
  importScripts(base + "pyodide.js");
  py = await loadPyodide({ indexURL: base });
  progress(2, 4, "packages");
  await py.loadPackage(["sqlalchemy", "cryptography", "xlrd", "sqlite3"]);
  for (const wheel of config.wheels) {
    const data = new Uint8Array(await (await fetch("../" + wheel)).arrayBuffer());
    py.unpackArchive(data, "wheel", { extractDir: "/lib/python3.13/site-packages" });
  }
  progress(3, 4, "kreix");
  const code = new Uint8Array(await (await fetch("../kreix.zip")).arrayBuffer());
  py.unpackArchive(code, "zip", { extractDir: "/kreix" });
  py.runPython("import sys; sys.path.insert(0, '/kreix')");
  await restoreFiles();
  bridge = py.pyimport("kreix_web");
  progress(4, 4, "ready");
  return call("boot", { language });
}

function call(fn, args) {
  const reply = JSON.parse(bridge.call(fn, JSON.stringify(args || {})));
  if (reply.error) {
    const error = new Error(reply.error);
    error.trace = reply.trace;
    throw error;
  }
  return reply;
}

let saving = Promise.resolve();

async function save() {
  // Una cola: dos guardados seguidos nunca se pisan.
  saving = saving.then(async () => {
    if (bridge.flush()) await persistFiles();
  });
  return saving;
}

onmessage = async (event) => {
  const { id, fn, args } = event.data;
  try {
    let result;
    if (fn === "boot") {
      result = (await boot(args)).ok;
    } else if (fn === "put_files") {
      // archivos elegidos en el movil (o recibidos por QR) -> /tmp/in, donde Python los lee
      py.FS.mkdirTree("/tmp/in");
      result = args.files.map(({ name, bytes }) => {
        const safe = name.replace(/[/\\]/g, "_");
        py.FS.writeFile(`/tmp/in/${safe}`, new Uint8Array(bytes));
        return `/tmp/in/${safe}`;
      });
    } else if (fn === "flush") {
      await save();
      result = true;
    } else {
      const reply = call(fn, args);
      result = reply.ok;
      if (result && result.__file__) {                       // un archivo para el movil (exportaciones): se manda en bytes
        result.bytes = py.FS.readFile(result.__file__);
        py.FS.unlink(result.__file__);
      }
      // crear ya escribe el .krx (y borrar lo quita): se copia tal cual; el resto guarda solo si cambio algo
      if (fn === "reset" || fn === "create") await persistFiles();
      else if (reply.dirty) await save();
    }
    postMessage({ id, ok: result });
  } catch (error) {
    postMessage({ id, error: String(error.message || error), trace: error.trace || error.stack });
  }
};
