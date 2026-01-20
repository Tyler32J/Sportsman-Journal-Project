from django import forms
from.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if len(username) < 3:
            raise forms.ValidationError(
                "Username must be at least 3 characters long."
            )

        if username in [".", ".."]:
            raise forms.ValidationError("Invalid username.")

        return username
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'title', 'date', 'picture', 'quantity', 'hunting_choices', 'fishing_choices','fishing_zone_choices']

        widgets = {
                'location': forms.TextInput(attrs={'required': True}),
                'title': forms.TextInput(attrs={'required': True}),
                'date': forms.DateInput(attrs={'type': 'date', 'required': True}),
                'picture': forms.FileInput(attrs={'required': True}),
                'quantity': forms.NumberInput(attrs={'required': True}),
                'hunting_choices': forms.Select(attrs={'required': True}),
                'fishing_choices': forms.Select(attrs={'required': True}),
                'fishing_zone_choices': forms.Select(attrs={'required': True}),
                "description": forms.TextInput(
                    attrs={"placeholder": "No description yet", 'value': '' }
                ),
            }
       
    def clean(self):
        cleaned_data = super().clean()

        picture = cleaned_data.get('picture')
        quantity = cleaned_data.get('quantity')
        hunting = cleaned_data.get('hunting_choices')
        fishing = cleaned_data.get('fishing_choices')
        zone = cleaned_data.get('fishing_zone_choices')

        if not picture:
             raise forms.ValidationError('picture', 'Please fill out this field - Image is required')

        if quantity is None or quantity == '':
             raise forms.ValidationError('quantity', 'Please fill out this field - Quantity is required')
    
        hunting_selected = hunting and hunting != 'none'
        fishing_selected = fishing and fishing != 'none'
        zone_selected = zone and zone != 'none'

        if not hunting_selected and not fishing_selected:
              raise forms.ValidationError(
                 "Please select either Hunting or Fishing"
             )

        if hunting_selected and fishing_selected:
            raise forms.ValidationError(
                "You can log Hunting OR Fishing, not both."
            )

        if fishing_selected:
             if not zone_selected:
                 raise forms.ValidationError(
                     "Fishing logs require both a fish AND a fishing zone."
                 )
        return cleaned_data
    

class HuntingForm(forms.ModelForm):
    class Meta:
        model = Hunting
        fields = ['location', 'title', 'date', 'picture', 'quantity', 'hunting_log_choices']

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

        return cleaned_data
        

class FishingForm(forms.ModelForm):
    class Meta:
        model = Fishing
        fields = ['location', 'title', 'date', 'picture', 'quantity', 'fishing_log_choices','fishing_zone_choices']

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