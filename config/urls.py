"""
Routes du projet : l'admin de Django et les pages de l'application blog.

Documentation : https://docs.djangoproject.com/fr/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]
