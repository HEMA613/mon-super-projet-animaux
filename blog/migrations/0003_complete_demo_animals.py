from django.db import migrations


def mettre_a_jour_animaux_demo(apps, schema_editor):
    Animal = apps.get_model("blog", "Animal")
    animaux_demo = {
        "Rio": ("chien", "Golden Retriever", "Grande", "Doré"),
        "Nala": ("chat", "Européen", "Petite", "Tigrée"),
        "Maya": ("chien", "Berger australien", "Moyenne", "Tricolore"),
        "Oscar": ("chat", "Maine Coon", "Grande", "Gris"),
        "Luna": ("chien", "Croisé labrador", "Moyenne", "Sable"),
    }

    for nom, (espece, race, taille, couleur) in animaux_demo.items():
        Animal.objects.filter(
            nom=nom,
            espece=espece,
            race=race,
        ).update(taille=taille, couleur=couleur)

    Animal.objects.filter(
        nom="Pistache",
        espece="nac",
        race="Lapin nain",
    ).update(disponible=False)


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_remove_animal_age_remove_animal_description_and_more"),
    ]

    operations = [
        migrations.RunPython(
            mettre_a_jour_animaux_demo,
            migrations.RunPython.noop,
        ),
    ]
