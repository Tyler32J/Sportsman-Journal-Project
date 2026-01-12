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
    title = models.CharField(max_length=25)
    date = models.DateField()
    picture = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=25, default='No description yet')

    GAME_CHOICES = [
    ('none','None'),
    ('deer_whitetail', 'White-tailed Deer'),
    ('deer_mule', 'Mule/Black-tailed Deer'),
    ('elk', 'Elk'),
    ('moose', 'Moose'),
    ('bear_black', 'Black Bear'),
    ('bighorn_sheep', 'Bighorn Sheep'),
    ('mountain_lion', 'Mountain Lion'),
    ('pronghorn', 'Pronghorn'),
    ('rabbit', 'Rabbit/Hare'),
    ('squirrel', 'Squirrel'),
    ('raccoon', 'Raccoon'),
    ('coyote', 'Coyote'),
    ('fox', 'Fox'),
    ('turkey', 'Wild Turkey'),
    ('grouse', 'Grouse'),
    ('quail', 'Quail'),
    ('pheasant', 'Pheasant'),
    ('dove', 'Dove'),
    ('duck', 'Duck'),
    ('goose', 'Goose'),
    ('rail', 'Rail/Snipe'),
    ]

    hunting_choices = models.CharField( max_length=50,
        choices=GAME_CHOICES,
        default='draft')
    
    FISH_CHOICES = [
    ('none','None'),
    ('bass_largemouth', 'Largemouth Bass'),
    ('bass_smallmouth', 'Smallmouth Bass'),
    ('bass_spotted', 'Spotted Bass'),
    ('trout_rainbow', 'Rainbow Trout'),
    ('trout_brown', 'Brown Trout'),
    ('trout_brook', 'Brook Trout'),
    ('trout_cutthroat', 'Cutthroat Trout'),
    ('trout_lake', 'Lake Trout'),
    ('walleye', 'Walleye'),
    ('pike_northern', 'Northern Pike'),
    ('muskellunge', 'Muskellunge'),
    ('catfish_channel', 'Channel Catfish'),
    ('catfish_blue', 'Blue Catfish'),
    ('catfish_flathead', 'Flathead Catfish'),
    ('crappie_black', 'Black Crappie'),
    ('crappie_white', 'White Crappie'),
    ('perch_yellow', 'Yellow Perch'),
    ('sunfish_bluegill', 'Bluegill'),
    ('carp_common', 'Common Carp'),
    ('trout_speckled', 'Spotted Seatrout (Speckled Trout)'),
    ('trout_sand', 'Sand Seatrout'),
    ('trout_silver', 'Silver Seatrout'),
    ('trout_weakfish', 'Weakfish (Gray Seatrout)'),
    ('black_drum', 'Black Drum'),
    ('sheepshead', 'Sheepshead'),
    ('redfish', 'Red Drum (Redfish)'),
    ('snook', 'Snook'),
    ('striped_bass', 'Striped Bass'),
    ('tarpon', 'Tarpon'),
    ('flounder', 'Flounder'),
    ('snapper_red', 'Red Snapper'),
    ('grouper', 'Grouper'),
    ('halibut_pacific', 'Pacific Halibut'),
    ('amberjack', 'Greater Amberjack'),
    ('tuna_bluefin', 'Bluefin Tuna'),
    ('tuna_yellowfin', 'Yellowfin Tuna'),
    ('tuna_bigeye', 'Bigeye Tuna'),
    ('swordfish', 'Swordfish'),
    ('marlin_blue', 'Blue Marlin'),
    ('marlin_white', 'White Marlin'),
    ('sailfish', 'Sailfish'),
    ('wahoo', 'Wahoo'),
    ('mahi_mahi', 'Mahi-Mahi (Dolphinfish)'),
    ('shark_blacktip', 'Blacktip Shark'),
    ('shark_spinner', 'Spinner Shark'),
    ('shark_bull', 'Bull Shark'),
    ('shark_lemon', 'Lemon Shark'),
    ('shark_tiger', 'Tiger Shark'),
    ('shark_sandbar', 'Sandbar Shark'),
    ('shark_smooth_dogfish', 'Smooth Dogfish Shark'),
    ('shark_atlantic_sharpnose', 'Atlantic Sharpnose Shark'),
    ('shark_bonnethead', 'Bonnethead Shark'),
    ]

    fishing_choices = models.CharField( max_length=50,
        choices=FISH_CHOICES,
        default='draft')
    
    FISH_ZONE_CHOICES = [
    ('none','None'),
    ('freshwater', 'Freshwater'),
    ('coastal', 'Coastal Saltwater'),
    ('offshore', 'Offshore / Deep Sea'),
    ('shark', 'Shark'),
    ]

    fishing_zone_choices = models.CharField( max_length=50,
        choices=FISH_ZONE_CHOICES,
        default='draft')
    
class Hunting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    title = models.CharField(max_length=25)
    date = models.DateField()
    picture = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=25, default='No description yet')

    
    GAME_CHOICES = [
    ('none','None'),
    ('deer_whitetail', 'White-tailed Deer'),
    ('deer_mule', 'Mule/Black-tailed Deer'),
    ('elk', 'Elk'),
    ('moose', 'Moose'),
    ('bear_black', 'Black Bear'),
    ('bighorn_sheep', 'Bighorn Sheep'),
    ('mountain_lion', 'Mountain Lion'),
    ('pronghorn', 'Pronghorn'),
    ('rabbit', 'Rabbit/Hare'),
    ('squirrel', 'Squirrel'),
    ('raccoon', 'Raccoon'),
    ('coyote', 'Coyote'),
    ('fox', 'Fox'),
    ('turkey', 'Wild Turkey'),
    ('grouse', 'Grouse'),
    ('quail', 'Quail'),
    ('pheasant', 'Pheasant'),
    ('dove', 'Dove'),
    ('duck', 'Duck'),
    ('goose', 'Goose'),
    ('rail', 'Rail/Snipe'),
    ]

    hunting_log_choices = models.CharField( max_length=50,
        choices=GAME_CHOICES,
        default='draft')
    
    
class Fishing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    title = models.CharField(max_length=25)
    date = models.DateField()
    picture = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=25, default='No description yet')

    FISH_CHOICES = [
    ('none','None'),
    ('bass_largemouth', 'Largemouth Bass'),
    ('bass_smallmouth', 'Smallmouth Bass'),
    ('bass_spotted', 'Spotted Bass'),
    ('trout_rainbow', 'Rainbow Trout'),
    ('trout_brown', 'Brown Trout'),
    ('trout_brook', 'Brook Trout'),
    ('trout_cutthroat', 'Cutthroat Trout'),
    ('trout_lake', 'Lake Trout'),
    ('walleye', 'Walleye'),
    ('pike_northern', 'Northern Pike'),
    ('muskellunge', 'Muskellunge'),
    ('catfish_channel', 'Channel Catfish'),
    ('catfish_blue', 'Blue Catfish'),
    ('catfish_flathead', 'Flathead Catfish'),
    ('crappie_black', 'Black Crappie'),
    ('crappie_white', 'White Crappie'),
    ('perch_yellow', 'Yellow Perch'),
    ('sunfish_bluegill', 'Bluegill'),
    ('carp_common', 'Common Carp'),
    ('trout_speckled', 'Spotted Seatrout (Speckled Trout)'),
    ('trout_sand', 'Sand Seatrout'),
    ('trout_silver', 'Silver Seatrout'),
    ('trout_weakfish', 'Weakfish (Gray Seatrout)'),
    ('black_drum', 'Black Drum'),
    ('sheepshead', 'Sheepshead'),
    ('redfish', 'Red Drum (Redfish)'),
    ('snook', 'Snook'),
    ('striped_bass', 'Striped Bass'),
    ('tarpon', 'Tarpon'),
    ('flounder', 'Flounder'),
    ('snapper_red', 'Red Snapper'),
    ('grouper', 'Grouper'),
    ('halibut_pacific', 'Pacific Halibut'),
    ('amberjack', 'Greater Amberjack'),
    ('tuna_bluefin', 'Bluefin Tuna'),
    ('tuna_yellowfin', 'Yellowfin Tuna'),
    ('tuna_bigeye', 'Bigeye Tuna'),
    ('swordfish', 'Swordfish'),
    ('marlin_blue', 'Blue Marlin'),
    ('marlin_white', 'White Marlin'),
    ('sailfish', 'Sailfish'),
    ('wahoo', 'Wahoo'),
    ('mahi_mahi', 'Mahi-Mahi (Dolphinfish)'),
    ('shark_blacktip', 'Blacktip Shark'),
    ('shark_spinner', 'Spinner Shark'),
    ('shark_bull', 'Bull Shark'),
    ('shark_lemon', 'Lemon Shark'),
    ('shark_tiger', 'Tiger Shark'),
    ('shark_sandbar', 'Sandbar Shark'),
    ('shark_smooth_dogfish', 'Smooth Dogfish Shark'),
    ('shark_atlantic_sharpnose', 'Atlantic Sharpnose Shark'),
    ('shark_bonnethead', 'Bonnethead Shark'),
    ]

    fishing_log_choices = models.CharField( max_length=50,
        choices=FISH_CHOICES,
        default='draft')
    
    FISH_ZONE_CHOICES = [
    ('none','None'),
    ('freshwater', 'Freshwater'),
    ('coastal', 'Coastal Saltwater'),
    ('offshore', 'Offshore / Deep Sea'),
    ('shark', 'Shark'),
    ]

    fishing_zone_choices = models.CharField( max_length=50,
        choices=FISH_ZONE_CHOICES,
        default='draft')