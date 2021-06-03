from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from siteapp.models import Post


class PostPhotoForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
