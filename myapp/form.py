from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User 
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User 
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'magic_number', 'role')
        labels = {
            'username': 'Nom d\'utilisateur',
            'magic_number': 'Nombre magique'
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )
from .models import Category

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'enabled']
        labels = {
            'name': 'Nom',
            'enabled': 'Actif'
        }

from .models import Card

class CardCreationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'image', 'music', 'video', 'description', 'size']
