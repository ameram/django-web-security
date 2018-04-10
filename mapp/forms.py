from django import forms
from django.contrib.auth.models import User
from mapp.models import UserProfileInfo
# Time to create model forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
