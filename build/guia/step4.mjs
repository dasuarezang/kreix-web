import { connect } from "./cdp.mjs";
const c = await connect();
const click = (txt) => c.ev(`[...document.querySelectorAll('button,a')].find(b=>b.innerText.trim()==${JSON.stringify(txt)}).click()`);
await click("Probar con datos de ejemplo");
await c.sleep(6000);
const pages = { inicio: "Inicio", cuentas: "Cuentas", inversiones: "Inversiones", datos: "Datos", ajustes: "Ajustes" };
for (const [id, label] of Object.entries(pages)) {
  await c.ev(`document.querySelector('.tabbar button[data-page="${id}"]').click()`);
  await c.sleep(2500);
  const h = await c.ev("document.documentElement.scrollHeight");
  console.log(id, "alto", h);
  for (const [i, y] of [[0, 0], [1, 800], [2, 1600], [3, 2400]]) {
    if (y > h - 400) break;
    await c.ev(`window.scrollTo(0,${y})`); await c.sleep(900);
    await c.shot(`img/mv-${id}-${i}.png`);
  }
}
c.close();
