"""Adresses des pages de l'application blog."""

from django.urls import path

from . import views

# Le préfixe "blog:" sert dans les templates : {% url 'blog:accueil' %}
app_name = "blog"

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("adopter/", views.animal_list, name="animal_list"),
    path("adopter/<int:pk>/", views.animal_detail, name="animal_detail"),
    path("proposer/", views.proposer_animal, name="proposer_animal"),
    path(
        "comment-ca-marche/",
        views.comment_ca_marche,
        name="comment_ca_marche",
    ),
    path("a-propos/", views.about, name="about"),
]
