# SaaS de Beats — progreso

Landing page para vender **tus propios beats** (Next.js 14 + Tailwind + TypeScript).
Carpeta: `web/` (la herramienta de video en la raíz queda intacta).

## Decisiones tomadas
- Modelo: **tu propia tienda** (vendes tus beats, no marketplace).
- Primer entregable: **landing page** con catálogo + licencias + captación.
- Stack: **Next.js 14 (App Router) + Tailwind + TypeScript**.

## Hecho ✅
- Configuración del proyecto: `package.json`, `next.config.mjs`, `tsconfig.json`,
  `postcss.config.mjs`, `tailwind.config.ts`.
- Estilos globales y tema oscuro con brillo: `app/globals.css`.
- Layout raíz + fuentes (Inter + Space Grotesk): `app/layout.tsx`.
- Datos editables de la tienda (marca, beats, licencias, pasos): `lib/site.ts`.

## Pendiente para mañana ⏳
1. Reproductor de beats (Web Audio: previsualización sintetizada al BPM/tono real,
   y usa tu MP3 en cuanto lo pongas en `/public/beats/`). Un solo beat suena a la vez,
   barra de reproducción fija abajo.
2. Componentes: `Navbar`, `Hero`, `Beats` (grid + filtros), `Licensing`, `Steps`,
   `Waitlist`, `Footer`.
3. `app/page.tsx` ensamblando todo.
4. `npm install` + `npm run build` para verificar que compila.
5. (Opcional) desplegar en Vercel.

## Cómo retomar
```bash
cd web
npm install
npm run dev   # http://localhost:3000
```
Personaliza tu marca, beats y precios en `web/lib/site.ts`.
