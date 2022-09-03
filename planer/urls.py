from django.urls import path
from django.contrib import admin
from planer import views
from .views import *

urlpatterns = [
	path('', views.MainPage, name = 'main'),
]