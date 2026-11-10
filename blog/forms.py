"""Formulaire pour proposer un animal à l'adoption."""

from django import forms

from .models import Animal


class AnimalForm(forms.ModelForm):
    """Les champs affichés sur la page /proposer/."""

    class Meta:
        model = Animal
        fields = [
            "nom",
            "espece",
            "taille",
            "couleur",
            "race",
            "sexe",
            "image",
            "situation",
        ]
