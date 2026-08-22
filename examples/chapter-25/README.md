# TaskFlow — Dự án cuối khóa

## Tech Stack

- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **State**: Zustand + TanStack Query
- **Forms**: React Hook Form + Zod
- **Backend**: Next.js API Routes
- **Database**: PostgreSQL + Prisma ORM
- **Auth**: JWT + httpOnly cookies
- **Real-time**: Server-Sent Events
- **Deploy**: Vercel + Supabase

## Bắt đầu

```bash
npx create-next-app@latest taskflow --typescript --tailwind --app
cd taskflow
npm install zustand @tanstack/react-query react-hook-form zod @hookform/resolvers
npm install prisma @prisma/client bcryptjs jsonwebtoken @dnd-kit/core @dnd-kit/sortable
npm install -D @types/bcryptjs @types/jsonwebtoken

# Setup database
npx prisma init
# Sửa DATABASE_URL trong .env
npx prisma db push

npm run dev
```

## Checklist phát triển

- [ ] Auth: Register, Login, Logout API routes
- [ ] Auth: JWT middleware + AuthContext
- [ ] Projects: CRUD API + UI
- [ ] Tasks: CRUD API + TaskCard component
- [ ] Kanban Board với @dnd-kit drag-and-drop
- [ ] Dashboard với thống kê
- [ ] Real-time SSE
- [ ] Dark mode với ThemeProvider
- [ ] Tests với Vitest + RTL
- [ ] Deploy Vercel + GitHub Actions CI/CD
