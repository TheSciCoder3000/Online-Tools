from django import template
import uuid


register = template.Library()

@register.filter
def get_root_folders(folders):
    return folders.filter(root=None)

@register.filter
def get_child_folders(folders):
    return folders.folders_set.all()

@register.filter
def get_child_notes(folder):
    return folder.notes_set.all()

@register.simple_tag
def get_uuid():
    return uuid.uuid4().hex[:3].upper()
