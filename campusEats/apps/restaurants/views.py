from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
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
        review.extra = get_restaurant_raction_for_review(review.ReviewID)
        print(review.extra)
        review.save()

        # Return the updated user reactions
        return JsonResponse({"user_reactions": review.user_reactions})

    except (Review.DoesNotExist, Reaction.DoesNotExist):
        return JsonResponse({"error": "Review or Reaction not found"}, status=400)
@csrf_exempt  
def get_reaction_emoji(request):
    if request.method == "POST":
        review_id = request.POST.get("review_id")
    try:
        review = Review.objects.get(ReviewID=review_id)
        emoji_ids = review.user_reactions
        emoji_ids = emoji_ids.split(",") 
        print("this", type(emoji_ids[0]))
        # emoji_ids = set(emoji_ids)

        reactions = [Reaction.objects.get(pk=int(i)) for i in emoji_ids]
        print("this", reactions)



        emojis = [reaction.emoji for reaction in reactions]

        # *******

        emoji_count = {}  # Create a dictionary to count emojis

        reactions = [Reaction.objects.get(pk=int(i)) for i in emoji_ids]

        for reaction in reactions:
            emoji = reaction.emoji
            if emoji in emoji_count:
                emoji_count[emoji] += 1
            else:
                emoji_count[emoji] = 1

        # Map emoji icons to emoji counts
        # emoji_count_with_icons = {emoji_icons[key]: count for key, count in emoji_count.items()}
        print(emoji_count)

        # ******
        return JsonResponse({"emoji": emoji_count})
    except Reaction.DoesNotExist:
        return JsonResponse({"error": "Reaction not found"}, status=404)

def update_extra(reviews):
    for review in reviews:
        review.extra = get_restaurant_raction_for_review(review.ReviewID)
    print(review.extra)
class MainView(TemplateView):
    template_name = 'restaurants/restaurant_listing.html'
class RestaurantJsonListview(View):
    def get(self, *args, **kwargs):
        upper = kwargs.get('restaurant_id') #5
        lower = upper - 5 #0
        restaurants = list(Restaurant.objects.values()[lower:upper])
        restaurant_size = len(Restaurant.objects.all())
        size = True if upper >= restaurant_size else False
        return JsonResponse({'data': restaurants, 'max':size}, safe=False)

def render_home(request):
    restaurants = get_all_restaurants()
    user = CustomUser.get_global_user()

    # Pass the list of users to the template
    return render(request, 'restaurants/home.html', {'restaurants': restaurants, "user" : user })
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
    reviews = get_restaurant_reviews(restaurant_id)

    review_list = list(reviews)
    update_extra(reviews)
    # new_review.extra = get_restaurant_raction_for_review(new_review.ReviewID)
    # emojis = get_restaurant_raction_for_review(review_id)

    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant, 'user': global_user, 'reviews': review_list, 'reactions': reactions })

def restaurant_list_view(request):
    restaurant_list = get_all_restaurants()
    return render(request, 'restaurants/restaurant_listing.html', {'restaurant_list': restaurant_list})
