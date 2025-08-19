from django.contrib.auth.views import LoginView, LogoutView

from . import views
from django.urls import path


urlpatterns=[
    path("",views.page,name="page"),
    path("accueil/",views.accueil,name="accueil"),
    path("licence/",views.licence,name="licence"),
    path("cours/",views.cours,name="choix_cours"),
    path("section/",views.section,name="section_cours"),
    path("evaluation/",views.evaluation,name="evaluation"),
    path("test/",views.faire_test,name="test"),
    path("espace_etud/",views.espace_etud,name="espace_etudiant"),
    path("chat/",views.chat,name="chat"),
    path("profil/",views.profil,name="profil"),
    path("parametres/",views.parametres,name="parametres"),
    path("chat/",views.chat,name="chat"),



    #partie connexion
    path("modifier_compte/",views.modifier_compte,name="modification_compte"),
    path("inscription/",views.inscription,name="inscription"),
    path("connexion/",views.connexion,name="connexion"),
    path("deconnection/",views.deconnexion,name="deconnection"),

]