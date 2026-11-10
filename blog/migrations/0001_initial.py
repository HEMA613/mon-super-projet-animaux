from django.db import migrations, models


def creer_animaux(apps, schema_editor):
    Animal = apps.get_model("blog", "Animal")
    Animal.objects.bulk_create(
        [
            Animal(
                nom="Rio",
                espece="chien",
                race="Golden Retriever",
                sexe="male",
                age="2 ans",
                ville="Lyon",
                description="Rio est calme en appartement et adore les longues balades au parc.",
            ),
            Animal(
                nom="Nala",
                espece="chat",
                race="Européen",
                sexe="femelle",
                age="3 ans",
                ville="Paris",
                description="Nala aime les genoux et les après-midis au soleil. Elle est déjà stérilisée.",
            ),
            Animal(
                nom="Maya",
                espece="chien",
                race="Berger australien",
                sexe="femelle",
                age="4 ans",
                ville="Bordeaux",
                description="Maya est sportive. Elle convient à une famille qui sort tous les jours.",
            ),
            Animal(
                nom="Oscar",
                espece="chat",
                race="Maine Coon",
                sexe="male",
                age="5 ans",
                ville="Lille",
                description="Oscar est sociable avec les enfants et les autres chats du refuge.",
            ),
            Animal(
                nom="Luna",
                espece="chien",
                race="Croisé labrador",
                sexe="femelle",
                age="8 mois",
                ville="Marseille",
                description="Luna apprend vite. Elle cherche une famille patiente pour ses premières balades.",
            ),
        ]
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nom", models.CharField(max_length=100, verbose_name="nom")),
                (
                    "espece",
                    models.CharField(
                        choices=[("chien", "Chien"), ("chat", "Chat")],
                        max_length=20,
                        verbose_name="espèce",
                    ),
                ),
                ("race", models.CharField(max_length=100, verbose_name="race")),
                (
                    "sexe",
                    models.CharField(
                        choices=[("male", "Mâle"), ("femelle", "Femelle")],
                        max_length=20,
                        verbose_name="sexe",
                    ),
                ),
                ("age", models.CharField(max_length=100, verbose_name="âge")),
                ("ville", models.CharField(max_length=100, verbose_name="ville")),
                ("description", models.TextField(verbose_name="description")),
                ("disponible", models.BooleanField(default=True, verbose_name="disponible à l'adoption")),
            ],
            options={
                "verbose_name": "animal",
                "verbose_name_plural": "animaux",
                "ordering": ["nom"],
            },
        ),
        migrations.RunPython(creer_animaux, migrations.RunPython.noop),
    ]
