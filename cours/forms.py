from django import forms

from cours.models import Lecon,Evaluation,Devoir


class Ajouter_lecon(forms.ModelForm):
    class Meta:
        model=Lecon
        fields=["titre","chapitre","video1","video2","pdf1","pdf2","description","lien_synchrone"]

class EvaluationForm(forms.ModelForm):
    class Meta:
        model=Evaluation
        fields=["titre","description","matiere","nombre_essaie","date_limite"]

class DevoirForm(forms.ModelForm):
    class Meta:
        model=Devoir
        fields=["titre","description","matiere","fichier","date_limite"]
