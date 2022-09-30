from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Gallery(models.Model):
    photo=models.ImageField(max_length=55, upload_to="gallery/")
    about=models.CharField(max_length=30, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.about
    
class News(models.Model):
    photo=models.ImageField(max_length=55,null=True, blank=True, upload_to="news/")
    title=models.CharField(max_length=100, null=True)
    about=models.CharField(max_length=500, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):
        return self.about
    
class Place(models.Model):
    photo=models.ImageField(max_length=55,null=True, blank=True, upload_to="places/")
    name=models.CharField(max_length=100, null=True)
    location=models.CharField(max_length=40, null=True)
    description=models.CharField(max_length=500, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    
    
class Culture(models.Model):
    name=models.CharField(max_length=40, null=True)
    description=models.CharField(max_length=2000, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    
