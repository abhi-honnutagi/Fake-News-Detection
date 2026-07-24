'use client';

import React from 'react';
import { PredictionResponse } from '../lib/api';
import { ShieldAlert, ShieldCheck, Tag, Gauge, Sparkles, Key } from 'lucide-react';

interface PredictionCardProps {
  result: PredictionResponse | null;
  loading: boolean;
}

export default function PredictionCard({ result, loading }: PredictionCardProps) {
  if (loading) {
    return (
      <div className="backdrop-blur-2xl bg-slate-900/60 rounded-3xl p-8 border border-slate-800 flex flex-col items-center justify-center space-y-4 min-h-[420px] shadow-2xl">
        <div className="relative w-16 h-16">
          <div className="absolute inset-0 rounded-full border-4 border-indigo-500/20 border-t-indigo-500 animate-spin"></div>
          <div className="absolute inset-2 rounded-full border-4 border-pink-500/20 border-b-pink-500 animate-spin" style={{ animationDirection: 'reverse', animationDuration: '0.8s' }}></div>
        </div>
        <p className="text-sm font-bold text-indigo-400">Transforming text into TF-IDF vector space & calculating probabilities...</p>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="backdrop-blur-2xl bg-slate-900/60 rounded-3xl p-8 border border-slate-800 flex flex-col items-center justify-center space-y-4 min-h-[420px] text-center shadow-2xl">
        <div className="w-20 h-20 rounded-3xl bg-slate-950 border border-slate-800 flex items-center justify-center text-slate-600 text-3xl">
          <ShieldCheck className="w-10 h-10 text-slate-600" />
        </div>
        <div className="space-y-1">
          <h4 className="text-base font-bold text-slate-300">Ready for Analysis</h4>
          <p className="text-xs text-slate-500 max-w-xs mx-auto">Enter article text and trigger the classification engine to extract features and compute prediction confidence.</p>
        </div>
      </div>
    );
  }

  const isFake = result.is_fake;
  const realP = (result.probabilities.REAL * 100).toFixed(1);
  const fakeP = (result.probabilities.FAKE * 100).toFixed(1);

  return (
    <div className={`backdrop-blur-2xl rounded-3xl p-6 md:p-8 border ${isFake ? 'border-rose-500/40 bg-rose-950/20 shadow-rose-500/10' : 'border-emerald-500/40 bg-emerald-950/20 shadow-emerald-500/10'} space-y-6 shadow-2xl relative overflow-hidden transition-all duration-500`}>
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <span className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
          <Gauge className="w-4 h-4 text-indigo-400" /> AI Verdict Analysis
        </span>
        <span className="text-xs font-bold px-3 py-1 rounded-full bg-slate-900 text-indigo-400 border border-slate-700">
          {result.model_used} Engine
        </span>
      </div>

      <div className="text-center space-y-3">
        <div className={`inline-flex items-center gap-2 text-xl font-black px-6 py-2.5 rounded-2xl uppercase tracking-wider ${isFake ? 'bg-rose-500/20 text-rose-400 border border-rose-500/40 shadow-lg shadow-rose-500/20' : 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 shadow-lg shadow-emerald-500/20'}`}>
          {isFake ? <ShieldAlert className="w-6 h-6" /> : <ShieldCheck className="w-6 h-6" />}
          {isFake ? 'FAKE NEWS DETECTED' : 'VERIFIED REAL NEWS'}
        </div>
        <div className="text-xs font-bold text-slate-400">
          Confidence: <span className="text-indigo-400 text-sm font-extrabold">{(result.confidence * 100).toFixed(1)}%</span>
        </div>
      </div>

      <div className="space-y-2.5 bg-slate-950/60 p-4 rounded-2xl border border-slate-800">
        <div className="flex justify-between text-xs font-extrabold">
          <span className="text-emerald-400">REAL: {realP}%</span>
          <span className="text-rose-400">FAKE: {fakeP}%</span>
        </div>
        <div className="w-full h-3.5 bg-slate-900 rounded-full overflow-hidden flex p-0.5 border border-slate-800">
          <div className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-700" style={{ width: `${realP}%` }}></div>
          <div className="bg-gradient-to-r from-rose-500 to-pink-500 h-full rounded-full transition-all duration-700" style={{ width: `${fakeP}%` }}></div>
        </div>
      </div>

      <div className="space-y-2.5">
        <span className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
          <Key className="w-3.5 h-3.5 text-indigo-400" /> Predictive Feature Indicators
        </span>
        <div className="flex flex-wrap gap-1.5 max-h-36 overflow-y-auto pr-1">
          {result.key_indicators.map((item, idx) => (
            <span key={idx} className="text-xs font-semibold px-2.5 py-1 rounded-xl bg-slate-900 text-slate-300 border border-slate-700/80 flex items-center gap-1">
              <span>{item.word}</span>
              <span className="text-[10px] text-indigo-400 font-mono">{item.weight}</span>
            </span>
          ))}
        </div>
      </div>

      <div className="text-[11px] text-slate-500 text-center pt-3 border-t border-slate-800/80">
        Processed at {result.timestamp}
      </div>
    </div>
  );
}
