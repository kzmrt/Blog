from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class TestForm(forms.Form):

    title1 = forms.CharField(
        initial='',
        label='タイトル1',
        required = False, # 必須ではない
    )
    title2 = forms.CharField(
        initial='',
        label='タイトル2',
        required=False,  # 必須ではない
    )
    title3 = forms.CharField(
        initial='',
        label='タイトル3',
        required=False,  # 必須ではない
    )