import { connect } from "./cdp.mjs";
const c = await connect();
if ((await c.ev("document.documentElement.getAttribute('data-theme')")) !== "light") {
  await c.ev(`document.querySelector('header button:last-child, .topbar button:last-child')?.click()`); await c.sleep(700);
}
await c.ev(`window.scrollTo(0,0)`); await c.sleep(600);
await c.shot("img/mv-vacio.png");
console.log(await c.ev("document.documentElement.getAttribute('data-theme')"));
c.close();
