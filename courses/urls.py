from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', RegisterView.as_view(), name="reg"),
    path('login/', LoginUserView.as_view(), name="login"),
]
