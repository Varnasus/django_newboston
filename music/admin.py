from django.contrib import admin

# Register your models here.
# must put any

from .models import Album
from .models import Song

admin.site.register(Album)
admin.site.register(Song)