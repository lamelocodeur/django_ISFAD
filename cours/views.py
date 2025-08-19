from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from cours.forms import Ajouter_lecon, EvaluationForm
from cours.models import Cours, Lecon, Evaluation


# Create your views here.



#gestion des lecon
def ajouter_lecon(request):
    if request.method == 'POST':
        form = Ajouter_lecon(request.POST,request.FILES)
        if form.is_valid():

            form.save()
            messages.success(request, "Enregistrement bien passé")
            return redirect('afficher')
        else:
            return render(request, 'cours/ajouter.html', {"form": form})
    else:
        form = Ajouter_lecon()
        return render(request, 'cours/ajouter.html', {"form": form})

def liste_lecon(request):
    lecon = Lecon.objects.all()
    print(f"Nombre de cours en base : {lecon.count()}")  #
    return render(request, 'cours/afficher.html', {'lecon': lecon})

def modifier_lecon(request,id):
    lecon = get_object_or_404(Lecon, pk=id)
    if request.method == 'POST':
        form = Ajouter_lecon(request.POST, instance=lecon)
        if form.is_valid():
            form.save()
            return redirect('liste')
    else:
        form = Ajouter_lecon(instance=lecon)
    return render(request, 'etudiants/modifier.html', {'form': form})

def supprimer_lecon(request, id):
    lecon = get_object_or_404(Lecon, pk=id)
    lecon.delete()
    return redirect('afficher')



#gestion des evaluations
def ajouter_evaluation(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enregistrement bien passé")
            return redirect('afficher_eval')
        else:
            return render(request, 'cours/ajouter_eval.html', {"form": form})
    else:
        form = EvaluationForm()
        return render(request, 'cours/ajouter_eval.html', {"form": form})

def liste_evaluation(request):
    evaluation = Evaluation.objects.all()
    print(f"Nombre de cours en base : {evaluation.count()}")  #
    return render(request, 'cours/afficher_eval.html', {'evaluation': evaluation})

def modifier_evaluation(request,id):
    evaluation = get_object_or_404(Evaluation, pk=id)
    if request.method == 'POST':
        form = EvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('afficher_eval')
    else:
        form = EvaluationForm(instance=evaluation)
    return render(request, 'etudiants/modifier_eval.html', {'form': form})

def supprimer_evaluation(request, id):
    evaluation = get_object_or_404(Evaluation, pk=id)
    evaluation.delete()
    return redirect('afficher_eval')

def quiz_data(request, eval_id):
    try:
        evaluation = Evaluation.objects.get(id=eval_id)
    except Evaluation.DoesNotExist:
        return JsonResponse([], safe=False)

    questions = evaluation.questions.all()
    data = []

    for q in questions:
        choices = list(q.choices.all())
        answers = [c.texte for c in choices]
        try:
            correct_index = next(i for i, c in enumerate(choices) if c.est_correcte)
        except StopIteration:
            correct_index = 0  # par défaut si aucune n’est correcte

        data.append({
            "question": q.question,
            "answers": answers,
            "correct": correct_index,
            "points": q.points
        })

    return JsonResponse(data, safe=False)