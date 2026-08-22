// Chương 6: Object và Array Nâng cao

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
