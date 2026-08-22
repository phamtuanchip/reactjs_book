// TypeScript — Typing React components

import React from 'react';

// Interfaces
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'editor' | 'user';
  createdAt: Date;
}

// Utility types
type PublicUser = Omit<User, 'createdAt'>;
type UserUpdate = Partial<Pick<User, 'name' | 'email'>>;
type UserId = User['id'];

// Generic API response
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// Typed Props
interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary' | 'danger';
  disabled?: boolean;
  onClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
  children?: React.ReactNode;
}

function Button({ label, variant = 'primary', disabled, onClick }: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant}`}
      disabled={disabled}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

// Typed useReducer
type TodoAction =
  | { type: 'ADD'; payload: string }
  | { type: 'TOGGLE'; payload: string }
  | { type: 'DELETE'; payload: string };

interface Todo {
  id: string;
  text: string;
  done: boolean;
}

function todoReducer(state: Todo[], action: TodoAction): Todo[] {
  switch (action.type) {
    case 'ADD':
      return [...state, { id: crypto.randomUUID(), text: action.payload, done: false }];
    case 'TOGGLE':
      return state.map(t => t.id === action.payload ? { ...t, done: !t.done } : t);
    case 'DELETE':
      return state.filter(t => t.id !== action.payload);
  }
}

export type { User, PublicUser, UserUpdate, ApiResponse, ButtonProps, Todo, TodoAction };
export { Button, todoReducer };
