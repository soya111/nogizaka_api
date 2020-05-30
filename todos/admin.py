from django.contrib import admin
from .models import Member, Song, SongMembers

# Register your models here.

# admin.site.register(Todo)
admin.site.register(Member)
admin.site.register(Song)
admin.site.register(SongMembers)
