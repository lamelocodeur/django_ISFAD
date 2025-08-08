from django.db import models

# Create your models here.



class Cours(models.Model):
    modules=[
        ('premier', 'Module 1'),
        ('Second', 'module 2'),
    ]
    titre = models.CharField(max_length=200)
    nom_du_prof_charger=models.CharField()
    description = models.TextField()
    durer_cours = models.DateField()
    modules=models.CharField(choices=modules)
    progression = models.IntegerField(default=0)  # En pourcentage
    lien_synchrone = models.URLField(blank=True, null=True)
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

    titre = models.CharField(max_length=200)
    chapitre = models.CharField(choices=[("A","ab"),("B","bb")])
    description = models.TextField()
    lien_synchrone = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titre


    class Meta:
        permissions = [
            ("peut_ajouter_lecon", "Peut ajouter une lecon"),
            ("peut_supprimer_lecon", "Peut supprimer une lecon"),
            ("peut_modifier_lecon", "Peut modifier une lecon"),
            ("peut_suivre_lecon", "Peut suivre une lecon"),
        ]
