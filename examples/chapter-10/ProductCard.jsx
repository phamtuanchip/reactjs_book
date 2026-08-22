// Component tái sử dụng với Props
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
