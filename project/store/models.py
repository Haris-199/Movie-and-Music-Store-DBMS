from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    genres = models.CharField(max_length=20)
    listeners = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name

class Song(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=64)
    album = models.CharField(max_length=64, default=None, blank=True, null=True)
    price = models.PositiveIntegerField()

class Album(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.artist.name}"

class Franchise(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    director = models.CharField(max_length=64)
    actors = models.CharField(max_length=64, default=None, blank=True, null=True)
    price = models.PositiveIntegerField() 
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, default=None, blank=True, null=True)
