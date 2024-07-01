from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_totals, name='show_totals' ),
    path('bibliometria/', views.bibliometria, name='bibliometria'),
    path('respuestas_forms/', views.respuestas_forms, name='respuestas_forms'), 
]