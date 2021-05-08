from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Event

class EventView(CreateView):
    model = Event
    fields = ['event']
    template_name = 'events/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
       context =  super().get_context_data(**kwargs)
       context['mapbox_access_token'] = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'
       context['events'] = Event.objects.all()
       return context