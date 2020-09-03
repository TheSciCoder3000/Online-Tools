from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tags'

class Folders(models.Model):
    root = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                             blank=True, default='root')
    name = models.CharField(max_length=100, null=True, default='New Folder')
    details = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Folders'

class Notes(models.Model):
    root = models.ForeignKey(Folders, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True, default='New Notes')
    content = models.TextField(blank=True, null=True, default='<div class="cell-row"><div class="cell-column" contenteditable></div></div>')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Notes'
