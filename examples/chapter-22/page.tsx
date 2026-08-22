// app/blog/[slug]/page.tsx — ISR page
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';

interface Post {
  id: number;
  title: string;
  body: string;
  userId: number;
}

async function getPost(slug: string): Promise<Post | null> {
  const id = parseInt(slug);
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${id}`,
    { next: { revalidate: 3600 } } // ISR: stale sau 1h
  );
  if (!res.ok) return null;
  return res.json();
}

// Dynamic metadata
export async function generateMetadata(
  { params }: { params: { slug: string } }
): Promise<Metadata> {
  const post = await getPost(params.slug);
  return {
    title: post?.title ?? 'Post not found',
    description: post?.body.slice(0, 100),
  };
}

// Pre-generate top 10 posts at build time
export async function generateStaticParams() {
  const posts: Post[] = await fetch(
    'https://jsonplaceholder.typicode.com/posts?_limit=10'
  ).then(r => r.json());
  return posts.map(p => ({ slug: String(p.id) }));
}

export default async function BlogPost({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug);
  if (!post) notFound();

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </article>
  );
}
