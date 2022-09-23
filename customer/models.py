from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from visit_admin.models import Visit
# Create your models here.

class PlanVisit(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name=models.CharField(max_length=40, null=True)
    last_name=models.CharField(max_length=40, null=True)
    email=models.EmailField(null=True)
    visit=models.ForeignKey(Visit, on_delete=models.SET_NULL, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.visit)