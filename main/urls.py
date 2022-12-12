from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('' , IndexView.as_view(), name='index'),
    path('get-docx', get_docx),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]