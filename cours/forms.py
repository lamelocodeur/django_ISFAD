from django import forms

from cours.models import Lecon


class Ajouter_lecon(forms.ModelForm):
    class Meta:
        model = Lecon
        fields = '__all__'