from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from cafe.models import UserInfo


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'password' ,'email' )

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username', 'password' ,'email')

