import { connect } from "./cdp.mjs";
const c = await connect();
console.log(await c.ev("JSON.stringify(Object.fromEntries(Object.entries(localStorage)))"), await c.ev("JSON.stringify(Object.entries(sessionStorage))"));
c.close();
