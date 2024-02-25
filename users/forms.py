from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django import forms
from django.forms import ModelForm

from users.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['password'].widget = forms.HiddenInput()

class UserVerifyCode(forms.Form):
    class Meta:
        model = User
        fields = ['verification_code',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ResetPassword(PasswordResetForm):
    class Meta:
        model = User

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)