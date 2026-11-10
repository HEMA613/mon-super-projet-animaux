from django.test import TestCase
from django.urls import reverse

from .models import Animal


class AnimalTests(TestCase):
    def creer_animal(self, **overrides):
        donnees = {
            "nom": "Rio",
            "espece": "chien",
            "taille": "Moyenne",
            "couleur": "Doré",
            "race": "Golden Retriever",
            "sexe": "male",
        }
        donnees.update(overrides)
        if "image" not in donnees:
            donnees["image"] = (
                "images/cat2.jpg"
                if donnees["espece"] == "chat"
                else "images/chien1.avif"
            )
        return Animal.objects.create(**donnees)

    def test_animal_disponible_visible(self):
        self.creer_animal()
        response = self.client.get(reverse("blog:animal_list"))
        self.assertContains(response, "Rio")

    def test_carte_affiche_la_photo_associee(self):
        self.creer_animal(
            nom="Mina",
            espece="chat",
            sexe="femelle",
            image="images/cat2.jpg",
        )

        response = self.client.get(reverse("blog:animal_list"))

        self.assertContains(response, 'src="/static/images/cat2.jpg"')

    def test_fiche_affiche_les_caracteristiques_de_l_animal(self):
        animal = self.creer_animal()

        response = self.client.get(
            reverse("blog:animal_detail", args=[animal.pk])
        )

        self.assertContains(response, "Golden Retriever")
        self.assertContains(response, "Moyenne")
        self.assertContains(response, "Doré")
        self.assertContains(response, "Mâle")
        self.assertContains(response, 'src="/static/images/chien1.avif"')

    def test_espece_non_pris_en_charge_non_visible(self):
        self.creer_animal(nom="Pistache", espece="nac")
        response = self.client.get(reverse("blog:animal_list"))

        self.assertContains(response, "Rio")
        self.assertNotContains(response, "Pistache")

    def test_animal_deja_adopte_cache(self):
        self.creer_animal(
            nom="Ghost",
            espece="chat",
            sexe="femelle",
            disponible=False,
        )
        response = self.client.get(reverse("blog:accueil"))
        self.assertNotContains(response, "Ghost")

    def test_filtre_par_situation(self):
        self.creer_animal(nom="Rio", situation="abandonne")
        self.creer_animal(nom="Mina", espece="chat", situation="cession")

        response = self.client.get(
            reverse("blog:animal_list"), {"situation": "cession"}
        )

        self.assertContains(response, "Mina")
        self.assertNotContains(response, "Rio")

    def test_proprietaire_peut_proposer_un_animal(self):
        response = self.client.post(
            reverse("blog:proposer_animal"),
            {
                "nom": "Mina",
                "espece": "chat",
                "taille": "Petite",
                "couleur": "Grise",
                "race": "Européen",
                "sexe": "femelle",
                "image": "images/cat2.jpg",
                "situation": "cession",
            },
        )

        animal = Animal.objects.get(nom="Mina")
        self.assertRedirects(
            response, reverse("blog:animal_detail", args=[animal.pk])
        )
        self.assertEqual(animal.situation, "cession")
        self.assertEqual(animal.image, "images/cat2.jpg")

    def test_formulaire_refuse_une_espece_non_autorisee(self):
        nombre_animaux = Animal.objects.count()
        response = self.client.post(
            reverse("blog:proposer_animal"),
            {
                "nom": "Pistache",
                "espece": "nac",
                "taille": "Petite",
                "couleur": "Blanche",
                "race": "Lapin",
                "sexe": "male",
                "situation": "abandonne",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Animal.objects.count(), nombre_animaux)

    def test_formulaire_refuse_une_annonce_sans_image(self):
        response = self.client.post(
            reverse("blog:proposer_animal"),
            {
                "nom": "Mina",
                "espece": "chat",
                "taille": "Petite",
                "couleur": "Grise",
                "race": "Européen",
                "sexe": "femelle",
                "situation": "cession",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Animal.objects.filter(nom="Mina").exists())

    def test_formulaire_refuse_une_image_d_une_autre_espece(self):
        response = self.client.post(
            reverse("blog:proposer_animal"),
            {
                "nom": "Mina",
                "espece": "chat",
                "taille": "Petite",
                "couleur": "Grise",
                "race": "Européen",
                "sexe": "femelle",
                "image": "images/chien1.avif",
                "situation": "cession",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Animal.objects.filter(nom="Mina").exists())
