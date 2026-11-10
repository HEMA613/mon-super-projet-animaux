from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AnimalForm
from .models import Animal


def _filtrer_animaux(request):
    """Animaux disponibles, filtrés par recherche et par espèce."""
    animaux = Animal.objects.filter(
        disponible=True, espece__in=dict(Animal.ESPECES)
    )
    recherche = request.GET.get("q", "").strip()
    if recherche:
        animaux = animaux.filter(
            Q(nom__icontains=recherche)
            | Q(race__icontains=recherche)
            | Q(couleur__icontains=recherche)
        )

    espece = request.GET.get("espece", "")
    if espece not in dict(Animal.ESPECES):
        espece = ""
    if espece:
        animaux = animaux.filter(espece=espece)

    situation = request.GET.get("situation", "")
    if situation not in dict(Animal.SITUATIONS):
        situation = ""
    if situation:
        animaux = animaux.filter(situation=situation)

    return animaux, recherche, espece, situation


def accueil(request):
    """Page d'accueil : promesse du site et quelques animaux à adopter."""
    animaux = Animal.objects.filter(
        disponible=True, espece__in=dict(Animal.ESPECES)
    )[:6]
    return render(request, "blog/accueil.html", {"animaux": animaux})


def animal_list(request):
    """Toutes les annonces, avec recherche et filtres."""
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
    """Fiche d'un animal disponible."""
    animal = get_object_or_404(
        Animal, pk=pk, disponible=True, espece__in=dict(Animal.ESPECES)
    )
    return render(request, "blog/animal_detail.html", {"animal": animal})


def proposer_animal(request):
    """Enregistre la proposition d'un animal par son propriétaire."""
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save()
            return redirect(animal)
    else:
        form = AnimalForm()

    return render(request, "blog/proposer_animal.html", {"form": form})


def comment_ca_marche(request):
    return render(request, "blog/comment_ca_marche.html")


def about(request):
    return render(request, "blog/about.html")
