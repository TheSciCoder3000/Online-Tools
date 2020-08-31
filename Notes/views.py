from django.shortcuts import render
from django.http import JsonResponse
from .models import Folders, Notes
from .forms import FolderForm
from django.views.decorators.csrf import csrf_protect

def home(request):
    form = FolderForm()
    context = {
        'Folders': Folders.objects.all(),
        'Notes': Notes.objects.all(),
        'FolderForm': form,
    }
    return render(request, 'Notes/home.html', context=context)

def update_notes(request):
    if request.is_ajax():
        note = Notes.objects.get(name=request.GET['data_filename'])
        note.content = request.GET['my_data']
        note.save()

        return JsonResponse({
            'msg': 'success'
        })

def update_folder_tree(request):
    if request.method == 'POST':
        print(request.POST)
        def get_root_root(foldername):
            if not foldername == '':
                return Folders.objects.get(name=foldername)
            else:
                return None

        folder_root = Folders.objects.get(root=get_root_root(request.POST.get('root_root')),
                                          name=request.POST.get('root'))

        if request.POST.get('action') == 'Delete':
            if request.POST.get('create_method') == 'Folder':
                print('deleting folder')
                Folders.objects.get(root=folder_root,name=request.POST.get('name')).delete()
            elif request.POST.get('create_method') == 'File':
                print('Deleting File')
                print(folder_root.name)
                print(request.POST.get('name'))
                Notes.objects.get(root=folder_root,name=request.POST.get('name')).delete()
        else:
            if request.POST.get('create_method') == 'Folder':
                cre_obj = Folders(root=folder_root,
                                 name=request.POST.get('name'))
            elif request.POST.get('create_method') == 'File':
                cre_obj = Notes(root=folder_root,
                                 name=request.POST.get('name'))
            cre_obj.save()

        return JsonResponse({
            'msg': 'success',
            'folder_id': '#{}'.format(folder_root.pk),
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
