from django.contrib import admin
from django.db import models
from django.db.models import Model
from .models import Artist, Album


# Register your models here.

admin.site.register(Artist)

admin.site.register(Album)
