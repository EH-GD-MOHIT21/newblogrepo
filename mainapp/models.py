from django.db import models

# Create your models here.

class htmlfields(models.Model):
    name =  models.CharField(max_length=100)
    timestamp =  models.CharField(max_length=100)
    place =  models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    desc1 = models.TextField()
    img1 = models.ImageField(upload_to='imgs')
    desc2 = models.TextField()
    img2 = models.ImageField(upload_to='imgs')
    desc3 = models.TextField()