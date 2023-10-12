from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import * 

def render_home(request):
    restaurants = get_all_restaurants()
    # Pass the list of users to the template
    return render(request, 'restaurants/home.html', {'restaurants': restaurants})
# Create your views here.

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})
