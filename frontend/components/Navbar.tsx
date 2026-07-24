'use client';

import React from 'react';
import Link from 'next/link';
import { ShieldCheck, Cpu, ChartBar, Layers, Clock, FileWord } from 'lucide-react';

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 bg-slate-950/90 backdrop-blur-md border-b border-slate-800/80 text-xs">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center space-x-3 cursor-pointer">
          <div className="w-9 h-9 rounded-lg bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center shadow-md shadow-blue-500/20">
            <ShieldCheck className="w-5 h-5 text-white" />
          </div>
          <div>
            <span className="text-base font-bold text-white tracking-tight flex items-center gap-2">
              ShieldNet <span class="text-[10px] font-semibold px-2 py-0.5 rounded bg-slate-900 text-slate-300 border border-slate-800">Enterprise AI</span>
            </span>
          </div>
        </Link>

        <nav className="hidden lg:flex items-center space-x-8 text-slate-400 font-medium h-full">
          <Link href="/" className="hover:text-white flex items-center gap-2 text-slate-200 font-semibold border-b-2 border-blue-500 h-full">
            <Cpu className="w-4 h-4 text-blue-400" /> Real-Time Classifier
          </Link>
          <Link href="/dashboard" className="hover:text-white flex items-center gap-2 h-full">
            <ChartBar className="w-4 h-4 text-purple-400" /> Model Benchmarks
          </Link>
          <Link href="/history" className="hover:text-white flex items-center gap-2 h-full">
            <Clock className="w-4 h-4 text-amber-400" /> Audit Logs
          </Link>
        </nav>

        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2 px-3 py-1.5 rounded-md bg-slate-900 border border-slate-800">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="text-slate-400">API: <strong className="text-slate-200 font-semibold">Online</strong></span>
          </div>
        </div>
      </div>
    </header>
  );
}
