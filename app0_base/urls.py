from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team', views.team, name='team'),
    path('expertise', views.expertise, name='expertise'),
    path('ai', views.ai, name='our ai'),
    path('serenicia', views.serenicia, name='serenicia'),
    path('contact', views.contact, name='contact'),
    path('legalnotice', views.legalnotice, name='legal notice'),
]
