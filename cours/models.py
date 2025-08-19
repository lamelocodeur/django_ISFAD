from django.db import models
from datetime import date

from etudiants.models import Etudiant


# Create your models here.



class Cours(models.Model):
    MODULES = [
        ('premier', 'Module 1'),
        ('second', 'Module 2'),
    ]
    titre = models.CharField(max_length=200)
    nom_du_prof_charger = models.CharField(max_length=100)
    description = models.TextField()
    durer_cours = models.DateField()
    modules = models.CharField(max_length=10, choices=MODULES)
    progression = models.IntegerField(default=0)  # En pourcentage
    suivi = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

    class Meta:
        permissions = [
            ("peut_ajouter_cours", "Peut ajouter un cours"),
            ("peut_supprimer_cours", "Peut supprimer un cours"),
            ("peut_modifier_cours", "Peut modifier un cours"),
            ("peut_suivre_cours", "Peut suivre un cours"),
        ]

class Lecon(models.Model):
    prof = models.ForeignKey(Etudiant, on_delete=models.CASCADE,null=True, blank=True)
    titre = models.CharField(max_length=200)
    chapitre = models.CharField(max_length=10, choices=[("A","ab"),("B","bb")])
    video1 = models.FileField(upload_to='videos/', blank=True, null=True)
    video2 = models.FileField(upload_to='videos/', blank=True, null=True)
    pdf1=models.FileField(upload_to='pdfs/')
    pdf2=models.FileField(upload_to='pdfs/')
    description = models.TextField()
    lien_synchrone = models.URLField(blank=True, null=True)
    date_de_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} (Chapitre {self.chapitre})"

    class Meta:
        permissions = [
            ("peut_ajouter_lecon", "Peut ajouter une lecon"),
            ("peut_supprimer_lecon", "Peut supprimer une lecon"),
            ("peut_modifier_lecon", "Peut modifier une lecon"),
            ("peut_suivre_lecon", "Peut suivre une lecon"),
        ]

class Evaluation(models.Model):
    prof = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True)
    titre = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    statut = models.BooleanField(default=True)
    matiere = models.CharField(max_length=55)
    note = models.PositiveSmallIntegerField(default=0)
    nombre_essaie = models.PositiveSmallIntegerField(default=1)
    date_depot = models.DateField(auto_now_add=True)
    date_limite = models.DateField(default=date.today)
    questionnaires=models.TextField()

    def __str__(self):
        return self.titre

    @property
    def jours_restants(self):
        diff = (self.date_limite - date.today()).days
        return diff if diff > 0 else 0

class Question(models.Model):
    question = models.TextField()
    evaluation = models.ForeignKey('Evaluation', on_delete=models.CASCADE, related_name='questions')
    points = models.PositiveIntegerField(default=1)
    reponse = models.JSONField()

class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='choices')
    texte = models.CharField(max_length=200)
    est_correcte = models.BooleanField(default=False)

class Tentative(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Devoir(models.Model):
    prof = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    titre = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    statut = models.BooleanField(default=True)
    matiere = models.CharField(max_length=55)
    note = models.PositiveSmallIntegerField(default=0)
    fichier = models.FileField(upload_to="devoirs/", max_length=5000)
    date_depot = models.DateField(auto_now_add=True)
    date_limite = models.DateField(default=date.today)

    def __str__(self):
        return self.titre

    @property
    def jours_restants(self):
        jours_restant = (self.date_limite - date.today()).days
        return jours_restant if jours_restant > 0 else 0

