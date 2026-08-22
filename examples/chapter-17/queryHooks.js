// TanStack Query hooks
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const API = 'https://jsonplaceholder.typicode.com';

// Custom hooks cho API calls
export function usePosts() {
  return useQuery({
    queryKey: ['posts'],
    queryFn: () => fetch(`${API}/posts?_limit=10`).then(r => r.json()),
    staleTime: 5 * 60 * 1000, // 5 phút
  });
}

export function usePost(id) {
  return useQuery({
    queryKey: ['posts', id],
    queryFn: () => fetch(`${API}/posts/${id}`).then(r => r.json()),
    enabled: !!id,
  });
}

export function useCreatePost() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (newPost) =>
      fetch(`${API}/posts`, {
        method: 'POST',
        body: JSON.stringify(newPost),
        headers: { 'Content-Type': 'application/json' },
      }).then(r => r.json()),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });
}

// Component example:
// function PostList() {
//   const { data: posts, isLoading, error } = usePosts();
//   const { mutate: createPost } = useCreatePost();
//   if (isLoading) return <div>Đang tải...</div>;
//   if (error) return <div>Lỗi: {error.message}</div>;
//   return <ul>{posts.map(p => <li key={p.id}>{p.title}</li>)}</ul>;
// }
