# Mon blog Django

Projet Django classique : l'application `blog` (articles, categories, commentaires) et l'admin.

## Dans Async Classroom

Clique sur **Executer** : l'apercu installe Django, applique les migrations et ouvre le site.
L'administration est sur `/admin/` (identifiant `admin`, mot de passe `admin`).

## Sur ta machine

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Le site est alors sur http://127.0.0.1:8000 et l'admin sur http://127.0.0.1:8000/admin/.

## Ou modifier quoi

- `blog/models.py` : les tables de la base (apres un changement : `makemigrations` puis `migrate`)
- `blog/admin.py` : ce que l'admin affiche
- `blog/views.py` et `blog/urls.py` : les pages du site
- `blog/templates/blog/` et `templates/base.html` : le HTML
- `static/css/style.css` : le style
# mon-super-projet-animaux
