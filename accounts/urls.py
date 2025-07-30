from django.shortcuts import render
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('login/', auth_views.LoginView.as_view(), name= 'login'),
]
