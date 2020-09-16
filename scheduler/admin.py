from django.contrib import admin
from .models import Task, scheduleObject

admin.site.register(Task)
admin.site.register(scheduleObject)
