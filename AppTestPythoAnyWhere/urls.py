from django.conf.urls import url, include
from . import views

#https://docs.djangoproject.com/en/1.11/ref/class-based-views/
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.Inicio, name='home'),
]