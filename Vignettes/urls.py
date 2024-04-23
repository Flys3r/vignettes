from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('accueil/', views.accueil, name='accueil'),
    path('categorie/', views.categorie, name='categorie'),
    path('edit_categorie/', views.edit_categorie, name='edit_categorie'),
]


