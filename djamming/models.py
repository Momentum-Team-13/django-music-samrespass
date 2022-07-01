from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    created = models.DateField(blank=True,null=True, auto_now_add=True)
    album_art = models.ImageField(upload_to='static/images/album_art/')

class Artist(models.Model):
    artist_name = models.CharField(max_length=255,null=False,blank=False)
    album = models.CharField(max_length=255, null=False,blank=False)

class Tracks(models.Model):
    track = models.CharField(max_length=255, null=False, blank=False)
