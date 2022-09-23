from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('plans/', views.plans, name="plans"),
    path('news/', views.news, name="news"),
    path('cultures/', views.cultures, name="cultures"),
    path('confirm-plan/<str:pk>/', views.plan, name="confirm-plan"),
    path('my-plan/<str:pk>/', views.myPlan, name="my-plan"),
    path('cancel-plan/<str:pk>/', views.cancelPlan, name="cancel-plan"),
    
]