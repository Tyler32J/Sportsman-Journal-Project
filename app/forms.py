from django import forms
from.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'date', 'picture', 'description', 'quantity', 'hunting_choices', 'fishing_choices','fishing_zone_choices']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            "description": forms.TextInput(
                attrs={"placeholder": "No description yet", 'value': '' }
            ),
        }
        
    def clean(self):
        cleaned_data = super().clean()

        hunting = cleaned_data.get('hunting_choices')
        fishing = cleaned_data.get('fishing_choices')
        zone = cleaned_data.get('fishing_zone_choices')

        hunting_selected = hunting and hunting != 'none'

        fishing_selected = (
            (fishing and fishing != 'none') or
            (zone and zone != 'none')
        )

        if hunting_selected and fishing_selected:
            raise forms.ValidationError(
                "You can log Hunting OR Fishing, not both."
            )

        if fishing_selected:
            if fishing == 'none' or zone == 'none':
                raise forms.ValidationError(
                    "Fishing logs require both a fish and a fishing zone."
                )

        return cleaned_data

class HuntingForm(forms.ModelForm):
    class Meta:
        model = Hunting
        fields = ['location', 'title', 'date', 'picture', 'description', 'quantity', 'hunting_log_choices']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            "description": forms.TextInput(
                attrs={"placeholder": "No description yet", 'value': '' }
            ),
            "title": forms.TextInput(
                attrs={"placeholder": "Title", 'value': '' }
            ),
            "location": forms.TextInput(
                attrs={"placeholder": "Location", 'value': '' }
            ),
        }
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('hunting_log_choices') == 'none':
            self.add_error('hunting_log_choices', 'This field is required.')

        if cleaned_data.get('hunting_zone_choices') == 'none':
            self.add_error('hunting_zone_choices', 'This field is required.')

        return cleaned_data
        

class FishingForm(forms.ModelForm):
    class Meta:
        model = Fishing
        fields = ['location', 'title', 'date', 'picture', 'description', 'quantity', 'fishing_log_choices','fishing_zone_choices']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            "description": forms.TextInput(
                attrs={"placeholder": "No description yet", 'value': '' }
            ),
            "title": forms.TextInput(
                attrs={"placeholder": "Title", 'value': '' }
            ),
            "location": forms.TextInput(
                attrs={"placeholder": "Location", 'value': '' }
            ),

        }
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('fishing_log_choices') == 'none':
            self.add_error('fishing_log_choices', 'This field is required.')

        if cleaned_data.get('fishing_zone_choices') == 'none':
            self.add_error('fishing_zone_choices', 'This field is required.')

        return cleaned_data