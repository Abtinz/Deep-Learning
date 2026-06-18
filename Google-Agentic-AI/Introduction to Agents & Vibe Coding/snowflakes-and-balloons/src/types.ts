export type EffectType = 'snowflakes' | 'balloons' | null;

export interface SnowflakeItem {
  id: string;
  x: number; // horizontal start position (0 - 100 %)
  scale: number; // size scaling factor
  duration: number; // animation fall time in seconds
  sway: number; // sway scale in pixels
  createdAt: number; // timestamp in milliseconds
}

export interface BalloonItem {
  id: string;
  x: number; // horizontal start position (0 - 100 %)
  scale: number; // size scaling factor
  color: string; // Tailwind bg color class or hex code
  duration: number; // animation rise time in seconds
  sway: number; // sway scale in pixels
  createdAt: number; // timestamp in milliseconds
}
