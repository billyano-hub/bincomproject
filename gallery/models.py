# myapp/models.py

from django.db import models
from django.utils import timezone

class Pictures(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True,null=True,upload_to='images/%y')
    date_created = models.DateTimeField(default=timezone.now)
    # Add other fields like date_created, tags, etc.

    def __str__(self):
        return self.title
    

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Track(models.Model):
    track_title = models.CharField(max_length=250)
    musician_name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_year = models.PositiveIntegerField()  # New field for release year
    track = models.FileField(upload_to='album/%y')

    def __str__(self):
        return self.track_title

class Video(models.Model):
    video_title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_year = models.PositiveIntegerField()  # New field for release year
    video = models.FileField(upload_to='videos/%y')

    def __str__(self):
        return self.video_title
