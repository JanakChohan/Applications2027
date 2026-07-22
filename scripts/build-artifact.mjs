// Inline the built Vite bundle into ONE self-contained HTML fragment suitable
// for a hosted Artifact (no external asset requests, which the Artifact CSP
// blocks). Run after `vite build`. Output: a fragment with <style> + the app
// root + an inline module <script>, no <!doctype>/<html>/<head>/<body> wrapper
// (the Artifact host provides those).
import { readFileSync, writeFileSync } from 'node:fs';

const dist = 'dist';
const out = process.argv[2] || 'dist/standalone.html';

let html = readFileSync(`${dist}/index.html`, 'utf8');

// inline stylesheet(s)
html = html.replace(/<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"[^>]*>/g, (_m, href) => {
  const css = readFileSync(`${dist}/${href.replace(/^\.?\//, '')}`, 'utf8');
  return `<style>${css}</style>`;
});
// inline the module script (escape any </script> in string literals)
html = html.replace(/<script[^>]*type="module"[^>]*src="([^"]+)"[^>]*><\/script>/g, (_m, src) => {
  const js = readFileSync(`${dist}/${src.replace(/^\.?\//, '')}`, 'utf8').replace(/<\/script/g, '<\\/script');
  return `<script type="module">${js}</script>`;
});
// drop preload hints that would point at now-removed files
html = html.replace(/<link[^>]*rel="modulepreload"[^>]*>/g, '');

// The Artifact host supplies <!doctype>/<html>/<head>/<body> and the favicon, so
// strip those wrappers and the favicon link, then keep everything else (inlined
// <style>, the deferred module <script>, and the #app root) in source order.
const fragment = html
  .replace(/<!doctype[^>]*>/gi, '')
  .replace(/<\/?html[^>]*>/gi, '')
  .replace(/<\/?head[^>]*>/gi, '')
  .replace(/<\/?body[^>]*>/gi, '')
  .replace(/<meta[^>]*>/gi, '')
  .replace(/<title>[\s\S]*?<\/title>/gi, '')
  .replace(/<link[^>]*rel="icon"[^>]*>/gi, '')
  .replace(/\n{3,}/g, '\n\n')
  .trim();

writeFileSync(out, `${fragment}\n`);
console.log(`wrote ${out} (${(readFileSync(out, 'utf8').length / 1024).toFixed(0)} KB)`);
