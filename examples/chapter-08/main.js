// ES Modules — Import
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
