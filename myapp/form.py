from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User 

class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    )

    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('password1', 'password2', 'magic_number', 'role')

        labels = {
            'username': 'Nom',
            'magic_number': 'Nombre magique'
        }


from .models import Category

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'enabled']
        labels = {
            'name': 'Nom',
            'enabled': 'Actif'
        }