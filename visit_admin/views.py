from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import Visit, VisitRoute
from .forms import VisitForm, VisitRouteForm
from django.contrib.auth.decorators import login_required
from customer.models import PlanVisit
from customer.decorators import allowed_users
from .decorators import admin_only
# Create your views here.

@login_required(login_url='login')
@admin_only
def home(request):
    context={}
    return render(request, 'visit_admin/home.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def manageVisit(request):
    visits=Visit.objects.all().order_by('-created')
    context={'visits':visits}
    return render(request, 'visit_admin/manage_visit.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def manageVisitRoute(request):
    visit_routes=VisitRoute.objects.all().order_by('-created')
    context={'visit_routes':visit_routes}
    return render(request, 'visit_admin/manage_visitroute.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def managePlans(request):
    plan_visits=PlanVisit.objects.all().order_by('-created')
    context={'plan_visits':plan_visits}
    return render(request, 'visit_admin/manage_plans.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def addVisit(request):
    form=VisitForm()
    
    if request.method == 'POST':
        form =VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_admin:home')
        
    context={'form':form}
    return render(request, 'visit_admin/visit_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def updateVisit(request, pk):
    visit =get_object_or_404(Visit, id=pk)
    form =VisitForm(instance=visit)
    
    if request.method=='POST':
        form=VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visit_admin:home')
        
    context={'form':form}
    # if request.user != subroute.bus.bus.bus_admin:
    #     return HttpResponse("You are not allowed here!")
    return render(request, 'visit_admin/visit_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def deleteVisit(request, pk):
    visit=get_object_or_404(Visit, id=pk)
    if request.method=='POST':
        visit.delete()
        return redirect('visit_admin:home')

    return render(request, 'visit_admin/delete.html', {'obj':visit})

# MANAGING VISIT VISITROUTE   


@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def addVisitRoute(request):
    form=VisitRouteForm()
    
    if request.method == 'POST':
        form =VisitRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_admin:home')
        
    context={'form':form}
    return render(request, 'visit_admin/visit_route_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def updateVisitRoute(request, pk):
    visit_route =get_object_or_404(VisitRoute, id=pk)
    form =VisitRouteForm(instance=visit_route)
    
    if request.method=='POST':
        form=VisitRouteForm(request.POST, instance=visit_route)
        if form.is_valid():
            form.save()
            return redirect('visit_admin:home')
        
    context={'form':form}
    # if request.user != subroute.bus.bus.bus_admin:
    #     return HttpResponse("You are not allowed here!")
    return render(request, 'visit_admin/visit_route_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['visit_admin'])
def deleteVisitRoute(request, pk):
    visit_route=get_object_or_404(VisitRoute, id=pk)
    if request.method=='POST':
        visit_route.delete()
        return redirect('visit_admin:home')

    return render(request, 'visit_admin/delete.html', {'obj':visit_route})