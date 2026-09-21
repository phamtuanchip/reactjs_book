# Sách: Lập Trình ReactJS - Từ Cơ Bản Đến Nâng Cao
**Đọc online (GitHub Pages): https://phamtuanchip.github.io/reactjs_book/**
> Sách tiếng Việt dành cho người mới bắt đầu, không yêu cầu kiến thức lập trình trước

---

## Mục tiêu dự án

Viết một quyển sách tiếng Việt hướng dẫn lập trình ReactJS cho người mới bắt đầu, chưa có kiến thức JavaScript cơ bản. Sách sẽ dẫn dắt học viên từ các khái niệm nền tảng về web, HTML, CSS, JavaScript đến các kỹ thuật ReactJS nâng cao và hệ sinh thái xung quanh React.

---

## Đối tượng độc giả

- Chưa biết về các khái niệm Single Page Application (SPA), PWA, Server Side Rendering (SSR)
- Chưa biết bất kỳ JavaScript framework nào
- Chưa vững về HTML, CSS, DOM
- Chưa hiểu cách JavaScript hoạt động, quản lý bộ nhớ và state
- Mong muốn trở thành Frontend Developer chuyên nghiệp

---

## Định dạng xuất bản

| Giai đoạn | Định dạng | Mô tả |
|-----------|-----------|-------|
| Giai đoạn 1 | HTML | Đọc trên trình duyệt, miễn phí |
| Giai đoạn 2 | PDF & EPUB | Tải về, đọc offline |
| Giai đoạn 3 | Amazon KDP | Xuất bản thương mại |

---

## Cấu trúc thư mục dự án

```
reactjs_book/
├── README.md               # File plan này
├── chapters/               # Nội dung từng chương (Markdown)
│   ├── part1-foundation/
│   ├── part2-javascript/
│   ├── part3-react-basic/
│   ├── part4-react-advanced/
│   └── part5-ecosystem/
├── examples/               # Code mẫu cho từng bài học
│   ├── chapter-01/
│   ├── chapter-02/
│   └── ...
├── exercises/              # Bài tập và câu hỏi ôn bài
└── assets/                 # Hình ảnh, sơ đồ minh họa
```

---

## Cấu trúc nội dung sách

### PHẦN 1 — NỀN TẢNG WEB (Chương 1–3)
> Dành cho người chưa biết gì về lập trình web

#### Chương 1: Làm quen với Web và Lập trình
- Web là gì? Internet hoạt động như thế nào?
- Client và Server: hai phía của ứng dụng web
- Trình duyệt làm gì khi bạn gõ một URL?
- Giới thiệu công cụ: VS Code, trình duyệt, DevTools
- **Bài tập**: Mở DevTools, quan sát Network tab khi tải một trang web

#### Chương 2: HTML — Xương sống của trang web
- HTML là gì? Cấu trúc một tài liệu HTML
- Các thẻ HTML phổ biến: heading, paragraph, link, image, list, table, form
- Semantic HTML: section, article, nav, header, footer
- HTML5 và những thay đổi quan trọng
- DOM (Document Object Model): cây tài liệu HTML
- **Bài tập**: Xây dựng trang profile cá nhân bằng HTML thuần

#### Chương 3: CSS — Trang điểm cho trang web
- CSS là gì? Cách liên kết CSS với HTML
- Selector, property, value — cú pháp cơ bản
- Box model: margin, padding, border, content
- Flexbox: căn chỉnh layout linh hoạt
- CSS Grid: bố cục hai chiều
- Responsive Design và Media Query
- CSS Variables và tổ chức code CSS
- **Bài tập**: Style lại trang profile từ Chương 2

---

### PHẦN 2 — JAVASCRIPT CƠ BẢN ĐẾN NÂNG CAO (Chương 4–8)
> Ngôn ngữ lập trình nền tảng của React

#### Chương 4: JavaScript Nhập môn
- JavaScript là gì? Chạy ở đâu?
- Biến: `var`, `let`, `const` và sự khác biệt
- Kiểu dữ liệu: string, number, boolean, null, undefined, object, array
- Toán tử: số học, so sánh, logic
- Cấu trúc điều kiện: `if/else`, `switch`
- Vòng lặp: `for`, `while`, `for...of`, `for...in`
- **Bài tập**: Viết chương trình tính điểm trung bình và xếp loại học lực

#### Chương 5: Hàm và Phạm vi biến
- Khai báo hàm: `function declaration` vs `function expression`
- Arrow function (`=>`) — cú pháp hiện đại
- Tham số, giá trị mặc định, rest parameters
- Scope: global, function, block
- Closure — hàm nhớ môi trường khi được tạo
- Higher-order function: hàm nhận/trả về hàm khác
- **Bài tập**: Xây dựng bộ công cụ xử lý mảng (filter, map, reduce)

#### Chương 6: Object và Array nâng cao
- Object: tạo, truy cập, destructuring, spread operator
- Array methods: `map`, `filter`, `reduce`, `find`, `some`, `every`
- Immutability — tại sao không nên thay đổi trực tiếp dữ liệu
- JSON: định dạng trao đổi dữ liệu phổ biến
- **Bài tập**: Xử lý danh sách sản phẩm với filter, sort, tổng giá trị

#### Chương 7: Lập trình bất đồng bộ (Async)
- Tại sao cần async? Event Loop hoạt động như thế nào?
- Callback — cách cũ và vấn đề "callback hell"
- Promise: `.then()`, `.catch()`, `.finally()`
- `async/await` — cú pháp hiện đại, dễ đọc
- Fetch API: gọi dữ liệu từ server
- Xử lý lỗi trong async code
- **Bài tập**: Gọi API công khai (OpenWeather hoặc JSONPlaceholder) và hiển thị dữ liệu

#### Chương 8: JavaScript hiện đại (ES6+)
- Template literals
- Modules: `import` / `export`
- Optional chaining (`?.`) và Nullish coalescing (`??`)
- Symbol, WeakMap, WeakSet (giới thiệu)
- Giới thiệu TypeScript — tại sao cần kiểu dữ liệu tĩnh?
- **Bài tập**: Tái cấu trúc code từ các chương trước dùng ES6+

---

### PHẦN 3 — REACT CƠ BẢN (Chương 9–14)
> Học React từ những khái niệm đầu tiên

#### Chương 9: Giới thiệu React
- SPA là gì? Tại sao React ra đời?
- Virtual DOM — React làm gì khác so với DOM thực?
- Cài đặt môi trường: Node.js, npm/yarn/pnpm
- Tạo dự án với Vite + React
- Cấu trúc thư mục dự án React
- **Bài tập**: Tạo dự án React đầu tiên, chạy và khám phá

#### Chương 10: JSX và Component
- JSX là gì? Khác HTML ở điểm nào?
- Functional Component — cách viết component hiện đại
- Props: truyền dữ liệu từ cha xuống con
- Children prop và component lồng nhau
- Conditional rendering: hiển thị có điều kiện
- Rendering danh sách với `key`
- **Bài tập**: Xây dựng trang danh sách sản phẩm với component tái sử dụng

#### Chương 11: State và Event
- State là gì? Tại sao cần state?
- `useState` hook — quản lý state trong functional component
- Xử lý sự kiện: onClick, onChange, onSubmit
- Controlled components — form được React kiểm soát
- State lifting: chia sẻ state giữa các component
- **Bài tập**: Xây dựng ứng dụng Todo List đầy đủ chức năng

#### Chương 12: useEffect và Vòng đời Component
- Component lifecycle: mount, update, unmount
- `useEffect` hook — xử lý side effects
- Dependency array: chạy effect khi nào?
- Cleanup function — dọn dẹp khi component unmount
- Gọi API trong useEffect
- **Bài tập**: Trang tìm kiếm với debounce gọi API

#### Chương 13: Styling trong React
- CSS Modules — style có phạm vi component
- Styled Components / Emotion — CSS-in-JS
- Tailwind CSS — utility-first framework
- Inline styles và khi nào nên dùng
- **Bài tập**: Thiết kế lại Todo List với Tailwind CSS

#### Chương 14: React Router — Điều hướng trang
- Routing trong SPA hoạt động như thế nào?
- Cài đặt và cấu hình React Router v6
- `<Link>`, `useNavigate`, `useParams`
- Nested routes và layout chung
- Protected routes — bảo vệ trang yêu cầu đăng nhập
- **Bài tập**: Xây dựng ứng dụng nhiều trang với navigation

---

### PHẦN 4 — REACT NÂNG CAO (Chương 15–20)
> Kỹ thuật và pattern cho ứng dụng thực tế

#### Chương 15: Hooks nâng cao
- `useReducer` — quản lý state phức tạp
- `useContext` — chia sẻ state toàn cục không cần props drilling
- `useRef` — tham chiếu DOM và giá trị không re-render
- `useMemo` và `useCallback` — tối ưu hiệu năng
- Custom Hooks — tái sử dụng logic
- **Bài tập**: Xây dựng custom hook `useFetch` và `useLocalStorage`

#### Chương 16: Quản lý State toàn cục
- Vấn đề với props drilling ở ứng dụng lớn
- Context API — giải pháp có sẵn trong React
- Zustand — thư viện state nhẹ, dễ dùng
- Redux Toolkit — giải pháp enterprise
- Khi nào dùng gì?
- **Bài tập**: Xây dựng giỏ hàng (shopping cart) với Zustand

#### Chương 17: Tương tác với API và Data Fetching
- REST API vs GraphQL — so sánh tổng quan
- TanStack Query (React Query) — server state management
- Caching, background refetch, optimistic updates
- Error boundaries — xử lý lỗi ở cấp component
- **Bài tập**: Ứng dụng blog đọc dữ liệu từ API với loading/error states

#### Chương 18: Form nâng cao
- Vấn đề với form phức tạp trong React
- React Hook Form — hiệu năng cao, ít re-render
- Validation với Zod hoặc Yup
- File upload và xử lý dữ liệu nhị phân
- **Bài tập**: Form đăng ký nhiều bước (multi-step form) với validation

#### Chương 19: Tối ưu hiệu năng
- React re-render hoạt động như thế nào?
- `React.memo` — tránh render không cần thiết
- Code splitting với `React.lazy` và `Suspense`
- Virtualization — render danh sách dài (react-window)
- Profiler — đo lường và phân tích hiệu năng
- **Bài tập**: Tối ưu ứng dụng danh sách 10,000 phần tử

#### Chương 20: Testing trong React
- Tại sao cần test? Các loại test
- Vitest — unit test runner
- React Testing Library — test theo hành vi người dùng
- Mock API calls trong test
- **Bài tập**: Viết test cho Todo List và shopping cart

---

### PHẦN 5 — HỆ SINH THÁI VÀ THỰC CHIẾN (Chương 21–25)
> Công nghệ và kỹ năng để đi làm thực tế

#### Chương 21: TypeScript với React
- Tại sao TypeScript quan trọng trong dự án thực tế?
- Typing props, state, event handlers
- Generic types trong React
- Tích hợp TypeScript vào dự án React có sẵn
- **Bài tập**: Chuyển đổi Todo List sang TypeScript hoàn toàn

#### Chương 22: Next.js — React cho Production
- CSR vs SSR vs SSG vs ISR — so sánh các chiến lược render
- App Router trong Next.js 14+
- Server Components vs Client Components
- API Routes và Server Actions
- Metadata, SEO tối ưu
- **Bài tập**: Xây dựng blog cá nhân với Next.js và Markdown

#### Chương 23: Authentication và Authorization
- JWT, Session, OAuth — các phương thức xác thực
- Tích hợp NextAuth.js / Auth.js
- Role-based access control (RBAC)
- Bảo mật: XSS, CSRF, và cách phòng tránh
- **Bài tập**: Hệ thống đăng nhập với Google OAuth

#### Chương 24: Triển khai ứng dụng (Deployment)
- Build production và tối ưu bundle
- Triển khai lên Vercel (Next.js) và Netlify (React thuần)
- CI/CD cơ bản với GitHub Actions
- Environment variables và quản lý cấu hình
- Domain, HTTPS, CDN — hiểu cơ bản
- **Bài tập**: Deploy ứng dụng blog lên Vercel với CI/CD

#### Chương 25: Dự án cuối khóa — Xây dựng ứng dụng hoàn chỉnh
- Phân tích yêu cầu và thiết kế kiến trúc
- Xây dựng ứng dụng quản lý công việc (Task Manager) đầy đủ:
  - Authentication với JWT
  - CRUD tasks với tags và priority
  - Dashboard với biểu đồ thống kê
  - Real-time notification
  - Dark mode
  - Responsive design
  - Deploy lên production

---

## Phụ lục

- **Phụ lục A**: Cheat Sheet HTML/CSS/JavaScript/React
- **Phụ lục B**: Danh sách thư viện và công cụ phổ biến trong hệ sinh thái React
- **Phụ lục C**: Tài nguyên học tập tiếp theo (docs, khóa học, cộng đồng)
- **Phụ lục D**: Câu hỏi phỏng vấn Frontend Developer thường gặp

---

## Quy ước viết sách

- Mỗi chương có: lý thuyết → ví dụ minh họa → bài tập thực hành → câu hỏi ôn bài
- Code mẫu đặt trong thư mục `examples/chapter-XX/`
- Hình ảnh/sơ đồ minh họa cho mọi khái niệm trừu tượng
- Giọng văn thân thiện, giải thích "tại sao" trước "làm như thế nào"
- Không dùng thuật ngữ kỹ thuật mà không giải thích trước

---

## Lộ trình viết

| Giai đoạn | Nội dung | Thời gian dự kiến |
|-----------|----------|-------------------|
| 1 | Phần 1 + Phần 2 (Chương 1–8) | Tháng 1–2 |
| 2 | Phần 3 (Chương 9–14) | Tháng 3–4 |
| 3 | Phần 4 (Chương 15–20) | Tháng 5–6 |
| 4 | Phần 5 (Chương 21–25) + Phụ lục | Tháng 7–8 |
| 5 | Review, chỉnh sửa, xuất bản HTML | Tháng 9 |
| 6 | PDF/EPUB + Amazon KDP | Tháng 10–12 |
