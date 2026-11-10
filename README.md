# Super Animaux

Super Animaux est une petite application Django pour consulter des chiens et des chats
proposés à l'adoption, ou ajouter un animal à la liste.

Chaque annonce enregistre le nom, l'espèce, la taille, la couleur, la race et le sexe.
Elle précise aussi si l'animal est abandonné ou proposé par son propriétaire.
Les annonces sont enregistrées dans la base SQLite du projet.

## Fonctionnalités

- `/` : accueil et aperçu des animaux disponibles
- `/adopter/` : consulter et filtrer les annonces par espèce, situation ou recherche
- `/adopter/<numéro>/` : consulter la fiche d'un animal
- `/proposer/` : enregistrer une annonce pour un chien ou un chat
- `/admin/` : gérer les animaux avec l'administration Django

Les annonces proposées depuis le formulaire sont publiées directement. Pour retirer une
annonce, l'administrateur peut décocher « disponible à l'adoption » dans l'administration.

## Installation sur Windows

Dans PowerShell, depuis le dossier du projet :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r templates/requirements.txt
python manage.py migrate
python manage.py runserver
```

Le site sera disponible sur http://127.0.0.1:8000. Pour ouvrir l'administration,
crée un compte administrateur dans un autre terminal avec :

```powershell
python manage.py createsuperuser
```

Puis connecte-toi sur http://127.0.0.1:8000/admin/.

## Installation sur macOS ou Linux

Depuis le dossier du projet :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r templates/requirements.txt
python manage.py migrate
python manage.py runserver
```

Pour créer un compte administrateur, lance `python manage.py createsuperuser`, puis
connecte-toi sur http://127.0.0.1:8000/admin/.

## Tests

Pour lancer les tests de l'application :

```bash
python manage.py test blog
```

## Organisation du code

- `blog/models.py` : modèle `Animal` et champs enregistrés en base
- `blog/forms.py` : formulaire de création d'une annonce
- `blog/views.py` et `blog/urls.py` : logique des pages et adresses du site
- `blog/templates/blog/` : pages HTML de l'application
- `templates/base.html` : structure commune des pages
- `static/css/style.css` : mise en forme
- `blog/admin.py` : affichage et gestion des animaux dans l'administration
- `blog/migrations/` : évolutions de la structure de la base de données
- `templates/requirements.txt` : dépendances Python du projet

Les classes utilisent le PascalCase. Les fonctions, variables et champs suivent le
`snake_case`, conformément aux conventions PEP 8.

Après une modification d'un modèle, crée une migration avec
`python manage.py makemigrations`, puis applique-la avec `python manage.py migrate`.
