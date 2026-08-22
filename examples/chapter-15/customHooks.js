// Custom Hooks — Tái sử dụng logic
import { useState, useEffect, useCallback, useRef } from 'react';

// useFetch — fetch data với loading/error
export function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetch(url)
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(d => { if (!cancelled) { setData(d); setLoading(false); }})
      .catch(e => { if (!cancelled) { setError(e.message); setLoading(false); }});
    return () => { cancelled = true; };
  }, [url]);

  return { data, loading, error };
}

// useLocalStorage — persist state
export function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try { return JSON.parse(localStorage.getItem(key)) ?? initialValue; }
    catch { return initialValue; }
  });

  const setStoredValue = useCallback((newValue) => {
    const val = typeof newValue === 'function' ? newValue(value) : newValue;
    setValue(val);
    localStorage.setItem(key, JSON.stringify(val));
  }, [key, value]);

  return [value, setStoredValue];
}

// useDebounce — delay value update
export function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);
  return debounced;
}

// useWindowSize — theo dõi kích thước window
export function useWindowSize() {
  const [size, setSize] = useState({ width: window.innerWidth, height: window.innerHeight });
  useEffect(() => {
    const handler = () => setSize({ width: window.innerWidth, height: window.innerHeight });
    window.addEventListener('resize', handler);
    return () => window.removeEventListener('resize', handler);
  }, []);
  return size;
}
