from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User 
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User 
from django.contrib.auth.forms import AuthenticationForm
from .models import Card

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
        fields = ['title', 'description', 'image', 'music', 'video', 'size']
    
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        music = cleaned_data.get('music')
        video = cleaned_data.get('video')
        
        if not image and not music and not video:
            raise forms.ValidationError('Vous devez télécharger soit une image, soit un fichier audio, soit une vidéo.')
        
        if (image and music) or (image and video) or (music and video):
            raise forms.ValidationError('Vous ne pouvez télécharger qu\'un seul type de fichier à la fois.')
        
        return cleaned_data


class CardUpdateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description']
        label = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
