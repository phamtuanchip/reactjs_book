// Chương 5: Hàm và Phạm vi biến

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
