// ES Modules — Named exports
export const PI = 3.14159;

export function add(a, b) { return a + b; }
export function multiply(a, b) { return a * b; }
export function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}
