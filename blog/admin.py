"""Réglage de la page d'administration des animaux."""

from django.contrib import admin

from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    """Colonnes, filtres et recherche dans /admin/."""

    list_display = [
        "nom",
        "espece",
        "taille",
        "couleur",
        "race",
        "sexe",
        "image",
        "situation",
        "disponible",
    ]
    list_filter = ["espece", "sexe", "situation", "disponible"]
    list_editable = ["disponible"]
    search_fields = ["nom", "race", "couleur"]
