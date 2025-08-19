from django.urls import path

from administrateurs import views

urlpatterns=[
    path("", views.dashboard, name="dashboard"),
    path("espace/", views.espace_admin, name="admin"),
    path("utilisateur/", views.utilisateurs, name="utilisateurs"),
    path("deconnection/",views.deconnexion,name="deconnection"),
    path("personnalisation/", views.personnalisation, name="personnalisation"),

]