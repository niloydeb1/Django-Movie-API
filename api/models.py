from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    year = models.CharField(max_length=200, null=False, blank=False)
    rated = models.CharField(max_length=200, null=False, blank=False)
    released = models.CharField(max_length=200, null=False, blank=False)
    runtime = models.CharField(max_length=200, null=False, blank=False)
    genre = models.CharField(max_length=200, null=False, blank=False)
    director = models.CharField(max_length=200, null=False, blank=False)
    writer = models.TextField(null=False)
    actors = models.TextField(null=False)
    plot = models.TextField(null=False)
    language = models.TextField(null=False)
    country = models.TextField(null=False)
    awards = models.TextField(null=True)
    poster = models.TextField(null=True)
    imdbRating = models.TextField(null=True)
    type = models.TextField(null=True)
    dvd = models.TextField(null=True)
    box_office = models.TextField(null=True)
    production = models.TextField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField(null=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
