// React Hook Form + Zod — Form hoàn chỉnh
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';

const schema = z.object({
  username: z.string().min(3, 'Tối thiểu 3 ký tự').max(20),
  email: z.string().email('Email không hợp lệ'),
  password: z.string()
    .min(8, 'Tối thiểu 8 ký tự')
    .regex(/[A-Z]/, 'Cần ít nhất 1 chữ hoa')
    .regex(/[0-9]/, 'Cần ít nhất 1 số'),
  confirmPassword: z.string(),
  agreeToTerms: z.literal(true, {
    errorMap: () => ({ message: 'Bạn phải đồng ý điều khoản' })
  }),
}).refine(d => d.password === d.confirmPassword, {
  message: 'Mật khẩu không khớp',
  path: ['confirmPassword'],
});

function RegisterForm() {
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = async (data) => {
    await new Promise(r => setTimeout(r, 1000)); // Simulate API
    console.log('Đăng ký:', data);
    alert('Đăng ký thành công!');
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <input {...register('username')} placeholder="Username" />
        {errors.username && <span>{errors.username.message}</span>}
      </div>
      <div>
        <input {...register('email')} type="email" placeholder="Email" />
        {errors.email && <span>{errors.email.message}</span>}
      </div>
      <div>
        <input {...register('password')} type="password" placeholder="Mật khẩu" />
        {errors.password && <span>{errors.password.message}</span>}
      </div>
      <div>
        <input {...register('confirmPassword')} type="password" placeholder="Nhập lại mật khẩu" />
        {errors.confirmPassword && <span>{errors.confirmPassword.message}</span>}
      </div>
      <div>
        <input {...register('agreeToTerms')} type="checkbox" id="terms" />
        <label htmlFor="terms">Tôi đồng ý điều khoản</label>
        {errors.agreeToTerms && <span>{errors.agreeToTerms.message}</span>}
      </div>
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Đang xử lý...' : 'Đăng ký'}
      </button>
    </form>
  );
}

export default RegisterForm;
