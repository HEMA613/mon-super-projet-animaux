from django import forms

from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ["auteur", "texte"]
        widgets = {"texte": forms.Textarea(attrs={"rows": 3})}
