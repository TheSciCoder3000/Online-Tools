from django.forms import ModelForm
from  django import forms
from .models import Folders, Notes

class FolderForm(ModelForm):
    class Meta:
        model = Folders
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'modal-input',
                                           'id': 'Folder_name'})
        }
class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'modal-input',
                                           'id': 'File_name'})
        }
