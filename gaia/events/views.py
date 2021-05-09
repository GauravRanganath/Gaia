from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Event
from .models import UserProfile
import json
from django.http import HttpResponseRedirect
from trycourier import Courier
from datetime import datetime

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
    fields = ['event_name', 'host_name', 'start_date', 'end_date', 'location', 'short_description', 'long_description']
    template_name = 'events/create_event.html'
    success_url = 'create_event'
    widgets = {
        'event_name': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }

    def get_context_data(self, **kwargs):
       context =  super().get_context_data(**kwargs)
       context['mapbox_access_token'] = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'
       context['events'] = Event.objects.all()
       return context

    def form_valid(self, form):
        print("successful submission")

        self.object = form.save()
        print(self.object.event_name, self.object.short_description)

        message = configure_sms(event_name=self.object.event_name, short_description=self.object.short_description, location=self.object.location, start_date=self.object.start_date, host_name=self.object.host_name)
        sms_loop(message)

        return HttpResponseRedirect("http://127.0.0.1:8000")


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

def sms_loop(message):
    print("\n")
    for user in UserProfile.objects.all():
        print(user.name, user.phone_number)
        send_sms(phone_number=user.phone_number, message=message)
    
    print("\n", message, "\n")
    return

def configure_sms(event_name, short_description, location, start_date, host_name):
    message = "It's time to save the planet!\n" + "You are invited to " + event_name + ".\n" + short_description + "\n\n"
    message = message + "Location: " + location + "\n"
    message = message + "Date: " + start_date.strftime("%m/%d/%Y") + "\n"
    message = message + "Time: " + start_date.strftime("%H:%M") + "\n\n"
    message = message + "Hope to see you there!\n\n"
    message = message + "Thanks\n" + host_name
    
    #print(message)
    return message

def send_sms(phone_number, message):
    client = Courier(auth_token="pk_prod_3NF6S5AZ4S4TSRPEM6AJVNRVCFJT")
    resp = client.send(
        event="3T9NBKMKHV4WTVPHZRPKF1Y5NVQ5",
        recipient="3T9NBKMKHV4WTVPHZRPKF1Y5NVQ5",
        profile={
            "email": "malharshah2000@gmail.com",
            "phone_number": phone_number
        },
        data={
            "unique_text": message,
        },
    )
    print(resp['messageId'])