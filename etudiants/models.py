from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Etudiant(AbstractUser):
    Roles = [
        ('super', 'Super administrateur'),
        ('admin', 'Administrateur'),
        ('prof', 'Prof'),
        ('etud', 'Etudiant')]

    Departements = [
        ('L1', 'Licence 1'),
        ('L2', 'Licence 2'),
        ('L3', 'Licence 3')]
    Licences = [
        ('L1', 'Licence 1'),
        ('L2', 'Licence 2'),
        ('L3', 'Licence 3')]
    Groupes = [
        ('A', 'Groupe A'),
        ('B', 'Groupe B'),
        ('C', 'Groupe C')]

    departement = models.CharField(max_length=100, choices=Departements)
    licence = models.CharField(max_length=2, choices=Licences)
    groupe = models.CharField(max_length=1, choices=Groupes)
    matricule = models.CharField(max_length=50, unique=True)
    date_inscription = models.DateField(auto_now_add=True)
    role = models.CharField(choices=Roles)




    def __str__(self):
        return self.username

