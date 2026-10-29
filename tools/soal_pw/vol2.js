// node vol.js <obec> <rok> <signatura> <pref> n1 n2 ...  – najde svazek hledáním, ověří signaturu, vypíše cesty snímků
const { open } = require('./lib'); const fs = require('fs');
const [place, year, sign, pref, ...nums] = process.argv.slice(2);
(async () => {
  fs.rmSync('state.json', { force: true });
  const s = await open(); const p = s.p;
  await p.goto('https://digi.soalitomerice.cz/digitalnibadatelna/', { timeout: 60000 }); await p.waitForTimeout(18000);
  await p.click('#geoAccessPointText'); await p.type('#geoAccessPointText', place, { delay: 100 });
  await p.fill('#timeRangeFrom', year); await p.fill('#timeRangeTo', year); if (process.env.PAT) await p.fill('#patternTxt', process.env.PAT);
  await p.locator('button[type=submit]').first().click(); await p.waitForTimeout(7000);
  const href = await p.evaluate((sign) => {
    for (const a of document.querySelectorAll('a[href*="vysledekDetail"]')) {
      if (!a.href.includes('scanLink')) continue;
      let el = a; for (let i=0;i<8 && el.parentElement && !el.innerText.includes('digi. sada');i++) el = el.parentElement;
      if (el.innerText.includes(sign)) return a.href;
    }
  }, sign);
  if (!href) { console.error('svazek nenalezen'); await s.close(); return; }
  await p.goto(href, { timeout: 60000 }); await p.waitForTimeout(6000);
  const info = await p.evaluate(() => document.body.innerText.match(/sign\.\s*\S+/g));
  console.error('detail:', [...new Set(info||[])].join(' '));
  const opts = await p.evaluate(() => [...document.querySelector('select').options].map(o => o.value));
  const ent = decodeURIComponent(href.split('vysledekDetail/')[1].split('?')[0]);
  fs.writeFileSync(`opts_${pref}.json`, JSON.stringify(opts)); fs.writeFileSync(`ent_${pref}.txt`, ent);
  console.error('snimku:', opts.length, 'entita', ent);
  for (const n of nums) {
    const uuid = opts[+n - 1].split('%20')[1];
    const r = await p.goto(`https://digi.soalitomerice.cz/digitalnibadatelna/showZoomify/${ent}/${uuid}`, { timeout: 60000 });
    const m = (await r.text()).match(/https?:\/\/images\.soalitomerice\.cz\/[^"' ]+?\.jpg/i);
    console.log(n + '\t' + (m ? m[0] : 'NENALEZENO') + '\t' + uuid);
    await p.waitForTimeout(3500);
  }
  await s.close();
})();
