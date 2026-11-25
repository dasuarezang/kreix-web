import { connect } from "./cdp.mjs";
const c = await connect();
console.log("antes", await c.ev("document.documentElement.getAttribute('data-theme')"));
await c.ev(`document.head.insertAdjacentHTML('beforeend','<style>::-webkit-scrollbar{display:none}html{scrollbar-width:none}</style>')`);
if ((await c.ev("document.documentElement.getAttribute('data-theme')")) !== "light") {
  await c.ev(`document.querySelector('header button:last-child, .topbar button:last-child')?.click()`);
  await c.sleep(600);
}
console.log("despues", await c.ev("document.documentElement.getAttribute('data-theme')"));
const pages = ["inicio", "cuentas", "inversiones", "datos", "ajustes"];
for (const id of pages) {
  await c.ev(`document.querySelector('.tabbar button[data-page="${id}"]').click()`);
  await c.sleep(2500);
  const h = await c.ev("document.documentElement.scrollHeight");
  for (const [i, y] of [[0, 0], [1, 800], [2, 1600], [3, 2400]]) {
    if (y > h - 400) break;
    await c.ev(`window.scrollTo(0,${y})`); await c.sleep(900);
    await c.shot(`img/mv-${id}-${i}.png`);
  }
}
c.close();
