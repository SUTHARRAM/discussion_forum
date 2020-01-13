from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('', post_list, name'list'),
    path('create/', post_create),
    path('(?P<slug>[\w-]+)/', post_detail, name='detail'),
    
]