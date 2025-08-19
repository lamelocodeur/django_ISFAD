from django import forms

from etudiants.models import Etudiant


class Connexion(forms.Form):
    matricule = forms.CharField(label="Matricule", max_length=50)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    Roles=[('super', 'Super administrateurs'),
        ('admin', 'Administrateur'),
        ('prof', 'Prof'),
        ('etud', 'Etudiant'),
    ]
    role = forms.ChoiceField(label="Rôle", choices=Roles)

class Inscription(forms.ModelForm):
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        required=True)
    first_name = forms.CharField(label="Prenom",required=True)
    last_name = forms.CharField(label="Nom",required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model=Etudiant
        fields=["first_name","last_name","matricule",'password',"email","departement","licence","groupe","role","telephone"]

class ModifierCompte(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ["last_name", "first_name", "email", "telephone","photo"]




