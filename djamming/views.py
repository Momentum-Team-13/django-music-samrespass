from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist, Track


def front_page(request):
    albums = Album.objects.all()
    return render(request, "djamming/home_page.html", {"albums": albums})

def single_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    track = Track.objects.all()
    return render(request, "djamming/view_album.html", {"tracks": track,"album": album})
