from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import * 
from apps.user.models import CustomUser
from apps.review.models import *



def render_home(request):
    restaurants = get_all_restaurants()
    # Pass the list of users to the template
    return render(request, 'restaurants/home.html', {'restaurants': restaurants})
# Create your views here.

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    # if request.custom_user:
    #     user = request.custom_user
    #     # Now you can work with the user object
    #     print(user)
    # else:
    #     # Handle the case when there is no authenticated user
    global_user = CustomUser.get_global_user()
    reviews = get_restaurant_reviews(restaurant_id)

    review_list = list(reviews)

    # Pass the review_list to the template context
    # context = {
    #     'reviews': review_list,
    # }
    # print(context)

    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant, 'user': global_user, 'reviews': review_list })

def restaurant_list_view(request):
    restaurant_list = get_all_restaurants()
    return render(request, 'restaurants/restaurant_listing.html', {'restaurant_list': restaurant_list})
