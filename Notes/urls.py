from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.home, name='home'),
    path('update_notes/', views.update_notes, name='update-notes'),
    path('get_notes/', views.send_note_data, name='get-notes'),
    path('update_folders/', views.update_folder_tree, name='update-folders'),
]
