const { open } = require('./lib');
const [place, from, to, pat] = process.argv.slice(2);
(async () => {
  require('fs').rmSync('state.json',{force:true}); const s = await open(); const p = s.p; await p.goto('https://digi.soalitomerice.cz/digitalnibadatelna/', { timeout: 60000 }); await p.waitForTimeout(18000);
  await p.goto('https://digi.soalitomerice.cz/digitalnibadatelna/', { timeout: 60000 });
  await p.waitForTimeout(1500);
  await p.click('#geoAccessPointText'); await p.type('#geoAccessPointText', place, { delay: 120 });
  await p.waitForTimeout(3000);
  const opts = await p.evaluate(() => [...document.querySelectorAll('.ui-menu-item, .ui-autocomplete li')].filter(e=>e.offsetParent).map(e=>e.innerText.trim()));
  console.log('opts:', opts.slice(0,10));
  if (opts.length) await p.locator('.ui-menu-item').filter({ hasText: place }).first().click();
  if (from) { await p.fill('#timeRangeFrom', from); await p.fill('#timeRangeTo', to); }
  if (pat) await p.fill('#patternTxt', pat);
  await p.waitForTimeout(500);
  await p.locator('button[type=submit]').first().click();
  await p.waitForTimeout(7000);
  const items = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('a[href*="vysledekDetail"]').forEach(a => {
      if (a.href.includes('scanLink')) return;
      let el = a; for (let i=0;i<6 && el.parentElement && el.innerText.length<120;i++) el = el.parentElement;
      out.push(el.innerText.replace(/\s+/g,' ').trim().slice(0,400) + ' || ' + a.href.split('?')[0].split('/').pop());
    });
    return [...new Set(out)];
  });
  console.log((await p.evaluate(()=>document.body.innerText.match(/Nalezeno[^\n]*/)||[]))[0]);
  console.log(items.join('\n'));
  await s.close();
})();
