"""Create code example files for all 25 chapters."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/examples'

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Created: {os.path.relpath(path, BASE)}')

# ======== CHAPTER 01 ========
write(f'{BASE}/chapter-01/index.html', '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Chương 1 — Trang web đầu tiên</title>
</head>
<body>
  <h1>Xin chào, World!</h1>
  <p>Đây là trang web đầu tiên của tôi.</p>
  <p>Hãy mở DevTools (F12) và xem tab Network để thấy các request!</p>
  <a href="https://google.com">Đi đến Google</a>
</body>
</html>
''')

# ======== CHAPTER 02 ========
write(f'{BASE}/chapter-02/index.html', '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chương 2 — HTML Semantic</title>
</head>
<body>

  <header>
    <nav>
      <a href="#">Trang chủ</a>
      <a href="#">Về chúng tôi</a>
      <a href="#">Liên hệ</a>
    </nav>
  </header>

  <main>
    <article>
      <h1>Bài viết đầu tiên</h1>
      <p>Đây là nội dung bài viết với <strong>chữ đậm</strong> và <em>chữ nghiêng</em>.</p>

      <h2>Danh sách không thứ tự</h2>
      <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
      </ul>

      <h2>Form đăng ký</h2>
      <form>
        <label for="name">Họ tên:</label>
        <input type="text" id="name" name="name" placeholder="Nhập tên...">

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="email@example.com">

        <button type="submit">Đăng ký</button>
      </form>
    </article>

    <aside>
      <h3>Bài viết liên quan</h3>
      <ul>
        <li><a href="#">Học HTML cơ bản</a></li>
        <li><a href="#">CSS cho người mới</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2025 Lập Trình ReactJS. All rights reserved.</p>
  </footer>

</body>
</html>
''')

# ======== CHAPTER 03 ========
write(f'{BASE}/chapter-03/index.html', '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Chương 3 — CSS Examples</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <h1>CSS Box Model, Flexbox, Grid</h1>

    <!-- Box Model -->
    <div class="box-demo">Box Model Demo</div>

    <!-- Flexbox -->
    <div class="flex-container">
      <div class="flex-item">Item 1</div>
      <div class="flex-item">Item 2</div>
      <div class="flex-item">Item 3</div>
    </div>

    <!-- Grid -->
    <div class="grid-container">
      <div class="grid-item">1</div>
      <div class="grid-item">2</div>
      <div class="grid-item">3</div>
      <div class="grid-item">4</div>
      <div class="grid-item">5</div>
      <div class="grid-item">6</div>
    </div>
  </div>
</body>
</html>
''')

write(f'{BASE}/chapter-03/styles.css', ''':root {
  --primary: #61dafb;
  --bg: #1e2127;
  --card: #282c34;
  --text: #abb2bf;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: sans-serif; background: var(--bg); color: var(--text); padding: 24px; }
.container { max-width: 800px; margin: 0 auto; }
h1 { color: var(--primary); margin-bottom: 24px; }

/* Box Model */
.box-demo {
  margin: 24px 0;
  padding: 24px;
  border: 3px solid var(--primary);
  background: var(--card);
  width: 300px;
}

/* Flexbox */
.flex-container {
  display: flex;
  gap: 16px;
  justify-content: center;
  align-items: center;
  margin: 24px 0;
  padding: 16px;
  background: var(--card);
  border-radius: 8px;
}
.flex-item {
  background: var(--primary);
  color: #1e2127;
  padding: 16px 24px;
  border-radius: 4px;
  font-weight: bold;
}

/* Grid */
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin: 24px 0;
}
.grid-item {
  background: #3e4451;
  padding: 24px;
  text-align: center;
  border-radius: 4px;
  font-size: 1.5rem;
}
''')

# ======== CHAPTER 04 ========
write(f'{BASE}/chapter-04/script.js', '''// Chương 4: JavaScript Nhập môn

// 1. Biến
let name = 'Nguyễn An';
const age = 25;
let isStudent = true;

console.log(`Tên: ${name}, Tuổi: ${age}`);

// 2. Kiểu dữ liệu
console.log(typeof 'hello');   // string
console.log(typeof 42);        // number
console.log(typeof true);      // boolean
console.log(typeof null);      // object (JavaScript quirk!)
console.log(typeof undefined); // undefined
console.log(typeof {});        // object
console.log(typeof []);        // object

// 3. Điều kiện
const score = 85;
if (score >= 90) {
  console.log('Xuất sắc');
} else if (score >= 80) {
  console.log('Giỏi');
} else if (score >= 70) {
  console.log('Khá');
} else {
  console.log('Trung bình');
}

// 4. Vòng lặp
const fruits = ['táo', 'chuối', 'cam'];
for (const fruit of fruits) {
  console.log(fruit);
}

// 5. Bài tập: Tính điểm trung bình
const scores = [8, 9, 7, 10, 6];
const sum = scores.reduce((acc, s) => acc + s, 0);
const avg = sum / scores.length;
console.log(`Điểm TB: ${avg}`);
console.log(`Xếp loại: ${avg >= 9 ? 'Xuất sắc' : avg >= 8 ? 'Giỏi' : avg >= 6.5 ? 'Khá' : 'TB'}`);
''')

write(f'{BASE}/chapter-04/index.html', '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Chương 4 — JavaScript Nhập môn</title>
</head>
<body>
  <h1>Mở Console (F12) để xem output!</h1>
  <script src="script.js"></script>
</body>
</html>
''')

# ======== CHAPTER 05 ========
write(f'{BASE}/chapter-05/scope.js', '''// Chương 5: Hàm và Phạm vi biến

// 1. Function declaration vs expression
function greet(name) {
  return `Xin chào, ${name}!`;
}

const greetArrow = (name) => `Xin chào, ${name}!`;

console.log(greet('An'));
console.log(greetArrow('Bình'));

// 2. Scope
const globalVar = 'Tôi là global';

function outer() {
  const outerVar = 'Tôi là outer';

  function inner() {
    const innerVar = 'Tôi là inner';
    console.log(globalVar); // Thấy global
    console.log(outerVar);  // Thấy outer
    console.log(innerVar);  // Thấy inner
  }

  inner();
  // console.log(innerVar); // Error! Không thấy inner
}

outer();

// 3. Closure
function makeCounter(start = 0) {
  let count = start;
  return {
    increment: () => ++count,
    decrement: () => --count,
    reset: () => { count = start; },
    value: () => count,
  };
}

const counter = makeCounter(10);
console.log(counter.increment()); // 11
console.log(counter.increment()); // 12
console.log(counter.decrement()); // 11
console.log(counter.value());     // 11

// 4. Higher-order functions
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evens = numbers.filter(n => n % 2 === 0);
const doubled = evens.map(n => n * 2);
const sum = doubled.reduce((acc, n) => acc + n, 0);
console.log(`Tổng chẵn nhân đôi: ${sum}`); // (2+4+6+8+10)*2 = 60
''')

# ======== CHAPTER 06 ========
write(f'{BASE}/chapter-06/arrays-objects.js', '''// Chương 6: Object và Array Nâng cao

// 1. Object destructuring
const user = { id: 1, name: 'Nguyễn An', age: 25, role: 'admin' };
const { name, age, role = 'user' } = user;
console.log(name, age, role); // Nguyễn An 25 admin

// Rename khi destructure
const { name: userName, age: userAge } = user;
console.log(userName, userAge); // Nguyễn An 25

// 2. Spread operator
const base = { theme: 'dark', language: 'vi' };
const extended = { ...base, fontSize: 16, language: 'en' }; // Override language
console.log(extended); // { theme: 'dark', language: 'en', fontSize: 16 }

// 3. Array methods pipeline
const products = [
  { id: 1, name: 'Laptop', price: 25000000, category: 'tech', inStock: true },
  { id: 2, name: 'Áo thun', price: 200000, category: 'fashion', inStock: false },
  { id: 3, name: 'Phone', price: 15000000, category: 'tech', inStock: true },
  { id: 4, name: 'Quần jeans', price: 500000, category: 'fashion', inStock: true },
  { id: 5, name: 'Tablet', price: 10000000, category: 'tech', inStock: true },
];

// Filter tech + inStock, sort by price desc, map to display format
const result = products
  .filter(p => p.category === 'tech' && p.inStock)
  .sort((a, b) => b.price - a.price)
  .map(p => `${p.name}: ${p.price.toLocaleString('vi-VN')}đ`);

console.log(result);
// ['Laptop: 25.000.000đ', 'Phone: 15.000.000đ', 'Tablet: 10.000.000đ']

// 4. Immutable updates (quan trọng trong React!)
const state = { count: 0, items: ['a', 'b'] };

// SAI: mutate trực tiếp
// state.count = 1;

// ĐÚNG: tạo object mới
const newState = { ...state, count: state.count + 1 };
const newStateWithItem = { ...state, items: [...state.items, 'c'] };
console.log(state);           // { count: 0, items: ['a', 'b'] } — không đổi
console.log(newState);        // { count: 1, items: ['a', 'b'] }
console.log(newStateWithItem);// { count: 0, items: ['a', 'b', 'c'] }
''')

# ======== CHAPTER 07 ========
write(f'{BASE}/chapter-07/async-examples.js', '''// Chương 7: Lập trình Async

// 1. Promise cơ bản
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function fetchUser(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve({ id, name: `User ${id}`, email: `user${id}@example.com` });
      } else {
        reject(new Error('ID không hợp lệ'));
      }
    }, 500);
  });
}

// 2. async/await
async function main() {
  // Sequential
  console.log('Bắt đầu...');
  const user = await fetchUser(1);
  console.log('User:', user);

  // Parallel với Promise.all
  console.log('Fetch parallel...');
  const [u1, u2, u3] = await Promise.all([
    fetchUser(1),
    fetchUser(2),
    fetchUser(3),
  ]);
  console.log('3 users:', u1.name, u2.name, u3.name);

  // Error handling
  try {
    await fetchUser(-1); // sẽ reject
  } catch (err) {
    console.error('Lỗi:', err.message);
  }
}

main();

// 3. Fetch API (chạy trong browser)
async function fetchPosts() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=3');
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const posts = await response.json();
  return posts;
}

// fetchPosts().then(posts => console.log(posts));
''')

# ======== CHAPTER 08 ========
write(f'{BASE}/chapter-08/math.js', '''// ES Modules — Named exports
export const PI = 3.14159;

export function add(a, b) { return a + b; }
export function multiply(a, b) { return a * b; }
export function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}
''')

write(f'{BASE}/chapter-08/main.js', '''// ES Modules — Import
import { PI, add, multiply } from './math.js';

console.log(PI);          // 3.14159
console.log(add(2, 3));   // 5
console.log(multiply(4, 5)); // 20

// Optional chaining
const user = { profile: { address: { city: 'HCM' } } };
console.log(user?.profile?.address?.city); // 'HCM'
console.log(user?.social?.twitter);         // undefined (không throw)

// Nullish coalescing
const config = { timeout: 0, name: '' };
console.log(config.timeout ?? 5000); // 0 (0 không phải null/undefined)
console.log(config.name ?? 'default'); // '' (empty string không phải null)
console.log(config.missing ?? 'fallback'); // 'fallback'

// Template literals
const name = 'ReactJS';
const year = 2024;
console.log(`Học ${name} năm ${year}!`);
console.log(`2 + 3 = ${2 + 3}`);
''')

# ======== CHAPTER 09 ========
write(f'{BASE}/chapter-09/README.md', '''# Chương 9 — Giới thiệu React

## Khởi tạo dự án

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

## Cấu trúc dự án sau khi tạo

```
my-react-app/
├── src/
│   ├── App.jsx        ← Component gốc
│   ├── main.jsx       ← Entry point
│   └── index.css
├── index.html
├── vite.config.js
└── package.json
```
''')

write(f'{BASE}/chapter-09/App.jsx', '''// App.jsx — Component React đầu tiên
import { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ textAlign: 'center', padding: '40px' }}>
      <h1>Hello, React! ⚛️</h1>
      <p>Dự án React đầu tiên với Vite</p>
      <button onClick={() => setCount(c => c + 1)}>
        Click: {count}
      </button>
    </div>
  );
}

export default App;
''')

# ======== CHAPTER 10 ========
write(f'{BASE}/chapter-10/ProductCard.jsx', '''// Component tái sử dụng với Props
function ProductCard({ name, price, image, badge, onAddToCart }) {
  return (
    <div className="card">
      {badge && <span className="badge">{badge}</span>}
      <img src={image} alt={name} />
      <h3>{name}</h3>
      <p>{price.toLocaleString('vi-VN')}đ</p>
      <button onClick={() => onAddToCart({ name, price })}>
        Thêm vào giỏ
      </button>
    </div>
  );
}

// ProductList — Render danh sách với key
function ProductList() {
  const products = [
    { id: 1, name: 'Laptop Dell', price: 25000000, badge: 'HOT' },
    { id: 2, name: 'iPhone 15', price: 30000000, badge: 'NEW' },
    { id: 3, name: 'AirPods Pro', price: 6000000, badge: null },
  ];

  const handleAddToCart = (product) => {
    alert(`Đã thêm ${product.name} vào giỏ!`);
  };

  return (
    <div className="product-list">
      {products.map(product => (
        <ProductCard
          key={product.id}       // KEY quan trọng!
          name={product.name}
          price={product.price}
          badge={product.badge}
          onAddToCart={handleAddToCart}
        />
      ))}
    </div>
  );
}

export default ProductList;
''')

# ======== CHAPTER 11 ========
write(f'{BASE}/chapter-11/TodoApp.jsx', '''// Bài tập: Todo List hoàn chỉnh
import { useState } from 'react';

function TodoApp() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Học React', done: false },
    { id: 2, text: 'Làm bài tập', done: true },
  ]);
  const [input, setInput] = useState('');

  const addTodo = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setTodos(prev => [...prev, { id: Date.now(), text: input.trim(), done: false }]);
    setInput('');
  };

  const toggleTodo = (id) => {
    setTodos(prev => prev.map(t => t.id === id ? { ...t, done: !t.done } : t));
  };

  const deleteTodo = (id) => {
    setTodos(prev => prev.filter(t => t.id !== id));
  };

  const remaining = todos.filter(t => !t.done).length;

  return (
    <div>
      <h1>Todo List ({remaining} còn lại)</h1>

      <form onSubmit={addTodo}>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Thêm todo mới..."
        />
        <button type="submit">Thêm</button>
      </form>

      <ul>
        {todos.map(todo => (
          <li key={todo.id} style={{ textDecoration: todo.done ? 'line-through' : 'none' }}>
            <input
              type="checkbox"
              checked={todo.done}
              onChange={() => toggleTodo(todo.id)}
            />
            {todo.text}
            <button onClick={() => deleteTodo(todo.id)}>×</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;
''')

# ======== CHAPTER 12 ========
write(f'{BASE}/chapter-12/useEffectExamples.jsx', '''// Các pattern useEffect thực tế
import { useState, useEffect } from 'react';

// Pattern 1: Fetch data với cleanup
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    fetch(`https://jsonplaceholder.typicode.com/users/${userId}`)
      .then(r => r.json())
      .then(data => {
        if (!cancelled) {
          setUser(data);
          setLoading(false);
        }
      })
      .catch(err => {
        if (!cancelled) {
          setError(err.message);
          setLoading(false);
        }
      });

    return () => { cancelled = true; }; // Cleanup
  }, [userId]); // Re-fetch khi userId thay đổi

  if (loading) return <div>Đang tải...</div>;
  if (error) return <div>Lỗi: {error}</div>;
  return <div>{user?.name}</div>;
}

// Pattern 2: Debounce search
function SearchBox() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  useEffect(() => {
    if (!query) { setResults([]); return; }

    const timer = setTimeout(() => {
      fetch(`https://jsonplaceholder.typicode.com/posts?q=${query}&_limit=5`)
        .then(r => r.json())
        .then(setResults);
    }, 300); // Chờ 300ms sau khi gõ xong

    return () => clearTimeout(timer); // Cleanup khi query thay đổi
  }, [query]);

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Tìm kiếm..." />
      <ul>{results.map(r => <li key={r.id}>{r.title}</li>)}</ul>
    </div>
  );
}
''')

# ======== CHAPTER 13 ========
write(f'{BASE}/chapter-13/README.md', '''# Chương 13 — Styling trong React

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
''')

# ======== CHAPTER 14 ========
write(f'{BASE}/chapter-14/AppRouter.jsx', '''// React Router v6 — Setup đầy đủ
import { BrowserRouter, Routes, Route, Link, NavLink, Navigate, useParams, Outlet } from 'react-router-dom';

// Pages
const Home = () => <h1>🏠 Trang chủ</h1>;
const About = () => <h1>ℹ️ Về chúng tôi</h1>;
const Products = () => <h1>📦 Danh sách sản phẩm</h1>;

function ProductDetail() {
  const { id } = useParams();
  return <h1>Chi tiết sản phẩm #{id}</h1>;
}

function NotFound() {
  return <h1>404 — Không tìm thấy trang!</h1>;
}

// Protected Route
function ProtectedRoute({ isLoggedIn }) {
  if (!isLoggedIn) return <Navigate to="/login" replace />;
  return <Outlet />;
}

// Dashboard Layout
function DashboardLayout() {
  return (
    <div>
      <nav>
        <NavLink to="/dashboard">Overview</NavLink>
        <NavLink to="/dashboard/settings">Settings</NavLink>
      </nav>
      <Outlet /> {/* Child routes render here */}
    </div>
  );
}

// Main App
function App() {
  const isLoggedIn = true; // Từ AuthContext trong thực tế

  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Trang chủ</Link>
        <Link to="/about">Về chúng tôi</Link>
        <Link to="/products">Sản phẩm</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/products" element={<Products />} />
        <Route path="/products/:id" element={<ProductDetail />} />

        {/* Protected routes */}
        <Route element={<ProtectedRoute isLoggedIn={isLoggedIn} />}>
          <Route path="/dashboard" element={<DashboardLayout />}>
            <Route index element={<div>Dashboard Overview</div>} />
            <Route path="settings" element={<div>Settings</div>} />
          </Route>
        </Route>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
''')

# ======== CHAPTER 15 ========
write(f'{BASE}/chapter-15/customHooks.js', '''// Custom Hooks — Tái sử dụng logic
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
''')

# ======== CHAPTER 16 ========
write(f'{BASE}/chapter-16/useStore.js', '''// Zustand store — Global State Management
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

// Cart store với persist
export const useCartStore = create(
  persist(
    (set, get) => ({
      items: [],
      isOpen: false,

      addItem: (product) => {
        const existing = get().items.find(i => i.id === product.id);
        if (existing) {
          set(state => ({
            items: state.items.map(i =>
              i.id === product.id ? { ...i, qty: i.qty + 1 } : i
            )
          }));
        } else {
          set(state => ({ items: [...state.items, { ...product, qty: 1 }] }));
        }
      },

      removeItem: (id) => set(state => ({
        items: state.items.filter(i => i.id !== id)
      })),

      clearCart: () => set({ items: [] }),

      get total() {
        return get().items.reduce((sum, i) => sum + i.price * i.qty, 0);
      },

      get count() {
        return get().items.reduce((sum, i) => sum + i.qty, 0);
      },
    }),
    { name: 'cart-storage' }
  )
);

// Dùng trong component:
// const { items, addItem, total } = useCartStore();
''')

# ======== CHAPTER 17 ========
write(f'{BASE}/chapter-17/queryHooks.js', '''// TanStack Query hooks
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const API = 'https://jsonplaceholder.typicode.com';

// Custom hooks cho API calls
export function usePosts() {
  return useQuery({
    queryKey: ['posts'],
    queryFn: () => fetch(`${API}/posts?_limit=10`).then(r => r.json()),
    staleTime: 5 * 60 * 1000, // 5 phút
  });
}

export function usePost(id) {
  return useQuery({
    queryKey: ['posts', id],
    queryFn: () => fetch(`${API}/posts/${id}`).then(r => r.json()),
    enabled: !!id,
  });
}

export function useCreatePost() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (newPost) =>
      fetch(`${API}/posts`, {
        method: 'POST',
        body: JSON.stringify(newPost),
        headers: { 'Content-Type': 'application/json' },
      }).then(r => r.json()),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });
}

// Component example:
// function PostList() {
//   const { data: posts, isLoading, error } = usePosts();
//   const { mutate: createPost } = useCreatePost();
//   if (isLoading) return <div>Đang tải...</div>;
//   if (error) return <div>Lỗi: {error.message}</div>;
//   return <ul>{posts.map(p => <li key={p.id}>{p.title}</li>)}</ul>;
// }
''')

# ======== CHAPTER 18 ========
write(f'{BASE}/chapter-18/RegisterForm.jsx', '''// React Hook Form + Zod — Form hoàn chỉnh
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';

const schema = z.object({
  username: z.string().min(3, 'Tối thiểu 3 ký tự').max(20),
  email: z.string().email('Email không hợp lệ'),
  password: z.string()
    .min(8, 'Tối thiểu 8 ký tự')
    .regex(/[A-Z]/, 'Cần ít nhất 1 chữ hoa')
    .regex(/[0-9]/, 'Cần ít nhất 1 số'),
  confirmPassword: z.string(),
  agreeToTerms: z.literal(true, {
    errorMap: () => ({ message: 'Bạn phải đồng ý điều khoản' })
  }),
}).refine(d => d.password === d.confirmPassword, {
  message: 'Mật khẩu không khớp',
  path: ['confirmPassword'],
});

function RegisterForm() {
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = async (data) => {
    await new Promise(r => setTimeout(r, 1000)); // Simulate API
    console.log('Đăng ký:', data);
    alert('Đăng ký thành công!');
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <input {...register('username')} placeholder="Username" />
        {errors.username && <span>{errors.username.message}</span>}
      </div>
      <div>
        <input {...register('email')} type="email" placeholder="Email" />
        {errors.email && <span>{errors.email.message}</span>}
      </div>
      <div>
        <input {...register('password')} type="password" placeholder="Mật khẩu" />
        {errors.password && <span>{errors.password.message}</span>}
      </div>
      <div>
        <input {...register('confirmPassword')} type="password" placeholder="Nhập lại mật khẩu" />
        {errors.confirmPassword && <span>{errors.confirmPassword.message}</span>}
      </div>
      <div>
        <input {...register('agreeToTerms')} type="checkbox" id="terms" />
        <label htmlFor="terms">Tôi đồng ý điều khoản</label>
        {errors.agreeToTerms && <span>{errors.agreeToTerms.message}</span>}
      </div>
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Đang xử lý...' : 'Đăng ký'}
      </button>
    </form>
  );
}

export default RegisterForm;
''')

# ======== CHAPTER 19 ========
write(f'{BASE}/chapter-19/VirtualizedList.jsx', '''// React.memo + Virtualization
import { useState, useMemo, memo } from 'react';
import { FixedSizeList } from 'react-window';

// Tạo 10,000 items
const ALL_ITEMS = Array.from({ length: 10000 }, (_, i) => ({
  id: i + 1,
  name: `User ${i + 1}`,
  email: `user${i + 1}@example.com`,
  score: Math.floor(Math.random() * 100),
}));

// Memoized row component — không re-render trừ khi data thay đổi
const Row = memo(({ index, style, data }) => (
  <div style={{ ...style, display: 'flex', alignItems: 'center', padding: '0 16px', borderBottom: '1px solid #333' }}>
    <span style={{ width: 40 }}>{data[index].id}</span>
    <span style={{ flex: 1 }}>{data[index].name}</span>
    <span>{data[index].score} điểm</span>
  </div>
));

function VirtualizedList() {
  const [search, setSearch] = useState('');

  // useMemo — chỉ filter lại khi search thay đổi
  const filteredItems = useMemo(() =>
    ALL_ITEMS.filter(item =>
      item.name.toLowerCase().includes(search.toLowerCase())
    ),
    [search]
  );

  return (
    <div>
      <input
        value={search}
        onChange={e => setSearch(e.target.value)}
        placeholder="Tìm kiếm..."
        style={{ width: '100%', padding: 8, marginBottom: 8 }}
      />
      <div style={{ fontSize: 14, marginBottom: 8 }}>
        Hiển thị {filteredItems.length} / {ALL_ITEMS.length} users
      </div>
      <FixedSizeList
        height={500}
        itemCount={filteredItems.length}
        itemSize={50}
        itemData={filteredItems}
        width="100%"
      >
        {Row}
      </FixedSizeList>
    </div>
  );
}

export default VirtualizedList;
''')

# ======== CHAPTER 20 ========
write(f'{BASE}/chapter-20/TodoApp.test.jsx', '''// Tests cho TodoApp — React Testing Library
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import TodoApp from './TodoApp';

describe('TodoApp', () => {
  it('render danh sách todos ban đầu', () => {
    render(<TodoApp />);
    expect(screen.getByText('Học React')).toBeInTheDocument();
    expect(screen.getByText('Làm bài tập')).toBeInTheDocument();
  });

  it('thêm todo mới khi submit form', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    await user.type(screen.getByPlaceholderText('Thêm todo mới...'), 'Todo mới');
    await user.keyboard('{Enter}');
    expect(screen.getByText('Todo mới')).toBeInTheDocument();
  });

  it('input được clear sau khi thêm', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    const input = screen.getByPlaceholderText('Thêm todo mới...');
    await user.type(input, 'Test todo');
    await user.keyboard('{Enter}');
    expect(input).toHaveValue('');
  });

  it('toggle done/undone', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    const checkbox = screen.getAllByRole('checkbox')[0];
    await user.click(checkbox);
    expect(checkbox).toBeChecked();
    await user.click(checkbox);
    expect(checkbox).not.toBeChecked();
  });

  it('xóa todo khi click nút ×', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    const deleteButtons = screen.getAllByText('×');
    await user.click(deleteButtons[0]);
    expect(screen.queryByText('Học React')).not.toBeInTheDocument();
  });
});
''')

write(f'{BASE}/chapter-20/TodoApp.jsx', '''import { useState } from 'react';

function TodoApp() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Học React', done: false },
    { id: 2, text: 'Làm bài tập', done: true },
  ]);
  const [input, setInput] = useState('');

  const addTodo = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setTodos(prev => [...prev, { id: Date.now(), text: input.trim(), done: false }]);
    setInput('');
  };
  const toggleTodo = (id) => setTodos(prev => prev.map(t => t.id === id ? { ...t, done: !t.done } : t));
  const deleteTodo = (id) => setTodos(prev => prev.filter(t => t.id !== id));

  return (
    <div>
      <form onSubmit={addTodo}>
        <input value={input} onChange={e => setInput(e.target.value)} placeholder="Thêm todo mới..." />
        <button type="submit">Thêm</button>
      </form>
      <ul>
        {todos.map(t => (
          <li key={t.id}>
            <input type="checkbox" checked={t.done} onChange={() => toggleTodo(t.id)} />
            <span style={{ textDecoration: t.done ? 'line-through' : 'none' }}>{t.text}</span>
            <button onClick={() => deleteTodo(t.id)}>×</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;
''')

# ======== CHAPTER 21 ========
write(f'{BASE}/chapter-21/types.ts', '''// TypeScript — Typing React components

import React from 'react';

// Interfaces
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'editor' | 'user';
  createdAt: Date;
}

// Utility types
type PublicUser = Omit<User, 'createdAt'>;
type UserUpdate = Partial<Pick<User, 'name' | 'email'>>;
type UserId = User['id'];

// Generic API response
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// Typed Props
interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'danger';
  disabled?: boolean;
  onClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
  children?: React.ReactNode;
}

function Button({ label, variant = 'primary', disabled, onClick }: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant}`}
      disabled={disabled}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

// Typed useReducer
type TodoAction =
  | { type: 'ADD'; payload: string }
  | { type: 'TOGGLE'; payload: string }
  | { type: 'DELETE'; payload: string };

interface Todo {
  id: string;
  text: string;
  done: boolean;
}

function todoReducer(state: Todo[], action: TodoAction): Todo[] {
  switch (action.type) {
    case 'ADD':
      return [...state, { id: crypto.randomUUID(), text: action.payload, done: false }];
    case 'TOGGLE':
      return state.map(t => t.id === action.payload ? { ...t, done: !t.done } : t);
    case 'DELETE':
      return state.filter(t => t.id !== action.payload);
  }
}

export type { User, PublicUser, UserUpdate, ApiResponse, ButtonProps, Todo, TodoAction };
export { Button, todoReducer };
''')

# ======== CHAPTER 22 ========
write(f'{BASE}/chapter-22/README.md', '''# Chương 22 — Next.js App Router

## Khởi tạo dự án

```bash
npx create-next-app@latest my-blog --typescript --tailwind --app
cd my-blog
npm run dev
```

## Cấu trúc App Router

```
app/
├── layout.tsx          # Root layout
├── page.tsx            # Route: /
├── blog/
│   ├── page.tsx        # Route: /blog
│   └── [slug]/
│       └── page.tsx    # Route: /blog/hello-world
└── api/
    └── posts/
        └── route.ts    # API: /api/posts
```
''')

write(f'{BASE}/chapter-22/page.tsx', '''// app/blog/[slug]/page.tsx — ISR page
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';

interface Post {
  id: number;
  title: string;
  body: string;
  userId: number;
}

async function getPost(slug: string): Promise<Post | null> {
  const id = parseInt(slug);
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${id}`,
    { next: { revalidate: 3600 } } // ISR: stale sau 1h
  );
  if (!res.ok) return null;
  return res.json();
}

// Dynamic metadata
export async function generateMetadata(
  { params }: { params: { slug: string } }
): Promise<Metadata> {
  const post = await getPost(params.slug);
  return {
    title: post?.title ?? 'Post not found',
    description: post?.body.slice(0, 100),
  };
}

// Pre-generate top 10 posts at build time
export async function generateStaticParams() {
  const posts: Post[] = await fetch(
    'https://jsonplaceholder.typicode.com/posts?_limit=10'
  ).then(r => r.json());
  return posts.map(p => ({ slug: String(p.id) }));
}

export default async function BlogPost({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug);
  if (!post) notFound();

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </article>
  );
}
''')

# ======== CHAPTER 23 ========
write(f'{BASE}/chapter-23/auth.ts', '''// JWT Authentication helpers
import jwt from 'jsonwebtoken';
import bcrypt from 'bcryptjs';

const JWT_SECRET = process.env.JWT_SECRET!;
const SALT_ROUNDS = 12;

interface JWTPayload {
  userId: string;
  email: string;
  role: 'admin' | 'editor' | 'user';
}

export async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, SALT_ROUNDS);
}

export async function verifyPassword(password: string, hash: string): Promise<boolean> {
  return bcrypt.compare(password, hash);
}

export function signToken(payload: JWTPayload): string {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: '7d' });
}

export function verifyToken(token: string): JWTPayload {
  return jwt.verify(token, JWT_SECRET) as JWTPayload;
}

// Middleware helper
export function getTokenFromCookies(cookieHeader: string | null): string | null {
  if (!cookieHeader) return null;
  const match = cookieHeader.match(/token=([^;]+)/);
  return match?.[1] ?? null;
}
''')

# ======== CHAPTER 24 ========
write(f'{BASE}/chapter-24/.github/workflows/ci.yml', '''name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"
      - run: npm ci
      - run: npm run type-check
      - run: npm run lint
      - run: npm test -- --run
      - run: npm run build
        env:
          NEXT_PUBLIC_API_URL: ${{ secrets.NEXT_PUBLIC_API_URL }}

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx vercel --prod --token ${{ secrets.VERCEL_TOKEN }}
        env:
          VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
          VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
''')

write(f'{BASE}/chapter-24/.env.example', '''# App
NEXT_PUBLIC_APP_NAME=My App
NEXT_PUBLIC_API_URL=https://api.example.com

# Auth (Server-only - KHÔNG expose ra client)
JWT_SECRET=your-super-secret-key-here

# Database (Server-only)
DATABASE_URL=postgresql://user:password@host:5432/dbname

# OAuth (nếu dùng)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
''')

# ======== CHAPTER 25 ========
write(f'{BASE}/chapter-25/README.md', '''# TaskFlow — Dự án cuối khóa

## Tech Stack

- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **State**: Zustand + TanStack Query
- **Forms**: React Hook Form + Zod
- **Backend**: Next.js API Routes
- **Database**: PostgreSQL + Prisma ORM
- **Auth**: JWT + httpOnly cookies
- **Real-time**: Server-Sent Events
- **Deploy**: Vercel + Supabase

## Bắt đầu

```bash
npx create-next-app@latest taskflow --typescript --tailwind --app
cd taskflow
npm install zustand @tanstack/react-query react-hook-form zod @hookform/resolvers
npm install prisma @prisma/client bcryptjs jsonwebtoken @dnd-kit/core @dnd-kit/sortable
npm install -D @types/bcryptjs @types/jsonwebtoken

# Setup database
npx prisma init
# Sửa DATABASE_URL trong .env
npx prisma db push

npm run dev
```

## Checklist phát triển

- [ ] Auth: Register, Login, Logout API routes
- [ ] Auth: JWT middleware + AuthContext
- [ ] Projects: CRUD API + UI
- [ ] Tasks: CRUD API + TaskCard component
- [ ] Kanban Board với @dnd-kit drag-and-drop
- [ ] Dashboard với thống kê
- [ ] Real-time SSE
- [ ] Dark mode với ThemeProvider
- [ ] Tests với Vitest + RTL
- [ ] Deploy Vercel + GitHub Actions CI/CD
''')

print('\nAll code examples created!')
