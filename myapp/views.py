from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Category,Card
from .form import CardUpdateForm,CategoryCreationForm, CustomAuthenticationForm, CustomUserCreationForm, UserCreationForm, CardCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import login

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('accueil')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accueil')
        else:
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


def vignette(request, category_id):
    category = Category.objects.get(id=category_id)
    cards = Card.objects.filter(category=category, deleted=False)
    return render(request, 'vignette.html', {'category': category, 'cards': cards})


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from django.contrib.auth.models import User

def create_card(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CardCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                card = form.save(commit=False)
                card.category = category
                card.owner = request.user
                card.save()
            else:
                try:
                    anonymous_user = User.objects.get(username='anonymous')
                except User.DoesNotExist:
                    # Si l'utilisateur "anonymous" n'existe pas, créez-le
                    anonymous_user = User.objects.create_user(username='anonymous', password='password')
                card = form.save(commit=False)
                card.category = category
                card.owner_id = anonymous_user.id  # Assigner l'ID de l'utilisateur "anonymous"
                card.save()
                
            return redirect('vignette', category_id=category.id)
    else:
        form = CardCreationForm()
    return render(request, 'form_vignette.html', {'form': form, 'category': category})


from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST

@require_POST
def delete_card(request, card_id):
    try:
        card = Card.objects.get(id=card_id)
        card.delete()
        messages.success(request, 'Carte supprimée avec succès.')
    except Card.DoesNotExist:
        messages.error(request, 'Carte introuvable.')
    return redirect('vignette', category_id=card.category.id)


def update_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    
    if request.method == 'POST':
        form = CardUpdateForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carte mise à jour avec succès.')
            return redirect('vignette', category_id=card.category.id)
    else:
        form = CardUpdateForm(instance=card)
        
    return render(request, 'edit_vignette.html', {'form': form, 'card': card})