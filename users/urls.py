from django.contrib import admin
from django.urls import path, include
from .import views
from .views import *

app_name = 'users'
urlpatterns = [
        path('', index , name="index"),
]