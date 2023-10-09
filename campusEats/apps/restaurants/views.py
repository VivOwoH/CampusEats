from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import * 

def render_home(request):
    restaurants = get_all_restaurants()
    print(restaurants[0].get('ImageURL'))
    # Pass the list of users to the template
    return render(request, 'restaurants/home.html', {'restaurants': restaurants})
# Create your views here.
