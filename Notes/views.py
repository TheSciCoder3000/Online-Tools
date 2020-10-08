from django.shortcuts import render
from django.http import JsonResponse
from .models import Folders, Notes
from .forms import FolderForm, NoteForm

def dash(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'Notes/dashboard.html', context=context)

def notes(request):
    form1 = FolderForm()
    form2 = NoteForm()
    context = {
        'title': 'Notes',
        'Folders': Folders.objects.all(),
        'Notes': Notes.objects.all(),
        'FolderForm': form1,
        'NoteForm': form2,
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
    no_root_folder = False
    if request.method == 'POST':
        if request.POST.get("root_folder") == "root":
            no_root_folder = True
            root_name = "rootF"
            print("\n\nROOT\n\n")
        else:
            root_folder = Folders.objects.get(pk=request.POST['root_folder'])
            root_name = root_folder.pk

        if request.POST.get('action') == 'Delete':
            if request.POST.get('obj_type') == 'Folder' and not (no_root_folder):
                Folders.objects.get(root=root_folder,name=request.POST.get('name')).delete()
            elif request.POST.get('obj_type') == 'File':
                Notes.objects.get(root=root_folder,name=request.POST.get('name')).delete()
            else:
                Folders.objects.get(owner=request.user,name=request.POST.get('name')).delete()
        else:
            if request.POST.get('obj_type') == 'Folder' and not (no_root_folder):
                cre_obj = Folders(root=root_folder,
                                  name=request.POST.get('name'))
            elif request.POST.get('obj_type') == 'File':
                cre_obj = Notes(root=root_folder,
                                name=request.POST.get('name'))
            else:
                cre_obj = Folders(owner=request.user,
                                  name=request.POST.get('name'),
                                  root=None)
            cre_obj.save()


        return JsonResponse({
            'msg': 'success',
            'folder_id': '#{}'.format(root_name),
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
