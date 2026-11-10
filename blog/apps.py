"""Configuration de l'application blog."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Nom affiché dans l'administration Django."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    verbose_name = "Animaux"
