from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=255, default="<noname>")
    email = models.CharField(max_length=255, default="<noemail>")
    phone_number = models.IntegerField()
    location = models.TextField()