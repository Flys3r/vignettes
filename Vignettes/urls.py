from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('accueil/', views.accueil, name='accueil'),
    path('categorie/', views.categorie, name='categorie'),
    path('edit_categorie/', views.edit_categorie, name='edit_categorie'),
    path('vignette/<int:category_id>/', views.vignette, name='vignette'),
    path('create_card/<int:category_id>/', views.create_card, name='create_card'),
]


