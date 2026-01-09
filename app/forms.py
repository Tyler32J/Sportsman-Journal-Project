from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Location, Trip, Harvested

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'state', 'city', 'county']


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['location', 'trip_date', 'notes']


class HarvestedForm(forms.ModelForm):
    class Meta:
        models = Harvested
        fields = ['species', 'quantity']


class SignupForm(UserCreationForm):
    class Meta:
        models = User
        fields = ['username','password']

