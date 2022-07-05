from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    def __str__(self):
        return(self.name)
    song = models.FileField(upload_to='static/media/tracks/')
    album = models.ForeignKey( "Album", on_delete=models.CASCADE, related_name="tracks", blank=False, null=False )

class Album(models.Model):
    artist = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return(self.name)
    created = models.DateField(blank=True,null=True, auto_now_add=True)
    album_art = models.ImageField(upload_to='static/images/album_art/')


class Artist(models.Model):
    artist_name = models.CharField(max_length=255,null=False,blank=False)
    album = models.CharField(max_length=255, null=False,blank=False)


    