from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index),
    path('get-docx', views.get_docx)
]