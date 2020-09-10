from django.shortcuts import render
from django.http import JsonResponse
from .models import Folders, Notes
from .forms import FolderForm

def dash(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'Notes/dashboard.html', context=context)

def notes(request):
    form = FolderForm()
    context = {
        'title': 'Notes',
        'Folders': Folders.objects.all(),
        'Notes': Notes.objects.all(),
        'FolderForm': form,
    }
    return render(request, 'Notes/notes.html', context=context)

def update_notes(request):
    print('\n\nUpdating notes\n\n')
    if request.is_ajax():
        note = Notes.objects.get(pk=request.POST['data_pk'])
        note.content = request.POST['my_data']
        note.save()

        return JsonResponse({
            'msg': 'success'
        })

def update_folder_tree(request):
    if request.method == 'POST':
        print(request.POST)
        def get_root_root(foldername):
            if not (foldername == '' or foldername == 'null'):
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
            print('\n\nAdding\n\n')
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
        if request.GET['note_pk']:
            print('\n\nSending Notes',request.GET['note_pk'],'\n\n')
            note = Notes.objects.get(pk=request.GET['note_pk'])
            content = note.content

        return JsonResponse({
            'msg': 'success',
            'note_content': content,
        })
