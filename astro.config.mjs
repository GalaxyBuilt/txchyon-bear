// @ts-check
import { defineConfig } from 'astro/config';

import react from '@astrojs/react';

import tailwindcss from '@tailwindcss/vite';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://txchyon.com',
  base: '/bear',
  integrations: [
    react(),
    sitemap()
  ],
  server: {
    port: 4325
  },
  vite: {
    plugins: [tailwindcss()],
  },
});