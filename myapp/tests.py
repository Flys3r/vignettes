from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class SignUpTests(TestCase):
    def test_sign_up_page_exists(self):
        # Vérifie si la page d'inscription existe et renvoie un code de statut 200
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_form(self):
        # Vérifie si le formulaire d'inscription est valide
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après inscription réussie

        # Vérifie si l'utilisateur a été créé dans la base de données
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_sign_up_form_invalid(self):
        # Vérifie si le formulaire d'inscription est invalide lorsque les mots de passe ne correspondent pas
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'differentpassword'
        })
        self.assertEqual(response.status_code, 200)  # Page de réinscription (formulaire invalide)

        # Vérifie si l'utilisateur n'a pas été créé dans la base de données
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_sign_up_duplicate_username(self):
        # Vérifie si le formulaire d'inscription échoue lorsque le nom d'utilisateur est déjà pris
        User.objects.create_user(username='testuser', password='testpassword123')
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',  # Nom d'utilisateur déjà pris
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)  # Page de réinscription (nom d'utilisateur déjà pris)

        # Vérifie si l'utilisateur n'a pas été créé dans la base de données
        self.assertFalse(User.objects.filter(username='testuser',).count() > 1)
