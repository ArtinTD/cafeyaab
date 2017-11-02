from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.db.models.fields import TextField, EmailField
from django.forms.models import ModelForm
# from cafe.models import UserInfo


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'email','password1', 'password2')
    def clean_username(self):
        username = self.cleaned_data.get("username")
    # user_model = get_user_model() # your way of getting the Use
        try:
            User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(("This username has already existed."))
#
# class UserInfoForm(ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = ('', 'address', 'profile_picture')
