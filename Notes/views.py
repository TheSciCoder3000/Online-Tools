from django.shortcuts import render
from django.http import JsonResponse
from .models import Folders, Notes

def home(request):
    context = {
        'Folders': Folders.objects,
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
        print("")
        print(request.GET['my_data'])
        print("")

        note = Notes.objects.all()[0]
        note.content = request.GET['my_data']
        note.save()

        return JsonResponse({
            'msg': 'success'
        })
