from . import views
from django.conf.urls import url, include


#https://docs.djangoproject.com/en/1.11/ref/class-based-views/
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.Inicio, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^photos', views.photos, name='photos'),
    url(r'^thanks', views.thanks, name='thanks'),
    ]