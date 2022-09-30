from tabnanny import verbose
from django.db import models

# Create your models here.


class VisitRoute(models.Model):
    name=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=800, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Visit(models.Model):
    visit_route=models.ForeignKey(VisitRoute, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=200, null=True)
    date=models.DateField(null=True)
    description=models.CharField(max_length=500, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
    
