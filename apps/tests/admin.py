from django.contrib import admin
from apps.tests.models import (
    Answer, Question, Test, FormForUser, 
    Adress, TestResult, OfflineRegistration

)


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(FormForUser)
class FormForUser(admin.ModelAdmin):
    pass


@admin.register(Adress)
class Adress(admin.ModelAdmin):
    pass


@admin.register(OfflineRegistration)
class OfflineRegistration(admin.ModelAdmin):
    pass


@admin.register(TestResult)
class Adress(admin.ModelAdmin):
    pass
