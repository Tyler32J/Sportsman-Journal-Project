from django.contrib import admin
from .models import Post, Hunting, Fishing
# from .models import Species, Location, Trip, Harvested 
# Register your models here.

admin.site.register(Post)
admin.site.register(Hunting)
admin.site.register(Fishing)


# admin.site.register(Species)
# admin.site.register(Location)
# admin.site.register(Trip)
# admin.site.register(Harvested)

