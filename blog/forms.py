from django import forms

from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "nom",
            "espece",
            "taille",
            "couleur",
            "race",
            "sexe",
            "situation",
        ]
