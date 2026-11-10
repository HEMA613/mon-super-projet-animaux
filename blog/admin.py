from django.contrib import admin

from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = [
        "nom",
        "espece",
        "taille",
        "couleur",
        "race",
        "sexe",
        "situation",
        "disponible",
    ]
    list_filter = ["espece", "sexe", "situation", "disponible"]
    list_editable = ["disponible"]
    search_fields = ["nom", "race", "couleur"]
