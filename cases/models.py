from django.db import models

# Create your models here.

class Case (models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=True, blank=True)

    message = models.TextField(default="", null=True)

    file01 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file02 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file03 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file04 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file05 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file06 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file07 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file08 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file09 = models.FileField(upload_to="media/files/", null=True, blank=True)
    file10 = models.FileField(upload_to="media/files/", null=True, blank=True)

    created = models.DateTimeField (auto_now_add=True)
    
    def __str__(self):
        return (self.name + " - " + self.first_name + " " + self.last_name)