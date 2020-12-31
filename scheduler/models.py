from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    date = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class scheduleObject(models.Model):
    name = models.CharField(max_length=100)
    weekday = models.CharField(max_length=50)
    links = models.CharField(max_length=200, null=True, blank=True)
    time = models.TimeField()

    def __str__(self):
        return self.name
