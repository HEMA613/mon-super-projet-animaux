from django.db import models
from django.urls import reverse


class Animal(models.Model):
    """Représente un animal proposé à l'adoption."""

    ESPECES = [
        ("chien", "Chien"),
        ("chat", "Chat"),
    ]
    SEXES = [
        ("male", "Mâle"),
        ("femelle", "Femelle"),
    ]
    SITUATIONS = [
        ("abandonne", "Animal abandonné"),
        ("cession", "Proposé par son propriétaire"),
    ]

    nom = models.CharField("nom", max_length=100)
    espece = models.CharField("espèce", max_length=20, choices=ESPECES)
    taille = models.CharField("taille", max_length=50, default="Non renseignée")
    couleur = models.CharField("couleur", max_length=50, default="Non renseignée")
    race = models.CharField("race", max_length=100)
    sexe = models.CharField("sexe", max_length=20, choices=SEXES)
    situation = models.CharField(
        "situation", max_length=20, choices=SITUATIONS, default="abandonne"
    )
    disponible = models.BooleanField("disponible à l'adoption", default=True)

    class Meta:
        ordering = ["nom"]
        verbose_name = "animal"
        verbose_name_plural = "animaux"

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("blog:animal_detail", args=[self.pk])
