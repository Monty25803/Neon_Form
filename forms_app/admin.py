"""Neon's Form - Admin configuration"""
from django.contrib import admin
from .models import Form, Question, Option, Response, Answer


class OptionInline(admin.TabularInline):
    model = Option
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'form', 'question_type', 'required', 'order')
    list_filter = ('form', 'question_type')
    inlines = [OptionInline]


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('form', 'submitted_at')
    list_filter = ('form',)
    inlines = [AnswerInline]


admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Answer)
