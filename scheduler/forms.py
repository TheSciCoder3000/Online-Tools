from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={"type": "date"})
        }
