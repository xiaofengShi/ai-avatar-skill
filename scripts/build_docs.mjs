// Markdown is authoritative; only the reading view is generated here.
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked, Marked } from 'marked';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const css = `*{box-sizing:border-box}body{margin:0;background:#f7f8f5;color:#25312e;font:16px/1.75 system-ui,sans-serif}
main{max-width:1040px;margin:auto;padding:clamp(16px,4vw,48px);overflow-wrap:anywhere}
h1{font-size:clamp(30px,5vw,48px);line-height:1.15}h2{margin-top:36px;padding-top:18px;border-top:1px solid #cbd4cb;font-size:24px}
h3{font-size:19px}a{color:#1b6261;text-underline-offset:3px}a:focus-visible{outline:3px solid #246d70;outline-offset:3px}
img{max-width:100%;height:auto;display:block;margin:12px auto;border-radius:8px}.table-scroll{overflow-x:auto}.table-scroll:focus-visible{outline:3px solid #246d70}table{border-collapse:collapse;width:100%;min-width:760px;table-layout:fixed}
td,th{padding:8px;text-align:left;border-bottom:1px solid #cbd4cb;vertical-align:top}td img{width:220px;max-width:100%;height:auto}
pre{overflow:auto;padding:18px;background:#e8eee9;border-radius:8px;font-size:14px;line-height:1.6}code{font-family:ui-monospace,monospace}li{margin:8px 0}
blockquote{margin:16px 0;padding:8px 20px;border-left:3px solid #558875;background:#edf1eb}
@media(max-width:480px){td,th{padding:4px;font-size:14px}}
@media print{body{background:white}main{padding:0}h2,h3{break-after:avoid}.table-scroll{overflow:visible}table{min-width:0;font-size:12px}tr{break-inside:avoid}img{max-height:85mm;width:auto}pre{white-space:pre-wrap;overflow-wrap:anywhere}}
`;
for (const [source, target, title, lang] of [
  ['SHOWCASE.md', 'showcase.html', 'Editorial Avatar · 案例展厅', 'zh-CN'],
  ['SHOWCASE.en.md', 'showcase.en.html', 'Editorial Avatar · Portrait cases', 'en'],
  ['VALIDATION.md', 'validation.html', 'Editorial Avatar · 验证记录', 'zh-CN'],
  ['VALIDATION.en.md', 'validation.en.html', 'Editorial Avatar · Validation record', 'en'],
]) {
  const english = lang === 'en';
  const markdown = readFileSync(resolve(root, source), 'utf8');
  let body = marked.parse(markdown)
    .replaceAll('<table>', `<div class="table-scroll" role="region" aria-label="${english ? 'Comparison table, scroll horizontally' : '对照表，可横向滚动'}" tabindex="0"><table>`)
    .replaceAll('</table>', '</table></div>');
  let html = `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title><style>${css}</style></head><body><main>${body}</main></body></html>\n`;
  if (source.startsWith('SHOWCASE')) {
    const gallery = new Marked({ renderer: {
      table(token) {
        if (token.header.length !== 4) throw new Error('Showcase requires four comparison columns');
        return '<div class="gallery">' + token.rows.map((row, index) => {
          const cells = row.map(cell => marked.parseInline(cell.text));
          const [title, ...brief] = cells[0].split('<br>');
          const figures = [1, 2].map((column) => `<figure>${cells[column].replaceAll('<img ', '<img loading="lazy" decoding="async" ')}<figcaption>${column === 1 ? (english ? 'Source photo / edit base' : '输入照片 / 编辑基底') : (english ? 'Generated result' : '生成结果')}</figcaption></figure>`).join('');
          return `<article class="case"><header><span class="case-number">${String(index + 1).padStart(2, '0')}</span><div><h3>${title}</h3><div class="brief">${brief.join('<br>')}</div></div></header><div class="pair">${figures}</div><div class="observation">${cells[3]}</div></article>`;
        }).join('') + '</div>';
      },
      heading(token) {
        const ids = {'案例对照':'examples','小尺寸，也值得认真看':'preview','从这里开始':'start','Case comparisons':'examples','Small sizes matter':'preview','Get started':'start'};
        const id = ids[token.text];
        return `<h${token.depth}${id ? ` id="${id}"` : ''}>${marked.parseInline(token.text)}</h${token.depth}>`;
      }
    }});
    body = gallery.parse(markdown);
    const introEnd = body.indexOf('<h2');
    let intro = body.slice(0, introEnd).replace(english ? '<p>Editorial Avatar / Case gallery</p>' : '<p>Editorial Avatar / 案例展厅</p>', match => match.replace('<p>', '<p class="eyebrow">'));
    intro = intro.replace(/(<h1>.*?<\/h1>)(<p class="eyebrow">.*?<\/p>)/s, '$2$1').replace(english ? '<p>The same photo' : '<p>同一张照片', match => match.replace('<p>', '<p class="intro">'));
    body = `<section class="hero">${intro}<div class="actions"><a class="primary" href="#examples">${english ? 'Browse cases ↓' : '浏览案例 ↓'}</a><a href="https://github.com/xiaofengShi/ai-avatar-skill/blob/main/${english ? 'README.md' : 'README.zh-CN.md'}">${english ? 'How to use ↗' : '开始使用 ↗'}</a></div></section>` + body.slice(introEnd);
    body = body.replace(english ? '<p>Examples made from' : '<p>示例完成于', match => `<details><summary>${english ? 'Process and known limits' : '试验过程与已知限制'}</summary>${match}`).replace('<h2 id="preview">', '</details><h2 id="preview">');
    html = readFileSync(resolve(root, english ? 'scripts/showcase.en.html' : 'scripts/showcase.html'), 'utf8').replace('{{content}}', body);
  }
  if (process.argv.includes('--check')) {
    if (readFileSync(resolve(root, target), 'utf8') !== html) throw new Error(`${target} is stale`);
  } else writeFileSync(resolve(root, target), html);
  console.log(`${target}: ${process.argv.includes('--check') ? 'synchronized' : 'built'}`);
}
