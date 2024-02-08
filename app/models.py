from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100,  null=False, blank=False)
    notes = models.TextField()

    def __str__(self):
        return  self.title + " - " + str(self.id)