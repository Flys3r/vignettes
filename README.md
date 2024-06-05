# Vignette

## Contexte
Au sein de votre école, il arrive de réaliser des maquettes, des projets graphiques ou visuels. Souhaitant promouvoir les travaux ainsi réalisés par vos proches, votre formateur vous demande de réaliser un site web. 

L'idée est de réaliser un site avec une rapide ressemblance à Pinterest. C'est-à-dire, une application où sont affichés de nombreux médias filtrables par catégories. Les noms des élèves ne seront pas affichés, mais uniquement un mystérieux chiffre dont le détenteur est le créateur de l'œuvre.

## Installation

Pour installer et configurer ce projet sur votre machine locale, suivez les étapes ci-dessous :

1. Clonez ce dépôt sur votre machine locale :
    ```sh
    git clone <url-du-dépôt>
    cd vignette
    ```

2. Installez les dépendances requises :
    ```sh
    pip install django
    pip install mysqlclient
    pip install Pillow
    pip install argon2-cffi
    ```

3. Assurez-vous que `pip` est à jour :
    ```sh
    python.exe -m pip install --upgrade pip
    ```

4. Configurez votre base de données. Modifiez le fichier `settings.py` pour ajouter les détails de votre base de données MySQL.

5. Appliquez les migrations pour configurer la base de données :
    ```sh
    python manage.py migrate
    ```

6. Exécutez le serveur de développement :
    ```sh
    python manage.py runserver
    ```

7. Accédez à l'application web en ouvrant votre navigateur et en naviguant à l'adresse suivante :
    ```
    http://127.0.0.1:8000/
    ```


## Utilisation

1. Pour créer un nouvel utilisateur, vous pouvez utiliser l'interface d'administration de Django :
    ```
    http://127.0.0.1:8000/admin/
    ```

2. Connectez-vous en tant qu'administrateur et commencez à ajouter des catégories, des vignettes, etc.

3. Les images et autres fichiers média téléchargés seront stockés dans le répertoire `media` et affichés sur le site web.

## Fonctionnalités

- Ajout de catégories pour organiser les vignettes.
- Création de vignettes avec des images, des descriptions et des fichiers multimédia (musique, vidéos).
- Affichage des vignettes filtrables par catégories.
- Chaque vignette affiche un chiffre mystérieux au lieu du nom de l'élève créateur.

## Auteurs

- Flys3r
