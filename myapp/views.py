from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Category,Card
from .form import CategoryCreationForm, CustomAuthenticationForm, CustomUserCreationForm, UserCreationForm, CardCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        print (request.POST)
        form = CustomAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accueil')
        else:
            print("OUINNNN")
            print(form.get_invalid_login_error())
            messages.error(request, 'Le nom d\'utilisateur ou le mot de passe est incorrect.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

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


@login_required
def edit_categorie(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        if 'delete_category' in request.POST:
            category_id = request.POST.get('delete_category')
            Category.objects.filter(id=category_id).delete()
        else:
            for category in categories:
                checked = request.POST.get(category.name) == 'true'
                category.enabled = checked
                category.save()

        if 'save_and_return' in request.POST:
            return redirect('accueil')

    return render(request, 'edit_categorie.html', {'categories': categories})

@login_required
def vignette(request, category_id):
    category = Category.objects.get(id=category_id)
    cards = Card.objects.filter(category=category, deleted=False)
    return render(request, 'vignette.html', {'category': category, 'cards': cards})

@login_required
def create_card(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CardCreationForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.category = category
            card.owner = request.user
            card.save()
            return redirect('vignette', category_id=category.id)
    else:
        form = CardCreationForm()
    return render(request, 'form_vignette.html', {'form': form, 'category': category})