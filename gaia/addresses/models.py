import geocoder
from django.db import models

mapbox_access_token = 'pk.eyJ1IjoibmtyYW1hOTkiLCJhIjoiY2tvZncwbjE1MGF0dTJvcG5uM3dlZTVqaCJ9.5hAFk9giRgnqm8SmSfFz3Q'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)


