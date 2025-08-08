from django.urls import path

from cours import views
from etudiants.urls import urlpatterns

# gestion cours
urlpatterns=[
    path("ajouter_lecon" ,views.ajouter_lecon ,name='ajouter_cours'),
    path("liste_lecon" ,views.liste_lecon ,name='afficher'),
    path("modifier_lecon" ,views.modifier_lecon ,name='ajouter_cours'),
    path("supprimer_lecon" ,views.supprimer_lecon ,name='afficher')
]