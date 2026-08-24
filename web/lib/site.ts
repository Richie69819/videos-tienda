// ─────────────────────────────────────────────────────────────
//  CONFIGURACIÓN DE TU TIENDA
//  Edita este archivo para personalizar tu marca, beats y precios.
// ─────────────────────────────────────────────────────────────

export const site = {
  brand: "PROD. NOVA",
  tagline: "Beats que suenan a hit antes de que escribas la primera línea.",
  subtitle:
    "Compra licencias al instante, descarga en segundos y publica sin trabas. Trap, drill, reggaetón y R&B producidos en estudio.",
  email: "contacto@prodnova.com",
  socials: {
    instagram: "https://instagram.com",
    youtube: "https://youtube.com",
    tiktok: "https://tiktok.com",
    spotify: "https://spotify.com",
  },
  stats: [
    { value: "1.2M+", label: "Streams con mis beats" },
    { value: "480+", label: "Beats vendidos" },
    { value: "24 h", label: "Entrega de exclusivas" },
  ],
};

export type Beat = {
  id: string;
  title: string;
  bpm: number;
  key: string;
  mood: string[];
  price: number;
  cover: string; // gradiente tailwind para la portada
  audioUrl?: string; // pon aquí el mp3 en /public/beats/tu-beat.mp3
  tag?: "Nuevo" | "Top" | "Exclusivo";
};

export const beats: Beat[] = [
  {
    id: "midnight",
    title: "Midnight Run",
    bpm: 140,
    key: "F# min",
    mood: ["Trap", "Dark"],
    price: 29,
    cover: "from-violet-600 via-fuchsia-600 to-indigo-700",
    tag: "Top",
  },
  {
    id: "veneno",
    title: "Veneno",
    bpm: 96,
    key: "A min",
    mood: ["Reggaetón", "Melódico"],
    price: 34,
    cover: "from-rose-500 via-pink-600 to-purple-700",
    tag: "Nuevo",
  },
  {
    id: "opps",
    title: "Opps",
    bpm: 145,
    key: "G min",
    mood: ["Drill", "Aggressive"],
    price: 29,
    cover: "from-cyan-500 via-blue-600 to-indigo-700",
  },
  {
    id: "seda",
    title: "Seda",
    bpm: 88,
    key: "D# min",
    mood: ["R&B", "Smooth"],
    price: 39,
    cover: "from-amber-400 via-orange-500 to-rose-600",
    tag: "Exclusivo",
  },
  {
    id: "neon",
    title: "Neón",
    bpm: 128,
    key: "C min",
    mood: ["Afrobeat", "Vibe"],
    price: 32,
    cover: "from-lime-400 via-emerald-500 to-teal-600",
  },
  {
    id: "humo",
    title: "Humo",
    bpm: 132,
    key: "E min",
    mood: ["Trap", "Melódico"],
    price: 29,
    cover: "from-slate-500 via-violet-600 to-fuchsia-700",
  },
];

export type License = {
  name: string;
  price: number;
  formats: string;
  streams: string;
  featured?: boolean;
  perks: string[];
};

export const licenses: License[] = [
  {
    name: "MP3 Lease",
    price: 29,
    formats: "MP3 con tag",
    streams: "50k streams",
    perks: [
      "Uso en 1 canción",
      "Distribución digital",
      "Videoclip en YouTube",
      "Entrega inmediata",
    ],
  },
  {
    name: "WAV Lease",
    price: 49,
    formats: "MP3 + WAV",
    streams: "150k streams",
    featured: true,
    perks: [
      "Calidad de estudio (WAV)",
      "Distribución en todas las plataformas",
      "Presentaciones en vivo",
      "Monetización en YouTube",
    ],
  },
  {
    name: "Trackout",
    price: 99,
    formats: "MP3 + WAV + Stems",
    streams: "500k streams",
    perks: [
      "Pistas separadas (stems)",
      "Mezcla y máster propios",
      "Radio y sync",
      "Uso comercial ampliado",
    ],
  },
  {
    name: "Exclusiva",
    price: 399,
    formats: "Todo + derechos",
    streams: "Ilimitado",
    perks: [
      "El beat se retira de venta",
      "Sin límite de streams",
      "Propiedad total de la instrumental",
      "Contrato de exclusividad",
    ],
  },
];

export const steps = [
  {
    title: "Explora y escucha",
    body: "Filtra por género, BPM o mood y previsualiza cada beat con el reproductor.",
  },
  {
    title: "Elige tu licencia",
    body: "Desde MP3 hasta exclusiva. Compara usos, streams y formatos en segundos.",
  },
  {
    title: "Paga y descarga",
    body: "Pago seguro con tarjeta. El archivo y el contrato llegan a tu correo al instante.",
  },
  {
    title: "Publícalo",
    body: "Sube tu canción a Spotify, YouTube o donde quieras. El crédito lo pones tú.",
  },
];
