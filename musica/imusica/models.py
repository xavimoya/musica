from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Companyia(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

class Artist(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, default='City')
    country = models.CharField(max_length=50, blank=True, default='Country')
    website = models.URLField(blank=True)
    idNumber = models.IntegerField(blank=True, null=True)
    companyia = models.ForeignKey(Companyia, null = True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('imusica:artist_detail', kwargs={'pk': self.pk})


class Album(models.Model):
    name = models.CharField(max_length=50)
    idNumber = models.TextField(null=True)
    artista = models.ForeignKey(Artist, null=True)
    companyia = models.ForeignKey(Companyia, null = True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

class Song(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50, blank=True, default='Pop')
    texte = models.CharField(max_length=50, blank=True, default='Lletra completa')
    artista = models.ForeignKey(Artist, null=True)
    album = models.ForeignKey(Album, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('imusica:song_detail', kwargs={'pkr': self.artist.pk, 'pk': self.pk})
