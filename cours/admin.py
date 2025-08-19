from django.contrib import admin

from cours.models import Lecon, Evaluation, Devoir, Choice,Question


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # nombre de réponses visibles par défaut

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nombre_essaie')
    inlines = [QuestionInline]

admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Lecon)
admin.site.register(Devoir)


