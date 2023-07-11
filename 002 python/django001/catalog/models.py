from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        return self.name

class Director (models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del director")

    def __str__(self):
        return self.name

class Film (models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=64, help_text="Pon aqui de que va la pelicula")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
