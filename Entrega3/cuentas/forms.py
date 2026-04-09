from django import forms
from .models import PerfilAutor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Avatar

class AuthorProfileForm(forms.ModelForm):

    class Meta:
        model = PerfilAutor
        fields = ["info", "region"]

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    bio = forms.CharField(required=False, label="Bio/Tu info")
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name" ,"email" , "password1", "password2"]
 
class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    bio = forms.CharField(required=False, label="Bio/Tu info")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password",)

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]