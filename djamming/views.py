from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist, Track
from .forms import AlbumForm


def front_page(request):
    albums = Album.objects.all()
    return render(request, "djamming/home_page.html", {"albums": albums})

def single_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    track = Track.objects.filter(album = pk)
    return render(request, "djamming/view_album.html", {"tracks": track,"album": album})

def new_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='front_page')

    return render(request, "djamming/add_album.html", {"form": form})

