"""Deplace les photos de images/ vers le dossier static/asset."""

from django.db import migrations, models


ANCIEN_PREFIXE = "images/"
NOUVEAU_PREFIXE = "asset/"

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


def _remplacer_prefixe(apps, ancien, nouveau):
    """Met a jour le chemin enregistre pour chaque animal."""
    Animal = apps.get_model("blog", "Animal")
    for animal in Animal.objects.all().iterator():
        if animal.image.startswith(ancien):
            nouveau_chemin = nouveau + animal.image[len(ancien):]
            Animal.objects.filter(pk=animal.pk).update(image=nouveau_chemin)


def vers_dossier_asset(apps, schema_editor):
    _remplacer_prefixe(apps, ANCIEN_PREFIXE, NOUVEAU_PREFIXE)


def retour_dossier_images(apps, schema_editor):
    _remplacer_prefixe(apps, NOUVEAU_PREFIXE, ANCIEN_PREFIXE)


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_animal_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="image",
            field=models.CharField(
                choices=IMAGES,
                max_length=100,
                verbose_name="image",
            ),
        ),
        migrations.RunPython(vers_dossier_asset, retour_dossier_images),
    ]
