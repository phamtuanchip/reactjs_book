// Zustand store — Global State Management
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

// Cart store với persist
export const useCartStore = create(
  persist(
    (set, get) => ({
      items: [],
      isOpen: false,

      addItem: (product) => {
        const existing = get().items.find(i => i.id === product.id);
        if (existing) {
          set(state => ({
            items: state.items.map(i =>
              i.id === product.id ? { ...i, qty: i.qty + 1 } : i
            )
          }));
        } else {
          set(state => ({ items: [...state.items, { ...product, qty: 1 }] }));
        }
      },

      removeItem: (id) => set(state => ({
        items: state.items.filter(i => i.id !== id)
      })),

      clearCart: () => set({ items: [] }),

      get total() {
        return get().items.reduce((sum, i) => sum + i.price * i.qty, 0);
      },

      get count() {
        return get().items.reduce((sum, i) => sum + i.qty, 0);
      },
    }),
    { name: 'cart-storage' }
  )
);

// Dùng trong component:
// const { items, addItem, total } = useCartStore();
