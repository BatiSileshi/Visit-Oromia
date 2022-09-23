from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def home(request):
    context={}
    return render(request, 'visit_admin/home.html', context)