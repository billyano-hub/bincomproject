from django.contrib import admin
from .models import Pictures,Genre,Track,Video


class PicturesAdmin(admin.ModelAdmin):
    list_display=('id','title','image')

class GenreAdmin(admin.ModelAdmin):
    list_display=('id','name')

class TrackAdmin(admin.ModelAdmin):
    list_display=('id','track_title','track')

class VideoAdmin(admin.ModelAdmin):
    list_display=('id','video_title','video')



# Register your models here.
admin.site.register(Pictures,PicturesAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(Video,VideoAdmin)