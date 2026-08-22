// React Router v6 — Setup đầy đủ
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
