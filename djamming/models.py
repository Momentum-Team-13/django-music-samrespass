from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    def __str__(self):
        return(self.name)
    song = models.FileField(upload_to='static/media/tracks/')
    album = models.ForeignKey( "Album", on_delete=models.CASCADE, related_name="tracks", blank=False, null=True )

class Album(models.Model):
    artist = models.ForeignKey( "Artist", on_delete=models.CASCADE, related_name="artist", blank=True, null=True )
    name = models.CharField(max_length=255, null=True, blank=False)
    def __str__(self):
        return(self.name)
    created = models.DateField(blank=True,null=True, auto_now_add=True)
    album_art = models.ImageField(upload_to='static/images/album_art/',null=True,blank=False)


class Artist(models.Model):
    name = models.CharField(max_length=255,null=True,blank=False)
    def __str__(self):
        return(self.name)
    bio = models.CharField(max_length=255,null=True,blank=False)
    profile_pic = models.ImageField(upload_to='static/images/profile_pic/',null=True,blank=False)




    