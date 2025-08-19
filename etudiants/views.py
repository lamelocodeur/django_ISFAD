from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from cours.forms import Ajouter_lecon
from cours.models import Lecon, Evaluation, Devoir
from .forms import Connexion, Inscription, ModifierCompte
from .models import Etudiant


#gestion dauthentification
def connexion(request):
    if request.method == "POST":
        form = Connexion(request.POST)
        if form.is_valid():
            matricule = form.cleaned_data.get("matricule")
            password = form.cleaned_data.get("password")
            role = form.cleaned_data.get("role")

            User = get_user_model()
            try:
                etudiant = Etudiant.objects.get(matricule=matricule)
            except Etudiant.DoesNotExist:
                messages.error(request, "Matricule ou mot de passe incorrect.")
                return render(request, "etudiants/connexion.html", {"form": form})
            if etudiant.role != role:
                messages.error(request, "Le rôle sélectionné ne correspond pas à cet utilisateur.")
                return render(request, "etudiants/connexion.html", {"form": form})
            user = authenticate(request, username=etudiant.username, password=password)
            if user is not None:
                login(request, user)
                # Redirection selon le rôle choisi dans le formulaire
                if role == 'prof':
                    return redirect('accueil')
                elif role == 'admin':
                    return redirect('dashboard')
                elif role == 'super':
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
            return render(request, "etudiants/inscription.html", {"form": form})
    else:
        form = Inscription()
    return render(request, "etudiants/inscription.html", {"form": form})
@login_required(login_url='page')
@require_POST
def deconnexion(request):
    logout(request)
    return redirect('page')
@login_required(login_url='connexion')
def modifier_compte(request):
    etudiant = request.user
    if etudiant.is_authenticated:
        if request.method == "POST":
            form = ModifierCompte(request.POST, request.FILES, instance=etudiant)
            if form.is_valid():
                form.save()
                return redirect("profil")
        else:
            form = ModifierCompte(instance=etudiant)
        return render(request, "etudiants/modifier_compte.html", {"form": form, "etudiant": etudiant})
    else:
        return redirect("deconnection")
#gestion des pages
def page(request):
    return render(request,"etudiants/page.html")
@login_required(login_url='connexion')
def accueil(request):
    return render(request,"etudiants/accueil.html")
@login_required(login_url='connexion')
def licence(request):
    etudiant=Etudiant.objects.get(matricule=request.user.matricule)
    return render(request, 'etudiants/choix_licence.html',{"etudiant":etudiant})
@login_required(login_url='connexion')
def cours(request):
    if request.user.role == "etud":
        return render(request,"etudiants/choix_cours.html")
    else:
        return render(request,"etudiants/section_cours.html")
@login_required(login_url='connexion')
def section(request):
    etudiant = request.user
    lecon=Lecon.objects.all()
    total_lecon=Lecon.objects.count()
    form=Ajouter_lecon()
    return render(request,"etudiants/section_cours.html",{'etudiant':etudiant,'form': form,"lecons":lecon,"total":total_lecon})
@login_required(login_url='connexion')
def evaluation(request):
    etudiant=Etudiant.objects.all()
    evaluation=Evaluation.objects.all()
    devoir=Devoir.objects.all()
    return render(request,"etudiants/eval.html",{"etudiant":etudiant,"evaluation":evaluation,"devoir":devoir})
@login_required(login_url='connexion')
def faire_test(request):
    return render(request,"etudiants/faire_test.html")
@login_required(login_url='connexion')
def espace_etud(request):
    return render(request,"etudiants/espace_etudiants.html")
@login_required(login_url='connexion')
def chat(request):
    return render(request,"etudiants/chat.html")
@login_required(login_url='connexion')
def profil(request):
    etudiant=request.user
    return render(request,"etudiants/profil.html",{"etudiant":etudiant})
@login_required(login_url='connexion')
def parametres(request):
    return render(request,"etudiants/parametres.html")



