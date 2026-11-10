from django.core.exceptions import ValidationError
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
    IMAGES_CHIENS = [
        ("images/chien1.avif", "Chien 1"),
        ("images/chien2.jpg", "Chien 2"),
        ("images/chien3.jpg", "Chien 3"),
        ("images/chien4.jpg", "Chien 4"),
        ("images/chien5.jpg", "Chien 5"),
        ("images/chien6.jpg", "Chien 6"),
    ]
    IMAGES_CHATS = [
        ("images/car1.jpg", "Chat 1 (car1.jpg)"),
        ("images/cat2.jpg", "Chat 2"),
        ("images/cat3.webp", "Chat 3"),
        ("images/cat4.webp", "Chat 4"),
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
        "situation", max_length=20, choices=SITUATIONS, default="abandonne"
    )
    disponible = models.BooleanField("disponible à l'adoption", default=True)

    class Meta:
        ordering = ["nom"]
        verbose_name = "animal"
        verbose_name_plural = "animaux"

    def __str__(self):
        return self.nom

    def clean(self):
        super().clean()
        images_par_espece = {
            "chien": {image for image, _ in self.IMAGES_CHIENS},
            "chat": {image for image, _ in self.IMAGES_CHATS},
        }
        if self.image and self.espece in images_par_espece:
            if self.image not in images_par_espece[self.espece]:
                raise ValidationError(
                    {"image": "Choisis une photo correspondant à l'espèce."}
                )

    def get_absolute_url(self):
        return reverse("blog:animal_detail", args=[self.pk])
