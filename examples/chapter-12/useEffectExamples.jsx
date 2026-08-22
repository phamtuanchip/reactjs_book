// Các pattern useEffect thực tế
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
