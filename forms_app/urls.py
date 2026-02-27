"""Neon's Form - URL configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/<int:form_id>/', views.form_detail, name='form_detail'),
    path('form/<int:form_id>/thanks/', views.form_thanks, name='form_thanks'),
    path('form/<int:form_id>/responses/', views.form_responses, name='form_responses'),
]
