from django import template


register = template.Library()

@register.filter
def get_root_folders(folders):
    return folders.filter(root=None)
