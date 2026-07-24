'use client';

import React, { useEffect, useState } from 'react';
import { getModelsSummary, AnalyticsResponse } from '../../lib/api';
import Chart from '../../components/Chart';
import Loader from '../../components/Loader';
import { Crown, Cpu, Layers } from 'lucide-react';

export default function DashboardPage() {
  const [data, setData] = useState<AnalyticsResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getModelsSummary()
      .then((res) => setData(res))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Loader text="Fetching model metrics..." />;
  if (!data) return <div className="text-center py-12 text-slate-500">Failed to load analytics data.</div>;

  const chartData = Object.keys(data.models).map((key) => ({
    name: key,
    accuracy: Number((data.models[key].accuracy * 100).toFixed(1)),
    f1: Number((data.models[key].f1_score * 100).toFixed(1)),
  }));

  return (
    <div className="space-y-8">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-black bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
            ML Benchmark Dashboard
          </h1>
          <p className="text-sm text-slate-400">Comparing 6 text classification algorithms</p>
        </div>
        <div className="flex items-center space-x-3 text-xs">
          <span className="px-3 py-1.5 rounded-xl bg-blue-500/10 text-blue-400 font-semibold border border-blue-500/20 flex items-center gap-1">
            <Cpu className="w-3.5 h-3.5" /> Best Model: {data.best_model}
          </span>
          <span className="px-3 py-1.5 rounded-xl bg-purple-500/10 text-purple-400 font-semibold border border-purple-500/20 flex items-center gap-1">
            <Layers className="w-3.5 h-3.5" /> Samples: {data.total_samples}
          </span>
        </div>
      </div>

      <div className="rounded-3xl p-6 border border-slate-800 bg-slate-900/60 shadow-2xl">
        <h2 className="text-lg font-bold text-slate-200 mb-4">Accuracy & F1-Score Comparison</h2>
        <Chart data={chartData} />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Object.keys(data.models).map((modelName) => {
          const m = data.models[modelName];
          const isBest = modelName === data.best_model;

          return (
            <div
              key={modelName}
              className={`rounded-2xl p-6 border ${isBest ? 'border-indigo-500/50 bg-indigo-950/20' : 'border-slate-800 bg-slate-900/40'} space-y-4 relative`}
            >
              {isBest && (
                <div className="absolute top-4 right-4 flex items-center gap-1 text-xs font-bold px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">
                  <Crown className="w-3.5 h-3.5" /> BEST
                </div>
              )}
              <h3 className="text-lg font-bold text-slate-100">{modelName}</h3>
              <div className="grid grid-cols-2 gap-4 text-xs">
                <div>
                  <span className="text-slate-500">Accuracy</span>
                  <div className="text-base font-bold text-blue-400">{(m.accuracy * 100).toFixed(1)}%</div>
                </div>
                <div>
                  <span className="text-slate-500">F1 Score</span>
                  <div className="text-base font-bold text-purple-400">{(m.f1_score * 100).toFixed(1)}%</div>
                </div>
                <div>
                  <span className="text-slate-500">Precision</span>
                  <div className="text-base font-semibold text-slate-200">{(m.precision * 100).toFixed(1)}%</div>
                </div>
                <div>
                  <span className="text-slate-500">Recall</span>
                  <div className="text-base font-semibold text-slate-200">{(m.recall * 100).toFixed(1)}%</div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
