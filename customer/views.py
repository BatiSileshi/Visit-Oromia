from django.shortcuts import render, get_object_or_404, redirect
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from visit_admin.models import VisitRoute, Visit
from .models import PlanVisit
from account.forms import SignUpForm
from system_admin.models import Culture, News, Gallery, Place
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    visits=Visit.objects.all()
    news=News.objects.all()
    galleries=Gallery.objects.all()
    visit_routes=VisitRoute.objects.all()
    places=Place.objects.all()
    context={'visits':visits, 'news':news, 'galleries':galleries, 'visit_routes':visit_routes, 'places':places}
    return render(request, 'customer/home.html', context)

def news(request):
    news=News.objects.all()
    context={'news':news}
    return render(request, 'customer/news.html', context)

def plans(request):
    visits=Visit.objects.all()
    context={'visits':visits}
    return render(request, 'customer/plans.html', context)

def gallery(request):
    galleries=Gallery.objects.all()
    context={'galleries':galleries}
    return render(request, 'customer/gallery.html', context)

def cultures(request):
    cultures=Culture.objects.all()
    context={'cultures':cultures}
    return render(request, 'customer/cultures.html', context)

# @unauthenticated_user
def loginPage(request):
    page='login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
             user=get_user_model().objects.get(username=username)
        except:
            messages.error(request, 'Sorry! User does not exist.')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
           
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            else: 
                return redirect('home')
        else :
          messages.error(request, 'Sorry! email or password does not exist.')  
    context={'page':page}
    return render(request, 'customer/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

# @unauthenticated_user
def registerPage(request):
    page='register'
    form=SignUpForm()
    
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()          

            user.save()
            return redirect('login')
        else:
            messages.error(request, "An error occured during registration")
    context={'page':page, 'form':form}
    return render(request, 'customer/login_register.html', context)

@login_required(login_url='register')
def plan(request, pk):
    visit=get_object_or_404(Visit, id=pk)
    if request.method == 'POST':
        plan=PlanVisit.objects.create(
           user=request.user,
           first_name=request.user.first_name,
           last_name=request.user.last_name,
           email=request.user.email,
           visit=visit,
        )
        return redirect('my-plan', request.user.id)
    context={'visit':visit}
    return render(request, 'customer/confirm_plan.html', context)

# def confirmPlan(request, pk):
@login_required(login_url='login')
def myPlan(request, pk):
    user=get_object_or_404(get_user_model(), id=pk)
    plan_visits=user.planvisit_set.all()
    context={'user':user, 'plan_visits':plan_visits}
    if request.user != user: 
        return HttpResponse("You are not allowed here!")
    return render(request, 'customer/my_plan.html', context)


@login_required(login_url='register')
def cancelPlan(request, pk):
    plan_visit=get_object_or_404(PlanVisit, id=pk)
    if request.method=='POST':
        plan_visit.delete()
        return redirect('home')
    
    if request.user != plan_visit.user: 
        return HttpResponse("You are not allowed here!")
    return render(request, 'customer/cancel.html', {'obj':plan_visit})