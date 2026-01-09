from django.contrib import admin
from .models import Species, Location, Trip, Harvested 
# Register your models here.

admin.site.register(Species)
admin.site.register(Location)
admin.site.register(Trip)
admin.site.register(Harvested)

