import React from 'react';
import { Snowflake } from 'lucide-react';
import { SnowflakeItem } from '../types';

interface SnowflakeEffectProps {
  snowflakes: SnowflakeItem[];
}

export default function SnowflakeEffect({ snowflakes }: SnowflakeEffectProps) {
  return (
    <div id="snowflake-overlay" className="fixed inset-0 pointer-events-none overflow-hidden z-50">
      {snowflakes.map((snowflake) => (
        <div
          key={snowflake.id}
          style={{
            position: 'absolute',
            left: `${snowflake.x}%`,
            top: '-50px',
            transform: `scale(${snowflake.scale})`,
            animation: `cssFall ${snowflake.duration}s linear forwards`,
            width: '24px',
            height: '24px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <div
            style={{
              '--sway-x': `${snowflake.sway}px`,
              animation: `cssSwaySnow ${snowflake.duration * 0.5}s ease-in-out infinite alternate`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            } as React.CSSProperties}
          >
            <Snowflake 
              id={`snowflake-icon-${snowflake.id}`}
              className="text-cyan-100/95 drop-shadow-[0_2px_8px_rgba(186,230,253,0.5)]" 
              size={24}
            />
          </div>
        </div>
      ))}
    </div>
  );
}

