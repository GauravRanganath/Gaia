from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Event

class EventView(CreateView):
    model = Event
    fields = ['event']
    template_name = 'events/home.html'
    success_url = '/'