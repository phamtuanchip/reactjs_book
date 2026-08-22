// Chương 7: Lập trình Async

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
