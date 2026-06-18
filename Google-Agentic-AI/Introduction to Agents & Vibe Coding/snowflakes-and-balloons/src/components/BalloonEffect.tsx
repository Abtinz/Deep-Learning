import React from 'react';
import { BalloonItem } from '../types';

interface BalloonEffectProps {
  balloons: BalloonItem[];
}

export default function BalloonEffect({ balloons }: BalloonEffectProps) {
  return (
    <div id="balloon-overlay" className="fixed inset-0 pointer-events-none overflow-hidden z-50">
      {balloons.map((balloon) => (
        <div
          key={balloon.id}
          style={{
            position: 'absolute',
            left: `${balloon.x}%`,
            bottom: '-150px',
            transform: `scale(${balloon.scale})`,
            animation: `cssRise ${balloon.duration}s ease-out forwards`,
            width: '40px',
            height: '110px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <div
            style={{
              '--sway-x': `${balloon.sway}px`,
              animation: `cssSwayBalloon ${balloon.duration * 0.4}s ease-in-out infinite alternate`,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            } as React.CSSProperties}
          >
            {/* Balloon Body with specular highlight */}
            <div 
              id={`balloon-body-${balloon.id}`}
              className={`w-10 h-13 rounded-full relative shadow-lg bg-gradient-to-t ${balloon.color} flex flex-col justify-end items-center`}
              style={{
                borderRadius: '50% 50% 50% 50% / 40% 40% 60% 60%',
                boxShadow: 'inset -3px -5px 12px rgba(0,0,0,0.3), 0 4px 10px rgba(0,0,0,0.15)'
              }}
            >
              {/* Specular highlight reflection */}
              <div className="absolute top-1.5 left-2.5 w-2 h-4 bg-white/40 rounded-full rotate-[15deg]"></div>

              {/* Knot */}
              <div 
                className="w-2.5 h-2 bg-inherit mb-[-1px] relative" 
                style={{ 
                  clipPath: 'polygon(20% 0%, 80% 0%, 100% 100%, 0% 100%)' 
                }}
              />
            </div>

            {/* String hanging down */}
            <div 
              id={`balloon-string-${balloon.id}`}
              className="w-0.5 h-16 bg-gradient-to-b from-gray-400/40 via-gray-400/20 to-transparent self-center" 
            />
          </div>
        </div>
      ))}
    </div>
  );
}

