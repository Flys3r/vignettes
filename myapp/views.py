from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Category
from .form import CategoryCreationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = UserCreationForm()
    return render(request, 'inscription.html', {'form': form})

from django.contrib import messages


def connexion(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')  
        else:
            messages.error(request, 'Le nom d\'utilisateur ou le mot de passe est incorrect.')
            return render(request, 'connexion.html') 
    else:
        return render(request, 'connexion.html')


def accueil(request):
    categories_actives = Category.objects.filter(enabled=True)
    return render(request, 'accueil.html', {'categories_actives': categories_actives})


def categorie(request):
    if request.method == 'POST':
        form = CategoryCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = CategoryCreationForm()
    return render(request, 'form_categorie.html', {'form': form})
