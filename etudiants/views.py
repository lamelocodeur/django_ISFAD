from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import Connexion, Inscription


#gestion dauthentification
def connexion(request):
    if request.method == "POST":
        form = Connexion(request.POST)
        if form.is_valid():
            matricule = form.cleaned_data.get("matricule")
            password = form.cleaned_data.get("password")
            role_form = form.cleaned_data.get("role")

            User = get_user_model()
            try:
                user_obj = User.objects.get(matricule=matricule)
            except User.DoesNotExist:
                messages.error(request, "Matricule ou mot de passe incorrect.")
                return render(request, "etudiants/connexion.html", {"form": form})

            # Vérifier que le rôle saisi correspond au rôle en base
            if user_obj.role != role_form:
                messages.error(request, "Le rôle sélectionné ne correspond pas à cet utilisateur.")
                return render(request, "etudiants/connexion.html", {"form": form})

            # Authentifier par username (car authenticate attend username)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)

                # Redirection selon le rôle choisi dans le formulaire
                if role_form == 'prof':
                    return redirect('accueil')
                elif role_form == 'admin':
                    return redirect('accueil_admin')
                elif role_form == 'super':
                    return redirect('accueil')
                else:
                    return redirect('accueil')
            else:
                messages.error(request, "Matricule ou mot de passe incorrect.")
    else:
        form = Connexion()
    return render(request, "etudiants/connexion.html", {"form": form})

def inscription(request):
    if request.method == "POST":
        form = Inscription(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Par exemple, utiliser matricule comme username
            user.username = user.matricule

            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("connexion")
        else:
            messages.error(request, "Erreur lors de l'inscription.")
    else:
        form = Inscription()
    return render(request, "etudiants/inscription.html", {"form": form})

def deconnexion(request):
    logout(request)
    return redirect('page')


#gestion des pages
def page(request):
    return render(request,"etudiants/page.html")

def accueil(request):
    return render(request,"etudiants/accueil.html")

def licence(request):
    return render(request, 'etudiants/choix_licence.html')

def cours(request):
    return render(request,"etudiants/choix_cours.html")

def section(request):
    return render(request,"etudiants/section_cours.html",)

def evaluation(request):
    return render(request,"etudiants/eval.html")

def faire_test(request):
    return render(request,"etudiants/faire_test.html")

def espace_etud(request):
    return render(request,"etudiants/espace_etudiants.html")

def chat(request):
    return render(request,"etudiants/chat.html")
@login_required(login_url='connexion')
def profil(request):
    return render(request,"etudiants/profil.html")

def parametres(request):
    return render(request,"etudiants/parametres.html")

def modifier_compte(request):
    return render(request,"etudiants/modifier_compte.html")


