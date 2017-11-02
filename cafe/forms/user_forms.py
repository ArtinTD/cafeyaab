from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.db.models.fields import TextField, EmailField
from django.forms.models import ModelForm
from cafe.models import UserInfo


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2', )

    def clean_username(self):
        username = self.cleaned_data.get("username")
    # user_model = get_user_model() # your way of getting the Use
        try:
            UserInfo.objects.get(username__iexact= "username")
        except UserInfo.DoesNotExist:
            return username
        raise forms.ValidationError(_("This username has already existed."))

# class SignupForm(ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     error_messages = {
#         'password_mismatch': ("The two password fields didn't match."),
#     }
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     #
#     # password1 = forms.CharField(
#     #     label= ("Password"),
#     #     strip=False,
#     #     widget=forms.PasswordInput,
#     #     help_text=password_validation.password_validators_help_text_html(),
#     # )
#     password2 = forms.CharField(
#         label= ("Password confirmation"),
#         widget=forms.PasswordInput,
#         strip=False,
#         help_text= ("Enter the same password as before, for verification."),
#     )
#     class Meta:
#         model = User
#         fields = ('username', 'password' ,'email')
#         # field_classes = {'username': UsernameField , 'password': TextField , 'email': EmailField}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self._meta.model.USERNAME_FIELD in self.fields:
#             self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
#
#     def clean_password2(self):
#         password = self.cleaned_data.get("password")
#         password2 = self.cleaned_data.get("password2")
#         if password and password2 and password != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         self.instance.username = self.cleaned_data.get('username')
#         password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
#         return password2
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
#     # send_mail(
#     # 'Subject here',
#     # 'Here is the message.',
#     # 'from@example.com',
#     # ['to@example.com'],
#     # fail_silently=False,
# # )
#
