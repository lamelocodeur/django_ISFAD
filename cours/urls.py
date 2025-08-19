from django.urls import path

from cours import views

# gestion des lecons
urlpatterns=[
    path("ajouter/",views.ajouter_lecon ,name='ajouter'),
    path("liste/",views.liste_lecon ,name='afficher'),
    path("modifier/<int:id>" ,views.modifier_lecon ,name='modifier'),
    path("supprimer/<int:id>" ,views.supprimer_lecon ,name='supprimer'),


# gestion des evaluations
path('quiz-data/<int:eval_id>/', views.quiz_data, name='quiz_data'),
    path("ajouter_eval/", views.ajouter_evaluation, name='ajouter_eval'),
    path("liste_eval/", views.liste_evaluation, name='afficher_eval'),
    path("modifier_eval/<int:id>", views.modifier_evaluation, name='modifier_eval'),
    path("supprimer_eval/<int:id>", views.supprimer_evaluation, name='supprimer_eval')

]