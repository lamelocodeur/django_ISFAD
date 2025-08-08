from django.contrib.auth.backends import ModelBackend
from .models import Etudiant

class MatriculeBackend(ModelBackend):
    def authenticate(self, request, matricule=None, password=None, **kwargs):
        try:
            user = Etudiant.objects.get(matricule=matricule)
            if user.check_password(password):
                return user
        except Etudiant.DoesNotExist:
            return None
