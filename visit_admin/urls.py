from django.urls import path
from . import views

app_name='visit_admin'
urlpatterns= [
    path('home/', views.home, name="home"),

    
]