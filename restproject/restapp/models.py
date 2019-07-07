from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length = 50)
    singer = models.ForeignKey('Singer', on_delete = models.CASCADE)
    genres = models.ForeignKey('Genre', on_delete = models.CASCADE)
    released_at = models.DateField()

class Singer(models.Model):
    name = models.CharField(max_length = 30)
    birth = models.DateField()

class Genre(models.Model):
    name = models.CharField(max_length = 30)

