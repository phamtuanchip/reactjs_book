// React.memo + Virtualization
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
