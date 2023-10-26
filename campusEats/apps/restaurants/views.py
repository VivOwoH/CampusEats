from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import * 
from apps.user.models import CustomUser
from apps.review.models import *

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.review.models import Review, ReactionForm

@csrf_exempt
def save_reaction(request):
    # You can access review_id and reaction_id directly in the function
    if request.method == "POST":
        review_id = request.POST.get("review_id")
        reaction_id = request.POST.get("reaction_id")

    print("Review ID:", review_id)
    print("Reaction ID:", reaction_id)

    try:
        review = Review.objects.get(ReviewID=review_id)
        reaction = Reaction.objects.get(pk=reaction_id)

        # Update the user reactions for the review (append the new reaction)
        if review.user_reactions:
            review.user_reactions += f",{reaction_id}"
        else:
            review.user_reactions = reaction_id
        review.save()

        # Return the updated user reactions
        return JsonResponse({"user_reactions": review.user_reactions})

    except (Review.DoesNotExist, Reaction.DoesNotExist):
        return JsonResponse({"error": "Review or Reaction not found"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)



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
    reactions = Reaction.objects.all()  
    print(reactions)
    reviews = get_restaurant_reviews(restaurant_id)

    review_list = list(reviews)

    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant, 'user': global_user, 'reviews': review_list, 'reactions': reactions })

def restaurant_list_view(request):
    restaurant_list = get_all_restaurants()
    return render(request, 'restaurants/restaurant_listing.html', {'restaurant_list': restaurant_list})
