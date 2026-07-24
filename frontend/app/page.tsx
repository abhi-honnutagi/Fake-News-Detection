'use client';

import React, { useState } from 'react';
import Hero from '../components/Hero';
import PredictionCard from '../components/PredictionCard';
import { classifyNews, PredictionResponse } from '../lib/api';
import { Wand2, RefreshCw, Trash2, FileText } from 'lucide-react';

export default function HomePage() {
  const [input, setInput] = useState('');
  const [selectedModel, setSelectedModel] = useState('RandomForest');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResponse | null>(null);

  const handleAnalyze = async () => {
    if (!input.trim() || input.length < 10) {
      alert('Please enter at least 10 characters.');
      return;
    }
    setLoading(true);
    try {
      const res = await classifyNews(input);
      setResult(res);
    } catch (err) {
      alert('Error communicating with ML backend API.');
    } finally {
      setLoading(false);
    }
  };

  const loadPreset = (key: string) => {
    const samples: Record<string, string> = {
      alien: "BREAKING: Secret Underground Bunker Discovered Containing Alien Quantum Supercomputers! Government Hiding Truth From Citizens!",
      lemon: "SHOCKING: Drinking Lemon Juice Mixed With Miracle Powder Cures All Incurable Diseases Overnight, Doctors Don't Want You To Know!",
      fed: "WASHINGTON — The Federal Reserve announced a quarter-point interest rate adjustment following its policy meeting, citing inflation trends and employment data.",
      who: "GENEVA — The World Health Organization released updated global health guidelines recommending balanced diets and regular physical activity to reduce cardiovascular risks."
    };
    setInput(samples[key] || '');
  };

  const words = input.trim() ? input.trim().split(/\s+/).length : 0;

  return (
    <div className="space-y-10">
      <Hero />

      {/* Preset Input Pills */}
      <div className="flex flex-wrap items-center justify-center gap-2 max-w-4xl mx-auto">
        <span className="text-xs font-bold text-slate-400 uppercase tracking-wider mr-2">Try Sample Inputs:</span>
        <button onClick={() => loadPreset('alien')} className="text-xs px-3.5 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800 hover:border-indigo-500/50 hover:bg-slate-800 text-slate-300 transition-all">
          🛸 Alien Bunker (Fake)
        </button>
        <button onClick={() => loadPreset('lemon')} className="text-xs px-3.5 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800 hover:border-indigo-500/50 hover:bg-slate-800 text-slate-300 transition-all">
          🍋 Miracle Cure (Fake)
        </button>
        <button onClick={() => loadPreset('fed')} className="text-xs px-3.5 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800 hover:border-indigo-500/50 hover:bg-slate-800 text-slate-300 transition-all">
          🏛️ Federal Reserve (Real)
        </button>
        <button onClick={() => loadPreset('who')} className="text-xs px-3.5 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800 hover:border-indigo-500/50 hover:bg-slate-800 text-slate-300 transition-all">
          🏥 WHO Health Guidelines (Real)
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Input Card */}
        <div className="lg:col-span-7 backdrop-blur-2xl bg-slate-900/60 rounded-3xl p-6 md:p-8 border border-slate-800 flex flex-col justify-between space-y-6 shadow-2xl">
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-bold text-slate-100 flex items-center gap-2">
                <FileText className="w-5 h-5 text-indigo-400" /> News Article Input
              </h2>
              <button onClick={() => setInput('')} className="text-xs text-slate-400 hover:text-slate-200 transition-colors flex items-center gap-1">
                <Trash2 className="w-3.5 h-3.5" /> Clear
              </button>
            </div>

            <textarea
              rows={8}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Paste news headline or full text here to classify..."
              className="w-full bg-slate-950/80 text-slate-100 placeholder-slate-500 rounded-2xl p-4 border border-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm leading-relaxed"
            />

            {/* Metrics counter bar */}
            <div className="grid grid-cols-4 gap-2 text-center text-xs">
              <div className="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800">
                <div className="text-[10px] font-bold text-slate-500 uppercase">Chars</div>
                <div className="font-extrabold text-slate-200">{input.length}</div>
              </div>
              <div className="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800">
                <div className="text-[10px] font-bold text-slate-500 uppercase">Words</div>
                <div className="font-extrabold text-slate-200">{words}</div>
              </div>
              <div className="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800">
                <div className="text-[10px] font-bold text-slate-500 uppercase">Read Time</div>
                <div className="font-extrabold text-slate-200">{Math.ceil(words / 3.5)}s</div>
              </div>
              <div className="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800">
                <div className="text-[10px] font-bold text-slate-500 uppercase">Tokens</div>
                <div className="font-extrabold text-slate-200">{words > 0 ? Math.ceil(words * 1.3) : 0}</div>
              </div>
            </div>
          </div>

          <div className="space-y-4 pt-4 border-t border-slate-800">
            <div className="flex items-center justify-between text-xs">
              <label className="font-semibold text-slate-300">Select Classifier Engine:</label>
              <select
                value={selectedModel}
                onChange={(e) => setSelectedModel(e.target.value)}
                className="bg-slate-950 text-indigo-300 border border-slate-800 font-semibold px-3 py-1.5 rounded-xl text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500"
              >
                <option value="KNN">K-Nearest Neighbors (KNN)</option>
                <option value="LogisticRegression">Logistic Regression</option>
                <option value="RandomForest">Random Forest Ensemble</option>
                <option value="NeuralNetwork">Neural Network (MLP)</option>
                <option value="NaiveBayes">Multinomial Naive Bayes</option>
                <option value="SVM">Support Vector Machine (SVM)</option>
              </select>
            </div>

            <button
              onClick={handleAnalyze}
              disabled={loading}
              className="w-full py-4 rounded-2xl bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 text-white font-extrabold text-base shadow-xl shadow-indigo-600/30 hover:scale-[1.01] active:scale-98 transition-all flex items-center justify-center gap-2.5"
            >
              {loading ? <RefreshCw className="w-5 h-5 animate-spin" /> : <Wand2 className="w-5 h-5" />}
              Classify Article Credibility
            </button>
          </div>
        </div>

        <div className="lg:col-span-5">
          <PredictionCard result={result} loading={loading} />
        </div>
      </div>
    </div>
  );
}
