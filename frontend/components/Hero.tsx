'use client';

import React from 'react';
import { Zap } from 'lucide-react';

export default function Hero() {
  return (
    <div className="text-center space-y-4 pt-4 max-w-3xl mx-auto">
      <div className="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-indigo-500/10 via-purple-500/10 to-pink-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-bold uppercase tracking-widest shadow-inner">
        <Zap className="w-3.5 h-3.5 text-amber-400" />
        <span>Scikit-Learn NLP Pipeline • TF-IDF + 6 Classification Models</span>
      </div>
      <h1 className="text-4xl md:text-6xl font-black tracking-tight leading-tight">
        Detect Fake News with{' '}
        <span className="bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
          AI Intelligence
        </span>
      </h1>
      <p className="text-slate-400 text-base md:text-lg">
        Paste any news article headline or text to evaluate credibility, extract feature importance keywords, and compare algorithm predictions in real-time.
      </p>
    </div>
  );
}
