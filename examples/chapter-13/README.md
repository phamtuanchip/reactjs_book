# Chương 13 — Styling trong React

## Tailwind CSS (khuyến nghị)

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Trong `tailwind.config.js`:
```js
content: ["./src/**/*.{js,jsx,ts,tsx}"]
```

Ví dụ component với Tailwind:
```jsx
function Button({ variant = 'primary', children, onClick }) {
  const base = 'px-4 py-2 rounded font-semibold transition-colors';
  const variants = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600',
    danger: 'bg-red-500 text-white hover:bg-red-600',
    outline: 'border-2 border-blue-500 text-blue-500 hover:bg-blue-50',
  };
  return (
    <button className={`${base} ${variants[variant]}`} onClick={onClick}>
      {children}
    </button>
  );
}
```
