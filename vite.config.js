import { defineConfig } from 'vite';

// Plain Vite. No framework. The app is vanilla ES modules + hand-rolled SVG.
// `npm run dev` serves index.html; `npm run build` emits a static bundle you can
// open offline. Nothing here talks to a backend or an external API.
export default defineConfig({
  root: '.',
  base: './',
  server: { open: true, port: 5173 },
  build: { outDir: 'dist', target: 'es2020' },
});
