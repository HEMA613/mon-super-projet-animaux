from django.db import models
from django.urls import reverse


class Categorie(models.Model):
    nom = models.CharField("nom", max_length=100, unique=True)

    class Meta:
        ordering = ["nom"]
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField("titre", max_length=200)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name="catégorie",
    )
    contenu = models.TextField("contenu")
    publie = models.BooleanField("publié", default=True)
    cree_le = models.DateTimeField("créé le", auto_now_add=True)
    modifie_le = models.DateTimeField("modifié le", auto_now=True)

    class Meta:
        ordering = ["-cree_le"]

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("blog:article_detail", args=[self.pk])


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="commentaires")
    auteur = models.CharField("ton prénom", max_length=80)
    texte = models.TextField("commentaire")
    cree_le = models.DateTimeField("posté le", auto_now_add=True)

    class Meta:
        ordering = ["cree_le"]

    def __str__(self):
        return f"{self.auteur} sur « {self.article} »"
