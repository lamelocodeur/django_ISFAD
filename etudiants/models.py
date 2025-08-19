from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Etudiant(AbstractUser):
    Roles = [
        ('super', 'Super administrateurs'),
        ('admin', 'Administrateur'),
        ('prof', 'Prof'),
        ('etud', 'Etudiant')]

    Departements = [
        ('Economie', 'Economie'),
        ('Dev_comunautaire', 'Dev_comunautaire'),
        ('Droit', 'Droit'),
        ('Latice', 'Latice'),
        ('Divers', 'Divers'),
        ('Remforcement', 'Remforcement des capacités')]
    Licences = [
        ('L1', 'Licence 1'),
        ('L2', 'Licence 2'),
        ('L3', 'Licence 3')]
    Groupes = [
        ('A', 'Groupe A'),
        ('B', 'Groupe B')]

    departement = models.CharField(max_length=100, choices=Departements)
    licence = models.CharField(max_length=2, choices=Licences)
    groupe = models.CharField(max_length=1, choices=Groupes)
    matricule = models.CharField(max_length=50, unique=True)
    photo=models.ImageField()
    date_inscription = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=Roles)
    telephone=models.CharField(max_length=18)


