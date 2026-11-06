from django.test import TestCase
from django.urls import reverse

from .models import Article


class ArticleTests(TestCase):
    def test_article_publie_visible_sur_l_accueil(self):
        Article.objects.create(titre="Premier article", contenu="Bonjour")
        response = self.client.get(reverse("blog:article_list"))
        self.assertContains(response, "Premier article")

    def test_article_brouillon_cache(self):
        Article.objects.create(titre="Brouillon", contenu="...", publie=False)
        response = self.client.get(reverse("blog:article_list"))
        self.assertNotContains(response, "Brouillon")
