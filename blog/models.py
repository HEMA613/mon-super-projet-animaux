"""Le modèle Animal : une fiche d'adoption enregistrée en base."""

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Animal(models.Model):
    """Un chien ou un chat proposé à l'adoption."""

    # Listes de choix. Le premier mot est enregistré en base,
    # le second est le texte affiché à l'écran.
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

    # Chemins des photos, relatifs au dossier static/.
    # Les fichiers sont dans static/asset/.
    IMAGES_CHIENS = [
        ("asset/chien1.avif", "Chien 1"),
        ("asset/chien2.jpg", "Chien 2"),
        ("asset/chien3.jpg", "Chien 3"),
        ("asset/chien4.jpg", "Chien 4"),
        ("asset/chien5.jpg", "Chien 5"),
        ("asset/chien6.jpg", "Chien 6"),
    ]
    IMAGES_CHATS = [
        ("asset/car1.jpg", "Chat 1"),
        ("asset/cat2.jpg", "Chat 2"),
        ("asset/cat3.webp", "Chat 3"),
        ("asset/cat4.webp", "Chat 4"),
    ]
    IMAGES = [*IMAGES_CHIENS, *IMAGES_CHATS]

    nom = models.CharField("nom", max_length=100)
    espece = models.CharField("espèce", max_length=20, choices=ESPECES)
    taille = models.CharField("taille", max_length=50, default="Non renseignée")
    couleur = models.CharField("couleur", max_length=50, default="Non renseignée")
    race = models.CharField("race", max_length=100)
    sexe = models.CharField("sexe", max_length=20, choices=SEXES)
    image = models.CharField("image", max_length=100, choices=IMAGES)
    situation = models.CharField(
        "situation",
        max_length=20,
        choices=SITUATIONS,
        default="abandonne",
    )
    disponible = models.BooleanField("disponible à l'adoption", default=True)

    class Meta:
        ordering = ["nom"]
        verbose_name = "animal"
        verbose_name_plural = "animaux"

    def __str__(self):
        """Texte utilisé dans l'admin et les listes déroulantes."""
        return self.nom

    def clean(self):
        """Refuse une photo de chien sur un chat, et l'inverse."""
        super().clean()
        images_par_espece = {
            "chien": {chemin for chemin, _label in self.IMAGES_CHIENS},
            "chat": {chemin for chemin, _label in self.IMAGES_CHATS},
        }
        if self.image and self.espece in images_par_espece:
            if self.image not in images_par_espece[self.espece]:
                raise ValidationError(
                    {"image": "Choisis une photo correspondant à l'espèce."}
                )

    def get_absolute_url(self):
        """Adresse de la fiche de cet animal."""
        return reverse("blog:animal_detail", args=[self.pk])
