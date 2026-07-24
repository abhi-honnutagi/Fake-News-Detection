'use client';

import React from 'react';

export default function Footer() {
  return (
    <footer className="border-t border-slate-800/80 bg-slate-950/80 py-6 text-xs text-slate-500">
      <div className="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>ShieldNet AI Misinformation Detection Platform</div>
        <div>FastAPI • Next.js 15 • Scikit-Learn Pipeline</div>
      </div>
    </footer>
  );
}
