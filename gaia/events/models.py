import geocoder
from django.db import models
from django.utils import timezone

mapbox_access_token = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'

class Event(models.Model):
    event_name = models.CharField(max_length=255, default="null")
    host_name = models.CharField(max_length=255, default="null")
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(default=timezone.now())
    location = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    short_description = models.TextField(default="short description")
    long_description = models.TextField(default="long description")

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.location, key=mapbox_access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.event_name

class UserProfile(models.Model):
    name = models.CharField(max_length=255, default="<noname>")
    email = models.CharField(max_length=255, default="<noemail>")
    phone_number = models.CharField(max_length=12)
    location = models.TextField()

    def __str__(self):
        return self.name