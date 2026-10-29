// node pth.js <pref> n1 n2 ... – cesty snímků pro svazek, jehož opts/ent jsou uložené (vol.js)
const { open } = require('./lib'); const fs = require('fs');
const [pref, ...nums] = process.argv.slice(2);
(async () => {
  const opts = JSON.parse(fs.readFileSync(`opts_${pref}.json`)); const ent = fs.readFileSync(`ent_${pref}.txt`, 'utf8');
  const s = await open(); const p = s.p;
  for (const n of nums) {
    const uuid = opts[+n - 1].split('%20')[1];
    await p.goto(`https://digi.soalitomerice.cz/digitalnibadatelna/showZoomifySeparate?imageNumberSeparate=${n}&myEntityUuid=${encodeURIComponent(ent)}&myImageUuid=${uuid}`, { timeout: 60000 });
    await p.waitForTimeout(1500);
    const m = (await p.content()).match(/https?:\/\/images\.soalitomerice\.cz\/[^"' ]+?\.jpg/i);
    console.log(n + '\t' + (m ? m[0] : 'NENALEZENO') + '\t' + uuid);
    await p.waitForTimeout(3500);
  }
  await s.close();
})();
