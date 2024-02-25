from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, reset_user_password, EmailConfirmationSentView, UserConfirmEmail

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('reset/', reset_user_password, name='reset'),

    path('confirmation/', TemplateView.as_view(template_name='users/email_confirmation.html'), name='confirmation'),
    path('verify/', EmailConfirmationSentView.as_view(template_name='users/verify_email.html'), name='verify'),
    path('email_confirm/<uidb64>/<token>/', UserConfirmEmail.as_view(), name='email_confirm'),

]