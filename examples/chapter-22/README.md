# Chương 22 — Next.js App Router

## Khởi tạo dự án

```bash
npx create-next-app@latest my-blog --typescript --tailwind --app
cd my-blog
npm run dev
```

## Cấu trúc App Router

```
app/
├── layout.tsx          # Root layout
├── page.tsx            # Route: /
├── blog/
│   ├── page.tsx        # Route: /blog
│   └── [slug]/
│       └── page.tsx    # Route: /blog/hello-world
└── api/
    └── posts/
        └── route.ts    # API: /api/posts
```
