from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    date = models.DateField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
