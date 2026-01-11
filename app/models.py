from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Species(models.Model):
    name_of_species = models.CharField(max_length=50)
    species_type = models.CharField(
        max_length=20, 
        choices = [('Fishing', 'Fishing'), ('Hunting', 'Hunting')]
    )

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    trip_date = models.DateField()
    notes = models.TextField(blank=True)


class Harvested(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    date = models.DateField()
    picture = models.ImageField(upload_to="images/")