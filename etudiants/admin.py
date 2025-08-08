from django.contrib import admin

from etudiants.models import Etudiant


admin.site.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'matricule', 'date_inscription')
    search_fields = ('nom', 'email', 'matricule')
    list_filter = ('date_inscription',)
    filter_horizontal = ('licence','groupe')



