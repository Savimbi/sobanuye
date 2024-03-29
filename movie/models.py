from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='movie/images', blank=True)
    url = models.URLField(max_length=250, blank=True)
