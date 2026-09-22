// Markdown is authoritative; only the reading view is generated here.
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

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
for (const [source, target, title] of [
  ['README.md', 'index.html', 'Editorial Avatar'],
  ['VALIDATION.md', 'validation.html', 'Editorial Avatar · 验证记录'],
]) {
  const body = marked.parse(readFileSync(resolve(root, source), 'utf8'))
    .replaceAll('<table>', '<div class="table-scroll" role="region" aria-label="对照表，可横向滚动" tabindex="0"><table>')
    .replaceAll('</table>', '</table></div>');
  const html = `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title><style>${css}</style></head><body><main>${body}</main></body></html>\n`;
  if (process.argv.includes('--check')) {
    if (readFileSync(resolve(root, target), 'utf8') !== html) throw new Error(`${target} is stale`);
  } else writeFileSync(resolve(root, target), html);
  console.log(`${target}: ${process.argv.includes('--check') ? 'synchronized' : 'built'}`);
}
