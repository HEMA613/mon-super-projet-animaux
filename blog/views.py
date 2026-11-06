from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentaireForm
from .models import Article, Categorie


def article_list(request):
    """Accueil : articles publies, avec recherche et filtre par categorie."""
    articles = Article.objects.filter(publie=True).select_related("categorie")

    recherche = request.GET.get("q", "").strip()
    if recherche:
        articles = articles.filter(titre__icontains=recherche)

    categorie = None
    categorie_id = request.GET.get("categorie")
    if categorie_id:
        categorie = get_object_or_404(Categorie, pk=categorie_id)
        articles = articles.filter(categorie=categorie)

    return render(
        request,
        "blog/article_list.html",
        {
            "articles": articles,
            "categories": Categorie.objects.all(),
            "categorie": categorie,
            "recherche": recherche,
        },
    )


def article_detail(request, pk):
    """Un article, ses commentaires et le formulaire pour en ajouter un."""
    article = get_object_or_404(Article, pk=pk, publie=True)

    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.save()
            messages.success(request, "Merci, ton commentaire est publié !")
            return redirect(article)
    else:
        form = CommentaireForm()

    return render(request, "blog/article_detail.html", {"article": article, "form": form})


def about(request):
    return render(request, "blog/about.html")
