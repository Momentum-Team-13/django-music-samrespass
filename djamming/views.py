from django.shortcuts import render
from .models import Album, Artist


def front_page(request):
    albums = Album.objects.all()
    return render(request, "djamming/home_page.html", {"albums": albums})

def images(request):
    return render(request, "djamming/static",)