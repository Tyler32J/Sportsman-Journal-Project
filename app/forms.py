from django import forms
from.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

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
        model = Harvested
        fields = ['species', 'quantity']


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'date', 'picture', 'description', 'hunting_choices', 'fishing_choices','fishing_zone_choices']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class HuntingForm(forms.ModelForm):
    class Meta:
        model = Hunting
        fields = ['location', 'title', 'date', 'picture', 'description', 'hunting_log_choices']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class FishingForm(forms.ModelForm):
    class Meta:
        model = Fishing
        fields = ['location', 'title', 'date', 'picture', 'description', 'fishing_log_choices','fishing_zone_choices']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }