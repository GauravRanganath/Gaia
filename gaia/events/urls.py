from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.show_map, name='home'),
    path('create_event/', views.CreateEventView.as_view(), name='create_event'),
    path('<int:event_id>/', views.show_event, name='show_event'),
]   