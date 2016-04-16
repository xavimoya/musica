from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Companyia(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    website = models.URLField(blank=True)

class Artist(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, default='City')
    country = models.CharField(max_length=50, blank=True, default='Country')
    website = models.URLField(blank=True)
    idNumber = models.IntegerField(blank=True, null=True)
    companyia = models.ForeignKey(Companyia, null = True)


class Album(models.Model):
    name = models.CharField(max_length=50)
    idNumber = models.TextField(null=True)
    artista = models.ForeignKey(Artist, null=True)
    companyia = models.ForeignKey(Companyia, null = True)

class Song(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50, blank=True, default='Pop')
    texte = models.CharField(max_length=50, blank=True, default='Lletra completa')
    artista = models.ForeignKey(Artist, null=True)
    album = models.ForeignKey(Album, null=True)
