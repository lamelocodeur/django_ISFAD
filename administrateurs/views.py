from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from etudiants.models import Etudiant


# Create your views here.

def dashboard(request):
    administrateur=request.user
    total_etudiant=Etudiant.objects.count()
    return render(request,"administrateurs/general.html",{"administrateur":administrateur,"total":total_etudiant})

def espace_admin(request):
    return render(request, "administrateurs/espace_admin.html")

def utilisateurs(request):
    administrateur = request.user
    etudiants = Etudiant.objects.all()
    return render(request, "administrateurs/utilisateurs.html",{"administrateur":administrateur,"etudiants":etudiants})

def personnalisation(request):
    administrateur = request.user
    etudiants = Etudiant.objects.all()
    return render(request, "administrateurs/personnalisation_admin.html",{"administrateur":administrateur,"etudiants":etudiants})

@login_required(login_url='page')
@require_POST
def deconnexion(request):
    logout(request)
    return redirect('page')