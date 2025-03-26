from django.db import models
from tinymce.models import HTMLField

class contact(models.Model):
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    message= models.TextField()
    contact_image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)

# Create your models here.
