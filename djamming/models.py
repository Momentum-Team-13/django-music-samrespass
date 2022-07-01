from django.db import models

class Track(models.Model):
    song = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return(self.song)
    album = models.ForeignKey( "Album", on_delete=models.CASCADE, related_name="album_tracks", blank=False, null=False )

class Album(models.Model):
    artist = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return(self.name)
    created = models.DateField(blank=True,null=True, auto_now_add=True)
    album_art = models.ImageField(upload_to='static/images/album_art/')
    tracks = models.ForeignKey( Track, on_delete=models.CASCADE, related_name="album_tracks", blank=True, null=True )


class Artist(models.Model):
    artist_name = models.CharField(max_length=255,null=False,blank=False)
    album = models.CharField(max_length=255, null=False,blank=False)


    