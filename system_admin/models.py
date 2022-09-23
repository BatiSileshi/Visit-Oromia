from django.db import models

# Create your models here.
class Gallery(models.Model):
    photo=models.ImageField(max_length=55)
    about=models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.about
    
class News(models.Model):
    photo=models.ImageField(max_length=55,null=True, blank=True)
    about=models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.about
    
class Place(models.Model):
    photo=models.ImageField(max_length=55,null=True, blank=True)
    location=models.CharField(max_length=40, null=True)
    description=models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.location
    
    
class Culture(models.Model):
    name=models.CharField(max_length=40, null=True)
    description=models.CharField(max_length=2000, null=True)
    
    def __str__(self):
        return self.name