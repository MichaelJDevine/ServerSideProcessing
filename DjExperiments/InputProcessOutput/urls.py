from django.urls import re_path as url
from django.urls import path
from . import views

app_name = 'InputProcessOutput'

urlpatterns = [
    url(r'^$', views.blog, name='blog')    
]
