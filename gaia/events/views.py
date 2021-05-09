from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Event
import json

class EventView(CreateView):
    model = Event
    fields = ['location']
    template_name = 'events/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
       context =  super().get_context_data(**kwargs)
       context['mapbox_access_token'] = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'
       context['events'] = Event.objects.all()
       return context

class CreateEventView(CreateView):
    model = Event
    fields = ['location', 'event_name']
    template_name = 'events/create_event.html'
    success_url = 'create_event'

    def get_context_data(self, **kwargs):
       context =  super().get_context_data(**kwargs)
       context['mapbox_access_token'] = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'
       context['events'] = Event.objects.all()
       return context

def serialize(data):
    geojson = {}
    geojson['type'] = 'geojson'
    geojson['data'] = {}
    geojson['data']['type'] = 'FeatureCollection'
    geojson['data']['features'] = []

    event_collection = geojson['data']['features']

    for event in data:
        event_instance = {}
        event_instance['type'] = 'Feature'
        event_instance['properties'] = {}

        properties = event_instance['properties']
        properties['event_name'] = event.event_name
        properties['host_name'] = event.host_name
        properties['start_date'] = (event.start_date).strftime("%d-%b-%Y %H:%M")
        properties['end_date'] = (event.end_date).strftime("%d-%b-%Y %H:%M")
        properties['location'] = event.location
        properties['short_description'] = event.short_description
        properties['long_description'] = event.long_description
        properties['event_id'] = event.id

        event_instance['geometry'] = {'type': 'Point', 'coordinates': [event.long, event.lat]}

        event_collection.append(event_instance)
    return geojson

def show_map(request):

    context =  {}
    context['mapbox_access_token'] = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'
    context['json_events'] = json.dumps(serialize(Event.objects.all()))
    context["events"] = Event.objects.all()

    return render(request, 'events/home.html', context)

def show_event(request, event_id):
    context = {}
    
    context['mapbox_access_token'] = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'

    event = Event.objects.get(id=event_id)
    context['event_name'] = event.event_name
    context['host_name'] = event.host_name
    context['start_date'] = (event.start_date).strftime("%d-%b-%Y %H:%M")
    context['end_date'] = (event.end_date).strftime("%d-%b-%Y %H:%M")
    context['location'] = event.location
    context['short_description'] = event.short_description
    context['long_description'] = event.long_description
    context['event_id'] = event.id
    context['geometry'] = [event.long, event.lat]

    return render(request, 'events/show_event.html', context)