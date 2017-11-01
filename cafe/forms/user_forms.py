from django.forms.models import ModelForm

from cafe.models import UserInfo


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'password')
