from django.urls import path
from . import views

app_name='visit_admin'
urlpatterns= [
    path('home/', views.home, name="home"),
    path('manage-visit/', views.manageVisit, name="manage-visit"),
    path('manage-visitroute/', views.manageVisitRoute, name="manage-visitroute"),
    path('manage-plans/', views.managePlans, name="manage-plans"),
    path('add-visit/', views.addVisit, name="add-visit"),
    path('update-visit/<str:pk>/', views.updateVisit, name="update-visit"),
    path('delete-visit/<str:pk>/', views.deleteVisit, name="delete-visit"),
    
    path('add-visitroute/', views.addVisitRoute, name="add-visitroute"),
    path('update-visitroute/<str:pk>/', views.updateVisitRoute, name="update-visitroute"),
    path('delete-visitroute/<str:pk>/', views.deleteVisitRoute, name="delete-visitroute"),
    
]