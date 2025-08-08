from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from cours.forms import Ajouter_lecon
from cours.models import Cours, Lecon

# Create your views here.



#gestion des lecon
def ajouter_lecon(request):
    if request.method == 'POST':
        form = Ajouter_lecon(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afficher')
        else:
            return render(request, 'cours/voir.html', {"form": form})
    else:
        form = Ajouter_lecon()
        return render(request, 'cours/voir.html', {"form": form})

def liste_lecon(request):
    lecon = Lecon.objects.all()
    print(f"Nombre de cours en base : {lecon.count()}")  # DEBUG
    return render(request, 'cours/voir.html', {'cours': lecon})

def modifier_lecon(request, id):
    lecon = get_object_or_404(Lecon, pk=id)
    if request.method == 'POST':
        form = Ajouter_lecon(request.POST, instance=lecon)
        if form.is_valid():
            form.save()
            return redirect('ajouter_cours')
    else:
        form = Ajouter_lecon(instance=lecon)
    return render(request, 'etudiants/modifier_lecon.html', {'form': form})

def supprimer_lecon(request, id):
    lecon = get_object_or_404(Lecon, pk=id)
    lecon.delete()
    return redirect('ajouter_cours')


