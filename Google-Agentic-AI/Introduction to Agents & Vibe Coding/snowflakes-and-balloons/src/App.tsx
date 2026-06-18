import { useState, useEffect } from 'react';
import { EffectType, SnowflakeItem, BalloonItem } from './types';
import ControlPanel from './components/ControlPanel';
import SnowflakeEffect from './components/SnowflakeEffect';
import BalloonEffect from './components/BalloonEffect';

const BALLOON_COLOR_PRESETS = [
  'from-rose-600 via-rose-700 to-rose-950',      // Monarch Burgundy/Crimson
  'from-amber-400 via-amber-500 to-amber-700',   // Heavy Gold
  'from-blue-600 via-blue-700 to-indigo-950',    // Sapphire Navy
  'from-emerald-600 via-emerald-700 to-teal-950', // Imperial Jade
  'from-purple-600 via-purple-700 to-indigo-950', // Royal Amethyst
  'from-cyan-500 via-cyan-600 to-blue-900',      // Steel Teal / Slate Blue
];

export default function App() {
  const [activeEffect, setActiveEffect] = useState<EffectType>(null);
  const [timeRemaining, setTimeRemaining] = useState<number>(0);
  const [snowflakes, setSnowflakes] = useState<SnowflakeItem[]>([]);
  const [balloons, setBalloons] = useState<BalloonItem[]>([]);

  // 1. Spawning & Countdown Loop
  useEffect(() => {
    if (activeEffect === null) return;

    // Immediately trigger an initial burst of particles for responsive, zero-delay feedback
    if (activeEffect === 'snowflakes') {
      const initialBurst: SnowflakeItem[] = Array.from({ length: 15 }).map((_, i) => ({
        id: `snow-init-${i}-${Math.random()}`,
        x: Math.random() * 100,
        scale: 0.75 + Math.random() * 0.45,
        duration: 5.0 + Math.random() * 3.0, // slower fall time: 5.0s to 8.0s
        sway: 15 + Math.random() * 25,
        createdAt: Date.now() - (Math.random() * 1500) // stagger starting positions slightly downwards
      }));
      setSnowflakes(initialBurst);
    } else if (activeEffect === 'balloons') {
      const initialBurst: BalloonItem[] = Array.from({ length: 8 }).map((_, i) => ({
        id: `balloon-init-${i}-${Math.random()}`,
        x: 10 + Math.random() * 80,
        scale: 0.75 + Math.random() * 0.4,
        color: BALLOON_COLOR_PRESETS[Math.floor(Math.random() * BALLOON_COLOR_PRESETS.length)],
        duration: 6.5 + Math.random() * 3.5, // slower rise time: 6.5s to 10.0s
        sway: 10 + Math.random() * 20,
        createdAt: Date.now() - (Math.random() * 1500) // stagger rises slightly upwards
      }));
      setBalloons(initialBurst);
    }

    const intervalMs = 120; // tick spacing rate for spawning (approx. 8 elements per second)
    const timer = setInterval(() => {
      setTimeRemaining((prevTime) => {
        const nextTime = Math.max(0, prevTime - (intervalMs / 1000));
        
        if (nextTime <= 0) {
          // 5 seconds completed: Stop simulation spawning
          setActiveEffect(null);
          return 0;
        }

        // Spawn a new particle on this calibration interval tick
        if (activeEffect === 'snowflakes') {
          const newFlake: SnowflakeItem = {
            id: `snow-${Date.now()}-${Math.random()}`,
            x: Math.random() * 100,
            scale: 0.75 + Math.random() * 0.45,
            duration: 5.0 + Math.random() * 3.0,
            sway: 15 + Math.random() * 25,
            createdAt: Date.now()
          };
          setSnowflakes((prev) => [...prev, newFlake]);
        } else if (activeEffect === 'balloons') {
          const newBalloon: BalloonItem = {
            id: `balloon-${Date.now()}-${Math.random()}`,
            x: 8 + Math.random() * 84,
            scale: 0.75 + Math.random() * 0.4,
            color: BALLOON_COLOR_PRESETS[Math.floor(Math.random() * BALLOON_COLOR_PRESETS.length)],
            duration: 6.5 + Math.random() * 3.5,
            sway: 12 + Math.random() * 20,
            createdAt: Date.now()
          };
          setBalloons((prev) => [...prev, newBalloon]);
        }

        return nextTime;
      });
    }, intervalMs);

    return () => clearInterval(timer);
  }, [activeEffect]);

  // 2. Automated React Garbage Collector Loop
  // Prunes particles whose life spans have expired so we don't hog DOM memory
  useEffect(() => {
    const garbageCollector = setInterval(() => {
      const now = Date.now();

      setSnowflakes((prev) => 
        prev.filter((flake) => now - flake.createdAt < flake.duration * 1000)
      );

      setBalloons((prev) => 
        prev.filter((balloon) => now - balloon.createdAt < balloon.duration * 1000)
      );
    }, 250);

    return () => clearInterval(garbageCollector);
  }, []);

  const handleTrigger = (effectType: 'snowflakes' | 'balloons') => {
    if (activeEffect !== null) return; // Prevent double trigger
    
    // Clear other particle system completely prior to initialization
    if (effectType === 'snowflakes') {
      setBalloons([]);
    } else {
      setSnowflakes([]);
    }

    setActiveEffect(effectType);
    setTimeRemaining(5.0);
  };

  const activeCount = activeEffect === 'snowflakes' 
    ? snowflakes.length 
    : activeEffect === 'balloons' 
      ? balloons.length 
      : 0;

  return (
    <div 
      id="main-app" 
      className="min-h-screen w-screen relative flex items-center justify-center p-6 bg-[#030712] overflow-hidden select-none"
      style={{
        backgroundImage: 'radial-gradient(circle, rgba(31,41,55,0.4) 1px, transparent 1px)',
        backgroundSize: '24px 24px'
      }}
    >
      {/* 5-second dynamic overlay simulators */}
      <SnowflakeEffect snowflakes={snowflakes} />
      <BalloonEffect balloons={balloons} />

      {/* Central control system */}
      <ControlPanel 
        activeEffect={activeEffect}
        timeRemaining={timeRemaining}
        onTrigger={handleTrigger}
        activeCount={activeCount}
      />
    </div>
  );
}
