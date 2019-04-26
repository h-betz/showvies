from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=90)
    imdb_rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    rt_rating = models.IntegerField(null=True)
    description = models.TextField()
    movie_id = models.CharField(max_length=60)
    thumbnail_url = models.TextField()


class Genre(models.Model):
    name = models.CharField(max_length=60)
    genre_id = models.IntegerField(primary_key=True)


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Provider(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)