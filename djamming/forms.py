from django import forms
from .models import Album, Track, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'name',
            'artist',
            'album_art',
        ]

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = [
            'name',
            'song',
            'album',
            
        ]

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'name',
            'profile_pic',
            'bio'
        ]