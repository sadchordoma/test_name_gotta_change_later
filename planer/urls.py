from django.urls import path
from django.contrib import admin
from main import planer
from .views import *

urlpatterns = [
	path('', views.MainPage, name = 'main'),
]