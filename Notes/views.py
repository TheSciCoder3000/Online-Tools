from django.shortcuts import render
from django.http import JsonResponse
from .models import Folders, Notes
from django.views.decorators.csrf import csrf_protect

def home(request):
    context = {
        'Folders': Folders.objects.all(),
        'Notes': Notes.objects.all()
    }
    return render(request, 'Notes/home.html', context=context)

def test(request):
    context = {
        'Folders': Folders.objects,
        'Notes': Notes.objects.all(),
    }
    return render(request, 'Notes/test.html', context=context)

def update_notes(request):
    if request.is_ajax():
        note = Notes.objects.get(name=request.GET['data_filename'])
        note.content = request.GET['my_data']
        note.save()

        return JsonResponse({
            'msg': 'success'
        })

def send_note_data(request):
    if request.is_ajax():
        if request.GET['note_data']:
            note = Notes.objects.get(name=request.GET['note_data'])
            content = note.content

        return JsonResponse({
            'msg': 'success',
            'note_content': content,
        })
