from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileUpdate
from .models import Profile

#weatherpie_algo_class imports.
from .weatherpie_algo import weatherpie_algo_class
import requests
from geopy.geocoders import Nominatim
import json
import datetime

def about(request):
    return render(request, 'weather_home/about.html')

@login_required
def update_pref(request):
    if request.method == 'POST':
        form = UserProfileUpdate(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Preferences updated successfully')
            return redirect('weather_home')       

    else:
        form = UserProfileUpdate()

    return render(request, 'weather_home/upupdatepref.html', {'form': form})

@login_required
def home(request):

    profile = Profile.objects.get(user=request.user)

    location = profile.location
    units = profile.units

    u = weatherpie_algo_class(User.username, location, units)
    data = u.ret()

    return render(request, 'weather_home/home.html', {'data': data})