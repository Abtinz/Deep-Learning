import { Snowflake, ToyBrick, Play, CalendarRange, Sparkles, Orbit } from 'lucide-react';
import { EffectType } from '../types';

interface ControlPanelProps {
  activeEffect: EffectType;
  timeRemaining: number;
  onTrigger: (type: 'snowflakes' | 'balloons') => void;
  activeCount: number;
}

export default function ControlPanel({ 
  activeEffect, 
  timeRemaining, 
  onTrigger, 
  activeCount 
}: ControlPanelProps) {
  const isSnowing = activeEffect === 'snowflakes';
  const isBallooning = activeEffect === 'balloons';
  const isAnyActive = activeEffect !== null;

  return (
    <div 
      id="control-panel-container"
      className="w-full max-w-lg bg-slate-900 text-slate-100 rounded-2xl border border-slate-800 shadow-2xl p-8 relative overflow-hidden backdrop-blur-xl"
      style={{
        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05)'
      }}
    >
      {/* Decorative subtle ambient light overlay inside the card */}
      <div className="absolute -top-24 -left-24 w-48 h-48 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -bottom-24 -right-24 w-48 h-48 bg-rose-500/10 rounded-full blur-3xl pointer-events-none" />

      {/* Header section */}
      <div className="border-b border-slate-800 pb-6 mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Orbit className="w-5 h-5 text-cyan-400 animate-spin-slow" />
          <span className="text-[10px] uppercase tracking-[0.25em] font-semibold text-cyan-400/80">
            System Control Deck
          </span>
        </div>
        <h1 className="text-2xl font-semibold tracking-tight text-white mb-1.5 font-sans">
          Atmospheric Simulator
        </h1>
        <p className="text-xs text-slate-400 font-sans leading-relaxed">
          Trigger precision vertical vector particle streams. Highly calibrated, responsive climate and balloon physics simulations.
        </p>
      </div>

      {/* Primary Action Buttons */}
      <div className="grid grid-cols-2 gap-4 mb-8">
        {/* Snowflakes trigger */}
        <button
          id="btn-trigger-snowflakes"
          onClick={() => onTrigger('snowflakes')}
          disabled={isAnyActive}
          className={`group relative flex flex-col items-center justify-center p-6 rounded-xl border transition-all duration-300 ${
            isSnowing 
              ? 'bg-cyan-950/40 border-cyan-500/50 text-cyan-200 shadow-[0_0_15px_rgba(34,211,238,0.15)]' 
              : 'bg-slate-950/60 border-slate-800 hover:border-slate-700 text-slate-300 hover:text-white hover:bg-slate-950/90'
          } disabled:opacity-50 disabled:cursor-not-allowed`}
        >
          <div className="p-3 bg-cyan-950/80 group-hover:bg-cyan-900/60 rounded-lg mb-3 border border-cyan-500/20 transition-all">
            <Snowflake 
              className={`w-6 h-6 text-cyan-400 ${isSnowing ? 'animate-spin' : 'group-hover:rotate-45 duration-500 transition-transform'}`} 
            />
          </div>
          <span className="font-medium text-sm tracking-wide">Snowflakes</span>
          <span className="text-[10px] text-slate-500 mt-1 uppercase tracking-wider">Downward Fall</span>
        </button>

        {/* Balloons trigger */}
        <button
          id="btn-trigger-balloons"
          onClick={() => onTrigger('balloons')}
          disabled={isAnyActive}
          className={`group relative flex flex-col items-center justify-center p-6 rounded-xl border transition-all duration-300 ${
            isBallooning 
              ? 'bg-rose-950/40 border-rose-500/50 text-rose-200 shadow-[0_0_15px_rgba(244,63,94,0.15)]' 
              : 'bg-slate-950/60 border-slate-800 hover:border-slate-700 text-slate-300 hover:text-white hover:bg-slate-950/90'
          } disabled:opacity-50 disabled:cursor-not-allowed`}
        >
          <div className="p-3 bg-rose-950/80 group-hover:bg-rose-900/60 rounded-lg mb-3 border border-rose-500/20 transition-all">
            {/* Elegant representation of balloon using simple shape and a string path */}
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" className={`w-6 h-6 text-rose-400 ${isBallooning ? 'animate-bounce' : 'group-hover:-translate-y-0.5 transition-transform'}`}>
              <path d="M12 2a5 6 0 0 0-5 6c0 3 2.5 5 5 5s5-2 5-5a5 6 0 0 0-5-6Z" />
              <path d="M12 13v6" />
            </svg>
          </div>
          <span className="font-medium text-sm tracking-wide">Balloons</span>
          <span className="text-[10px] text-slate-500 mt-1 uppercase tracking-wider">Upward Float</span>
        </button>
      </div>

      {/* Physics Monitors Panel */}
      <div className="bg-slate-950/80 rounded-xl border border-slate-800/80 p-5 font-mono">
        <div className="flex items-center justify-between border-b border-slate-800/60 pb-3 mb-3">
          <span className="text-[10px] font-semibold text-slate-500 uppercase tracking-widest">
            Telemetry Monitor
          </span>
          <div className="flex items-center gap-1.5">
            <span className={`w-1.5 h-1.5 rounded-full ${isAnyActive ? 'bg-emerald-500 animate-pulse' : 'bg-slate-600'}`} />
            <span className="text-[10px] text-slate-400 uppercase tracking-wider">
              {isAnyActive ? 'Active Stream' : 'Ready'}
            </span>
          </div>
        </div>

        {/* Real-time metrics list */}
        <div className="space-y-2.5 text-xs">
          {/* Status Metric */}
          <div className="flex justify-between items-center text-slate-400">
            <span>Simulation State</span>
            <span className={`font-semibold ${isAnyActive ? 'text-white' : 'text-slate-500'}`}>
              {isSnowing ? 'PRECI-SNOW' : isBallooning ? 'HELI-FLOAT' : 'STANDBY'}
            </span>
          </div>

          {/* Time Remaining */}
          <div className="flex justify-between items-center text-slate-400">
            <span>Cycle Time Remaining</span>
            <div className="flex items-center gap-1.5">
              <span className={`font-semibold ${isAnyActive ? 'text-amber-400' : 'text-slate-500'}`}>
                {timeRemaining.toFixed(1)}s
              </span>
              <div className="w-16 h-1.5 bg-slate-800 rounded-full overflow-hidden">
                <div 
                  className={`h-full transition-all duration-100 ease-linear ${isSnowing ? 'bg-cyan-500' : 'bg-rose-500'}`}
                  style={{ width: `${(timeRemaining / 5) * 100}%` }}
                />
              </div>
            </div>
          </div>

          {/* Active Particles */}
          <div className="flex justify-between items-center text-slate-400">
            <span>Active Particle Count</span>
            <span className="text-white font-semibold">
              {activeCount} <span className="text-slate-600 text-[10px]">elements</span>
            </span>
          </div>

          {/* Static environmental coefficients for formal styling */}
          <div className="border-t border-slate-800/40 my-2 pt-2.5 grid grid-cols-2 gap-y-1.5 text-[10px] text-slate-500">
            <div className="flex justify-between pr-3 border-r border-slate-800/60">
              <span>GRAVITY</span>
              <span className="text-slate-400">{isSnowing ? '9.81 m/s²' : isBallooning ? '-3.20 m/s²' : '0.00 m/s²'}</span>
            </div>
            <div className="flex justify-between pl-3 font-mono">
              <span>DRAG COEFF</span>
              <span className="text-slate-400">{isAnyActive ? '0.24 Cd' : '0.00 Cd'}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
