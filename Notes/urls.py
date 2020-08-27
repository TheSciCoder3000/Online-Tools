from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('update_notes/', views.update_notes, name='update-notes'),
]
