from django.urls import path
from .views import EventView
from .views import CreateEventView
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', EventView.as_view(), name='home'),
    path('create_event/', CreateEventView.as_view(), name='create_event'),
]   