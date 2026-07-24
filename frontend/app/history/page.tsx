'use client';

import React, { useEffect, useState } from 'react';
import { getPredictionHistory } from '../../lib/api';
import Loader from '../../components/Loader';
import { History, Download } from 'lucide-react';

export default function HistoryPage() {
  const [history, setHistory] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getPredictionHistory()
      .then((data) => setHistory(data.history || []))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Loader text="Loading history..." />;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-black bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent flex items-center gap-2">
            <History className="w-7 h-7 text-indigo-400" /> Prediction Audit Log
          </h1>
          <p className="text-sm text-slate-400">History of article classifications in current session</p>
        </div>
      </div>

      <div className="rounded-3xl border border-slate-800 bg-slate-900/60 overflow-hidden shadow-2xl">
        <table className="w-full text-left text-sm text-slate-300">
          <thead class="text-xs uppercase bg-slate-950 text-slate-400 border-b border-slate-800">
            <tr>
              <th className="py-4 px-6">Timestamp</th>
              <th className="py-4 px-6">Article Text</th>
              <th className="py-4 px-6">Model</th>
              <th className="py-4 px-6">Verdict</th>
              <th className="py-4 px-6">Confidence</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {history.length === 0 ? (
              <tr>
                <td colSpan={5} className="py-8 text-center text-slate-500">
                  No prediction history found.
                </td>
              </tr>
            ) : (
              history.map((item, idx) => (
                <tr key={idx} className="hover:bg-slate-900/80 transition-colors">
                  <td className="py-4 px-6 text-xs text-slate-400">{item.timestamp}</td>
                  <td className="py-4 px-6 font-medium max-w-sm truncate text-slate-200">{item.text}</td>
                  <td className="py-4 px-6 text-xs text-slate-400">{item.model_used}</td>
                  <td className="py-4 px-6">
                    <span className={`px-2.5 py-1 rounded-full text-xs font-bold ${item.label === 'FAKE' ? 'bg-rose-500/20 text-rose-400 border border-rose-500/30' : 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'}`}>
                      {item.label}
                    </span>
                  </td>
                  <td className="py-4 px-6 text-xs font-bold text-slate-300">{(item.confidence * 100).toFixed(1)}%</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
