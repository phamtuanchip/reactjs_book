// Tests cho TodoApp — React Testing Library
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import TodoApp from './TodoApp';

describe('TodoApp', () => {
  it('render danh sách todos ban đầu', () => {
    render(<TodoApp />);
    expect(screen.getByText('Học React')).toBeInTheDocument();
    expect(screen.getByText('Làm bài tập')).toBeInTheDocument();
  });

  it('thêm todo mới khi submit form', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    await user.type(screen.getByPlaceholderText('Thêm todo mới...'), 'Todo mới');
    await user.keyboard('{Enter}');
    expect(screen.getByText('Todo mới')).toBeInTheDocument();
  });

  it('input được clear sau khi thêm', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    const input = screen.getByPlaceholderText('Thêm todo mới...');
    await user.type(input, 'Test todo');
    await user.keyboard('{Enter}');
    expect(input).toHaveValue('');
  });

  it('toggle done/undone', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    const checkbox = screen.getAllByRole('checkbox')[0];
    await user.click(checkbox);
    expect(checkbox).toBeChecked();
    await user.click(checkbox);
    expect(checkbox).not.toBeChecked();
  });

  it('xóa todo khi click nút ×', async () => {
    const user = userEvent.setup();
    render(<TodoApp />);
    const deleteButtons = screen.getAllByText('×');
    await user.click(deleteButtons[0]);
    expect(screen.queryByText('Học React')).not.toBeInTheDocument();
  });
});
