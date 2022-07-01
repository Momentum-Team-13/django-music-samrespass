from django.contrib import admin
from django.db import models
from django.db.models import Model
from .models import Artist, Album, Track


# Register your models here.

admin.site.register(Artist)

admin.site.register(Album)

admin.site.register(Track)