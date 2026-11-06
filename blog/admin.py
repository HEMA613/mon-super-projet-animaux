from django.contrib import admin

from .models import Article, Categorie, Commentaire


class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 0


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ["nom", "nb_articles"]
    search_fields = ["nom"]

    @admin.display(description="articles")
    def nb_articles(self, obj):
        return obj.articles.count()


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["titre", "categorie", "publie", "cree_le"]
    list_filter = ["publie", "categorie"]
    list_editable = ["publie"]
    search_fields = ["titre", "contenu"]
    inlines = [CommentaireInline]


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ["auteur", "article", "cree_le"]
    search_fields = ["auteur", "texte"]
