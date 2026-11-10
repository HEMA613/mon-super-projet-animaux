"""Les pages du site : chaque fonction répond à une adresse."""

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AnimalForm
from .models import Animal


def _filtrer_animaux(request):
    """Garde les animaux disponibles, puis applique la recherche."""
    animaux = Animal.objects.filter(
        disponible=True,
        espece__in=dict(Animal.ESPECES),
    )

    # Le mot tapé dans la barre de recherche (nom, race ou couleur).
    recherche = request.GET.get("q", "").strip()
    if recherche:
        animaux = animaux.filter(
            Q(nom__icontains=recherche)
            | Q(race__icontains=recherche)
            | Q(couleur__icontains=recherche)
        )

    # Filtre espèce : on ignore une valeur qui n'est pas dans la liste.
    espece = request.GET.get("espece", "")
    if espece not in dict(Animal.ESPECES):
        espece = ""
    if espece:
        animaux = animaux.filter(espece=espece)

    # Filtre situation : abandonné ou proposé par le propriétaire.
    situation = request.GET.get("situation", "")
    if situation not in dict(Animal.SITUATIONS):
        situation = ""
    if situation:
        animaux = animaux.filter(situation=situation)

    return animaux, recherche, espece, situation


def accueil(request):
    """Page d'accueil : le message du site et 6 animaux."""
    animaux = Animal.objects.filter(
        disponible=True,
        espece__in=dict(Animal.ESPECES),
    )[:6]
    return render(request, "blog/accueil.html", {"animaux": animaux})


def animal_list(request):
    """Liste des annonces, avec recherche et filtres."""
    animaux, recherche, espece, situation = _filtrer_animaux(request)
    return render(
        request,
        "blog/animal_list.html",
        {
            "animaux": animaux,
            "recherche": recherche,
            "espece": espece,
            "especes": Animal.ESPECES,
            "situation": situation,
            "situations": Animal.SITUATIONS,
        },
    )


def animal_detail(request, pk):
    """Fiche d'un seul animal. pk est son numéro en base."""
    animal = get_object_or_404(
        Animal,
        pk=pk,
        disponible=True,
        espece__in=dict(Animal.ESPECES),
    )
    return render(request, "blog/animal_detail.html", {"animal": animal})


def proposer_animal(request):
    """Formulaire pour ajouter un animal.

    GET  : on affiche le formulaire vide.
    POST : on enregistre si les champs sont corrects.
    """
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save()
            return redirect(animal)
    else:
        form = AnimalForm()

    return render(request, "blog/proposer_animal.html", {"form": form})


def comment_ca_marche(request):
    """Page qui explique les 3 étapes."""
    return render(request, "blog/comment_ca_marche.html")


def about(request):
    """Page à propos du site."""
    return render(request, "blog/about.html")
