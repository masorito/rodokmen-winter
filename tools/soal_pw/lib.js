const { chromium } = require('playwright');
const fs = require('fs');
async function open() {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const opts = { ignoreHTTPSErrors: true, locale: 'cs-CZ' };
  if (fs.existsSync('state.json')) opts.storageState = 'state.json';
  const ctx = await b.newContext(opts);
  const p = await ctx.newPage();
  return { b, ctx, p, async close() { await ctx.storageState({ path: 'state.json' }); await b.close(); } };
}
module.exports = { open };
