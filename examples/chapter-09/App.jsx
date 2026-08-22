// App.jsx — Component React đầu tiên
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
