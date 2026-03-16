from django import forms
from .models import PerfilAutor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AuthorProfileForm(forms.ModelForm):

    class Meta:
        model = PerfilAutor
        fields = ["info", "region"]

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]