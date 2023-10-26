from django.shortcuts import render, redirect
from apps.restaurants.models import Restaurant #I assume were using render but this can change.
from .models import Review
from apps.user.models import CustomUser
from .forms import ReviewForm
from datetime import datetime

global_user = None
global_user = CustomUser.get_global_user()

def cancel_review(request, restaurant_id):
    # Do any necessary processing and retrieve the restaurant details
    # For example, you can query the database to get restaurant data
    # print(restaurant)
    restaurant = Restaurant.objects.get(pk=restaurant_id)  # Adjust this according to your model
    # print(restaurant_id)
    # Render the "Cancel Review" template with the restaurant context variable
    
    return render(request, 'cancel_review.html', {'restaurant': restaurant})


def create_review(request):
    global_user = CustomUser.get_global_user()

    if global_user is None:
        # User is not authenticated (not logged in)
        # You can handle this situation here, e.g., redirect to a login page or show an error message.
        return redirect('login')  
    
    restaurant_id = request.GET.get('restaurant_id')
    review_id = request.GET.get('review_id')

    
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant_id')
        review_id = request.POST.get('review_id')


        if review_id  != 'None':
            restaurant = Restaurant.objects.get(pk=restaurant_id) 
            rating = request.POST.get('rating')
            description = request.POST.get('review')  # Adjust the field name as per your form

            # Create a new Review instance
            new_review = Review(
                RestaurantID=restaurant,
                UserID=global_user,  # Assuming you have a logged-in user
                Rating=rating,
                Description=description,
                Timestamp=datetime.now(),
                ParentReviewID = Review.objects.get(pk=review_id)

            )

            # Save the new review
            new_review.save()

            return redirect('success') 




        restaurant = Restaurant.objects.get(pk=restaurant_id) 
        # Get data from the POST request
        rating = request.POST.get('rating')
        description = request.POST.get('review')  # Adjust the field name as per your form

        # Create a new Review instance
        new_review = Review(
            RestaurantID=restaurant,
            UserID=global_user,  # Assuming you have a logged-in user
            Rating=rating,
            Description=description,
            Timestamp=datetime.now(),
            ParentReviewID = None

        )

        # Save the new review
        new_review.save()

        # return redirect('restaurant/restaurant_detail') 
        # return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant, 'user': global_user, 'reviews': review_list, 'reactions': reactions })
        # previous_url = request.META.get('HTTP_REFERER', '/')
        # return redirect(previous_url)
        return redirect('success') 


    
 # Redirect to a confirmation page or the review list page

    else:
        # Handle GET request to display the form
        return render(request, 'review/create_review.html', {'restaurant_id': restaurant_id, 'review_id': review_id, 'user': global_user})


def display_reviews(request, restaurant_id):
    reviews = Review.objects.filter(RestaurantID=restaurant_id)
    return render(request, 'reviews_template.html', {'reviews': reviews})


# @login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, ReviewID=review_id)
    review.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# @login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, ReviewID=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            modified_review = form.save(commit=False)  # Save the form, but don't commit to database yet

            # Append 'Edited' with the datetime stamp to the Description if it's been modified
            if 'Description' in form.changed_data:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Formatting the datetime
                modified_review.Description += "\n\n(Edited on {})\n".format(current_time)

            modified_review.save()
            return redirect('some_view_name')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review_template.html', {'form': form})
