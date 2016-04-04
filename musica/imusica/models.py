from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=50)

class Artist(models.Model):
    name = models.CharField(max_length=50)
