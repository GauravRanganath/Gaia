from django.contrib import admin
from .models import Event
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Event)
