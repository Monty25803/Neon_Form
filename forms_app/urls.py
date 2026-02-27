"""Neon's Form - URL configuration"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^form/(?P<form_id>\d+)/$', views.form_detail, name='form_detail'),
    url(r'^form/(?P<form_id>\d+)/thanks/$', views.form_thanks, name='form_thanks'),
    url(r'^form/(?P<form_id>\d+)/responses/$', views.form_responses, name='form_responses'),
]
