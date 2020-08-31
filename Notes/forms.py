from django.forms import ModelForm
from  django import forms
from .models import Folders, Notes

class FolderForm(ModelForm):
    class Meta:
        model = Folders
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'modal-input'})
        }
