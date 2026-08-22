// Chương 4: JavaScript Nhập môn

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
