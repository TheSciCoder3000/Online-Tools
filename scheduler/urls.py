from django.urls import path
from . import views

urlpatterns = [
    path('', views.sched, name='schedule'),
    path('getTask/', views.getTasksData, name='get-task'),
    path('updateTask/', views.updateTasks, name='update-tasks'),
    path('createTask/', views.createTask, name='create-task'),
    path('removeTask/', views.removeTask, name='remove-task'),
    path('getSchedule/', views.getDaySchedule, name='get-sched')
]
