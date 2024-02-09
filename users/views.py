import random
import django.core.mail.backends.smtp
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from users.forms import UserRegisterForm, UserProfileForm, ResetPassword
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject='Регистрация прошла успешно',
            message=f'Ваша регистрация прошла успешно, 1-{user}, 2-{user.email}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def reset_user_password(request):

    qwerty = ''.join([str(random.randint(0,9)) for _ in range(12)])
    # context = {
    #     request.user.password: qwerty
    # }
    request.user.set_password(qwerty)
    request.user.save()
    send_mail(
            subject='Проверка',
            message=f'Ваш новый пароль: {qwerty}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email]
        )
    return redirect(reverse('users:login'))


