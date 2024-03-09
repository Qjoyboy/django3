import random
import django.core.mail.backends.smtp
from django.conf import settings
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView, TemplateView
from users.forms import UserRegisterForm, UserProfileForm, ResetPassword, UserVerifyCode
from users.models import User
from users.utils import send_email_for_verify
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator

User = get_user_model()

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:activated_mail')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = self.request.get_host()
        token = token_generator.make_token(user)
        context = {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token
        }
        message = render_to_string('users/email_confirm.html', context=context)
        email = EmailMessage('Verify_email', message, to=[user.email])
        try:
            email.send()
        except Exception as e:
            print(f'Error sending email {str(e)}')
        return redirect('users:verify')


class UserConfirmEmail(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:login')
        return redirect('catalog:home')


    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/verify'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


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


