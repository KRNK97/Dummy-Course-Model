from .views import *
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name="reg"),
    path('', HomeView.as_view(), name="home"),
]
