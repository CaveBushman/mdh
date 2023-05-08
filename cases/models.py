from django.db import models

# Create your models here.

class Case (models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    message = models.TextField(default="", null=True)

    file01 = models.FileField(upload_to="media/files/")
    file02 = models.FileField(upload_to="media/files/")
    file03 = models.FileField(upload_to="media/files/")
    file04 = models.FileField(upload_to="media/files/")
    file05 = models.FileField(upload_to="media/files/")
    file06 = models.FileField(upload_to="media/files/")
    file07 = models.FileField(upload_to="media/files/")
    file08 = models.FileField(upload_to="media/files/")
    file09 = models.FileField(upload_to="media/files/")
    file10 = models.FileField(upload_to="media/files/")

    created = models.DateTimeField (auto_now_add=True)
    
    def __str__(self):
        return (self.name + " - " + self.first_name + " " + self.last_name)