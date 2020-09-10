from django.urls import path
from . import views

urlpatterns = [
    path('', views.sched, name='schedule'),
    path('getTask/', views.getTasksData, name='get-task')
]
