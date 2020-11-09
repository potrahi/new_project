from django.db import models

# Create your models here.

class Folder(models.Model):
    title = models.CharField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'ID %d.\tTitle: %s.\tDate created: %s.\tLast Update: %s.\t' % (self.id ,self.title, self.date_create, self.date_update)