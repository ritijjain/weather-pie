from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'units']